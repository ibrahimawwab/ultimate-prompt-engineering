# Controlled Prompt Experiments

Prompt iteration is an experiment. Change a defined factor, hold other conditions as constant as practical, and record the outcome.

## Baseline and candidate

- **Baseline:** the current prompt or simplest reasonable instruction.
- **Candidate:** the revised prompt with a documented change.
- **Hypothesis:** a falsifiable statement about the expected improvement.
- **Test set:** the same representative inputs for both versions.
- **Evaluation:** a predefined rubric and task-specific automated checks.

Avoid changing the prompt, model, tools, retrieval corpus, and decoding settings simultaneously. If multiple factors must change, document a factorial or staged design.

## Control the comparison

Record provider, model identifier and version when available, date, system/developer instructions, sampling settings, tool configuration, retrieval snapshot, and relevant application version. If a value is unavailable, write UNKNOWN; do not infer it.

Use identical inputs and equivalent settings for both prompt versions. Where outputs are stochastic, repeat runs when feasible and report the number of runs. Do not select only the best completion.

## Example hypothesis

"Adding an explicit JSON schema and a rule to return needs_review when required fields are absent will reduce invalid outputs on the fixed test set without increasing incorrect confident classifications."

Test this with schema validation and reviewer assessment. Do not assume the candidate will succeed.

## What to measure

- Task-specific success or error rate.
- Per-criterion rubric scores.
- Critical failures.
- Schema or parser validity.
- Latency and token usage when available and relevant.
- Reviewer disagreement and unresolved uncertainty.

Report numerator and denominator, not only percentages. For small samples, show raw counts and avoid implying statistical significance.

## Iteration protocol

1. Freeze and label the baseline prompt.
2. Write the hypothesis and planned change.
3. Run both versions against the same cases.
4. Validate outputs mechanically where possible.
5. Score outputs using the predeclared rubric.
6. Inspect regressions and critical failures.
7. Accept, reject, or run another experiment.
8. Preserve prompts, test data, outputs, scores, and metadata.

## Interpretation

A result on one model and one test set applies only to that setup. Model updates, provider changes, prompt wrappers, tools, and user populations can change behavior. Re-run evaluations after material changes. A prompt that scores higher on a narrow test set may still be worse in production.

## Exercise

Compare a baseline ticket-classification prompt with a candidate that adds explicit missing-field handling. Use the same ten cases, schema validation, and rubric. Report regressions even if the overall score improves.
