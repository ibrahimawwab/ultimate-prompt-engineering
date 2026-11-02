# Research and Academic Writing

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Research question refinement

- **Purpose:** Turn a broad topic into a focused, answerable research question.
- **Difficulty:** Beginner
- **Recommended use:** Scoping a literature review or research proposal.

### Copy-ready prompt

> Help refine this research topic: {{TOPIC}}. Field and context: {{FIELD_CONTEXT}}. Population or unit of analysis: {{POPULATION}}. Available methods/data: {{METHODS}}. Produce up to three candidate questions, explain scope and feasibility, define key concepts, identify assumptions, and suggest inclusion/exclusion boundaries. Do not invent evidence or imply the topic is novel without a literature search.

### Example input

Topic: antimicrobial resistance in hospital wastewater. Context: regional scoping review.

### Expected output

Focused questions with defined concepts, scope, and feasibility notes.

### Adaptation tips

Check that the question is answerable with accessible data and an appropriate method.

### Limitations

The model cannot establish research novelty or ethics approval from the prompt alone.

### Safety considerations

Do not include identifiable patient information. Obtain ethics review where human-subject research requires it.

---

## 2. Literature review evidence matrix

- **Purpose:** Extract comparable claims from supplied papers without fabricating details.
- **Difficulty:** Intermediate
- **Recommended use:** Organizing a set of articles for a narrative or systematic review.

### Copy-ready prompt

> Using only the supplied sources, create an evidence matrix for {{RESEARCH_QUESTION}}. Sources: {{SOURCE_TEXTS_OR_METADATA}}. Columns: citation as supplied; design; setting/sample; methods; main findings; limitations; relevance; exact supporting passage or page if available. Mark absent information as 'not reported'. Separate author claims from your synthesis. Do not add external facts or fabricate citations.

### Example input

Question: Does intervention X reduce outcome Y? Sources: abstracts and methods from three supplied studies.

### Expected output

A traceable matrix with unknown fields marked and no unsupported bibliographic details.

### Adaptation tips

Verify every extracted value against the full text; preserve page numbers and source IDs.

### Limitations

Abstract-only extraction may omit methods and limitations; the matrix is not a risk-of-bias assessment.

### Safety considerations

Remove personal data and respect copyright; summarize rather than reproduce substantial copyrighted text.

---

## 3. Critical appraisal of a study

- **Purpose:** Assess methodological strengths and weaknesses using a named framework.
- **Difficulty:** Advanced
- **Recommended use:** Appraising a study design before using its findings.

### Copy-ready prompt

> Critically appraise the supplied study using {{APPRAISAL_FRAMEWORK}}. Study text: {{STUDY}}. Research question: {{QUESTION}}. Assess design fit, sampling, measurement, bias, confounding, analysis, missing data, generalizability, and reporting. For each judgment cite the supplied section/page or state that evidence is unavailable. Distinguish limitations stated by authors from your appraisal. Do not infer unreported methods.

### Example input

Framework: CASP cohort checklist. Study: supplied cohort paper on exposure and outcome.

### Expected output

Structured appraisal with evidence-linked judgments and explicit unknowns.

### Adaptation tips

Use the framework's official current version and have a second reviewer check high-impact assessments.

### Limitations

A language model appraisal is not a substitute for trained independent reviewers or full-text verification.

### Safety considerations

Do not infer participant identities. Avoid treating observational association as causation.

---

## 4. Academic paragraph with source discipline

- **Purpose:** Draft a concise paragraph that preserves the strength and scope of supplied evidence.
- **Difficulty:** Intermediate
- **Recommended use:** Writing a synthesis paragraph from verified notes.

### Copy-ready prompt

> Draft a {{WORD_COUNT}}-word academic paragraph about {{CLAIM_OR_TOPIC}} using only these notes and sources: {{EVIDENCE_NOTES}}. Preserve qualifiers, distinguish findings from interpretation, attach citations only where supplied, and identify gaps. Do not create references, quotations, statistics, or causal claims. After the paragraph, list claims that need verification.

### Example input

Topic: association between shift work and sleep quality. Notes: two cross-sectional studies report associations; no causal inference.

### Expected output

A balanced paragraph with accurate qualifiers and a short verification list.

### Adaptation tips

Check citations, terminology, and the original studies before submission; adapt to the target journal style.

### Limitations

Supplied notes may omit contradictory evidence and cannot support a comprehensive conclusion.

### Safety considerations

Follow institutional authorship and disclosure rules; do not submit generated text as original analysis without required review.

---

## 5. Research protocol outline

- **Purpose:** Draft a protocol structure and surface methodological decisions needing expert review.
- **Difficulty:** Advanced
- **Recommended use:** Preparing an initial protocol for a study or review.

### Copy-ready prompt

> Create a protocol outline for {{STUDY_TYPE}} on {{TOPIC}} in {{SETTING}}. Objectives: {{OBJECTIVES}}. Proposed data/methods: {{METHODS}}. Include rationale, question, design, eligibility, sampling, variables, procedures, analysis, missing-data plan, bias control, ethics, data management, dissemination, and feasibility. Mark decisions requiring statistician, domain expert, or ethics committee input. Do not invent sample-size calculations.

### Example input

Study type: retrospective cohort. Topic: treatment outcomes. Setting: de-identified hospital records.

### Expected output

A protocol skeleton with operational sections and explicit unresolved decisions.

### Adaptation tips

Use the relevant reporting/protocol guideline and calculate sample size with a validated method and actual assumptions.

### Limitations

This outline is not an approved protocol or substitute for a statistical analysis plan.

### Safety considerations

Obtain ethics approval and data-access authorization; minimize and secure sensitive records.
