# Reproducible Cross-Model Evaluation

This directory contains a standard-library harness for comparing configured models through OpenAI-compatible Chat Completions endpoints. This is an intentionally narrow first adapter; it does not claim support for every provider or API format.

## What it measures

The fixed synthetic ticket-classification set contains 12 cases. Each configured model receives the same system prompt, user inputs, temperature, and maximum output-token setting. The model identifier necessarily differs by provider.

The runner records per case: raw output and strict JSON/schema validation; predicted and expected category with exact-match correctness; provider-reported input/output token usage when available; request latency; estimated cost only when token usage and both input/output prices are configured; and API/configuration errors without silently dropping failed cases.

The summary reports schema-valid rate, category accuracy among schema-valid outputs, errors, format failures, token totals, mean latency, and estimated cost when calculable. Accuracy is not divided by all cases when some outputs fail schema validation; those failures remain separately visible.

## Requirements and compatibility

- Python 3.10 or newer; no third-party Python packages.
- API credentials for each selected provider.
- A compatible POST endpoint accepting model, messages, temperature, and max_tokens and returning choices[0].message.content. Usage fields are optional.

Some providers use different parameter names, authentication, response shapes, or API protocols. They require a dedicated adapter rather than being described as compatible without verification.

## Configure models

1. Copy config.example.json to a local file such as config.local.json. Do not commit the local file.
2. Replace example URLs and model IDs with exact values from provider documentation.
3. Record the exact model version or release identifier. If undisclosed, write not-disclosed and document that limitation.
4. Set API-key environment variable names and provide secrets through your local environment or a CI secret store.
5. Enter verified per-million-token input and output prices in USD. Do not enter a price in another currency; convert separately and document exchange rate/date if needed.
6. Leave prices null if the applicable rate is unknown. Cost will remain unreported rather than guessed.

Never commit API keys, local configuration, production prompts, personal data, or confidential test cases.

## Validate without API calls

From the repository root:

    python -m unittest discover -s evaluation/tests -v
    python evaluation/run_eval.py --config evaluation/config.example.json --cases evaluation/cases.jsonl --validate-only

The example config is structurally valid but intentionally not runnable until endpoints, model IDs, model versions, and environment variables are configured.

## Run a real evaluation

Set the environment variables referenced by your local config, then run:

    python evaluation/run_eval.py --config evaluation/config.local.json --cases evaluation/cases.jsonl --output-dir evaluation-results

The runner creates per-case JSONL and summary JSON files. Keep generated results outside the repository unless sanitized, reproducible, and intentionally approved for publication. Review raw outputs before sharing them.

## Reproducibility and limitations

- Configuration, test-set, and system-prompt SHA-256 hashes, UTC timestamps, settings, provider URL, model ID, and declared model version are recorded.
- A hosted model alias may change; a model ID does not prove an immutable snapshot.
- Temperature zero does not guarantee deterministic outputs across providers or model updates.
- Identical prompts and settings do not equalize tokenization, system wrappers, safety layers, or inference stacks.
- The task metric is exact-match category accuracy. It does not assess summary quality, rationale quality, or real-world routing outcomes.
- Schema validity is reported separately. Valid JSON can still be wrong or unsafe.
- Provider token counts and configured prices are not independently audited. Cached-token discounts, batch pricing, taxes, minimum charges, and billing adjustments are not modeled.
- Failed requests are recorded and not silently retried. Transient failures should be handled in a separately documented rerun.
- The 12-case synthetic set is a teaching fixture, not a statistically representative benchmark. It cannot support broad model rankings or capability claims.
- No empirical cross-model results are included until real runs are completed and reviewed.

## Reporting checklist

Before publishing results, include sanitized config, test-set and prompt hashes, exact model IDs and version disclosures, run date/time, settings, run counts, per-case outputs or a reviewable sanitized subset, schema failures, category errors, API errors, token usage, pricing source/date/currency, cost assumptions, latency method, and limitations. Report counts with denominators. Preserve failures; do not publish only the best run.

For consequential use, expand the test set, add domain-specific criteria, include independent human review, and validate against real task outcomes before drawing conclusions.
