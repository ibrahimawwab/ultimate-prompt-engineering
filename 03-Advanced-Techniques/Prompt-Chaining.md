# Prompt Chaining and Decomposition

## Overview

Prompt chaining divides a larger task into stages. The output of one stage becomes input to the next, often with an explicit intermediate representation. Decomposition is the broader practice of splitting a task into smaller, verifiable subtasks; chaining is one way to connect them.

This is an established workflow design pattern, but its benefit depends on task structure, model capability, and the quality of intermediate checks.

## When to use it

Use a chain when subtasks have distinct goals, later steps depend on earlier results, or intermediate outputs can be reviewed or validated. Avoid chains that merely add calls without reducing error or improving control.

## Example: evidence-based report

**Stage 1 — Extract:** "Extract claims, dates, and named entities from this source. Quote short supporting passages and mark missing details."

**Stage 2 — Organize:** "Group the extracted claims by topic. Preserve source identifiers. Do not add new claims."

**Stage 3 — Draft:** "Write a report using only the organized claims. Distinguish source statements from analysis and list unresolved questions."

**Stage 4 — Verify:** "Compare every factual statement in the draft with the supplied claims. Return unsupported statements and omissions; do not silently repair them."

A production workflow should pass structured records between stages rather than relying only on free-form prose.

## Design and evaluation

Define the input and output contract for each stage. Preserve provenance. Validate intermediate formats. Set limits on retries, tokens, time, and tool calls. Log stage outcomes and allow a human to inspect high-impact decisions.

Compare the chain against a single-call baseline on the same representative test set. Measure factual errors, omissions, latency, cost, and review effort.

## Limitations

- Errors in early stages can propagate.
- Summaries can discard details needed later.
- Additional calls increase latency, cost, and operational complexity.
- A later stage may treat an earlier model-generated statement as verified fact.
- Chains can fail partially and need explicit recovery behavior.

## Exercise

Design a three-stage chain that turns meeting notes into action items. Specify a JSON contract for each stage, then test missing owners, conflicting dates, and duplicated tasks. Record errors at each boundary.

## Further reading

- [OpenAI prompting guide](https://platform.openai.com/docs/guides/prompt-engineering)
