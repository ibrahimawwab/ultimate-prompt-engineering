# Zero-Shot Prompting

## Overview

Zero-shot prompting asks a model to perform a task using instructions and context, without supplying task-specific demonstrations. The model relies on patterns learned during training and the information in the current conversation.

## When to use it

Use zero-shot prompting when the task is familiar, the instructions can be stated clearly, and no specialized output pattern needs demonstration. It is a useful baseline before adding examples or more elaborate prompt structures.

## How to write one

Specify the objective, relevant input, constraints, and output format. Define ambiguous terms and state how missing or uncertain information should be handled. Keep unrelated context out of the prompt.

## Worked example

### Weak prompt

```text
Summarize this.
```

### Improved prompt

```text
Summarize the report below for a non-specialist reader.

Requirements:
- Use 4–6 bullet points.
- Preserve the report's key findings and numerical values.
- Distinguish reported facts from recommendations.
- Do not add information absent from the report.
- If a passage is unclear, identify it rather than guessing.

Report:
[Paste report]
```

The improved version makes the audience, scope, structure, and uncertainty behavior explicit.

## Limitations and failure modes

- A model may interpret underspecified tasks differently than intended.
- Zero-shot performance can vary with model, version, task difficulty, and context.
- Instructions cannot supply facts that are absent from the prompt or the model's reliable knowledge.
- A confident answer is not evidence of correctness.
- Long or conflicting instructions can reduce compliance.

For high-impact tasks, verify outputs against authoritative sources and domain review. Treat zero-shot as a baseline, not a quality guarantee.

## Best practices

1. State one primary objective.
2. Provide only relevant context.
3. Define audience, scope, constraints, and output shape.
4. Include a rule for missing information.
5. Test representative easy, typical, and difficult inputs.

## Exercise

Write a zero-shot prompt that extracts the date, organization, decision, and action items from a meeting note. Test it on a note with one missing field. Revise the prompt so the model marks missing values as `Not stated` instead of inferring them.

## Further reading

- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google Cloud: Prompt design strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies)
