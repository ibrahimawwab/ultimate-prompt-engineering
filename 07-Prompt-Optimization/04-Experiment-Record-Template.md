# Prompt Experiment Record Template

Copy this template for each experiment. Keep records with the relevant prompt versions and test-set revision.

## Experiment identity

- Experiment ID:
- Owner/reviewer:
- Date and time (include timezone):
- Task and intended users:
- Risk level and review requirements:

## Hypothesis and change

- Baseline prompt version or hash:
- Candidate prompt version or hash:
- Single planned change:
- Expected benefit:
- Possible regression or safety risk:
- Acceptance criteria defined before the run:

## Environment

- Provider:
- Model identifier:
- Model/version or release date:
- Interface/API version:
- System and developer instruction versions:
- Sampling settings:
- Tool configuration:
- Retrieval/data snapshot:
- Application or code commit:
- Unknown or unavailable metadata:

## Dataset

- Test-set identifier/revision:
- Development cases:
- Holdout cases:
- Number of cases and categories:
- Data provenance and license:
- Confirmation that sensitive data was excluded:

## Procedure

- Were the same inputs used for both prompts?
- Number of runs per case:
- Retry policy:
- Exclusions and reasons:
- Automated validators:
- Human reviewers and blinding method:

## Results

| Measure | Baseline | Candidate | Notes |
| --- | --- | --- | --- |
| Cases evaluated | | | |
| Task successes | | | |
| Schema-valid outputs | | | |
| Critical failures | | | |
| Mean rubric score (if meaningful) | | | |
| Median latency (if measured) | | | |
| Token/cost measure (if measured) | | | |

Attach or link per-case scores and representative failures. Do not report a measure that was not collected.

## Decision

- Decision: accept / reject / revise / inconclusive
- Evidence supporting decision:
- Regressions:
- Remaining risks:
- Limitations and threats to validity:
- Follow-up experiment:
- Reviewer sign-off:

## Reproducibility statement

State what another reviewer needs to reproduce the experiment and what cannot be reproduced (for example, an unavailable historical model version). Never claim exact reproducibility when the provider does not guarantee a fixed model or deterministic output.
