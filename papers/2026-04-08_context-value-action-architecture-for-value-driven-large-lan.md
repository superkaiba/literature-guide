---
title: "Context-Value-Action Architecture for Value-Driven Large Language Model Agents"
authors: ['TianZe Zhang', 'Sirui Sun', 'Yuhang Xie', 'Xin Zhang', 'Zhiqiang Wu', 'Guojie Song']
url: http://arxiv.org/abs/2604.05939v1
source: arxiv
published_date: 2026-04-07
topics: ['language model personas', 'AI alignment']
relevance_score: 0.35
---

## Summary
This paper identifies 'value polarization' in LLM-based human behavior simulation, showing that increased prompt-driven reasoning actually reduces population diversity rather than improving fidelity. The authors propose the Context-Value-Action (CVA) architecture, which integrates Schwartz's Theory of Basic Human Values and the Stimulus-Organism-Response model, using a Value Verifier trained on real human interaction data to decouple value activation from action generation. Evaluated on a large-scale benchmark of 1.1 million real-world traces, CVA outperforms baselines on behavioral fidelity and interpretability.

## Why It Matters
This work directly addresses alignment-relevant questions about whether LLMs can faithfully represent diverse human values rather than collapsing to modal or self-referential behaviors, which has implications for persona simulation, value pluralism in AI systems, and the reliability of LLM-as-a-judge evaluation paradigms.

## Related Papers
### [Schwartz's Theory of Basic Human Values] (1992)
Shalom Schwartz's foundational work proposes a universal structure of ten basic human values (e.g., security, benevolence, achievement) organized in a circular motivational continuum. This theory has been widely applied in cross-cultural psychology and serves as the value taxonomy underlying the CVA architecture's Value Verifier.

### [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (2023)
Park et al. present an architecture for LLM-based agents that simulate believable human behavior through memory, reflection, and planning modules in a sandbox environment. This is a key baseline for LLM persona simulation and highlights the challenges of behavioral consistency and diversity that CVA directly addresses.
