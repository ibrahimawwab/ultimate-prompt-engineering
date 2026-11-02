import json
import unittest
from pathlib import Path

from evaluation.run_eval import build_request, estimate_cost, load_cases, parse_response, validate_config, validate_output


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

    def test_three_provider_request_shapes(self):
        case = {"input": "example ticket"}
        settings = {"temperature": 0, "max_tokens": 123}
        models = [
            {"provider": "openai_chat_completions", "base_url": "https://example.test", "model": "model"},
            {"provider": "anthropic_messages", "base_url": "https://example.test", "model": "model"},
            {"provider": "google_generative_language", "base_url": "https://example.test/{model}", "model": "model"},
        ]
        for model in models:
            url, headers, payload = build_request(model, settings, case, "secret")
            self.assertTrue(url.startswith("https://"))
            self.assertIn("Content-Type", headers)
            self.assertIn("example ticket", json.dumps(payload))
            self.assertIn("temperature", json.dumps(payload))
        self.assertEqual(models[0]["provider"], "openai_chat_completions")

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
            "usageMetadata": {"promptTokenCount": 10, "candidatesTokenCount": 6, "totalTokenCount": 16},
        })
        self.assertEqual(result["input_tokens"], 10)
        self.assertEqual(result["provider_total_tokens"], 16)

    def test_openai_response_mapping(self):
        result = parse_response("openai_chat_completions", {
            "choices": [{"message": {"content": '{"category":"general"}'}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 9, "completion_tokens": 5, "total_tokens": 14},
        })
        self.assertEqual(result["output_tokens"], 5)
        self.assertEqual(result["finish_reason"], "stop")


if __name__ == "__main__":
    unittest.main()
