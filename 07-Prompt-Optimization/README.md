# 07 — Prompt Optimization

Improve prompts through controlled experiments rather than intuition alone. A higher score on a small test set is not proof of general improvement.

## Lessons and tools

1. [Test-Set Design for Prompt Evaluation](01-Test-Set-Design.md)
2. [A Practical Evaluation Rubric](02-Evaluation-Rubric.md)
3. [Controlled Prompt Experiments](03-Controlled-Prompt-Experiments.md)
4. [Prompt Experiment Record Template](04-Experiment-Record-Template.md)

## Evaluation principles

- Compare baseline and candidate prompts on the same representative inputs.
- Define criteria and critical failures before running an experiment.
- Record provider, model/version, settings, test-set revision, and run count.
- Use automated validation where objective checks are available.
- Preserve per-case results and report regressions.
- Treat LLM-based judging as an aid, not ground truth.
- Do not claim cross-model performance without actual tests on identified models and versions.

Performance, cost, and latency trade-offs should be measured when relevant. If metadata or measurements are unavailable, mark them as unknown or not collected.
