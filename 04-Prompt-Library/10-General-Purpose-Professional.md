# General-Purpose Professional

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Complex task clarification

- **Purpose:** Convert an ambiguous request into explicit scope, constraints, and deliverables.
- **Difficulty:** Beginner
- **Recommended use:** Starting work when requirements are incomplete.

### Copy-ready prompt

> Help clarify this request: {{REQUEST}}. Context: {{CONTEXT}}. Identify the intended outcome, known constraints, assumptions, ambiguities, dependencies, and acceptance criteria. Ask only the highest-value clarification questions; if safe to proceed, state provisional assumptions and a bounded first step. Do not silently invent requirements.

### Example input

Request: prepare a report on customer feedback. Context: quarterly review, no audience specified.

### Expected output

A concise requirements brief with uncertainties and prioritized questions.

### Adaptation tips

Confirm audience, deadline, and source material before drafting the final deliverable.

### Limitations

Clarification quality depends on the context supplied; assumptions can still be wrong.

### Safety considerations

Do not request unnecessary personal, confidential, or credential information.

---

## 2. Compare options using explicit criteria

- **Purpose:** Build a transparent comparison rather than a vague recommendation.
- **Difficulty:** Intermediate
- **Recommended use:** Choosing between tools, vendors, approaches, or plans.

### Copy-ready prompt

> Compare {{OPTIONS}} for {{GOAL}}. Criteria and weights: {{CRITERIA}}. Constraints: {{CONSTRAINTS}}. Evidence available: {{EVIDENCE}}. Create a comparison matrix, identify unknowns, explain trade-offs, and provide a conditional recommendation. Do not fabricate prices, capabilities, or ratings; mark data that needs current verification.

### Example input

Options: self-hosted and managed issue trackers. Criteria: cost, maintenance, access control, portability.

### Expected output

A criteria-based comparison with assumptions and a conditional recommendation.

### Adaptation tips

Verify changing facts directly with vendors and test shortlisted options.

### Limitations

A comparison is only as fair as the criteria and evidence; weights are subjective.

### Safety considerations

Consider privacy, accessibility, contractual terms, and data portability.

---

## 3. Professional document quality review

- **Purpose:** Review a document for clarity, completeness, consistency, and audience fit.
- **Difficulty:** Beginner
- **Recommended use:** Editing a report, proposal, policy, or procedure.

### Copy-ready prompt

> Review this document for {{AUDIENCE}} and purpose {{PURPOSE}}. Text: {{DOCUMENT}}. Check structure, clarity, terminology, unsupported claims, contradictions, missing sections, tone, and actionability. Return prioritized findings with section references available in the text, then a revised version only if requested. Preserve intended meaning and flag substantive changes.

### Example input

Purpose: internal project proposal. Audience: technical leadership. Text: supplied draft.

### Expected output

An editorial review with prioritized issues and no unrequested rewriting.

### Adaptation tips

Verify factual statements and obtain owner approval for substantive policy changes.

### Limitations

Editing cannot validate facts or replace legal, technical, or subject-matter review.

### Safety considerations

Remove confidential or personal information before sharing.

---

## 4. Translate with terminology control

- **Purpose:** Translate a text while preserving meaning, register, and domain terms.
- **Difficulty:** Intermediate
- **Recommended use:** Translating professional material across languages.

### Copy-ready prompt

> Translate from {{SOURCE_LANGUAGE}} to {{TARGET_LANGUAGE}}. Audience: {{AUDIENCE}}. Domain: {{DOMAIN}}. Text: {{TEXT}}. Preserve meaning, numbers, names, units, and formatting. Use this glossary: {{GLOSSARY}}. Flag ambiguous phrases and offer alternatives where meaning is uncertain. Do not add explanatory content inside the translation.

### Example input

From English to Dari. Domain: laboratory quality management. Text: supplied paragraph; glossary includes QC = quality control.

### Expected output

A faithful translation plus a separate ambiguity note where needed.

### Adaptation tips

Have a qualified bilingual domain reviewer check high-stakes terminology.

### Limitations

Nuance, dialect, and specialist terms may not map one-to-one.

### Safety considerations

Do not translate identifiable records unless authorized and appropriately protected.

---

## 5. After-action review

- **Purpose:** Turn an event or completed project into specific, blameless improvements.
- **Difficulty:** Intermediate
- **Recommended use:** Reviewing an incident, launch, or project milestone.

### Copy-ready prompt

> Facilitate an after-action review for {{EVENT}}. Intended objectives: {{OBJECTIVES}}. Timeline: {{TIMELINE}}. Evidence: {{EVIDENCE}}. Identify what was expected, what happened, contributing factors, what worked, what did not, impact, and prioritized improvements with owners and measures. Distinguish evidence from recollection and avoid assigning blame without evidence.

### Example input

Event: delayed software release. Evidence: milestone log and incident notes.

### Expected output

A factual review with corrective actions, owners to assign, and measurable follow-up.

### Adaptation tips

Validate timeline with participants and track actions to completion.

### Limitations

Incomplete records and hindsight bias can distort conclusions.

### Safety considerations

Limit access to sensitive incident details and protect people from unnecessary disclosure.
