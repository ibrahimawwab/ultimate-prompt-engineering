# Data Analysis

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Exploratory data analysis plan

- **Purpose:** Create a reproducible EDA plan before interpreting a dataset.
- **Difficulty:** Intermediate
- **Recommended use:** Starting analysis of a new structured dataset.

Copy-ready prompt:

> Plan EDA for dataset {{DATASET_DESCRIPTION}}. Variables/schema: {{SCHEMA}}. Research or business question: {{QUESTION}}. Identify data-quality checks, missingness, duplicates, ranges, distributions, relationships, subgroup checks, visualizations, and assumptions. Provide code only for {{LANGUAGE_OR_TOOL}} if requested. Do not infer results without data.

Example input:

Dataset: de-identified lab turnaround times. Schema: received_at, verified_at, test_type, site.

Expected output:

A staged checklist and analysis outputs tied to the question.

Adaptation tips:

Run checks on raw data first and document exclusions and transformations.

Limitations:

A plan is not an analysis; apparent patterns may reflect data collection artifacts.

Safety considerations:

Remove identifiers, secrets, and small-cell details that could re-identify individuals.

---

## 2. SQL query review

- **Purpose:** Review a SQL query for correctness, performance, and access-control concerns.
- **Difficulty:** Advanced
- **Recommended use:** Checking a query before use in an application or report.

Copy-ready prompt:

> Review this SQL for {{GOAL}}. Database/version: {{DATABASE}}. Schema: {{SCHEMA}}. Query: {{SQL}}. Assess semantics, joins, null behavior, aggregation, indexing opportunities, transaction implications, injection exposure, and tenant/row-level restrictions. Suggest a corrected query only where justified. State assumptions and propose EXPLAIN-based validation.

Example input:

Database: PostgreSQL. Goal: count monthly orders by tenant. Query: supplied parameterized SQL.

Expected output:

A concrete review with correctness issues, safe query pattern, and validation steps.

Adaptation tips:

Test against representative data and inspect execution plans in a safe environment.

Limitations:

Without schema, constraints, and data distribution, performance claims are provisional.

Safety considerations:

Use parameterized queries and least-privilege roles; never paste production secrets or personal records.

---

## 3. Statistical test selection

- **Purpose:** Compare candidate statistical methods based on design, outcome, and assumptions.
- **Difficulty:** Advanced
- **Recommended use:** Choosing an analysis method before looking at results.

Copy-ready prompt:

> Recommend candidate analyses for this study. Design: {{DESIGN}}. Outcome type/distribution: {{OUTCOME}}. Predictors/groups: {{PREDICTORS}}. Sampling/dependence: {{DEPENDENCE}}. Question: {{QUESTION}}. Explain assumptions, alternatives, diagnostics, effect size, confidence intervals, and missing-data concerns. Ask for missing design details. Do not select a test solely from a normality test.

Example input:

Design: paired pre/post measurements on same participants; outcome continuous.

Expected output:

A conditional decision with assumptions and diagnostic checks stated.

Adaptation tips:

Consult a statistician for complex designs, clustering, multiple comparisons, or small samples.

Limitations:

Method selection depends on design and data properties not fully captured in a prompt.

Safety considerations:

Use de-identified data and report uncertainty; do not p-hack or misrepresent exploratory analyses.

---

## 4. Dashboard specification

- **Purpose:** Translate stakeholder questions into a metric and dashboard specification.
- **Difficulty:** Intermediate
- **Recommended use:** Defining a dashboard before implementation.

Copy-ready prompt:

> Specify a dashboard for {{AUDIENCE}} to answer {{QUESTIONS}}. Data sources: {{SOURCES}}. Refresh cadence: {{CADENCE}}. Define each metric, formula, grain, filters, segments, freshness indicator, access rules, chart choice, alert threshold rationale, and known caveats. Distinguish target metrics from diagnostic metrics.

Example input:

Audience: operations team. Questions: weekly volume, median resolution time, backlog age.

Expected output:

A metric dictionary and dashboard layout with explicit definitions.

Adaptation tips:

Validate metric definitions with data owners and test totals against source systems.

Limitations:

A dashboard can mislead through poor definitions, stale data, or selection effects.

Safety considerations:

Apply role-based access, aggregation thresholds, and privacy review to sensitive data.

---

## 5. Data cleaning transformation specification

- **Purpose:** Document transformations so cleaning is transparent and reproducible.
- **Difficulty:** Intermediate
- **Recommended use:** Preparing a dataset for analysis or migration.

Copy-ready prompt:

> Specify a reproducible cleaning pipeline for {{DATASET}}. Known issues: {{ISSUES}}. Intended use: {{USE}}. Define each transformation, rationale, before/after checks, treatment of missing and invalid values, duplicate policy, audit trail, and reversibility. Do not silently drop rows or invent replacement values.

Example input:

Dataset: survey responses. Issues: inconsistent date formats, duplicate submissions, missing age.

Expected output:

A documented pipeline with explicit decisions and validation assertions.

Adaptation tips:

Preserve immutable raw data and version the transformation code and outputs.

Limitations:

Cleaning choices can introduce bias; decisions require domain and data-owner approval.

Safety considerations:

Minimize sensitive fields and maintain access controls and retention rules.
