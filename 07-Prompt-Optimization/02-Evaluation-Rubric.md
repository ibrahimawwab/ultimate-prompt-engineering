# A Practical Rubric for Evaluating Prompt Outputs

A rubric converts vague judgments into observable criteria. Adapt the criteria to the task; not every task needs every dimension.

## Core criteria

Score each criterion from 0 to 4. Define task-specific anchors before evaluating outputs.

| Criterion | 0 — Fails | 2 — Partial | 4 — Meets requirement |
| --- | --- | --- | --- |
| Task completion | Does not perform the task | Performs part of the task; important gaps remain | Completes the defined task |
| Factual support | Contains material unsupported or false claims | Mostly plausible but some claims need verification | Claims are supported by supplied evidence or clearly qualified |
| Instruction adherence | Violates critical instructions | Follows most instructions with minor violations | Follows all applicable instructions |
| Format validity | Unusable or invalid structure | Mostly valid with repairable defects | Fully conforms to the output contract |
| Safety and privacy | Creates a material safety or privacy failure | Risk is incompletely handled | Respects constraints and handles risk appropriately |
| Robustness | Breaks on expected variations | Handles common variations but misses edge cases | Handles the defined test variations |

## Add task-specific criteria

Examples include code execution success, citation traceability, reading-level suitability, extraction precision, or classification accuracy. Define criteria in terms of observable evidence.

## Critical failures and weighting

A high average must not hide a critical failure. Define critical failures before testing, such as exposing a secret, inventing a source, violating a required schema, or requesting an unauthorized action. A critical failure may disqualify an output regardless of its numeric score.

If criteria have different importance, define weights before reviewing outputs. Document the rationale. Do not change weights after seeing results to make a preferred prompt win.

## Reviewer procedure

1. Remove prompt-version labels from outputs where practical.
2. Apply the same rubric to every output.
3. Record evidence for each non-obvious score.
4. Have a second reviewer independently score a sample when warranted.
5. Resolve disagreements by clarifying the rubric, not by silently averaging incompatible interpretations.
6. Preserve examples of failures and borderline cases.

## Limits of automated judging

An LLM judge can help triage or compare outputs, but it is not ground truth. It may share the evaluated model's biases, prefer longer answers, miss subtle factual errors, or be sensitive to presentation. Validate judge decisions against human review and objective checks where available. For critical tasks, use independent evidence and domain-qualified reviewers.

## Reporting

Present per-criterion scores, critical-failure counts, sample size, reviewer method, and uncertainty. An average score is a summary, not proof of correctness or safety.

## Exercise

Apply this rubric to five outputs from the same prompt. Write a one-sentence justification for every score below 4 and identify whether any critical failure overrides the average.
