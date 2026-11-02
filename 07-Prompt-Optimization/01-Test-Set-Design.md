# Test-Set Design for Prompt Evaluation

A prompt should be evaluated on inputs that represent its intended task. One impressive example is not evidence of general reliability.

## Define the task contract

Specify the task, input format, output contract, observable success criteria, failure conditions, and out-of-scope cases. Keep the task narrow enough for consistent review.

## Build a representative set

Include typical cases, boundary cases with missing or malformed inputs, difficult constraint-following cases, negative cases that require clarification or abstention, and distribution-shift cases. Use synthetic or appropriately licensed data. Exclude personal data, credentials, secrets, and confidential records.

## Separate development and holdout cases

Use a development set to improve the prompt. Keep a holdout set untouched until a candidate is ready. Repeatedly tuning against the holdout set turns it into development data. For small educational exercises, state that the set is illustrative and too small to support statistical generalization.

## Avoid leakage and accidental bias

- Do not place expected answers in the prompt unless that is part of the task.
- Do not make test cases that merely repeat the prompt's examples.
- Do not discard difficult cases because they lower the score.
- Use the same test inputs for baseline and candidate versions.
- Record manual edits, retries, and exclusions.

## Test-set record

For each case, record an ID, input, category, expected characteristics, critical constraints, and evaluation notes. Expected characteristics should describe what a valid answer must contain, not require exact wording unless exact wording is part of the contract.

## Reporting

Report the number of cases and their categories. Show per-criterion results and important failure examples, not only an aggregate score. A small test set supports local diagnosis, not a universal claim about model quality.

## Exercise

Create ten synthetic test cases for a structured support-ticket classifier: four typical tickets, two ambiguous tickets, two with missing information, and two out-of-scope requests. Define the expected schema and one critical failure condition for each category. Keep at least two additional cases as holdout data.

## Further reading

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [HELM: Holistic Evaluation of Language Models](https://crfm.stanford.edu/helm/)
