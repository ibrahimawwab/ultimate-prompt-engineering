# What Is Prompt Engineering?

## Introduction

Prompt engineering is the practice of designing, structuring, and evaluating the inputs and surrounding instructions given to a generative AI model so that it is more likely to produce useful results for a defined task.

A prompt may contain a task, background context, source material, examples, constraints, and an expected output format. In an application, it may also be assembled from system instructions, user input, retrieved information, and tool results.

Prompt engineering is not a way to guarantee truth or force a model to behave perfectly. It is one part of a larger process that can include data preparation, retrieval, software validation, permissions, monitoring, and human review.

## Why it matters

A vague request leaves important decisions to the model: what the user means, which details matter, how long the response should be, and what counts as success. A well-specified request reduces avoidable ambiguity and makes the result easier to evaluate.

Prompt design is especially useful when a task has:
- A clearly defined objective.
- Relevant context that the model would not otherwise know.
- Constraints such as audience, length, tone, or allowed sources.
- A required structure, schema, or set of fields.
- Criteria that can be used to assess the output.

## A practical prompt model

A useful starting structure is:

1. **Task:** What should the model do?
2. **Context:** What information does it need?
3. **Constraints:** What must it include, avoid, or preserve?
4. **Output:** What form should the answer take?
5. **Evaluation:** What properties would make the answer acceptable?

Not every prompt needs all five parts. Simple tasks may need only a direct instruction. Add structure when it resolves a real ambiguity.

## Weak prompt versus improved prompt

**Weak:**

> Tell me about cybersecurity.

This does not specify the audience, scope, purpose, or expected level of detail.

**Improved:**

> Explain the difference between authentication and authorization for a beginner studying application security. Use plain language, one practical example for each concept, and a short comparison table. Do not assume the reader has prior security experience. End with three review questions.

The improved version gives the model a defined audience, scope, format, and completion criteria. It still requires review for technical accuracy.

## How to develop a prompt

1. Write the desired outcome in one sentence.
2. Identify information the model needs and supply only relevant context.
3. State constraints explicitly, including what to do when information is missing.
4. Specify a useful output format.
5. Test the prompt on several representative inputs.
6. Inspect errors and revise one important variable at a time.
7. Keep a record of the model, version, settings, and test cases when reproducibility matters.

## Common use cases

- **Learning:** request explanations at a specified level, followed by practice questions.
- **Writing:** specify audience, purpose, tone, length, and facts that must remain unchanged.
- **Software development:** provide language, framework, constraints, expected behavior, and test requirements.
- **Research support:** define the research question, source standards, date range, and uncertainty handling.
- **Data work:** describe the fields, allowed transformations, output schema, and validation rules.

## Limitations and failure modes

- **Incorrect outputs:** a clear prompt can still produce false or incomplete information.
- **Missing context:** the model cannot reliably infer private, local, or unstated facts.
- **Ambiguous instructions:** conflicting requirements can lead to inconsistent results.
- **Model variation:** different models and versions may respond differently to the same prompt.
- **Prompt injection:** instructions embedded in untrusted content may attempt to redirect a model or tool-enabled workflow.
- **False confidence:** fluent wording is not evidence that a claim is correct.

For consequential decisions, verify important claims against authoritative sources and involve qualified human reviewers. In software systems, enforce access control and validation outside the prompt.

## Best practices

- Be explicit about the task and intended audience.
- Include only context that helps complete the task.
- Separate instructions from quoted or retrieved source material.
- Define output structure when downstream processing depends on it.
- Ask the model to identify missing information rather than invent it.
- Evaluate with multiple cases, including edge cases.
- Track changes so improvements can be compared fairly.
- Protect confidential information and credentials.

## Summary

Prompt engineering is disciplined task specification and evaluation for generative AI systems. Strong prompts make goals, context, constraints, and expected outputs clear. Reliable results still depend on model capability, source quality, testing, validation, and appropriate human oversight.

## Further reading

- [OpenAI documentation](https://platform.openai.com/docs/)
- [Anthropic documentation](https://docs.anthropic.com/)
- [Google AI for Developers](https://ai.google.dev/)
- [Prompt engineering guide — DAIR.AI](https://www.promptingguide.ai/)
