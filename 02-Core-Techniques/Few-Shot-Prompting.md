# Few-Shot Prompting

## Overview

Few-shot prompting provides a small set of input-and-output demonstrations inside the prompt. The examples communicate the task, label meanings, style, or output pattern by showing what a successful result looks like.

It differs from fine-tuning: examples in a prompt are temporary context for that request and do not update model weights.

## When to use it

Use few-shot prompting when a task has a recurring pattern that is difficult to explain fully in prose—for example, classifying support requests, normalizing records, or matching a particular writing style.

## How to design examples

- Select examples that represent the range of expected inputs.
- Keep labels and output conventions consistent.
- Include boundary cases where ambiguity is common.
- Avoid examples that contradict the written instructions.
- Use the smallest set that demonstrates the pattern; more examples consume context and are not automatically better.

## Worked example: classify support requests

```text
Classify each message as BILLING, TECHNICAL, or ACCOUNT.
Return only the label.

Example 1
Message: "I was charged twice this month."
Label: BILLING

Example 2
Message: "The mobile app closes whenever I upload a photo."
Label: TECHNICAL

Example 3
Message: "I cannot reset my password."
Label: ACCOUNT

Now classify:
Message: "My invoice shows a fee I do not recognize."
Label:
```

Expected label: `BILLING`.

The demonstrations establish the label set and illustrate how to map messages to it.

## Limitations and failure modes

- Poor or unrepresentative examples can teach the wrong pattern.
- The model may imitate accidental details in examples, including formatting errors.
- Similar examples may not cover unusual or adversarial inputs.
- Too many examples can crowd out the actual task or relevant context.
- Example order and wording can affect results; behavior is model-dependent.

Do not use examples as the sole control for safety-sensitive classification. Validate outputs and use deterministic rules where possible.

## Best practices

1. Define the task and labels before showing examples.
2. Use balanced, representative examples.
3. Include at least one difficult or borderline case when relevant.
4. Separate examples clearly from the new input.
5. Evaluate on held-out cases that were not included in the prompt.

## Exercise

Create three examples for classifying feedback as BUG, FEATURE_REQUEST, or PRAISE. Then create a test set of at least ten new messages. Record accuracy and inspect every error. Add or revise examples only when the change addresses a demonstrated failure.

## Further reading

- [Google Cloud: Prompt design strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies)
- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
