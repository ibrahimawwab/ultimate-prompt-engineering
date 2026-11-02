# Advanced Case Study: Evidence-Grounded Research Synthesis

## Objective

Design a prompt workflow that summarizes a fixed set of public documents while preserving source traceability and uncertainty. The goal is not a persuasive narrative; it is to prevent unsupported claims and make omissions visible.

## Scenario

A research team provides three public documents about a narrowly defined topic. The task is to prepare a concise evidence brief for an expert reviewer. The model must not browse beyond the supplied documents or invent references.

Use public, non-sensitive documents that you are permitted to reproduce or summarize. Short synthetic excerpts are also acceptable for a classroom exercise.

## Workflow

### Step 1: Extract source-grounded observations

For each document, record source ID and title, publisher and publication date if stated, exact passage or page/section locator, neutral paraphrase, stated scope/method/limitations, and missing metadata marked as unknown. Do not treat a source's assertion as independently verified fact.

### Step 2: Build a claim-evidence matrix

Each proposed claim should link to one or more source observations. Mark whether sources agree, conflict, or do not address the claim. Keep inference separate from direct source statements.

### Step 3: Draft the brief

Required sections:

1. Question and scope.
2. Key findings.
3. Evidence table with source IDs.
4. Conflicts and gaps.
5. Limitations.
6. Questions for expert review.

If evidence is insufficient, state that the question cannot be answered from the supplied material.

### Step 4: Verify

A human reviewer checks every material claim against the original source and confirms that citations resolve to the cited passage. Do not rely on model-generated quotations without checking the source.

## Prompt design constraints

- Restrict the model to supplied source text.
- Require a source ID for every evidence-backed claim.
- Prohibit fabricated quotations, page numbers, publication dates, and references.
- Require explicit labels for inference and uncertainty.
- Permit abstention when sources do not support a conclusion.
- Ask the model to list relevant contradictions and missing information.

## Evaluation

Use the rubric with task-specific criteria:

- Claim traceability: every material claim maps to a source passage.
- Attribution fidelity: paraphrases preserve source meaning and scope.
- Conflict handling: disagreement is reported rather than silently resolved.
- Abstention quality: unsupported conclusions are withheld.

Critical failures include fabricated sources, invented quotations, and presenting an inference as a direct finding.

## Deliverables

- Source inventory.
- Observation ledger.
- Claim-evidence matrix.
- Draft evidence brief.
- Human verification log.
- Prompt experiment record, if baseline and candidate prompts are compared.

## Limitations

This exercise evaluates source-grounded summarization on a fixed document set. It does not establish that the source documents themselves are correct, that the search process was comprehensive, or that the workflow is suitable for clinical, legal, financial, or other high-stakes decisions. Domain experts remain responsible for consequential interpretation.
