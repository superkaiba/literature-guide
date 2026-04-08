---
title: "Context-Value-Action Architecture for Value-Driven Large Language Model Agents"
authors: ['TianZe Zhang', 'Sirui Sun', 'Yuhang Xie', 'Xin Zhang', 'Zhiqiang Wu', 'Guojie Song']
url: http://arxiv.org/abs/2604.05939v1
source: arxiv
published_date: 2026-04-07
topics: ['AI alignment', 'language model personas']
relevance_score: 0.45
---

## Summary
This paper identifies a critical flaw in LLM-based human behavior simulation: behavioral rigidity and value polarization, where agents collapse toward extreme, homogeneous outputs rather than reflecting realistic population diversity. The authors argue that standard 'LLM-as-a-judge' evaluation masks this problem due to self-referential bias, and propose evaluating against empirical ground truth instead. Their proposed Context-Value-Action (CVA) architecture draws on the Stimulus-Organism-Response (S-O-R) psychological model and Schwartz's Theory of Basic Human Values to explicitly model how contextual stimuli activate different human values before generating actions. A key innovation is a 'Value Verifier' component trained on authentic human behavioral data that decouples value activation from action generation, avoiding over-reliance on chain-of-thought reasoning. Evaluated on CVABench—a dataset of over 1.1 million real-world interaction traces—CVA outperforms baselines on behavioral fidelity and diversity metrics. The work has implications for building more realistic human-simulacra agents and highlights the dangers of reasoning-intensity as a proxy for alignment quality.

## About the Authors
The authors—TianZe Zhang, Sirui Sun, Yuhang Xie, Xin Zhang, Zhiqiang Wu, and Guojie Song—appear to be affiliated with Chinese academic or industrial institutions; Guojie Song is a professor at Peking University known for research in graph neural networks and social computing. The other authors are less widely recognized in the international ML community, suggesting this is likely a group of students and collaborators within Song's lab or related institutions. This paper appears to be a preprint from arXiv, and the team's prior work focuses more on graph learning and social simulation rather than core LLM alignment.

## Reliability Assessment
MEDIUM confidence. The paper presents a well-motivated critique and a grounded methodology drawing on established psychological theory (Schwartz values, S-O-R model), and the use of 1.1M real-world traces for evaluation is a meaningful empirical strength. However, as an arXiv preprint it has not undergone peer review, the authors are not widely established in the LLM alignment community, and key claims—such as the counter-intuitive finding that more reasoning worsens fidelity—require scrutiny of experimental design details not fully verifiable from the abstract alone. The CVABench dataset is self-constructed and not yet independently validated.

## Why It Matters
This paper directly addresses the challenge of making LLM personas behaviorally realistic and diverse rather than polarized, which is central to alignment concerns around model homogenization and the loss of human value pluralism. The critique of 'LLM-as-a-judge' evaluation as self-referentially biased is particularly relevant for researchers using LLMs to evaluate alignment, as it suggests systematic blind spots in current methodology. The grounding in Schwartz's value theory also bridges social psychology and AI alignment in a way that could inform more rigorous frameworks for value specification.

## Related Papers
### [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (2023)
Park et al. introduced LLM-powered agents with memory, reflection, and planning to simulate believable human social behavior in a sandbox environment. This is a foundational paper for LLM-as-human-simulacra work that CVA explicitly builds upon and critiques for lacking grounded value diversity.

### [An Overview of the Schwartz Theory of Basic Values](https://doi.org/10.9707/2307-0919.1116) (2012)
Schwartz's seminal theoretical paper defining 10 universal human values and their motivational structure is the direct psychological foundation for the CVA architecture's value modeling component. Understanding this theory is essential for evaluating the plausibility of CVA's design choices.
