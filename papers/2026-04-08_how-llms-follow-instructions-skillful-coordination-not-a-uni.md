---
title: "How LLMs Follow Instructions: Skillful Coordination, Not a Universal Mechanism"
authors: ['Elisabetta Rocchetti', 'Alfio Ferrara']
url: http://arxiv.org/abs/2604.06015v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability', 'language model personas']
relevance_score: 0.72
---

## Summary
This paper investigates whether instruction-following in LLMs relies on a single universal mechanism or task-specific skill coordination. Through diagnostic probing, cross-task transfer analysis, and causal ablation across nine tasks in three instruction-tuned models, the authors find evidence against a universal mechanism: task-specific probes outperform general ones, cross-task transfer is weak and similarity-clustered, and constraint satisfaction operates as dynamic layer-wise monitoring rather than pre-generation planning.

## Why It Matters
For mechanistic interpretability, this work directly challenges the assumption of a unified instruction-following circuit, suggesting instead that probing and circuit-finding efforts must account for task-specific representations and sparse asymmetric dependencies. For persona research, the finding that semantic tasks emerge in later layers while structural constraints emerge early has implications for understanding how model identity and behavioral constraints are encoded and maintained during generation.

## Related Papers
### [FLAN: Finetuned Language Models are Zero-Shot Learners](https://arxiv.org/abs/2109.01652) (2021)
This foundational paper introduced instruction tuning by fine-tuning language models on a large mixture of tasks phrased as natural language instructions, demonstrating strong zero-shot generalization. It established the assumption of domain-general instruction-following ability that the Rocchetti & Ferrara paper directly interrogates and challenges.

### [Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small](https://arxiv.org/abs/2211.00593) (2022)
This mechanistic interpretability paper identified a specific circuit in GPT-2 responsible for indirect object identification, demonstrating that specific capabilities can be localized to sparse, task-specific subnetworks rather than diffuse representations. This approach of causal circuit analysis is directly relevant to the ablation methodology used in the Rocchetti & Ferrara paper.
