# Example 1: Prompt Anatomy in Practice

## Scenario

You need a short summary of synthetic meeting notes. The prompt should distinguish confirmed decisions from proposed ideas and avoid inventing owners or deadlines.

## Input notes

> The team agreed to publish the help page on 15 June. Maya will prepare the draft. The analytics dashboard was discussed but no decision was made. Someone should investigate the reported login delay; no owner or deadline was assigned.

## Weak prompt

> Summarize these notes and list tasks.

This does not define how to handle undecided items or missing assignments.

## Improved prompt

> Summarize the meeting notes below for the project team.
>
> 1. Separate confirmed decisions from discussion items.
> 2. List action items in a table with columns: task, owner, deadline, and status.
> 3. Use "Not specified" when an owner or deadline is absent.
> 4. Do not turn proposals into decisions or add facts not present in the notes.
> 5. Keep the summary concise.
>
> Meeting notes:
> [PASTE NOTES]

## Expected output characteristics

- The help-page publication date appears as a confirmed decision.
- Maya is identified as the draft owner.
- The dashboard remains a discussion item, not a decision.
- The login-delay investigation is recorded as an action item with owner and deadline marked "Not specified" unless the notes provide them.

Exact wording may vary by model. Check the result against the original notes.

## Evaluation checklist

- [ ] No invented owner or deadline.
- [ ] Discussion item is not presented as an approved decision.
- [ ] All explicit facts are preserved.
- [ ] The requested sections and columns are present.

## Limitation

This is a demonstration of prompt structure, not an automated meeting-record system. A human should confirm decisions and assignments before distributing official minutes.
