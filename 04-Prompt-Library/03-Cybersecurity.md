# Cybersecurity

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Authorized security assessment scope

- **Purpose:** Convert written authorization into a bounded, testable assessment scope.
- **Difficulty:** Intermediate
- **Recommended use:** Planning an assessment before any scanning or testing.

Copy-ready prompt:

> Create a security assessment scope from this authorization: {{AUTHORIZATION}}. Assets: {{ASSETS}}. Allowed techniques: {{ALLOWED_TECHNIQUES}}. Prohibited actions: {{PROHIBITIONS}}. Window and contacts: {{WINDOW_AND_CONTACTS}}. Output in-scope targets, exclusions, permitted test cases, rate limits, evidence handling, stop conditions, escalation contacts, and approval gaps. Do not expand scope by inference.

Example input:

Authorization: assess staging.example.test only; passive review and low-rate authenticated checks; no denial-of-service or social engineering.

Expected output:

A scope checklist with explicit exclusions, constraints, and unresolved approvals.

Adaptation tips:

Have the asset owner sign off on the final scope and confirm ownership of every target.

Limitations:

A written scope summary does not itself grant authorization or technical access.

Safety considerations:

Only test systems you are explicitly authorized to assess. Never infer permission for third-party infrastructure.

---

## 2. Threat model for an application

- **Purpose:** Identify assets, trust boundaries, abuse cases, and mitigations for a defined system.
- **Difficulty:** Advanced
- **Recommended use:** Design review for a web service or application feature.

Copy-ready prompt:

> Threat-model this system: {{SYSTEM_DESCRIPTION}}. Data/assets: {{ASSETS}}. Actors: {{ACTORS}}. Trust boundaries: {{BOUNDARIES}}. Use {{THREAT_MODEL_METHOD}}. List entry points, security assumptions, threats, attack paths, impact, mitigations, residual risks, and validation tests. Distinguish confirmed architecture from assumptions; ask for missing details.

Example input:

System: multi-tenant document API with users, admins, object storage, and PostgreSQL.

Expected output:

A threat register focused on tenant isolation, identity, storage access, and auditability.

Adaptation tips:

Validate the model with engineers who know deployment and data flows; update when architecture changes.

Limitations:

A prompt-based model can omit threats and cannot certify security.

Safety considerations:

Use synthetic architecture details; do not paste secrets, keys, or exploitable private customer data.

---

## 3. Log and alert triage

- **Purpose:** Triage supplied security telemetry without overstating attribution or certainty.
- **Difficulty:** Intermediate
- **Recommended use:** Initial analysis of a suspicious event or alert.

Copy-ready prompt:

> Triage this event using only the supplied telemetry. Alert: {{ALERT}}. Logs: {{LOGS}}. Environment baseline: {{BASELINE}}. Provide timeline, observed facts, plausible hypotheses ranked by support, indicators to validate, scope questions, containment options with impact, and evidence-preservation steps. Label confidence and unknowns. Do not attribute an actor without evidence.

Example input:

Alert: repeated failed logins followed by one success. Logs: timestamps, source IPs, user IDs pseudonymized.

Expected output:

A cautious timeline and investigation checklist separating facts from hypotheses.

Adaptation tips:

Correlate identity, endpoint, network, and application telemetry before deciding severity.

Limitations:

Partial logs can create false positives or miss context; no definitive attribution from a single signal.

Safety considerations:

Preserve evidence and follow incident-response authority. Do not publish personal identifiers or attacker claims prematurely.

---

## 4. Secure code review for an input boundary

- **Purpose:** Inspect a code fragment for input-validation and injection risks.
- **Difficulty:** Advanced
- **Recommended use:** Reviewing parsers, query construction, file handling, or API boundaries.

Copy-ready prompt:

> Review this code for security issues at the {{INPUT_BOUNDARY}} boundary. Language/framework: {{STACK}}. Threat assumptions: {{THREATS}}. Code: {{CODE}}. Identify concrete vulnerabilities, attacker-controlled inputs, exploit preconditions, impact, safe remediation, and regression tests. Cite exact supplied lines only. If context is missing, state what is needed. Do not provide weaponized payloads beyond benign validation examples.

Example input:

Boundary: SQL filter parameter. Stack: Python and psycopg. Code: supplied query builder.

Expected output:

Actionable findings such as unsafe string interpolation, with parameterized-query remediation and tests.

Adaptation tips:

Inspect call sites, database permissions, and framework behavior; run static analysis and tests.

Limitations:

A snippet review cannot establish exploitability or rule out issues elsewhere.

Safety considerations:

Keep examples defensive and bounded to authorized code. Never expose production credentials or data.

---

## 5. Incident response tabletop

- **Purpose:** Facilitate a structured tabletop for a defensive incident scenario.
- **Difficulty:** Intermediate
- **Recommended use:** Training responders and identifying process gaps.

Copy-ready prompt:

> Run a tabletop for scenario {{SCENARIO}} in environment {{ENVIRONMENT}}. Participants: {{ROLES}}. Constraints: {{CONSTRAINTS}}. Present one inject at a time; ask the team to decide, then evaluate against detection, containment, evidence, communications, recovery, legal/privacy escalation, and lessons learned. Do not assume tools or authority not listed.

Example input:

Scenario: suspected compromise of a SaaS administrator account. Roles: on-call, security lead, legal, communications.

Expected output:

A facilitator script with staged injects, decision prompts, and evaluation criteria.

Adaptation tips:

Tailor escalation paths to the real incident plan and record owners and deadlines for gaps.

Limitations:

A tabletop tests readiness but does not prove technical controls work.

Safety considerations:

Use fictional data and do not conduct live disruptive actions during the exercise.
