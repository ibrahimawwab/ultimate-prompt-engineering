# Business and Productivity

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Decision memo

- **Purpose:** Prepare a concise decision memo that makes trade-offs explicit.
- **Difficulty:** Intermediate
- **Recommended use:** Presenting a decision to a manager or project owner.

### Copy-ready prompt

> Prepare a decision memo for {{DECISION}}. Context: {{CONTEXT}}. Options: {{OPTIONS}}. Constraints: {{CONSTRAINTS}}. Include decision needed, criteria, comparison table, costs and benefits with assumptions, risks, reversibility, recommendation, and next actions. Separate known facts from estimates and identify missing data.

### Example input

Decision: choose between two ticketing systems. Constraints: team of 12, annual budget ceiling.

### Expected output

A decision-ready memo with transparent criteria and assumptions rather than unsupported certainty.

### Adaptation tips

Validate costs, contract terms, and stakeholder requirements before approval.

### Limitations

The analysis is only as reliable as supplied inputs; estimates are not vendor quotes.

### Safety considerations

Do not include confidential customer, employee, or financial details unnecessarily.

---

## 2. Process improvement analysis

- **Purpose:** Map a workflow and identify measurable bottlenecks and low-risk improvements.
- **Difficulty:** Intermediate
- **Recommended use:** Improving a repeatable operational process.

### Copy-ready prompt

> Analyze this process: {{PROCESS}}. Current steps and volumes: {{BASELINE}}. Desired outcome: {{GOAL}}. Constraints: {{CONSTRAINTS}}. Produce a simple current-state map, likely bottlenecks, evidence needed, improvement hypotheses, metrics, small pilot, and failure/rollback criteria. Distinguish observed facts from assumptions.

### Example input

Process: customer support ticket triage. Baseline: 500 tickets/week, median first response 18 hours.

### Expected output

A pilot plan with measurable response-time and quality metrics.

### Adaptation tips

Collect a baseline and involve front-line staff before changing responsibilities or systems.

### Limitations

A text description may omit informal work and exceptional cases.

### Safety considerations

Consider employee privacy, accessibility, and service quality; do not optimize solely for speed.

---

## 3. Stakeholder update

- **Purpose:** Convert project facts into a concise, audience-appropriate status update.
- **Difficulty:** Beginner
- **Recommended use:** Communicating progress, risks, and decisions needed.

### Copy-ready prompt

> Draft a status update for {{AUDIENCE}}. Project: {{PROJECT}}. Period: {{PERIOD}}. Verified progress: {{PROGRESS}}. Risks/blockers: {{RISKS}}. Decisions needed: {{DECISIONS}}. Use clear status language, owners, and dates only when supplied. Separate completed work from planned work. Do not hide material risks or invent progress.

### Example input

Audience: department leadership. Progress: prototype tested with 8 users; accessibility review not yet started.

### Expected output

A concise update with completed work, next steps, risks, and explicit asks.

### Adaptation tips

Confirm dates, owners, and status labels with the project lead before sending.

### Limitations

The draft cannot independently verify reported progress.

### Safety considerations

Exclude sensitive employee and customer details; share only with the intended audience.

---

## 4. Meeting agenda and decision log

- **Purpose:** Design a meeting that produces clear decisions and accountable actions.
- **Difficulty:** Beginner
- **Recommended use:** Preparing a focused meeting with a defined outcome.

### Copy-ready prompt

> Create an agenda for {{MEETING_GOAL}}. Participants/roles: {{PARTICIPANTS}}. Time available: {{DURATION}}. Context: {{CONTEXT}}. Include desired decisions, time-boxed topics, pre-reads, facilitator questions, decision rules, and an action-log template with owner and due date. Do not invent attendee availability.

### Example input

Goal: approve pilot scope. Participants: product, engineering, security. Duration: 30 minutes.

### Expected output

A time-boxed agenda and reusable decision/action log.

### Adaptation tips

Send pre-reads early and record dissent or unresolved questions.

### Limitations

The agenda cannot guarantee consensus or replace stakeholder consultation.

### Safety considerations

Avoid recording unnecessary personal or sensitive discussion details.

---

## 5. Risk register starter

- **Purpose:** Turn project uncertainties into a prioritized, reviewable risk register.
- **Difficulty:** Intermediate
- **Recommended use:** Early project planning or periodic risk review.

### Copy-ready prompt

> Create a risk register for {{PROJECT}}. Context: {{CONTEXT}}. Dependencies: {{DEPENDENCIES}}. Constraints: {{CONSTRAINTS}}. For each risk state cause, uncertain event, consequence, likelihood rationale, impact rationale, existing controls, owner role, mitigation, trigger, and residual risk. Mark ratings as provisional and explain the scale.

### Example input

Project: migrate a small business website to a new hosting provider.

### Expected output

A structured register with explicit rating rationale and owners to assign.

### Adaptation tips

Calibrate scales with stakeholders and review risks at defined milestones.

### Limitations

A generated register may miss organization-specific or emerging risks.

### Safety considerations

Do not disclose sensitive infrastructure details in public prompts; restrict distribution appropriately.
