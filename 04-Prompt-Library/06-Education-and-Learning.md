# Education and Learning

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Personalized lesson plan

- **Purpose:** Create a lesson sequence aligned to learner level and measurable objectives.
- **Difficulty:** Beginner
- **Recommended use:** Planning a class or self-study session.

### Copy-ready prompt

> Design a {{DURATION}} lesson on {{TOPIC}} for {{LEARNER_LEVEL}}. Prior knowledge: {{PRIOR_KNOWLEDGE}}. Resources: {{RESOURCES}}. Include measurable objectives, short explanation, worked example, guided practice, independent task, formative checks, misconception checks, and adaptation for different needs. Do not assume access to unlisted resources.

### Example input

Topic: fractions. Level: early secondary. Duration: 45 minutes.

### Expected output

A timed lesson plan with observable learning checks and practice.

### Adaptation tips

Check curriculum alignment and adjust pacing after observing learners.

### Limitations

Generated plans need teacher review for level, cultural context, and accessibility.

### Safety considerations

Avoid collecting unnecessary student personal data; accommodate disabilities and language needs.

---

## 2. Socratic tutor

- **Purpose:** Guide a learner through a problem using questions rather than immediately giving the answer.
- **Difficulty:** Beginner
- **Recommended use:** Practice where reasoning matters more than answer delivery.

### Copy-ready prompt

> Tutor me on {{TOPIC}} at {{LEVEL}}. My goal: {{GOAL}}. Ask one question at a time. Wait for my answer, diagnose the misconception if present, give a small hint, and gradually increase support. Do not reveal the full solution until I request it or have made a genuine attempt. End with a short transfer problem.

### Example input

Topic: balancing linear equations. Level: beginner. Goal: solve one-step equations.

### Expected output

An interactive sequence of scaffolded questions and feedback.

### Adaptation tips

If the learner is stuck, offer a worked example and then a new analogous question.

### Limitations

The tutor may misread an answer or teach an inaccurate explanation; verify important content.

### Safety considerations

Do not shame learners or infer ability from a single response; protect student information.

---

## 3. Quiz with answer rationale

- **Purpose:** Generate an assessment that tests understanding and explains the answer key.
- **Difficulty:** Intermediate
- **Recommended use:** Creating a formative quiz from supplied learning outcomes.

### Copy-ready prompt

> Create {{QUESTION_COUNT}} questions for {{TOPIC}} and {{LEVEL}} based on these outcomes: {{OUTCOMES}}. Mix recall, application, and reasoning. Provide answer key with concise rationale, misconception targeted, and difficulty. Ensure one unambiguous best answer for single-choice items. Flag any question needing teacher verification.

### Example input

Topic: bacterial cell structure. Outcomes: distinguish cell wall, membrane, ribosomes, nucleoid.

### Expected output

A balanced quiz and rationale aligned to the stated outcomes.

### Adaptation tips

Review scientific accuracy, reading level, and alignment before student use.

### Limitations

Generated questions can contain ambiguity or incorrect keys; pilot with a teacher.

### Safety considerations

Do not use live exam questions or facilitate cheating; follow assessment integrity policies.

---

## 4. Explain a difficult concept at multiple levels

- **Purpose:** Adapt one explanation to progressively deeper levels without changing core facts.
- **Difficulty:** Beginner
- **Recommended use:** Teaching a concept to audiences with different prior knowledge.

### Copy-ready prompt

> Explain {{CONCEPT}} at three levels: beginner, intermediate, and advanced. Audience context: {{AUDIENCE}}. Use one consistent analogy only if it is scientifically appropriate; identify where the analogy breaks. Include a concrete example, common misconception, and a one-question comprehension check at each level.

### Example input

Concept: how vaccines train immune responses. Audience: mixed-level learners.

### Expected output

Three progressively deeper explanations with caveats and comprehension checks.

### Adaptation tips

Verify technical details and replace analogies that could create misconceptions.

### Limitations

Simplification may omit important nuance; advanced level still needs subject review.

### Safety considerations

For health topics, distinguish general education from personal medical advice.

---

## 5. Study schedule with retrieval practice

- **Purpose:** Build a realistic schedule that uses spaced review and active recall.
- **Difficulty:** Intermediate
- **Recommended use:** Planning study sessions around a deadline and available time.

### Copy-ready prompt

> Create a study plan for {{SUBJECTS}} until {{DEADLINE}}. Available time: {{TIME_BUDGET}}. Current confidence: {{CONFIDENCE}}. Fixed commitments: {{COMMITMENTS}}. Schedule focused blocks, retrieval practice, spaced review, mixed practice, breaks, and buffer time. Include a weekly checkpoint and adjustment rule. Do not assume unlimited study time.

### Example input

Subjects: microbiology and statistics. Time: 90 minutes/day. Deadline: 4 weeks.

### Expected output

A realistic calendar with review intervals and progress checks.

### Adaptation tips

Adjust based on actual recall performance, not time spent alone.

### Limitations

Spacing intervals are starting points; learning needs differ by topic and learner.

### Safety considerations

Protect sleep and wellbeing; do not encourage unsafe overwork.
