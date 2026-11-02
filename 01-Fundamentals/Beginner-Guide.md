# Beginner Guide: Write Your First Reliable Prompt

## Goal

This guide walks through a repeatable process for turning an everyday request into a prompt that can be tested and improved.

## Step 1: Define the outcome

Describe what you need in one sentence.

Example: "Create a study plan for an introductory biology exam."

Avoid starting with a long list of loosely related requests. Define the main deliverable first.

## Step 2: Add the relevant context

Identify the details that materially affect the answer:

- Learner level: beginner.
- Available study time: 30 minutes per day.
- Time remaining: 14 days.
- Topics: cell structure, genetics, and basic microbiology.

Use placeholders for information that changes. Do not include private data that the model does not need.

## Step 3: Set constraints

Examples:

- Keep each daily session to 30 minutes.
- Include one review day.
- Do not assume access to paid courses.
- Mark any assumptions that need confirmation.

Constraints should be realistic and consistent.

## Step 4: Specify the output

For example: "Return a 14-row table with day, topic, activity, and a short self-test."

If the output will be processed by software, define a schema and validate the result in the application.

## Step 5: Assemble the prompt

> Create a 14-day study plan for a beginner preparing for an introductory biology exam. The learner can study for 30 minutes per day and needs to cover cell structure, genetics, and basic microbiology. Include one cumulative review day. Use free learning activities and do not assume access to paid courses. Return a table with columns for day, topic, 30-minute activity, and one self-test question. If the schedule requires an assumption, state it before the table.

## Step 6: Evaluate the result

Check the answer against a simple rubric:

| Criterion | Check |
| --- | --- |
| Completeness | Are all three topics covered? |
| Feasibility | Does each activity fit the time limit? |
| Clarity | Can a beginner understand each task? |
| Constraint adherence | Is a review day included and are paid resources avoided? |
| Accuracy | Are scientific statements correct and appropriately sourced? |

A prompt that produces a well-formatted table can still contain incorrect biology. Verify subject-matter claims.

## Step 7: Improve one thing at a time

If the plan is too broad, add topic-level detail. If it exceeds the time limit, specify the maximum number of activities. If it omits review, state where review should occur.

Change one major requirement at a time so you can understand which change affected the result.

## Common beginner errors

- Asking several unrelated questions in one prompt.
- Omitting the intended audience.
- Providing unnecessary personal or confidential context.
- Treating a confident answer as a verified answer.
- Assuming the same prompt will behave identically on every model.
- Failing to test edge cases or missing information.

## Practice challenge

Write a prompt that asks a model to turn a short set of meeting notes into decisions, action items, owners, and deadlines. Your prompt must instruct the model to use "Not specified" when an owner or deadline is absent. Test it with synthetic notes that intentionally omit one owner.

## Summary

A dependable beginner workflow is: define the outcome, add relevant context, state constraints, specify the output, test the result, and refine based on observed errors. Prompt engineering is iterative and evidence-driven.
