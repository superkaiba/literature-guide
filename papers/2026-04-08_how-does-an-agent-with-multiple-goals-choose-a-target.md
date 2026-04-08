---
title: "How Does an Agent with Multiple Goals Choose a Target?"
authors: ['sturb']
url: https://www.lesswrong.com/posts/XWmqSTX89rgqeqyfv/how-does-an-agent-with-multiple-goals-choose-a-target
source: lesswrong
published_date: 2026-04-08
topics: ['mechanistic interpretability', 'AI alignment']
relevance_score: 0.55
---

## Summary
This paper (a master's thesis from University of Cape Town) investigates how a maze-solving RL agent with a convolutional neural network (not a transformer) internally represents and switches between multiple sequential goals. The core mechanistic finding is that the network uses 'spatial gating through negative activations' — regions of strong negative activation effectively mask or inhibit areas of the observation space, and as the agent collects entities sequentially, these inhibited regions are progressively 'disinhibited' (the negative activations lift), revealing the next target. Crucially, the authors find no significant channel specialisation for different targets; individual channels do not correspond to specific goal entities. This is confirmed by applying Sparse Autoencoders (SAEs), which also fail to find target-specific channels. The authors demonstrate that a simple uniform offset applied to channel activations can completely redirect the agent's targeting behaviour, suggesting the representation is distributed rather than localised. The methodological contribution highlights that tracking mean activation intensity across channels over rollouts is a valuable and underexplored tool for mechanistic interpretability of RL agents.

## About the Authors
Benjamin Sturgeon (username 'sturb') is an AI safety researcher based in Cape Town, South Africa, who completed his MPhil in Applied Mathematics at the University of Cape Town supervised by Jonathan Shock. He co-founded AI Safety Cape Town, participated in the MATS (ML Alignment Theory Scholars) extension program, and has a spotlight paper 'SAGE-Eval' at NeurIPS 2025 Datasets and Benchmarks Track. Jonathan Shock is an Associate Professor in Mathematics and Applied Mathematics at UCT who directs the UCT AI Initiative, with ~2,400 citations on Google Scholar; his research spans reinforcement learning, string theory, computational neuroscience, and machine learning. As an early-career researcher, Sturgeon does not yet have an established h-index, though he is building a publication record in AI safety and LLM evaluation.

## Reliability Assessment
MEDIUM confidence. The work is a master's thesis published as a LessWrong post rather than peer-reviewed at a major venue, and the lead author is early-career without an extensive publication track record; however, the supervisor (Jonathan Shock) is an established academic with significant citations and relevant expertise in RL. The methodology appears thoughtful — using multiple complementary techniques (mean activation analysis, SAEs, uniform offset interventions) to validate the core finding — and the claims are proportionate to the evidence (a single maze-solving agent), though the generalisability beyond this specific small-scale setting remains unestablished.

## Why It Matters
This work directly addresses a key open problem in mechanistic interpretability — understanding how RL agents represent and select between goals — which is central to AI alignment concerns about goal misgeneralisation, deceptive alignment, and mesa-optimisation. The finding that goal representations use distributed spatial gating rather than discrete channel specialisation suggests that detecting and steering agent goals may require different tools than the feature-localization approaches common in transformer interpretability, which has important implications for developing practical alignment interventions on agentic systems.

## Related Papers
### [Interpreting Emergent Planning in Model-Free Reinforcement Learning](https://arxiv.org/abs/2504.01871) (2025)
Published at ICLR 2025, this paper provides the first mechanistic evidence that model-free RL agents (DRC agents in Sokoban) internally learn to plan, using concept-based interpretability and causal interventions. It is closely related as it also reverse-engineers internal representations of RL agents to understand goal-directed behaviour, finding that agents form spatial plans resembling bidirectional search.

### [Mechanistic Interpretability of Reinforcement Learning Agents](https://arxiv.org/abs/2411.00867) (2024)
This paper applies mechanistic interpretability techniques (saliency mapping, feature mapping) to an IMPALA agent trained on procedurally generated mazes, studying goal misgeneralisation. It directly complements Sturgeon's work by investigating similar maze-solving RL agents but focusing on how learned biases (e.g., always navigating toward one corner) manifest in network internals.
