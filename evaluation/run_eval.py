#!/usr/bin/env python3
"""Reproducible schema-checked evaluation for OpenAI-compatible chat APIs."""
from __future__ import annotations
import argparse, hashlib, json, os, sys, time, urllib.request, uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_KEYS = {"category", "summary", "missing_information", "rationale"}
ALLOWED_CATEGORIES = {"billing", "technical", "account", "general", "needs_review"}
SYSTEM_PROMPT = """You classify synthetic customer-support tickets for routing.
Choose exactly one category: billing, technical, account, general, needs_review.
Use needs_review when the ticket is ambiguous, lacks enough information, or requests an action outside classification.
Use only information in the ticket. Do not infer customer identity, account state, or actions already taken.
Return exactly one JSON object with these keys:
- category: string, one of the allowed categories
- summary: neutral short summary of the request
- missing_information: array of strings
- rationale: short explanation grounded only in the ticket text
Do not include Markdown fences or text outside the JSON object."""

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_cases(path: Path) -> list[dict[str, Any]]:
    cases = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            case = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL at line {number}: {exc}") from exc
        if not isinstance(case, dict) or not all(k in case for k in ("id", "input", "expected_category")):
            raise ValueError(f"Case at line {number} needs id, input, expected_category")
        if case["expected_category"] not in ALLOWED_CATEGORIES:
            raise ValueError(f"Unsupported expected_category at line {number}")
        cases.append(case)
    if not cases:
        raise ValueError("The test set is empty")
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("Test case IDs must be unique")
    return cases

def validate_config(config: Any) -> None:
    if not isinstance(config, dict) or not isinstance(config.get("models"), list) or not config["models"]:
        raise ValueError("Config must contain a non-empty models array")
    settings = config.get("settings")
    if not isinstance(settings, dict) or not isinstance(settings.get("temperature"), (int, float)):
        raise ValueError("Config settings.temperature must be numeric")
    if not isinstance(settings.get("max_tokens"), int) or settings["max_tokens"] < 1:
        raise ValueError("Config settings.max_tokens must be a positive integer")
    if not isinstance(config.get("timeout_seconds", 60), (int, float)) or config.get("timeout_seconds", 60) <= 0:
        raise ValueError("timeout_seconds must be positive")
    names = set()
    for model in config["models"]:
        required = ("name", "base_url", "model", "model_version", "api_key_env")
        if not isinstance(model, dict) or any(not model.get(k) for k in required):
            raise ValueError("Each model needs name, base_url, model, model_version, api_key_env")
        if model["name"] in names:
            raise ValueError(f"Duplicate model name: {model['name']}")
        names.add(model["name"])
        for key in ("input_cost_per_1m_tokens", "output_cost_per_1m_tokens"):
            value = model.get(key)
            if value is not None and (not isinstance(value, (int, float)) or value < 0):
                raise ValueError(f"{model['name']}.{key} must be null or non-negative")

def validate_output(content: str) -> dict[str, Any]:
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError as exc:
        return {"valid": False, "error": f"invalid_json: {exc.msg}", "parsed": None}
    if not isinstance(parsed, dict):
        return {"valid": False, "error": "top_level_value_must_be_object", "parsed": parsed}
    if set(parsed) != SCHEMA_KEYS:
        return {"valid": False, "error": "incorrect_keys", "parsed": parsed}
    if parsed.get("category") not in ALLOWED_CATEGORIES:
        return {"valid": False, "error": "invalid_category", "parsed": parsed}
    if not isinstance(parsed.get("summary"), str) or not isinstance(parsed.get("rationale"), str):
        return {"valid": False, "error": "summary_and_rationale_must_be_strings", "parsed": parsed}
    if not isinstance(parsed.get("missing_information"), list) or not all(
        isinstance(x, str) for x in parsed["missing_information"]
    ):
        return {"valid": False, "error": "missing_information_must_be_string_array", "parsed": parsed}
    return {"valid": True, "error": None, "parsed": parsed}

