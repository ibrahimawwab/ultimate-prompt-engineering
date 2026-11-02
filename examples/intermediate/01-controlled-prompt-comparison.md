# Controlled Prompt Comparison: Ticket Classification

This worked example demonstrates an evaluation design. It does not report model benchmark results.

## Task

Classify a synthetic support message into billing, technical, account, general, or needs_review. Return valid JSON with category, summary, missing_information, and rationale.

## Baseline prompt

> Classify the support ticket into billing, technical, account, or general. Return JSON with category and summary.

## Candidate prompt

> Classify the supplied ticket into exactly one of: billing, technical, account, general, or needs_review. Use only information in the ticket. If the message plausibly belongs to multiple categories or lacks enough information, choose needs_review. Do not infer customer identity, account state, or actions already taken. Return one JSON object with exactly these keys: category (string), summary (string), missing_information (array of strings), rationale (string). Do not include Markdown fences or text outside the JSON object.

## Example input

> I was charged twice this month for the same subscription.

## Expected characteristics

- Category should be billing.
- Summary should mention a reported duplicate charge.
- Missing information may include transaction dates or references if needed for follow-up.
- Rationale should cite the duplicate-charge wording.
- The output must not claim that a refund has been issued.

There is no single required wording.

## Evaluation plan

Run both prompts against the same fixed test set. Check JSON parsing and exact key presence automatically. Score task completion, factual support, instruction adherence, format validity, safety, and robustness. Record all failures.

## Result record

No model was run as part of this static teaching example. Fill in provider, model/version, date, settings, test-set revision, run count, scores, and representative outputs only after conducting an actual experiment.

## Lesson

The candidate makes ambiguity handling and output constraints explicit. Whether that improves real performance is an empirical question; this example alone does not establish an improvement.
