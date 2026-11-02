# Content Creation

Five reviewed starting-point prompts. Replace every {{VARIABLE}} with task-specific information and remove fields that do not apply. These prompts guide model behavior; they do not guarantee correctness or enforce application permissions.

## 1. Evidence-led article outline

- **Purpose:** Structure an article around verified claims and an intended audience.
- **Difficulty:** Beginner
- **Recommended use:** Planning an informational article before drafting.

**Copy-ready prompt**

> Create an outline for an article about {{TOPIC}} for {{AUDIENCE}}. Purpose: {{PURPOSE}}. Available sources: {{SOURCES}}. Provide a clear thesis, section sequence, key claims each section needs, evidence required, counterpoints, and conclusion. Mark claims that need sourcing. Do not invent facts, quotations, or statistics.

**Example input**

Topic: safe password practices for small organizations. Audience: nontechnical managers.

**Expected output**

A useful outline with a source checklist and balanced treatment.

**Adaptation tips**

Verify claims against current authoritative sources before drafting.

**Limitations**

An outline is not evidence and may omit important perspectives.

**Safety considerations**

Avoid defamation, privacy violations, and misleading security guarantees.

---

## 2. Short-form video script

- **Purpose:** Draft a platform-aware script with clear pacing and factual placeholders.
- **Difficulty:** Intermediate
- **Recommended use:** Creating a short educational video from verified source notes.

**Copy-ready prompt**

> Write a {{DURATION}} script for {{PLATFORM}} on {{TOPIC}}. Audience: {{AUDIENCE}}. Verified facts: {{FACTS}}. Required caveats: {{CAVEATS}}. Include hook, narration, visual suggestions, on-screen text, transitions, and closing. Preserve uncertainty; label reenactments or illustrative visuals. Do not fabricate quotes or events.

**Example input**

Duration: 60 seconds. Platform: vertical video. Topic: how a laboratory confirms a result. Facts: supplied workflow notes.

**Expected output**

A timed script with narration and matching visual cues, using only supplied facts.

**Adaptation tips**

Read aloud for timing and verify every factual line and visual against source material.

**Limitations**

Timing varies by speaker; visual suggestions do not establish that footage exists or is licensed.

**Safety considerations**

Respect dignity and consent; do not depict identifiable patients or imply AI-generated scenes are real evidence.

---

## 3. Social post adaptation

- **Purpose:** Adapt one verified message to several platform formats without changing its meaning.
- **Difficulty:** Beginner
- **Recommended use:** Repurposing an announcement or educational message.

**Copy-ready prompt**

> Adapt this message for {{PLATFORMS}}. Audience: {{AUDIENCE}}. Original: {{MESSAGE}}. Required facts and links: {{FACTS_AND_LINKS}}. Preserve meaning and qualifications. For each platform provide suitable length, accessible language, and a non-deceptive call to action. Do not add claims, hashtags implying endorsement, or fabricated links.

**Example input**

Original: announcement of a free open-source prompt engineering repository. Platforms: LinkedIn and X.

**Expected output**

Platform-specific drafts that retain the same factual content.

**Adaptation tips**

Check character limits, link destinations, accessibility, and current platform rules before publishing.

**Limitations**

Platform algorithms and engagement cannot be guaranteed.

**Safety considerations**

Do not impersonate people, buy engagement, or disclose private information.

---

## 4. Editorial fact-check checklist

- **Purpose:** Audit a draft for claims that require verification and unsupported certainty.
- **Difficulty:** Intermediate
- **Recommended use:** Reviewing content before publication.

**Copy-ready prompt**

> Fact-check this draft: {{DRAFT}}. Intended audience: {{AUDIENCE}}. Source set: {{SOURCES}}. Extract factual claims, classify each as supported/partly supported/unsupported/not verifiable from supplied sources, identify the exact supporting passage where available, and list needed corrections. Check dates, numbers, names, causal language, and image captions. Do not search or invent sources unless browsing is explicitly available.

**Example input**

Draft: supplied article with claims about a recent technology policy. Sources: three official documents.

**Expected output**

A claim-by-claim audit table with evidence gaps and suggested cautious wording.

**Adaptation tips**

Verify primary sources and publication dates manually; review high-impact claims independently.

**Limitations**

Source excerpts may be incomplete or outdated; absence from supplied sources is not proof of falsity.

**Safety considerations**

Correct harmful misinformation promptly and avoid publishing private or identifying details.

---

## 5. Podcast interview preparation

- **Purpose:** Prepare neutral questions that elicit detail without presuming facts.
- **Difficulty:** Intermediate
- **Recommended use:** Planning an interview with an expert or project participant.

**Copy-ready prompt**

> Prepare an interview guide about {{TOPIC}} with guest role {{GUEST_ROLE}} and audience {{AUDIENCE}}. Goals: {{GOALS}}. Include opening context, open-ended questions, follow-ups, clarification prompts, and a closing question. Avoid leading or defamatory premises. Mark claims that need independent verification and suggest consent/recording checks.

**Example input**

Topic: community cybersecurity awareness. Guest: incident responder. Audience: small business owners.

**Expected output**

A sequenced guide with neutral questions and verification prompts.

**Adaptation tips**

Tailor questions to the guest's expertise and confirm recording permissions.

**Limitations**

A guide cannot guarantee balanced coverage or accurate answers.

**Safety considerations**

Respect consent, confidentiality, and embargoes; do not solicit sensitive incident details.
