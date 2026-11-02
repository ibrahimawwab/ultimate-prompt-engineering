# Meta-Prompting

## Overview

Meta-prompting uses a model to help design, critique, or improve prompts. The model may transform a task description into a prompt template, identify ambiguities, or propose test cases.

It is an iterative design aid—not an automatic guarantee that the resulting prompt is effective.

## When to use it

Use meta-prompting when a task is recurring, has multiple constraints, or needs a reusable template. It is less valuable for a one-off task whose instructions are already clear.

## Example

```text
Help design a reusable prompt for this task:
[Describe the task and intended users.]

First identify:
- missing requirements;
- ambiguous terms;
- required inputs;
- output fields and constraints;
- likely failure cases.

Then draft a prompt template with clearly marked variables.
Do not invent requirements. List assumptions separately.
Finally propose five test cases, including one edge case and one unanswerable case.
```

Review the proposed template against the real task specification. Run it on a held-out test set and revise based on observed failures.

## Limitations

- The model may optimize for clarity or style rather than actual task performance.
- It may introduce unsupported requirements or omit important constraints.
- A prompt can appear polished while failing on edge cases.
- Prompt improvements may not transfer across models or versions.

## Best practices

Keep the original task specification as the source of truth. Version prompts, retain test cases, compare candidate versions against a baseline, and document the model and settings used. Require human review before deploying prompts in consequential workflows.

## Exercise

Ask a model to generate a prompt for extracting structured fields from invoices. Review the template, create 12 varied test documents, and compare its output with a manually verified reference set. Report exact field-level errors before accepting revisions.

## Further reading

- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
