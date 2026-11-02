# Instructional Prompting

## Overview

Instructional prompting expresses the task as explicit directions. It makes the desired action, constraints, sequence, and completion criteria clear. It is often more valuable to improve the instructions than to add elaborate role-play or jargon.

## When to use it

Use explicit instructions for multi-constraint tasks, repeatable workflows, transformations, extraction, and outputs that must satisfy a defined specification.

## A practical instruction structure

A useful pattern is:

1. **Task:** what the model must do.
2. **Input:** what material it should use.
3. **Constraints:** what it must include, exclude, or preserve.
4. **Procedure:** any required order of operations.
5. **Output:** the expected structure and level of detail.
6. **Uncertainty:** what to do when information is missing or conflicting.
7. **Acceptance criteria:** how a successful result will be judged.

This is a checklist, not a universal syntax. Adapt it to the task.

## Worked example

```text
Task: Convert the notes below into a concise incident summary.

Instructions:
1. Extract the time, affected service, observed impact, and confirmed cause.
2. Separate confirmed facts from hypotheses.
3. Do not infer a cause if none is established.
4. Preserve identifiers and timestamps exactly.
5. List unresolved questions separately.

Output:
- Summary
- Confirmed facts
- Hypotheses (if any)
- Unresolved questions

Notes:
[Paste incident notes]
```

## Limitations and failure modes

- Instructions may conflict or leave important terms undefined.
- A model can miss a constraint, especially in long prompts or long outputs.
- A stated procedure does not prove the model followed it internally.
- Prompt instructions cannot enforce application permissions, data access controls, or other security boundaries.
- Exact compliance should be checked programmatically where possible.

## Best practices

- Use direct, testable language.
- Put critical constraints close to the relevant task.
- Avoid redundant or contradictory directions.
- Define what to do with missing, ambiguous, or out-of-scope input.
- Use schemas, validators, and tests for requirements that must be enforced.

## Exercise

Take a vague instruction such as "make this document better." Rewrite it as a task with a target audience, permitted edits, preserved facts, output format, and acceptance criteria. Test it on a document containing an ambiguous sentence and check whether the model flags rather than silently resolves the ambiguity.

## Further reading

- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic: Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
