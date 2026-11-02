# Types of Prompts

## Introduction

Prompts can be classified by their purpose, structure, or the way they provide examples and context. These categories overlap: one prompt can be instructional, contextual, and structured-output oriented at the same time.

The labels in this lesson describe common patterns rather than a universal taxonomy.

## Common prompt types

### Direct instruction prompts

Ask the model to perform a clearly stated task.

**Example:** "Convert the following meeting notes into a list of decisions and action items. Do not infer owners when none are named."

**Use when:** The task is straightforward and the requirements can be expressed directly.

### Question-answering prompts

Ask a question and provide any context or source material needed to answer it.

**Example:** "Using only the passage below, identify the policy's stated renewal period. If the passage does not specify one, say 'Not specified.'"

**Use when:** The task is to answer a bounded question, especially from supplied material.

### Transformation prompts

Convert existing content from one form to another while preserving specified meaning.

**Example:** "Rewrite this technical paragraph for a general audience. Preserve all numerical values, warnings, and qualifications."

**Use when:** Summarizing, translating, reformatting, simplifying, or changing tone.

### Extraction and classification prompts

Identify fields or assign labels based on explicit definitions.

**Example:** "Extract each invoice number and due date from the text. Return null for a field that is absent; do not infer it."

**Use when:** Turning unstructured content into structured information. Validate extracted fields against the source.

### Creative-generation prompts

Request original content with a defined audience, purpose, style, and constraints.

**Example:** "Generate three original names for a fictional environmental education newsletter. Avoid names already listed here: [EXISTING_NAMES]."

**Use when:** Brainstorming, drafting, ideation, and creative exploration.

### Role or perspective prompts

Frame the response from a professional or audience perspective.

**Example:** "Review this user guide from the perspective of a first-time reader. Identify unclear steps and explain why each may confuse a beginner."

**Use when:** A perspective helps focus the review. A role instruction does not grant real credentials or guarantee expert-level correctness.

### Few-shot prompts

Include a small set of input-output examples to demonstrate the desired pattern.

**Example:**

> Input: "The package arrived two days late."
>
> Output: {"sentiment":"negative","topic":"delivery"}
>
> Input: "The support agent resolved my issue quickly."
>
> Output: {"sentiment":"positive","topic":"support"}
>
> Classify this new feedback: "[FEEDBACK]"

**Use when:** The expected pattern is easier to show than explain. Check that examples cover relevant edge cases.

### Structured-output prompts

Specify fields, types, allowed values, or a schema for the response.

**Example:** "Return JSON with keys 'summary' (string) and 'open_questions' (array of strings). Do not include additional keys."

**Use when:** Results feed a downstream workflow. Use provider-supported constrained output or application-side parsing and validation when available.

### Multimodal prompts

Combine text with image, audio, video, or other supported input.

**Example:** "Describe the visible components in this diagram. Distinguish readable labels from your interpretation, and state when text is too small to read."

**Use when:** The model and interface support the required modality. Capabilities vary by product and model.

## Selecting a prompt type

Choose the simplest pattern that meets the task:

1. Define the required outcome.
2. Decide whether the model needs supplied context or examples.
3. Determine whether the output must follow a strict schema.
4. Check whether the input includes non-text media or external information.
5. Add safety and validation controls appropriate to the consequences.

## Limitations

- A category name does not ensure the model will follow the intended pattern.
- Few-shot examples can bias the response or fail to represent edge cases.
- Role framing cannot create professional qualifications.
- Structured output may be syntactically valid but factually wrong.
- Multimodal interpretation may omit details or misread content.
- Classification results need validation, especially when labels affect people or important decisions.

## Summary

Prompt types are reusable ways to frame tasks: instruction, question answering, transformation, extraction, creative generation, role framing, few-shot examples, structured output, and multimodal input. Select by task requirements and evaluate actual performance rather than assuming a named technique is inherently superior.
