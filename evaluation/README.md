# Reproducible Cross-Model Evaluation

This directory contains a standard-library evaluation harness with native request/response adapters for three API formats: OpenAI-compatible Chat Completions, Anthropic Messages, and Google Gemini generateContent. Separate adapters are necessary because authentication, request bodies, response structures, and token-usage fields differ.

## Dataset and metrics

The fixed synthetic dataset contains 40 English customer-support classification cases across five labels: billing, technical, account, general, and needs_review. Cases are tagged by difficulty (easy, medium, hard) and topic. The set includes boundary cases, multi-intent requests, underspecified inputs, sensitive requests, and a prompt-injection-style ticket. Labels are a teaching fixture and should be reviewed before consequential use.

Each configured model receives the same system prompt, user input, temperature, and maximum output-token setting where provider controls are equivalent. Provider-specific system-message placement and JSON response controls differ; these protocol differences are documented and reflected in the adapters.

Per-case results include raw output, schema validation, expected/predicted labels, correctness, request status, latency, request ID when exposed, provider-reported token usage, finish reason, and estimated cost when configured. Summary metrics include request success rate, schema-valid rate, category accuracy across all cases (invalid output and request failures count as incorrect), accuracy among schema-valid outputs, confusion matrix, mean/median latency, token totals, and estimated cost.

## Supported adapters

| Adapter | API format | Authentication | Usage fields |
|---|---|---|---|
| openai_chat_completions | Chat Completions | Bearer token | prompt_tokens, completion_tokens |
| anthropic_messages | Messages API | x-api-key and anthropic-version | input_tokens, output_tokens |
| google_generative_language | Gemini generateContent | x-goog-api-key | promptTokenCount, candidatesTokenCount |

This is not a claim that every provider endpoint or compatible gateway has been tested. Use the exact documented endpoint for the selected model. The Google endpoint template substitutes the configured model ID into {model}. Verify request parameters against current provider documentation before a real run.

## Configure models

1. Copy config.example.json to a local file such as config.local.json; do not commit the local file.
2. Replace placeholder model IDs with exact identifiers accepted by each provider.
3. Record an immutable model snapshot/version where available. If the provider does not disclose one, explicitly record not-disclosed.
4. Set the environment variables named by api_key_env. Never put API keys in the config.
5. Enter verified input/output prices per million tokens in USD, or leave both null. Record the provider pricing source and effective date separately in any published report.
6. Keep temperature and output-token limits consistent where possible. Provider tokenization and serving stacks are not directly comparable.

Never commit API keys, local configuration, generated outputs, personal data, or confidential test cases.

## Validate and test without API calls

From the repository root:

    python -m unittest discover -s evaluation/tests -v
    python evaluation/run_eval.py --config evaluation/config.example.json --cases evaluation/cases.jsonl --validate-only

The example configuration is structurally valid but contains placeholder model IDs and is not ready for paid API calls.

## Run a real evaluation

Set the environment variables referenced by the local config, then run:

    python evaluation/run_eval.py --config evaluation/config.local.json --cases evaluation/cases.jsonl --output-dir evaluation-results

The runner does not silently retry failed requests. It preserves per-case failures in the JSONL results. Run comparisons in a controlled time window and avoid concurrent provider load where practical. Generated result files should be reviewed and sanitized before publication.

## Reproducibility, scoring, and limitations

- Configuration, test-set, and system-prompt SHA-256 hashes, UTC timestamps, settings, provider, endpoint, model ID, and declared model version are recorded.
- Accuracy across all cases is the primary category score: schema failures and request errors count as incorrect. Accuracy among valid outputs is shown separately to expose conditional performance, not as a substitute for the all-case score.
- Confusion matrices help identify systematic label confusions. The dataset is small and synthetic; 40 examples cannot support broad model rankings or statistically strong claims.
- A hosted model alias may change; a model ID does not prove an immutable snapshot. Temperature zero does not guarantee deterministic outputs.
- Identical settings do not equalize tokenization, safety layers, provider wrappers, or inference infrastructure.
- The task metric does not grade summary quality, rationale quality, calibration, or actual support-routing outcomes. Human review remains necessary.
- Provider token counts and configured prices are not independently audited. Cached-token discounts, batch pricing, taxes, minimum charges, and billing adjustments may not be represented.
- Latency is client-observed request round-trip time, including network effects; it is not pure model-inference time.
- Request failures, malformed responses, and format failures must remain visible in reports. Do not silently discard them or publish only the best run.
- No real cross-model results are included until provider API calls are performed and the resulting artifacts are reviewed.

## Publication checklist

Publish sanitized configuration, case-set and prompt hashes, run date/time, provider and exact model IDs, version disclosure, settings, counts and denominators, per-case results or a reviewable sanitized subset, all error and format-failure counts, confusion matrices, token usage, pricing source/date/currency, cost assumptions, latency methodology, and limitations. Include independent reviewer's scoring notes. Do not claim one model is better based on this small synthetic fixture alone.

For high-impact use, create a larger domain-specific test set, independently adjudicate labels, run multiple repetitions where stochasticity matters, and validate against real task outcomes before drawing operational conclusions.
