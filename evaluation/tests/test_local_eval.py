import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from evaluation.run_local_eval import (
    build_request, load_cases, local_open, parse_response, RejectRedirectHandler, run, validate_config, validate_output
)


class LocalEvaluationTests(unittest.TestCase):
    def config(self):
        return {
            "ollama_base_url": "http://127.0.0.1:11434",
            "timeout_seconds": 10,
            "temperature": 0,
            "num_predict": 128,
            "models": [{"name": "qwen3-4b", "model": "qwen3:4b", "license": "Apache-2.0"}],
        }

    def test_loopback_config_is_accepted_without_api_key(self):
        validate_config(self.config())

    def test_remote_or_https_host_is_rejected(self):
        for url in ("https://127.0.0.1:11434", "http://example.com:11434", "http://192.168.1.4:11434"):
            config = self.config()
            config["ollama_base_url"] = url
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_config(config)

    def test_hosted_credentials_are_rejected(self):
        config = self.config()
        config["models"][0]["api_key_env"] = "OPENAI_API_KEY"
        with self.assertRaises(ValueError):
            validate_config(config)

    def test_request_uses_local_chat_and_json_schema(self):
        url, headers, payload = build_request(self.config()["models"][0], self.config(), {"input": "ticket"})
        self.assertEqual(url, "http://127.0.0.1:11434/api/chat")
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertFalse(payload["stream"])
        self.assertIsInstance(payload["format"], dict)
        self.assertIn("ticket", json.dumps(payload))
        self.assertEqual(payload["options"]["temperature"], 0)

    def test_local_requests_disable_proxies_and_redirects(self):
        with patch("evaluation.run_local_eval.urllib.request.build_opener") as build_opener:
            opener = build_opener.return_value
            request = object()
            local_open(request, 3)
            handlers = build_opener.call_args.args
            self.assertEqual(handlers[0].proxies, {})
            self.assertIsInstance(handlers[1], RejectRedirectHandler)
            opener.open.assert_called_once_with(request, timeout=3)

    def test_response_parsing_preserves_usage_and_latency_fields(self):
        parsed = parse_response({
            "model": "qwen3:4b", "message": {"content": '{"category":"general"}'},
            "prompt_eval_count": 21, "eval_count": 9, "done_reason": "stop",
            "total_duration": 1000, "load_duration": 200,
        })
        self.assertEqual(parsed["input_tokens"], 21)
        self.assertEqual(parsed["output_tokens"], 9)
        self.assertEqual(parsed["served_model"], "qwen3:4b")
        self.assertEqual(parsed["total_duration_ns"], 1000)

    def test_missing_token_counts_are_not_reported_as_zero(self):
        parsed = parse_response({"message": {"content": "{}"}})
        self.assertIsNone(parsed["input_tokens"])
        self.assertIsNone(parsed["output_tokens"])

    def test_schema_validation(self):
        valid = {"category": "billing", "summary": "Duplicate charge", "missing_information": [],
                 "rationale": "The ticket says it was charged twice."}
        self.assertTrue(validate_output(json.dumps(valid))["valid"])
        self.assertFalse(validate_output("not json")["valid"])
        self.assertFalse(validate_output(json.dumps({**valid, "unexpected": True}))["valid"])

    def test_dataset_has_forty_unique_cases(self):
        cases = load_cases(Path(__file__).parents[1] / "cases.jsonl")
        self.assertEqual(len(cases), 40)
        self.assertEqual(len({case["id"] for case in cases}), 40)

    def test_run_writes_reproducible_reports_and_null_incomplete_usage(self):
        config = self.config()
        cases = [{"id": "T-1", "input": "ticket", "expected_category": "billing"}]
        fake_result = {
            "content": json.dumps({"category": "billing", "summary": "Charge issue",
                                   "missing_information": [], "rationale": "Charge is mentioned."}),
            "input_tokens": None, "output_tokens": None, "served_model": "qwen3:4b",
            "created_at": None, "finish_reason": "stop", "total_duration_ns": 10,
            "load_duration_ns": 2, "prompt_eval_duration_ns": 3, "eval_duration_ns": 4,
            "latency_ms": 12.5,
        }
        with tempfile.TemporaryDirectory() as tmp, \
             patch("evaluation.run_local_eval.call_model", return_value=fake_result), \
             patch("evaluation.run_local_eval.model_metadata", return_value={"model_digest": "sha256:test"}):
            result = run(config, cases, Path(tmp), "config-hash", "cases-hash")
            self.assertTrue(Path(result["summary_path"]).exists())
            self.assertTrue(Path(result["results_path"]).exists())
            self.assertTrue(Path(result["errors_path"]).exists())
            self.assertTrue(Path(result["report_path"]).exists())
            metrics = result["summary"]["models"][0]
            self.assertIsNone(metrics["input_tokens"])
            self.assertIsNone(metrics["output_tokens"])
            self.assertEqual(metrics["category_accuracy_all_cases"], 1.0)


if __name__ == "__main__":
    unittest.main()
