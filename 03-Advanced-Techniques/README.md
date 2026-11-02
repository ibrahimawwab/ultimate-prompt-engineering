# 03 — Advanced Techniques

This section covers workflows and system patterns that extend beyond a single prompt. Some are established research approaches; others are broad engineering patterns whose implementation varies by provider. Treat reported benefits as task- and model-dependent, and evaluate against simpler baselines.

## Learning outcomes

After completing this section, you should be able to:

- decompose multi-stage tasks and validate intermediate outputs;
- explain tree-search-style approaches without mistaking a prompt scaffold for a search algorithm;
- describe a retrieval-augmented generation pipeline and evaluate retrieval separately from generation;
- design bounded tool-use workflows with application-enforced permissions;
- understand sampling and self-consistency without treating agreement as proof;
- use meta-prompting to develop testable prompt templates;
- account for modality-specific limitations;
- identify agentic workflow risks and define operational controls;
- recognize prompt injection and apply defense in depth.

## Lessons

1. [Prompt Chaining and Decomposition](Prompt-Chaining.md)
2. [Tree-Search-Style Reasoning Patterns](Tree-of-Thought.md)
3. [Retrieval-Augmented Generation (RAG)](Retrieval-Augmented-Generation.md)
4. [ReAct-Style Reasoning and Tool Use](ReAct-Prompting.md)
5. [Self-Consistency and Sampling](Self-Consistency.md)
6. [Meta-Prompting](Meta-Prompting.md)
7. [Multimodal Prompting](Multimodal-Prompting.md)
8. [Agentic Workflows](Agentic-Workflows.md)
9. [Prompt Injection and Defensive Design](Prompt-Injection-and-Defensive-Design.md)

## How to evaluate advanced workflows

For each technique, record:

- task definition and representative test set;
- model/provider/version and relevant settings;
- baseline and candidate workflow;
- quality, factuality, and constraint-satisfaction results;
- latency, token/tool usage, and cost;
- failure cases, security tests, and human-review requirements.

Do not attribute gains to a technique without a controlled comparison. Research results on selected benchmarks do not guarantee gains on other models or tasks.

## Safety principle

A prompt is not a security boundary. Enforce identity, permissions, resource access, tool allowlists, argument validation, approval requirements, and execution limits in the application. Treat user input, retrieved content, and tool output as potentially untrusted.
