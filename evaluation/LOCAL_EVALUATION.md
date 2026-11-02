# Zero-cost local model evaluation

This is a separate evaluation path from the optional hosted-provider runner. It uses Ollama on the user's own computer and sends inference requests only to a loopback address (127.0.0.1, localhost, or ::1). It does not read API-key environment variables, call OpenAI/Anthropic/Google endpoints, or require hosted model credentials.

## Model profile

The example configuration defaults to **Qwen3 1.7B** through Ollama as `qwen3:1.7b`. This is the recommended starting point for a Windows computer with 8 GB of system RAM. The smaller model reduces memory pressure compared with Qwen3 4B, but may deliver lower classification accuracy; the evaluation must measure that trade-off rather than assume parity.

- Ollama Qwen3 model listing and available tags: https://ollama.com/library/qwen3
- Qwen3 model family and Apache-2.0 license information: https://github.com/QwenLM/Qwen3
- Ollama local chat API and JSON-schema structured outputs: https://github.com/ollama/ollama/blob/main/docs/api.md

Model download size is not the same as required runtime RAM. Actual memory use depends on quantization, context length, runtime, operating system, and other processes. Close memory-intensive applications before running a benchmark. If Qwen3 1.7B is stable and sufficient, retain it as the baseline. A larger model such as `qwen3:4b` can be added later only if measured memory headroom permits it.

The model tag is not treated as immutable. The runner records the local digest from Ollama's `/api/tags` response when available, plus the Ollama version. Review the actual downloaded model metadata before redistribution or publication.

## Install and prepare (Windows)

1. Install Ollama from https://ollama.com/download/windows.
2. Start Ollama. Its local API normally listens on `http://127.0.0.1:11434`.
3. Open Command Prompt or PowerShell and download the recommended model once:

       ollama pull qwen3:1.7b

   This downloads model weights to your computer. It is not an API purchase, but it uses disk space and internet bandwidth. The model pull is intentionally not part of GitHub Actions.
4. Verify the model is installed:

       ollama list

   Confirm that `qwen3:1.7b` appears in the list.
5. From the repository root, run offline validation:

       python evaluation/run_local_eval.py --validate-only

6. When ready, run the full 40-case local evaluation:

       python evaluation/run_local_eval.py --output-dir evaluation-results

No API key or paid provider account is used by this command.

## Compare additional local models

Edit `evaluation/config.local.example.json` or create an untracked local copy and add another entry to `models`, for example:

       {
         "name": "qwen3-4b",
         "model": "qwen3:4b",
         "license": "Apache-2.0",
         "license_url": "https://ollama.com/library/qwen3:4b"
       }

Pull each selected model manually with `ollama pull MODEL_TAG` before running. On an 8 GB computer, do not run multiple models concurrently; test a larger model only after confirming that the smaller baseline runs reliably. Each model receives the same 40 cases and prompt. Use exact model tags and retain output artifacts so comparisons can be reproduced.

## Output artifacts

Each run creates:

- Combined per-case JSONL with raw model output, expected/predicted category, validation, status, latency, and available Ollama usage/duration fields.
- One per-model JSON report with model metadata, aggregate metrics, confusion matrix, and per-case rows.
- Summary JSON with hashes, run timestamps, environment metadata, and metrics.
- Error-only JSONL.
- Markdown comparison report.

Metrics include all-case category accuracy, accuracy on valid outputs, valid-output rate, request success rate, invalid outputs, failed requests, confusion matrix, mean/median client-observed latency, and token totals where complete. Token counts are null, not zero, when any case lacks provider-reported usage. The standard-library runner records OS, Python, CPU architecture/processor string, and logical CPU count; it does not reliably detect physical RAM or GPU details.

## Tests and GitHub Actions

Run all offline tests:

       python -m unittest discover -s evaluation/tests -v

Validate the example configuration and dataset:

       python evaluation/run_local_eval.py --config evaluation/config.local.example.json --cases evaluation/cases.jsonl --validate-only

The local-evaluation GitHub Actions workflow runs tests and configuration/dataset validation only. It does not install Ollama, download model weights, invoke inference, or use hosted-provider secrets. GitHub-hosted runner usage remains subject to the repository owner's included Actions quota and applicable GitHub terms.

## Cost and limitations

- No commercial model API calls or API credits are required for this path.
- Local model downloads use bandwidth and disk space; inference uses the user's CPU/GPU, RAM, electricity, and time.
- The 40-case dataset is synthetic and small. It is useful for functional comparison, not a statistically strong general-purpose model ranking.
- A local benchmark measures this computer's runtime and the selected quantized model, not abstract model capability alone.
- Ollama may expose cloud model features separately; this runner rejects non-loopback URLs, disables environment-configured HTTP proxies, and rejects redirects so prompts cannot be forwarded away from the local endpoint.
- The optional paid-provider adapters and their separate workflow are not part of this free evaluation path. Do not trigger the live hosted-provider workflow for a zero-cost run.
