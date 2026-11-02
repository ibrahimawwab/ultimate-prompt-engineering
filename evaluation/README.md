# Reproducible Cross-Model Evaluation

This directory contains a standard-library evaluation harness with native request/response adapters for three API formats: OpenAI-compatible Chat Completions, Anthropic Messages, and Google Gemini generateContent. Separate adapters are necessary because authentication, request bodies, response structures, and token-usage fields differ.

## Dataset and metrics

The fixed synthetic dataset contains 40 English customer-support classification cases across five labels: billing, technical, account, general, and needs_review. Cases are tagged by difficulty (easy, medium, hard) and topic. The set includes boundary cases, multi-intent requests, underspecified inputs, sensitive requests, and a prompt-injection-style ticket. Labels are a teaching fixture and should be reviewed before consequential use.

Each model receives the same system prompt, ticket text, and 512-token output ceiling. Provider-specific controls are not identical:

- OpenAI GPT-6 Luna: Chat Completions, reasoning_effort=none, temperature=0, max_completion_tokens=512, service_tier=default (standard pricing).
- Anthropic Claude Haiku 5.5: Messages API version 2026-10-21, output_config.effort=low, max_tokens=512, temperature omitted. Adaptive thinking is enabled by default; thinking tokens count toward max_tokens.
- Google Gemini 3.8 Flash: generateContent, thinkingLevel=low, temperature omitted because Gemini 3.8 documentation instructs clients to remove temperature, top_p, and top_k. maxOutputTokens=512.

The Gemini and Anthropic settings are low-effort profiles, while OpenAI uses no reasoning. This is a pragmatic low-cost comparison profile, not an exact equality of inference effort. The 512-token cap includes reasoning/thinking tokens where the provider defines them as part of generated output.

All three providers receive the same required JSON object schema through their native structured-output mechanism: OpenAI response_format JSON Schema, Anthropic output_config.format JSON Schema, and Gemini generationConfig.responseFormat. The category value is checked against the five allowed labels by the local evaluator; it is not forced by the schema enum. Provider constrained-decoding implementations differ, so format success is still measured and reported separately.

Per-case results include raw output, schema validation, expected/predicted labels, correctness, request status, latency, request ID when exposed, provider-reported token usage, finish reason, and estimated cost when configured. Summary metrics include request success rate, schema-valid rate, category accuracy across all cases (invalid output and request failures count as incorrect), accuracy among schema-valid outputs, confusion matrix, mean/median latency, token totals, and estimated cost.

## Supported adapters

| Adapter | API format | Authentication | Usage fields |
| --- | --- | --- | --- |
| openai_chat_completions | Chat Completions | Bearer token | prompt_tokens, completion_tokens |
| anthropic_messages | Messages API | Bearer token and anthropic-version | input_tokens, output_tokens |
| google_generative_language | Gemini generateContent | x-goog-api-key | promptTokenCount, candidatesTokenCount, thoughtsTokenCount |

This is not a claim that every provider endpoint or compatible gateway has been tested. Use the exact documented endpoint for the selected model. The Google endpoint template substitutes the configured model ID into {model}. The Generate Content API remains supported but is documented as the legacy API; Google recommends its newer Interactions API for new projects. This adapter is intentionally scoped to the requested generateContent format. Verify request parameters against current provider documentation before a real run.

## Configure models

1. Copy config.example.json to a local file such as config.local.json; do not commit the local file.
2. The example profile contains current documented model IDs. Recheck provider availability and pricing before each run.
3. Record provider-returned model versions where available; a stable ID or alias is not necessarily an immutable snapshot.
4. Set the environment variables named by api_key_env. Never put API keys in the config.
5. Enter verified input/output prices per million tokens in USD, or leave both null. Record the provider pricing source and effective date separately in any published report.
6. Keep temperature and output-token limits consistent where possible. Provider tokenization and serving stacks are not directly comparable.

Never commit API keys, local configuration, generated outputs, personal data, or confidential test cases.

## Validate and test without API calls

From the repository root:

    python -m unittest discover -s evaluation/tests -v
    python evaluation/run_eval.py --config evaluation/config.example.json --cases evaluation/cases.jsonl --validate-only

The example configuration names GPT-6 Luna, Claude Haiku 5.5, and Gemini 3.8 Flash. Prices and sources were checked against official provider documentation on 2026-11-02. GPT-6 Luna standard short-context rates are USD 0.10 input / USD 0.50 output per million tokens; Claude Haiku 5.5 base rates are USD 0.10 / USD 0.50 for prompts up to 100,000 tokens; Gemini 3.8 Flash introductory rates are USD 0.75 / USD 3.75 through 2026-12-31. The profile still requires API credentials. Provider model identifiers may not be immutable snapshots.

## Run a real evaluation

