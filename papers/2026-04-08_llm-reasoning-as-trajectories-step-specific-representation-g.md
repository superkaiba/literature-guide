---
title: "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals"
authors: ['Lihao Sun', 'Hang Dong', 'Bo Qiao', 'Qingwei Lin', 'Dongmei Zhang', 'Saravan Rajmohan']
url: http://arxiv.org/abs/2604.05655v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability']
relevance_score: 0.62
---

## Summary
This paper analyzes LLM chain-of-thought reasoning as geometric trajectories through representation space, finding that mathematical reasoning occupies functionally ordered, layer-depth-separable subspaces. Key findings include that correct and incorrect solutions diverge systematically in late reasoning steps (enabling mid-reasoning correctness prediction with ROC-AUC up to 0.87), that this structure exists in base models before reasoning-specific training, and that 'trajectory-based steering' can intervene at inference time to correct reasoning or control length.

## Why It Matters
This work directly advances mechanistic interpretability by revealing how reasoning computations are geometrically organized within LLM representation spaces, providing concrete tools for predicting and steering internal reasoning processes rather than just observing outputs.

## Related Papers
### [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) (2023)
This paper introduces Representation Engineering (RepE), which analyzes and controls LLM behavior by identifying linear directions in activation space corresponding to high-level cognitive phenomena. It provides a foundational framework for reading and steering model internals, directly related to the trajectory-based steering approach proposed in the summarized paper.

### [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://arxiv.org/abs/2305.04388) (2023)
This paper investigates whether chain-of-thought reasoning faithfully reflects the model's internal computation, finding systematic cases where CoT explanations are unfaithful to the actual reasoning process. It is closely related as it questions the mechanistic relationship between verbalized reasoning steps and underlying representations, a question the summarized paper addresses geometrically.
