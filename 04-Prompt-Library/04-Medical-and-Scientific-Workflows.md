# Medical and Scientific Workflows

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Scientific paper summary

- **Purpose:** Summarize a supplied paper while preserving methods, findings, and uncertainty.
- **Difficulty:** Beginner
- **Recommended use:** Rapidly orienting to a scientific article before full appraisal.

**Copy-ready prompt**

> Summarize this paper for {{AUDIENCE}}. Text: {{PAPER_TEXT}}. Structure: objective; design and setting; population/sample; methods; primary findings with units and denominators; limitations; authors' conclusion; what cannot be concluded. Use only supplied text. Mark missing details 'not reported' and do not add clinical recommendations.

**Example input**

Audience: laboratory scientists. Paper: supplied abstract and methods on assay performance.

**Expected output**

A structured, source-bounded summary that retains numerical context and limitations.

**Adaptation tips**

Read the full paper and verify values in tables before citing or applying findings.

**Limitations**

An abstract summary is incomplete and may omit bias, protocol detail, and adverse findings.

**Safety considerations**

Do not include identifiable patient data. This is educational synthesis, not patient-specific medical advice.

---

## 2. Laboratory SOP review

- **Purpose:** Review a draft laboratory procedure for clarity, traceability, and safety gaps.
- **Difficulty:** Advanced
- **Recommended use:** Quality review of a laboratory SOP before controlled approval.

**Copy-ready prompt**

> Review this draft SOP: {{SOP_TEXT}}. Laboratory context: {{TEST_OR_PROCESS}}. Applicable standards/policies: {{REFERENCES}}. Check purpose, scope, responsibilities, specimen criteria, equipment/reagents, controls, steps, acceptance criteria, QC, result reporting, biosafety, waste, deviations, records, and version control. Flag ambiguity and missing validation evidence. Do not invent validated parameters.

**Example input**

SOP: draft specimen reception and rejection process. References: supplied institutional policy.

**Expected output**

A gap table with section, risk, clarification needed, and suggested editorial correction.

**Adaptation tips**

Verify all technical limits against validated local methods and current authoritative standards; route through document control.

**Limitations**

A language review cannot validate analytical performance or replace competency assessment.

**Safety considerations**

Follow biosafety procedures, institutional SOPs, and applicable regulations; do not expose patient identifiers.

---

## 3. Diagnostic test evidence interpretation

- **Purpose:** Interpret supplied diagnostic accuracy data without converting it into a diagnosis.
- **Difficulty:** Advanced
- **Recommended use:** Understanding sensitivity, specificity, likelihood ratios, and study limitations.

**Copy-ready prompt**

> Interpret these diagnostic test data for an educational audience. Test and target condition: {{TEST_AND_CONDITION}}. Study design/population: {{POPULATION}}. 2x2 data or reported estimates: {{DATA}}. Calculate only values supported by the data; show formulas and denominators. Discuss prevalence/context, uncertainty, spectrum and verification bias, and applicability. Do not diagnose an individual or invent missing numbers.

**Example input**

Data: TP 80, FP 20, FN 10, TN 90. Study population: specified cohort.

**Expected output**

Transparent calculations: sensitivity 88.9%, specificity 81.8%, with caveats about study population and prevalence.

**Adaptation tips**

Verify calculations independently and consult the original study and current diagnostic guidelines.

**Limitations**

Accuracy estimates may not generalize across settings; predictive values depend on prevalence.

**Safety considerations**

Not for individual diagnosis or treatment decisions. Use validated local guidance and qualified clinical oversight.

---

## 4. Research data dictionary

- **Purpose:** Create a consistent data dictionary from supplied study variables.
- **Difficulty:** Intermediate
- **Recommended use:** Documenting a dataset before analysis or handover.

**Copy-ready prompt**

> Build a data dictionary from this variable list and study context. Study: {{STUDY_CONTEXT}}. Variables: {{VARIABLES}}. For each variable provide name, label, definition, type, unit, allowed values, missing-value representation, source, derivation, and privacy classification. Mark assumptions for confirmation; do not infer clinical meaning from ambiguous codes.

**Example input**

Variables: age_years, specimen_type, result_code, collection_date. Context: de-identified laboratory dataset.

**Expected output**

A table with consistent definitions and flagged unknown code mappings.

**Adaptation tips**

Have the data owner approve code lists, units, and derived-variable definitions before analysis.

**Limitations**

Variable names alone may be insufficient to infer meaning or measurement rules.

**Safety considerations**

Minimize data, de-identify appropriately, and restrict access to sensitive health information.

---

## 5. Scientific result-to-discussion bridge

- **Purpose:** Draft a cautious discussion paragraph from supplied results and literature notes.
- **Difficulty:** Advanced
- **Recommended use:** Connecting findings to prior work without overstating causality.

**Copy-ready prompt**

> Draft a discussion section using only these results and literature notes. Study design: {{DESIGN}}. Results: {{RESULTS}}. Comparison literature: {{LITERATURE_NOTES}}. Address principal finding, consistency or difference with prior work, plausible explanations clearly labeled as hypotheses, strengths, limitations, implications, and future research. Do not introduce new results, fabricate citations, or claim causation beyond the design.

**Example input**

Design: cross-sectional. Results: supplied prevalence and association estimates. Literature notes: three verified studies.

**Expected output**

A balanced discussion that separates observed results from interpretation and notes design limitations.

**Adaptation tips**

Check all claims against source papers and align with journal reporting guidance.

**Limitations**

The model cannot judge unprovided methods or establish clinical significance.

**Safety considerations**

Protect participant confidentiality; disclose assistance according to journal and institutional policy.
