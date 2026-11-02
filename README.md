# Ultimate Prompt Engineering

**Learn, Build, Optimize, and Master Prompt Engineering.**

A free, open-source, practical curriculum for designing, testing, and improving prompts and AI workflows. This repository covers foundational concepts, established techniques, advanced patterns, evaluation, safety, reusable templates, and real-world exercises.

> **Scope note:** Prompt behavior varies across models, providers, versions, and interfaces. This guide distinguishes general principles from model-dependent techniques and experimental patterns. It does not promise that a particular wording will guarantee a particular result.

## Who this is for

- Beginners learning to communicate clearly with generative AI systems.
- Developers building reliable LLM-powered applications.
- Researchers, educators, analysts, and professionals using AI in their workflows.
- Teams evaluating prompt quality, structured outputs, and AI-assisted processes.

No paid API, subscription, or proprietary tool is required to read or use the learning materials. Some examples may optionally reference provider-specific features; alternatives and limitations should be stated.

## Learning objectives

By working through this repository, you will learn to:

1. Explain how prompts interact with language models and their context.
2. Write clear instructions with explicit goals, constraints, and output requirements.
3. Select techniques appropriate to the task rather than relying on prompt jargon.
4. Use examples, structured outputs, decomposition, retrieval, and tool workflows responsibly.
5. Evaluate outputs against criteria and representative test cases.
6. Identify uncertainty, hallucinations, prompt injection, privacy risks, and other failure modes.
7. Build reusable prompt assets that are maintainable and testable.

## Learning path

| Stage | Focus | Suggested outcome |
| --- | --- | --- |
| 1. Fundamentals | Model behavior, prompt anatomy, context | Write a clear, bounded prompt |
| 2. Core techniques | Zero-shot, few-shot, roles, instructions, context, structured outputs | Choose and test a suitable prompting pattern |
| 3. Advanced techniques | Chaining, RAG, ReAct, multimodal and agentic workflows | Design a multi-step workflow |
| 4. Prompt library | Reusable prompts by task and domain | Adapt a reviewed starting point |
| 5. Applications | Coding, research, education, business | Apply techniques to realistic work |
| 6. Optimization | Testing, evaluation, iteration | Compare versions using explicit criteria |
| 7. Projects | Guided exercises and case studies | Demonstrate practical competence |

## Repository map

- [01 — Fundamentals](01-Fundamentals/README.md)
- [02 — Core Techniques](02-Core-Techniques/README.md)
- [03 — Advanced Techniques](03-Advanced-Techniques/README.md)
- [04 — Prompt Library](04-Prompt-Library/README.md)
- [05 — Real-World Applications](05-Real-World-Applications/README.md)
- [06 — Frameworks and Templates](06-Frameworks-and-Templates/README.md)
- [07 — Prompt Optimization](07-Prompt-Optimization/README.md)
- [08 — Projects and Exercises](08-Projects-and-Exercises/README.md)
- [09 — Resources](09-Resources/README.md)
- [10 — Glossary](10-Glossary/AI-and-Prompt-Engineering-Glossary.md)
- [Examples](examples/)
- [Cross-Model Evaluation Suite](evaluation/README.md)

## Core principles

- **Clarity over cleverness:** state the task, context, constraints, and desired result.
- **Evidence over confidence:** ask for sources when needed and verify important claims independently.
- **Evaluation over anecdotes:** test prompts on representative inputs and compare outputs against a rubric.
- **Least privilege:** give tools and agents only the access required for their task.
- **Human accountability:** review consequential outputs; do not delegate high-impact decisions blindly.
- **Privacy by design:** do not put secrets, credentials, or unnecessary personal data in prompts.
- **Honest limitations:** disclose uncertainty, missing information, and model-dependent behavior.

## What prompt engineering can and cannot do

Prompt engineering can improve task specification, context selection, output structure, and repeatability. It cannot guarantee factual correctness, eliminate model limitations, create capabilities the model does not have, or replace secure application design. For high-stakes use, combine prompts with authoritative data, validation, domain expertise, and human review.

## Contributing

Contributions are welcome: corrections, clearer explanations, tested examples, translations, exercises, and references to primary sources. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Do not submit confidential data, credentials, copyrighted material without permission, or claims that cannot be substantiated.

## Safety and responsible use

Read [SECURITY.md](SECURITY.md) for vulnerability reporting and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community expectations. Examples are educational starting points, not guarantees or professional advice.

## Roadmap

- [x] Establish repository purpose, learning scope, and contribution standards.
- [x] Publish the initial fundamentals curriculum and beginner exercises.
- [x] Complete and publish the six core technique lessons.
- [x] Develop the advanced technique curriculum with limitations and citations.
- [x] Build a categorized library of 50 reusable prompt templates across ten domains.
- [x] Add intermediate and advanced exercises, case studies, and reproducible evaluation examples.
- [ ] Run and publish reviewed cross-model evaluations using identified model versions and verified pricing.
- [ ] Expand authoritative resources and maintain links over time.

Progress is tracked through reviewed content and tests, not arbitrary completion badges or unverified statistics.

## License

Unless a file states otherwise, this project is released under the [MIT License](LICENSE).

## Maintainer

Created and maintained by **Dr. Muhammad Ibrahim Awwab**. Contributions from the open-source community are welcome.
