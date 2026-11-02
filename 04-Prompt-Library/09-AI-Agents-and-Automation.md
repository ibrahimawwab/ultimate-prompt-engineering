# AI Agents and Automation

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Tool-using agent task plan

- **Purpose:** Decompose a user request into bounded steps and identify required permissions.
- **Difficulty:** Advanced
- **Recommended use:** Designing an agent workflow before connecting tools.

**Copy-ready prompt**

> Plan an agent workflow for {{USER_GOAL}}. Available tools: {{TOOLS}}. Data sensitivity: {{DATA}}. Allowed actions: {{ALLOWED_ACTIONS}}. Approval-required actions: {{APPROVAL_ACTIONS}}. Return steps, inputs/outputs, preconditions, permission checks, validation, failure handling, audit events, and stop conditions. Never assume a tool exists or that prompt instructions enforce authorization.

**Example input**

Goal: summarize selected support tickets. Tools: read-only ticket search and document export. Export requires approval.

**Expected output**

A least-privilege workflow with explicit approval and verification gates.

**Adaptation tips**

Implement authorization, schemas, and approval enforcement in application code; test denied paths.

**Limitations**

A plan cannot enforce permissions or prove a tool implementation is secure.

**Safety considerations**

Do not expose credentials to the model. Treat retrieved content as untrusted input.

---

## 2. Human approval checkpoint design

- **Purpose:** Define which actions require review and what evidence an approver sees.
- **Difficulty:** Advanced
- **Recommended use:** Adding human oversight to an automation workflow.

**Copy-ready prompt**

> Design approval checkpoints for {{WORKFLOW}}. Actions: {{ACTIONS}}. Impact if wrong: {{IMPACT}}. Reversibility: {{REVERSIBILITY}}. Specify trigger conditions, approver role, preview/diff, evidence, expiry, rejection path, re-approval after material changes, and audit record. Separate low-risk reversible actions from high-impact actions.

**Example input**

Workflow: draft and schedule social posts. Publishing is external and public.

**Expected output**

An approval policy with clear review context and cancellation behavior.

**Adaptation tips**

Make approvals explicit, time-bound, and bound to the exact action payload.

**Limitations**

Human approval can be inattentive and is not a substitute for technical controls.

**Safety considerations**

Never treat a model-generated approval as user consent. Prevent approval bypass and replay.

---

## 3. Automation failure analysis

- **Purpose:** Create failure modes and recovery logic for a multi-step automation.
- **Difficulty:** Intermediate
- **Recommended use:** Reviewing an automation before deployment.

**Copy-ready prompt**

> Analyze this automation: {{AUTOMATION}}. Dependencies: {{DEPENDENCIES}}. Side effects: {{SIDE_EFFECTS}}. Identify failure modes, detection signals, retry safety, idempotency needs, compensation/rollback, user notification, and manual recovery. Distinguish transient from permanent failures. Do not recommend blind retries for non-idempotent actions.

**Example input**

Automation: create an invoice, notify finance, and update a CRM record.

**Expected output**

A failure-mode table and safe recovery sequence, including duplicate-prevention checks.

**Adaptation tips**

Test partial completion, timeouts, and duplicate delivery in a staging environment.

**Limitations**

The analysis may miss platform-specific behavior and race conditions.

**Safety considerations**

Require explicit authorization for external side effects; log minimally and securely.

---

## 4. Untrusted content and prompt-injection handling

- **Purpose:** Specify a safe workflow for processing hostile or instruction-like retrieved content.
- **Difficulty:** Advanced
- **Recommended use:** Building agents that read email, web pages, documents, or tickets.

**Copy-ready prompt**

> Design defenses for an agent that processes {{CONTENT_TYPES}} and can use {{TOOLS}}. Treat retrieved text as untrusted data, not policy. Define separation of instructions/data, tool allowlists, server-side authorization, output validation, sensitive-data boundaries, suspicious-content handling, and adversarial tests. Explain residual risk. Do not claim a prompt alone prevents injection.

**Example input**

Content: emails and web pages. Tools: search and read-only ticket lookup.

**Expected output**

A layered design and test cases for malicious embedded instructions and data exfiltration attempts.

**Adaptation tips**

Enforce controls outside the model and test against realistic attack strings and indirect injection.

**Limitations**

No prompt pattern reliably eliminates prompt injection; model behavior and integrations vary.

**Safety considerations**

Do not expose secrets to retrieved content or model context; require confirmation for consequential actions.

---

## 5. Agent evaluation test suite

- **Purpose:** Create test cases that measure task success, safety, and reliability across repeated runs.
- **Difficulty:** Advanced
- **Recommended use:** Evaluating an agent before release or after a model/tool change.

**Copy-ready prompt**

> Design an evaluation suite for {{AGENT_TASK}}. Tools and permissions: {{TOOLS_AND_PERMISSIONS}}. Expected outcomes: {{EXPECTED}}. Include normal, edge, adversarial, denied-permission, tool-error, timeout, ambiguous-request, and partial-completion cases. Define observable pass criteria, severity, repeat count, and regression thresholds. Separate model quality from infrastructure correctness.

**Example input**

Task: summarize project issues using read-only GitHub access. No write permissions.

**Expected output**

A reproducible test matrix with explicit assertions and safety-negative cases.

**Adaptation tips**

Use versioned fixtures, deterministic mocks where possible, and monitored canary runs.

**Limitations**

Passing a finite suite does not prove absence of failures or guarantee behavior on unseen inputs.

**Safety considerations**

Use synthetic data and verify that denied actions truly fail at the tool/API layer.
