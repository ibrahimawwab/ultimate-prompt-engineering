# Anatomy of a Prompt

## Introduction

A prompt is the information and instructions supplied to a model for a particular interaction. Depending on the product or application, it may include one or more messages, system-level instructions, user requests, examples, retrieved documents, tool results, or multimodal inputs.

There is no universal prompt syntax. The components below are a practical design checklist, not a mandatory format.

## Common components

### 1. Task or objective

State the action the model should perform. Prefer a specific verb and a defined deliverable.

- Vague: "Help with my report."
- Clearer: "Summarize the report's main findings in five bullet points for a non-technical manager."

### 2. Context

Provide the background facts needed to complete the task: audience, domain, purpose, relevant definitions, and source material. Include only information that is relevant and appropriate to share.

### 3. Constraints

State boundaries such as word count, tone, scope, date range, allowed sources, exclusions, or requirements to preserve original meaning. Avoid contradictory constraints.

### 4. Output format

Specify the desired form: paragraphs, table, checklist, JSON object, or another structure. If software consumes the output, define a schema and validate it in code rather than relying on formatting instructions alone.

### 5. Examples

Examples can demonstrate the expected transformation or style. They are most useful when the task is repetitive or the desired pattern is difficult to describe. Examples should be representative and should not contain sensitive data.

### 6. Uncertainty and missing information

Tell the model how to handle gaps: ask a clarifying question, state assumptions, mark unknown fields, or explain that the supplied information is insufficient. Do not instruct it to fill gaps with invented facts.

### 7. Evaluation criteria

Describe what a satisfactory result must achieve. Criteria might include factual fidelity, completeness, readability, schema validity, or coverage of required points.

## Example: building a prompt from components

**Task:** Summarize a supplied policy.

**Context:** The audience is new employees. The policy text will be pasted below the instruction.

**Constraints:** Preserve obligations and exceptions. Do not add rules that are not in the source. Use plain language.

**Output:** A short summary followed by a checklist of employee actions.

**Uncertainty:** If a section is ambiguous, quote or identify it rather than interpreting it as a definite rule.

**Complete prompt:**

> Summarize the policy text below for new employees. Preserve all obligations, exceptions, and deadlines. Do not add requirements that are not stated in the source. Start with a summary of no more than 150 words, then provide an action checklist. If any provision is ambiguous, identify the relevant passage and explain what remains unclear rather than guessing.
>
> Policy text: [PASTE APPROVED POLICY TEXT HERE]

## Weak versus improved

**Weak:** "Write a professional email."

**Improved:** "Draft a concise email to a supplier requesting an updated delivery date for order [ORDER_ID]. Use a neutral, professional tone. Do not invent dates or order details. Include a clear subject line and one direct request."

The improved prompt specifies recipient context, purpose, tone, variable data, and a boundary against inventing facts.

## Common mistakes

- Adding irrelevant background that obscures the actual task.
- Combining several unrelated tasks without defining priorities.
- Using vague adjectives such as "perfect" or "best" without criteria.
- Requiring a strict format without defining its fields.
- Supplying examples that contradict the written instructions.
- Treating a prompt as an access-control or security mechanism.

## Practice exercise

Take the request "Analyze this customer feedback" and write a prompt that specifies the analysis goal, audience, data boundaries, output structure, and how to report uncertainty. Use synthetic feedback rather than real customer information.

## Summary

A useful prompt makes the task, relevant context, constraints, and expected output clear. Examples and evaluation criteria can improve repeatability. Include only the components needed for the task and verify consequential results independently.
