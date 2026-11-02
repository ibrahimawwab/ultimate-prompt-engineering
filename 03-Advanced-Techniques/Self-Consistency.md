# Self-Consistency and Sampling

## Overview

Self-consistency is a research technique that samples multiple reasoning paths for a problem and aggregates their final answers, often by majority vote. It is intended for tasks where diverse sampled solutions may reveal a more reliable consensus.

It is not the same as asking the model to repeat an answer, and repeated agreement is not independent evidence of truth.

## When to use it

Consider it for tasks with a well-defined answer and a reliable way to compare candidate outputs, such as selected arithmetic or symbolic reasoning problems. It is less useful when answers are open-ended, subjective, or depend on one authoritative source.

## Practical procedure

1. Define the question and output schema.
2. Generate a bounded number of independent samples using documented sampling settings.
3. Normalize equivalent answers.
4. Aggregate using a task-appropriate rule.
5. Verify the selected answer using an external method where possible.
6. Preserve disagreement rather than hiding it.

## Example instruction

```text
Solve the problem and return only:
- answer;
- assumptions;
- a concise justification;
- any ambiguity in the problem statement.

Problem: [problem]
```

An application can run this prompt multiple times with controlled sampling and aggregate the answer. The aggregation logic should be implemented and tested outside the prompt.

## Limitations

- Samples from one model are correlated, not independent witnesses.
- Majority vote can reinforce a shared systematic error.
- More samples increase latency and cost.
- Normalization can incorrectly merge distinct answers.
- Consensus does not establish factual truth.

## Best practices and exercise

Set a fixed sampling budget, compare against a single-sample baseline, and use deterministic checks when possible. Test 20 problems with known answers; record accuracy, disagreement rate, cost, and whether aggregation corrects or introduces errors.

## Further reading

- [Wang et al., Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
