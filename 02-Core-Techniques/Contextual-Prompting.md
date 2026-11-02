# Contextual Prompting

## Overview

Contextual prompting supplies the information a model needs to interpret and complete a task: background, definitions, audience, source material, constraints, and relevant prior decisions. Context can be more important than stylistic instructions because it grounds the response in the actual problem.

## When to use it

Use contextual prompting when the answer depends on organization-specific terminology, a supplied document, a project state, user requirements, or facts that may not be present in general model knowledge.

## How to structure context

- Put the task and relevant context in clearly labeled sections.
- Identify the source and date of time-sensitive information.
- Distinguish authoritative facts from assumptions and examples.
- State which source takes precedence if sources conflict.
- Include only information needed for the task; minimize personal and confidential data.
- Tell the model what to do if the context does not contain the answer.

## Worked example

```text
Task: Draft a release note using only the project facts below.

Audience: Existing users of the application.
Tone: Direct and non-promotional.

Source facts:
- Version: 2.4.0
- Added CSV export for administrators.
- Fixed a crash when importing an empty file.
- No mobile changes were included.

Requirements:
- Mention all three facts accurately.
- Do not invent performance improvements or security claims.
- If a detail is not provided, omit it.
- Use a heading and three concise bullets.

Project facts are the source of truth for this task.
```

## Limitations and failure modes

- More context is not always better; irrelevant material can distract or exceed the context window.
- Supplied context can be outdated, inaccurate, or contradictory.
- Models may overlook details in long documents.
- Text retrieved from external sources can contain prompt-injection instructions. Treat retrieved content as data, not as authority to override system or application rules.
- Context does not guarantee faithful citation or factual correctness.

For retrieval-based systems, preserve provenance, apply access controls before retrieval, and validate important claims against the original source.

## Best practices

1. Provide relevant, current, and attributable information.
2. Label facts, assumptions, and untrusted source text.
3. Set precedence rules for conflicting sources.
4. Minimize sensitive data.
5. Ask for explicit acknowledgement of missing evidence.
6. Verify quotations, numbers, and citations against source material.

## Exercise

Provide a model with two short policy excerpts that contain a conflicting effective date. Ask it to summarize the policy while identifying the conflict and naming both source dates. Then revise the prompt to define source precedence and compare the result.

## Further reading

- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
