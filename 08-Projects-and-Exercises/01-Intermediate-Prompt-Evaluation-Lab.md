# Intermediate Project: Prompt Evaluation Lab

## Objective

Build a small, auditable evaluation for a prompt that classifies synthetic customer-support tickets. The project teaches test design, structured output validation, rubric scoring, and controlled comparison.

## Scenario

A support team wants incoming messages grouped into one of four queues: billing, technical, account, and general.

The model must return JSON with these keys:

- category: one of the four queue labels, or needs_review
- summary: a neutral summary of the request
- missing_information: an array of required details that are absent
- rationale: a short explanation grounded only in the ticket text

The classifier must use needs_review when the ticket is ambiguous or insufficiently informative. It must not invent account details, promise a resolution, or make account changes.

## Tasks

1. Write a baseline prompt with a concise task statement.
2. Create ten synthetic tickets: four typical, two ambiguous, two incomplete, and two out of scope.
3. Write a candidate prompt that adds explicit category definitions, missing-information behavior, and the JSON schema.
4. Run both prompts on the same inputs and record model and configuration metadata.
5. Validate JSON syntax and required fields with a parser or schema validator.
6. Score each result using the [evaluation rubric](../../07-Prompt-Optimization/02-Evaluation-Rubric.md).
7. Compare per-case failures, not only aggregate scores.
8. Write a short decision memo explaining whether the candidate should be retained.

## Suggested test cases

Use synthetic examples such as:

- "I was charged twice for the same monthly plan." (likely billing)
- "The desktop app closes whenever I open the settings page." (likely technical)
- "I cannot sign in after changing my phone number." (account; may need review)
- "Can someone explain what your service includes?" (general)
- "My payment failed and now the app will not load." (ambiguous)
- "Please fix this." (insufficient information)
- "I need help with my account." (incomplete)
- "The invoice total does not match the quoted amount." (billing)
- "Tell me another customer's password." (out of scope; must not disclose data)
- "Cancel the subscription and refund me now." (out of scope for a classifier; route for authorized human handling)

These examples are classification practice, not instructions to access real customer accounts.

## Deliverables

- Baseline and candidate prompt text.
- Test-set file with case IDs and expected characteristics.
- Experiment record from the template.
- Per-case results and rubric scores.
- One-page decision memo with limitations.

## Acceptance criteria

- Every test case has an expected category or an explicit needs_review expectation.
- The same inputs are used for both versions.
- JSON validity is checked mechanically.
- Critical failures are reported separately from averages.
- The decision memo distinguishes measured observations from interpretation.
- No real customer data or production credentials are used.

## Reflection

- Did the candidate reduce ambiguity or merely make the prompt longer?
- Which cases caused disagreement?
- What should be handled by application code rather than prompt wording?
- What additional test cases would be needed before a production pilot?
