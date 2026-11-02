import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.error import HTTPError

from evaluation.run_eval import build_request, call_model, estimate_cost, load_cases, parse_response, run, validate_config, validate_output


class EvaluationHarnessTests(unittest.TestCase):
    def test_valid_output(self):
        value = {"category": "billing", "summary": "Duplicate charge reported.",
                 "missing_information": [], "rationale": "The ticket says charged twice."}
        self.assertTrue(validate_output(json.dumps(value))["valid"])

    def test_markdown_fence_is_rejected(self):
        self.assertFalse(validate_output(chr(96) * 3 + "json\n{}\n" + chr(96) * 3)["valid"])

    def test_wrong_keys_are_rejected(self):
        value = {"category": "billing", "summary": "x", "missing_information": [],
                 "rationale": "x", "extra": "no"}
        self.assertEqual(validate_output(json.dumps(value))["error"], "incorrect_keys")
        self.assertEqual(validate_output(None)["error"], "response_content_must_be_text")

    def test_invalid_category_is_rejected(self):
        value = {"category": "other", "summary": "x", "missing_information": [], "rationale": "x"}
        self.assertEqual(validate_output(json.dumps(value))["error"], "invalid_category")

    def test_cost_requires_usage_and_both_rates(self):
        model = {"input_cost_per_1m_tokens": 1.0, "output_cost_per_1m_tokens": 2.0}
        self.assertIsNone(estimate_cost(model, None, 100))
        self.assertEqual(estimate_cost(model, 1000, 1000), 0.003)

    def test_fixture_has_forty_unique_cases(self):
        cases = load_cases(Path(__file__).parents[1] / "cases.jsonl")
        self.assertEqual(len(cases), 40)
        self.assertEqual(len({case["id"] for case in cases}), 40)
        self.assertTrue(all(case.get("difficulty") in {"easy", "medium", "hard"} for case in cases))

    def test_config_requires_provider_and_model_metadata(self):
        with self.assertRaises(ValueError):
            validate_config({"settings": {"temperature": 0, "max_tokens": 100},
                             "models": [{"name": "incomplete"}]})

    def test_example_model_profile_has_pricing_provenance(self):
        config_path = Path(__file__).parents[1] / "config.example.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        validate_config(config)
        self.assertEqual(len(config["models"]), 3)
        anthropic = next(model for model in config["models"] if model["provider"] == "anthropic_messages")
        self.assertFalse(anthropic["supports_temperature"])
        self.assertTrue(anthropic["pricing_source"].startswith("https://"))
        self.assertIn("100,000", anthropic["pricing_conditions"])
        self.assertEqual(anthropic["api_version"], "2026-10-21")
        self.assertEqual(anthropic["effort"], "low")
        gemini = next(model for model in config["models"] if model["provider"] == "google_generative_language")
        self.assertFalse(gemini["supports_temperature"])
        self.assertEqual(gemini["thinking_level"], "low")

    def test_example_config_rejects_non_provider_hosts(self):
        config_path = Path(__file__).parents[1] / "config.example.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["models"][0]["base_url"] = "https://attacker.example/v1/chat/completions"
        with self.assertRaises(ValueError):
            validate_config(config)

    def test_invalid_temperature_support_setting_is_rejected(self):
        config = {
            "settings": {"temperature": 0, "max_tokens": 100},
            "models": [{
                "name": "invalid", "provider": "openai_chat_completions",
                "base_url": "https://example.test", "model": "model",
                "model_version": "version", "api_key_env": "API_KEY",
                "supports_temperature": "false",
            }],
        }
        with self.assertRaises(ValueError):
            validate_config(config)

    def test_three_provider_request_shapes(self):
        case = {"input": "example ticket"}
        settings = {"temperature": 0, "max_tokens": 123}
        models = [
            {"provider": "openai_chat_completions", "base_url": "https://example.test", "model": "model"},
            {"provider": "anthropic_messages", "base_url": "https://example.test", "model": "model",
             "api_version": "2026-10-21", "effort": "low"},
            {"provider": "google_generative_language", "base_url": "https://example.test/{model}", "model": "model",
             "supports_temperature": False, "thinking_level": "low"},
        ]
        for model in models:
            url, headers, payload = build_request(model, settings, case, "secret")
            self.assertTrue(url.startswith("https://"))
            self.assertIn("Content-Type", headers)
            self.assertIn("example ticket", json.dumps(payload))
            if model.get("supports_temperature", True):
                self.assertIn("temperature", payload if "temperature" in payload else json.dumps(payload))
            else:
                self.assertNotIn("temperature", json.dumps(payload))
        openai_url, openai_headers, openai_payload = build_request(models[0], settings, case, "secret")
        self.assertEqual(openai_headers["Authorization"], "Bearer secret")
        self.assertEqual(openai_payload["messages"][0]["role"], "system")
        anthropic_url, anthropic_headers, anthropic_payload = build_request(models[1], settings, case, "secret")
        self.assertEqual(anthropic_headers["Authorization"], "Bearer secret")
        self.assertIn("system", anthropic_payload)
        self.assertEqual(anthropic_headers["anthropic-version"], "2026-10-21")
        self.assertEqual(anthropic_payload["output_config"]["effort"], "low")
        self.assertEqual(anthropic_payload["output_config"]["format"]["type"], "json_schema")
        haiku_model = {"provider": "anthropic_messages", "base_url": "https://example.test",
                       "model": "claude-haiku-5-5", "supports_temperature": False}
        _, _, haiku_payload = build_request(haiku_model, settings, case, "secret")
        self.assertNotIn("temperature", haiku_payload)
        luna_model = {"provider": "openai_chat_completions", "base_url": "https://example.test",
                      "model": "gpt-6-luna", "reasoning_effort": "none"}
        _, _, luna_payload = build_request(luna_model, settings, case, "secret")
        self.assertEqual(luna_payload["reasoning_effort"], "none")
        self.assertEqual(luna_payload["temperature"], 0)
        self.assertEqual(luna_payload["max_completion_tokens"], 123)
        self.assertEqual(luna_payload["service_tier"], "default")
        self.assertEqual(luna_payload["response_format"]["type"], "json_schema")
        self.assertTrue(luna_payload["response_format"]["json_schema"]["strict"])
        self.assertNotIn("max_tokens", luna_payload)
        google_url, google_headers, google_payload = build_request(models[2], settings, case, "secret")
        self.assertEqual(google_headers["x-goog-api-key"], "secret")
        self.assertNotIn("{model}", google_url)
        self.assertIn("generationConfig", google_payload)
        self.assertNotIn("temperature", google_payload["generationConfig"])
        self.assertEqual(google_payload["generationConfig"]["thinkingConfig"]["thinkingLevel"], "low")
        self.assertEqual(google_payload["generationConfig"]["responseFormat"]["text"]["mimeType"], "APPLICATION_JSON")
        self.assertEqual(google_payload["generationConfig"]["responseFormat"]["text"]["schema"]["type"], "OBJECT")

    def test_anthropic_response_mapping(self):
        result = parse_response("anthropic_messages", {
            "content": [{"type": "text", "text": '{"category":"general"}'}],
            "usage": {"input_tokens": 11, "output_tokens": 7},
            "stop_reason": "end_turn",
        })
        self.assertEqual(result["input_tokens"], 11)
        self.assertEqual(result["output_tokens"], 7)
        self.assertEqual(result["content"], '{"category":"general"}')

    def test_google_response_mapping(self):
        result = parse_response("google_generative_language", {
            "candidates": [{"content": {"parts": [{"text": '{"category":"general"}'}]},
                           "finishReason": "STOP"}],
            "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 6,
                              "thoughtsTokenCount": 4, "totalTokenCount": 20},
        })
        self.assertEqual(result["input_tokens"], 10)
        self.assertEqual(result["candidate_output_tokens"], 6)
        self.assertEqual(result["thoughts_tokens"], 4)
        self.assertEqual(result["output_tokens"], 10)
        self.assertEqual(result["provider_total_tokens"], 20)

    def test_provider_error_body_is_not_written_to_exception(self):
        model = {
            "provider": "openai_chat_completions",
            "base_url": "https://api.openai.com/v1/chat/completions",
            "model": "gpt-6-luna",
            "api_key_env": "OPENAI_API_KEY",
        }
        opener = Mock()
        opener.open.side_effect = HTTPError(
            model["base_url"], 400, "Bad Request", {}, io.BytesIO(b"private-prompt-and-secret-echo")
        )
        with patch("evaluation.run_eval.urllib.request.build_opener", return_value=opener):
            with patch.dict("os.environ", {"OPENAI_API_KEY": "test-secret"}):
                with self.assertRaisesRegex(RuntimeError, "HTTP 400 from provider") as raised:
                    call_model(model, {"temperature": 0, "max_tokens": 100},
                               {"input": "synthetic ticket"}, 5)
        self.assertNotIn("private-prompt-and-secret-echo", str(raised.exception))
        self.assertNotIn("test-secret", str(raised.exception))

    def test_run_writes_combined_provider_and_markdown_reports(self):
        cases = [{"id": "case-1", "input": "ticket", "expected_category": "billing"}]
        config = {
            "settings": {"temperature": 0, "max_tokens": 100},
            "models": [{
                "name": "unit-test-model", "provider": "openai_chat_completions",
                "base_url": "https://api.example.test/chat/completions", "model": "test-model",
                "model_version": "test-snapshot", "api_key_env": "TEST_API_KEY",
                "input_cost_per_1m_tokens": 1.0, "output_cost_per_1m_tokens": 2.0,
            }],
        }
        fake_response = {
            "content": json.dumps({"category": "billing", "summary": "Charge issue",
                                   "missing_information": [], "rationale": "Billing is mentioned."}),
            "input_tokens": 10, "output_tokens": 20, "candidate_output_tokens": 20,
            "thoughts_tokens": None, "provider_total_tokens": 30, "finish_reason": "stop",
            "latency_ms": 12.5, "request_id": "req-test", "provider_model_version": "test-snapshot",
            "system_fingerprint": None,
        }
        with tempfile.TemporaryDirectory() as temp_dir, patch("evaluation.run_eval.call_model", return_value=fake_response):
            result = run(config, cases, Path(temp_dir), "config-hash", "cases-hash")
            output_dir = Path(temp_dir)
            self.assertTrue(Path(result["summary_path"]).exists())
            self.assertTrue(Path(result["results_path"]).exists())
            self.assertTrue(Path(result["errors_path"]).exists())
            self.assertTrue(Path(result["comparison_path"]).exists())
            per_model = list(output_dir.glob("*-unit-test-model.json"))
            self.assertEqual(len(per_model), 1)
            provider_report = json.loads(per_model[0].read_text(encoding="utf-8"))
            self.assertEqual(len(provider_report["cases"]), 1)
            self.assertIn("Accuracy", Path(result["comparison_path"]).read_text(encoding="utf-8"))

    def test_openai_response_mapping(self):
        result = parse_response("openai_chat_completions", {
            "choices": [{"message": {"content": '{"category":"general"}'}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 9, "completion_tokens": 5, "total_tokens": 14},
        })
        self.assertEqual(result["output_tokens"], 5)
        self.assertEqual(result["finish_reason"], "stop")


if __name__ == "__main__":
    unittest.main()