Set the environment variables referenced by the local config, then run:

    python evaluation/run_eval.py --config evaluation/config.local.json --cases evaluation/cases.jsonl --output-dir evaluation-results

The runner makes one request per case and model and does not retry. It creates a combined per-case JSONL file, combined summary JSON, one per-model JSON file containing its summary and case rows, an error-only JSONL file, and a Markdown comparison report. Generated outputs should be reviewed and sanitized before publication.

## Reproducibility, scoring, and limitations

- Configuration, test-set, and system-prompt SHA-256 hashes, UTC timestamps, settings, provider, endpoint, model ID, declared model version, pricing source/date, and configured rates are recorded.
- Accuracy across all cases is the primary category score: schema failures and request errors count as incorrect. Accuracy among valid outputs is shown separately to expose conditional performance, not as a substitute for the all-case score.
- Confusion matrices help identify systematic label confusions. The dataset is small and synthetic; 40 examples cannot support broad model rankings or statistically strong claims.
- A hosted model alias may change; a model ID does not prove an immutable snapshot. Temperature zero does not guarantee deterministic outputs.
- Identical settings do not equalize tokenization, safety layers, provider wrappers, or inference infrastructure.
- The task metric does not grade summary quality, rationale quality, calibration, or actual support-routing outcomes. Human review remains necessary.
- Provider token counts and configured prices are not independently audited. Gemini billable output includes reported candidate and thinking tokens; if thinking-token usage is absent, cost is reported as unavailable rather than silently excluding it. Cached-token discounts, batch pricing, taxes, minimum charges, and billing adjustments may not be represented.
- Latency is client-observed request round-trip time, including network effects; it is not pure model-inference time.
- Request failures, malformed responses, and format failures must remain visible in reports. Do not silently discard them or publish only the best run.
- No real cross-model results are included until provider API calls are performed and the resulting artifacts are reviewed.

## Publication checklist

Publish sanitized configuration, case-set and prompt hashes, run date/time, provider and exact model IDs, version disclosure, settings, counts and denominators, per-case results or a reviewable sanitized subset, all error and format-failure counts, confusion matrices, token usage, pricing source/date/currency, cost assumptions, latency methodology, and limitations. Include independent reviewer's scoring notes. Do not claim one model is better based on this small synthetic fixture alone.

For high-impact use, create a larger domain-specific test set, independently adjudicate labels, run multiple repetitions where stochasticity matters, and validate against real task outcomes before drawing operational conclusions.

## Live evaluation through GitHub Actions

A separate manually triggered workflow runs the configured three-model comparison and uploads the JSONL/summary artifacts. It requires these repository Actions secrets:

- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- GOOGLE_API_KEY

The workflow is manually dispatched from main, requires an explicit billing-confirmation input, and does not run on pushes or pull requests. Before credentials are checked or provider requests are sent, it rejects pricing records older than 30 days or past their declared validity date, then prints a planning estimate. The current estimate is about USD 0.19 for 120 requests, based on one input token per character plus 1,000 characters of request-envelope and structured-schema overhead and a maximum of 300 generated tokens per request. This is a rough planning estimate, not a guaranteed upper bound or spending cap. The workflow makes no automatic retries, uses a 60-second per-request timeout, and checks for another live dispatch in the previous 24 hours and blocks GitHub reruns of an already attempted workflow. A repeat requires a second explicit workflow input. Concurrency serializes runs. API credentials are scoped only to the secret-check and live-request steps, not checkout or offline test steps.

## Verified model documentation (checked 2026-11-02)

- OpenAI GPT-6 Luna model and Chat Completions support: https://developers.openai.com/api/docs/models/gpt-6-luna and https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create
- OpenAI Structured Outputs: https://developers.openai.com/api/docs/guides/structured-outputs
- OpenAI standard short-context pricing: https://developers.openai.com/api/docs/pricing
- Anthropic Claude Haiku 5.5 model ID, effort, temperature, and pricing: https://platform.claude.com/docs/en/models/haiku-5-5/overview and https://platform.claude.com/docs/en/build-with-claude/effort
- Anthropic structured JSON outputs: https://platform.claude.com/docs/en/build-with-claude/structured-outputs
- Anthropic Messages API versioning: https://platform.claude.com/docs/en/api/versioning
- Gemini 3.8 Flash model and generation settings: https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash and https://ai.google.dev/api/generate-content
- Gemini Generate Content structured JSON responses: https://ai.google.dev/api/generate-content
- Gemini 3.8 Flash pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini API key authentication and key restrictions: https://ai.google.dev/gemini-api/docs/api-key

Google API key note: the workflow checks only that GOOGLE_API_KEY is non-empty. It cannot determine whether the key is a supported authorization key or a restricted standard key. Google's current guidance rejects unrestricted standard keys; ensure the configured key is appropriately restricted to the Gemini API or is a supported authorization key before a live run.
