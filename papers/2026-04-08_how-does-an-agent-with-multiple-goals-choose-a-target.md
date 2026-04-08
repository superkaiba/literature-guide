---
title: "How Does an Agent with Multiple Goals Choose a Target?"
authors: ['sturb']
url: https://www.lesswrong.com/posts/XWmqSTX89rgqeqyfv/how-does-an-agent-with-multiple-goals-choose-a-target
source: lesswrong
published_date: 2026-04-08
topics: ['mechanistic interpretability', 'AI safety']
relevance_score: 0.55
---

## Summary
This thesis investigates how a maze-solving RL agent internally represents and switches between multiple sequential goals, finding that the network uses spatial gating via negative activations to mark regions of interest rather than channel specialisation for different targets. A key finding is that a simple uniform offset to channel activations can completely redirect the agent's targeting behaviour, and this lack of channel specialisation was confirmed even when applying Sparse Autoencoders (SAEs). The work demonstrates that meaningful mechanistic insights can emerge from straightforward analysis of mean activations across channels.

## Why It Matters
This work is directly relevant to mechanistic interpretability of RL agents, offering concrete findings about how goal representations are encoded and manipulated in neural networks, which has implications for understanding and controlling AI systems pursuing multiple objectives.

## Related Papers
### [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) (2020)
This Distill publication introduces the 'circuits' framework for mechanistic interpretability, arguing that neural networks can be understood by examining individual neurons and their connections. It establishes foundational concepts for identifying feature representations and computational motifs within networks, directly relevant to the channel specialisation analysis in this thesis.

### [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemanticity-features/index.html) (2023)
This paper from Anthropic applies Sparse Autoencoders (SAEs) to decompose superposed features in neural networks into more interpretable, monosemantic components. Its methodology is directly relevant to this thesis, which also applies SAEs to investigate whether specific channels encode specific goal-related entities in the RL agent.