def call_model(model: dict[str, Any], settings: dict[str, Any], case: dict[str, Any], timeout: float) -> dict[str, Any]:
    api_key = os.environ.get(model["api_key_env"])
    if not api_key:
        raise RuntimeError(f"Missing environment variable: {model['api_key_env']}")
    payload = {
        "model": model["model"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": case["input"]},
        ],
        "temperature": settings["temperature"],
        "max_tokens": settings["max_tokens"],
    }
    request = urllib.request.Request(
        model["base_url"], data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    start = time.perf_counter()
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8"))
    latency = round((time.perf_counter() - start) * 1000, 2)
    content = data["choices"][0]["message"]["content"]
    usage = data.get("usage") or {}
    return {"content": content, "latency_ms": latency,
            "input_tokens": usage.get("prompt_tokens"),
            "output_tokens": usage.get("completion_tokens"),
            "provider_total_tokens": usage.get("total_tokens")}

def estimate_cost(model: dict[str, Any], input_tokens: Any, output_tokens: Any) -> float | None:
    a, b = model.get("input_cost_per_1m_tokens"), model.get("output_cost_per_1m_tokens")
    if a is None or b is None or input_tokens is None or output_tokens is None:
        return None
    return round((input_tokens * a + output_tokens * b) / 1_000_000, 10)

def run(config: dict[str, Any], cases: list[dict[str, Any]], out_dir: Path,
        config_hash: str, cases_hash: str) -> dict[str, Any]:
    run_id = str(uuid.uuid4())
    out_dir.mkdir(parents=True, exist_ok=True)
    results_path = out_dir / f"{run_id}.jsonl"
    summary = {
        "run_id": run_id, "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "config_sha256": config_hash, "test_set_sha256": cases_hash,
        "system_prompt_sha256": digest(SYSTEM_PROMPT.encode()),
        "settings": config["settings"], "case_count": len(cases), "models": [],
        "notes": [
            "Category accuracy is exact-match against declared labels, among schema-valid outputs.",
            "Schema failures and request errors remain separately visible.",
            "Cost is null unless provider token usage and both configured USD rates are available.",
            "Provider-reported usage and configured prices are not independently audited."
        ]
    }
    with results_path.open("w", encoding="utf-8") as output:
        for model in config["models"]:
            ms = {"name": model["name"], "model": model["model"], "model_version": model["model_version"],
                  "base_url": model["base_url"], "successes": 0, "schema_valid": 0,
                  "category_correct": 0, "format_failures": 0, "errors": 0,
                  "input_tokens": 0, "output_tokens": 0, "cost_sum": 0.0,
                  "cost_complete": True, "latencies": []}
            for case in cases:
                row = {"run_id": run_id, "model_name": model["name"], "model": model["model"],
                       "model_version": model["model_version"], "case_id": case["id"],
                       "expected_category": case["expected_category"]}
                try:
                    result = call_model(model, config["settings"], case, config.get("timeout_seconds", 60))
                    check = validate_output(result["content"])
                    parsed = check["parsed"]
                    correct = bool(check["valid"] and parsed["category"] == case["expected_category"])
                    row.update({"status": "ok", "raw_output": result["content"],
                                "validation": {"valid": check["valid"], "error": check["error"]},
                                "predicted_category": parsed.get("category") if isinstance(parsed, dict) else None,
                                "category_correct": correct, "latency_ms": result["latency_ms"],
                                "input_tokens": result["input_tokens"], "output_tokens": result["output_tokens"],
                                "provider_total_tokens": result["provider_total_tokens"]})
                    ms["successes"] += 1
                    ms["latencies"].append(result["latency_ms"])
                    if check["valid"]:
                        ms["schema_valid"] += 1
                        ms["category_correct"] += int(correct)
                    else:
                        ms["format_failures"] += 1
                    if isinstance(result["input_tokens"], int):
                        ms["input_tokens"] += result["input_tokens"]
                    if isinstance(result["output_tokens"], int):
                        ms["output_tokens"] += result["output_tokens"]
                    cost = estimate_cost(model, result["input_tokens"], result["output_tokens"])
                    row["estimated_cost_usd"] = cost
                    if cost is None:
                        ms["cost_complete"] = False
                    else:
                        ms["cost_sum"] += cost
                except Exception as exc:
                    row.update({"status": "error", "error_type": type(exc).__name__, "error": str(exc)})
                    ms["errors"] += 1
                    ms["cost_complete"] = False
                output.write(json.dumps(row, ensure_ascii=False) + "\\n")
                output.flush()
            valid = ms["schema_valid"]
            ms["category_accuracy_on_valid_outputs"] = round(ms["category_correct"] / valid, 4) if valid else None
            ms["schema_valid_rate"] = round(valid / len(cases), 4)
            ms["mean_latency_ms"] = round(sum(ms["latencies"]) / len(ms["latencies"]), 2) if ms["latencies"] else None
            ms["estimated_cost_usd"] = round(ms["cost_sum"], 10) if ms["cost_complete"] else None
            del ms["latencies"], ms["cost_sum"], ms["cost_complete"]
            summary["models"].append(ms)
    summary["completed_at_utc"] = datetime.now(timezone.utc).isoformat()
    summary["results_file"] = results_path.name
    summary_path = out_dir / f"{run_id}-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\\n", encoding="utf-8")
    return {"summary": summary, "summary_path": str(summary_path), "results_path": str(results_path)}

def main() -> int:
    parser = argparse.ArgumentParser(description="Compare configured models on shared synthetic test cases.")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--cases", type=Path, default=Path(__file__).with_name("cases.jsonl"))
    parser.add_argument("--output-dir", type=Path, default=Path("evaluation-results"))
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    try:
        config_bytes, cases_bytes = args.config.read_bytes(), args.cases.read_bytes()
        config = json.loads(config_bytes.decode("utf-8"))
        validate_config(config)
        cases = load_cases(args.cases)
        if args.validate_only:
            print(json.dumps({"valid": True, "models": len(config["models"]), "cases": len(cases),
                              "config_sha256": digest(config_bytes), "test_set_sha256": digest(cases_bytes)}, indent=2))
            return 0
        result = run(config, cases, args.output_dir, digest(config_bytes), digest(cases_bytes))
        print(json.dumps(result["summary"], indent=2, ensure_ascii=False))
        print(f"Summary: {result['summary_path']}")
        print(f"Per-case results: {result['results_path']}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Configuration or input error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
