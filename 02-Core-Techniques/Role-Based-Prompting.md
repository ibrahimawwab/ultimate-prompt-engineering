# Role-Based Prompting

## Overview

Role-based prompting frames the model's response from a specified professional or functional perspective, such as editor, tutor, test engineer, or policy analyst. A role can establish audience, vocabulary, priorities, and review criteria.

A role is an instruction about response framing—not a credential, real-world identity, or guarantee of expertise.

## When to use it

Use a role when the task benefits from a clearly defined perspective or set of evaluation priorities. For example, asking for a code review from a security-review perspective can focus attention on trust boundaries, input validation, and authorization.

## Worked example

### Weak prompt

```text
Review this code.
```

### Improved prompt

```text
Act as a cautious application security reviewer.

Review the code below for:
- input validation and injection risks;
- authentication and authorization boundaries;
- secrets and sensitive-data handling;
- error handling and logging.

For each finding, provide:
1. affected component;
2. realistic impact;
3. evidence from the supplied code;
4. a proportionate remediation.

Do not claim that the code is secure based only on this review. Mark assumptions and areas that require runtime testing.

Code:
[Paste code]
```

The role is useful because it defines a review lens and deliverable. The explicit criteria do the substantive work.

## Limitations and failure modes

- A role prompt does not make the model a licensed professional or a substitute for one.
- Grandiose titles can encourage overconfident language without improving accuracy.
- A role may narrow attention and cause other relevant perspectives to be missed.
- Conflicting roles or objectives can produce inconsistent responses.
- The model may still overlook defects or invent supporting details.

For consequential decisions, require evidence, independent verification, and qualified human review.

## Best practices

1. Choose a role that maps to the task.
2. Define responsibilities and evaluation criteria, not just a title.
3. Specify the intended audience and level of detail.
4. Ask the model to distinguish evidence, assumptions, and recommendations.
5. Avoid implying real credentials, access, or authority the model does not possess.

## Exercise

Write two prompts for reviewing the same short code sample: one from a maintainability perspective and one from a security perspective. Compare the findings. Identify which differences come from the review criteria and which findings need independent validation.

## Further reading

- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
