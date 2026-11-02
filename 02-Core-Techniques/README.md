# 02 — Core Techniques

Learn established prompting patterns, understand their trade-offs, and select techniques based on task requirements. No technique is universally best; evaluate results on representative inputs.

## Learning outcomes

After completing this section, you should be able to:

- establish a baseline with zero-shot prompting;
- use demonstrations to communicate patterns with few-shot prompting;
- use role framing without overstating model capabilities;
- write explicit, testable instructions;
- supply relevant context with provenance and uncertainty handling;
- request structured outputs and validate them outside the prompt.

## Lessons

1. [Zero-Shot Prompting](Zero-Shot-Prompting.md)
2. [Few-Shot Prompting](Few-Shot-Prompting.md)
3. [Role-Based Prompting](Role-Based-Prompting.md)
4. [Instructional Prompting](Instructional-Prompting.md)
5. [Contextual Prompting](Contextual-Prompting.md)
6. [Structured-Output Prompting](Structured-Output-Prompting.md)

Each lesson includes a worked example, appropriate use cases, limitations, best practices, and an exercise.

## Suggested practice sequence

1. Solve a task with a clear zero-shot prompt and record the result.
2. Add representative demonstrations and compare the few-shot result.
3. Rewrite the task with explicit instructions and relevant context.
4. Request a structured response and validate it against a schema.
5. Compare outputs using the same test set and a written evaluation rubric.

## Evaluation checklist

- Does the output satisfy the actual task?
- Are factual claims supported by the supplied context or reliable sources?
- Are missing and ambiguous values handled explicitly?
- Does the format pass mechanical validation?
- Does the prompt behave acceptably on edge cases and adversarial inputs?

Prompting is not a security boundary. Enforce permissions, access controls, and validation in the application that uses model outputs.
