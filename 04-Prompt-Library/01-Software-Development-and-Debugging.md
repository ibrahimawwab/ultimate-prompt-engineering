# Software Development and Debugging

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Requirements-to-implementation plan

- **Purpose:** Turn a bounded feature request into an implementation plan before code changes.
- **Difficulty:** Intermediate
- **Recommended use:** Planning a feature with known repository and runtime constraints.

### Copy-ready prompt

> Act as a senior software engineer. Plan this feature: {{FEATURE}}. Context: {{STACK_AND_ARCHITECTURE}}. Constraints: {{CONSTRAINTS}}. Return: assumptions and questions; user-visible behavior; data/API changes; implementation steps in dependency order; tests; security and accessibility considerations; rollout and rollback. Do not invent repository files or APIs. Mark unknowns explicitly.

### Example input

Feature: add CSV export to a Python reporting service. Stack: FastAPI, PostgreSQL. Constraint: exports must be streamed and authorized.

### Expected output

A sequenced plan with explicit unknowns, test cases, and risks; no unverified code references.

### Adaptation tips

Confirm architecture and acceptance criteria before implementation; split large changes into reviewable commits.

### Limitations

The plan is not proof that the design is compatible with the actual codebase.

### Safety considerations

Do not include secrets or real customer records. Require authorization checks and data minimization for exports.

---

## 2. Reproduce and diagnose a bug

- **Purpose:** Create a reproducible investigation plan that separates observations from hypotheses.
- **Difficulty:** Intermediate
- **Recommended use:** Debugging an issue with logs, symptoms, and environment details.

### Copy-ready prompt

> Investigate this defect without assuming a cause. Symptom: {{SYMPTOM}}. Expected: {{EXPECTED}}. Actual: {{ACTUAL}}. Environment: {{ENVIRONMENT}}. Evidence: {{LOGS_OR_TRACE}}. Provide: concise restatement; missing information; ranked hypotheses with evidence for/against; minimal reproduction; diagnostic steps; likely fix options; regression tests. Label speculation and do not claim to have run commands.

### Example input

Symptom: API returns 500 for empty search query. Expected: validation error. Actual: stack trace shows None passed to query builder. Environment: Python 3.12, FastAPI.

### Expected output

A testable reproduction and ranked hypotheses tied to the supplied trace.

### Adaptation tips

Redact tokens, identifiers, and personal data from logs before sharing.

### Limitations

Logs can be incomplete or misleading; diagnosis requires reproduction and code inspection.

### Safety considerations

Never request production credentials. Avoid destructive debugging steps on live systems.

---

## 3. Code review against a change brief

- **Purpose:** Review a patch for correctness, maintainability, and concrete regressions.
- **Difficulty:** Advanced
- **Recommended use:** Reviewing a diff against requirements and project conventions.

### Copy-ready prompt

> Review the following change. Requirements: {{REQUIREMENTS}}. Relevant conventions: {{CONVENTIONS}}. Diff: {{DIFF}}. Report only actionable findings, ordered by severity. For each: file/line if supplied; violated behavior; concrete failure scenario; impact; suggested correction; test that would catch it. Then list residual risks and questions. Do not invent line numbers or report stylistic preferences as defects.

### Example input

Requirements: reject expired sessions. Diff: token expiry check added after protected data is fetched.

### Expected output

Findings identify the authorization-order flaw and a test proving protected data is not fetched for expired sessions.

### Adaptation tips

Provide the complete diff and surrounding code for reliable review.

### Limitations

A text-only review cannot compile, execute, or inspect omitted dependencies.

### Safety considerations

Treat supplied code as untrusted. Do not expose secrets found in the diff; flag them for rotation and removal.

---

## 4. Test design from acceptance criteria

- **Purpose:** Derive meaningful unit, integration, and boundary tests from stated behavior.
- **Difficulty:** Intermediate
- **Recommended use:** Building a test plan before or alongside implementation.

### Copy-ready prompt

> Convert these acceptance criteria into a test matrix. Criteria: {{CRITERIA}}. System boundary: {{BOUNDARY}}. Test framework: {{FRAMEWORK}}. Include happy paths, negative cases, boundaries, malformed input, authorization, concurrency where relevant, and regression cases. For each test give setup, action, expected assertion, and test level. Identify criteria that are ambiguous or untestable.

### Example input

Criteria: users can reset passwords using a single-use token valid for 15 minutes.

### Expected output

A test matrix covering valid, expired, reused, malformed, and cross-account tokens, with appropriate integration boundaries.

### Adaptation tips

Map each test to a requirement ID and keep fixtures deterministic.

### Limitations

Generated tests may miss domain-specific edge cases; execute them against the real implementation.

### Safety considerations

Use synthetic accounts and tokens. Never place live credentials in fixtures or logs.

---

## 5. Refactor safely without changing behavior

- **Purpose:** Plan a behavior-preserving refactor with measurable safeguards.
- **Difficulty:** Advanced
- **Recommended use:** Reducing complexity in a working component without changing its contract.

### Copy-ready prompt

> Design a behavior-preserving refactor for {{COMPONENT}}. Current behavior and contract: {{CONTRACT}}. Pain points: {{PAIN_POINTS}}. Constraints: {{CONSTRAINTS}}. Propose small steps, compatibility boundaries, characterization tests, observability checks, and rollback criteria. Identify behavior that must remain unchanged. Do not silently add features or alter public interfaces.

### Example input

Component: legacy invoice calculator. Contract: same rounding and tax behavior for existing inputs. Pain: duplicated rules.

### Expected output

Incremental refactor steps anchored by characterization tests for rounding, tax, and compatibility.

### Adaptation tips

Capture current behavior before restructuring; compare outputs over representative fixtures.

### Limitations

A prompt cannot verify semantic equivalence; tests and review are required.

### Safety considerations

Do not use real financial or personal data in examples; validate calculations with authoritative business rules.
