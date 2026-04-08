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
This paper summarizes a master's thesis investigating the internal mechanisms of a maze-solving reinforcement learning agent that must select and pursue multiple sequential goals. The key finding is that the agent uses 'spatial gating through negative activations' to mark regions of interest, rather than dedicating separate channels to different targets — meaning there is little to no channel specialization for different goal representations. The authors demonstrate that a simple uniform offset applied to channel activations can completely redirect the agent's targeting behavior, suggesting a surprisingly low-dimensional control mechanism. They further validate the lack of channel specialization using Sparse Autoencoders (SAEs), finding no specific channels responsible for specific entities. The methodological insight came from analyzing mean activations across all channels as a function of agent position, a relatively simple technique that proved more revealing than more complex decompositions.

## About the Authors
The primary author is Ben Sturgeon (username 'sturb'), a master's student at the University of Cape Town supervised by Jonathan Shock. The work was done in collaboration with Paul Colognese and Narmeen Oozeer on an early version. Ben Sturgeon does not appear to be a widely recognized figure in the broader ML research community, but the thesis represents serious graduate-level mechanistic interpretability research.

## Reliability Assessment
MEDIUM confidence. This is a master's thesis posted as a LessWrong blog summary, not a peer-reviewed publication, which limits formal credibility. However, the methodology appears sound — combining activation analysis, intervention experiments (uniform offsets), and SAE probing — and the claims are appropriately scoped to the specific RL agent studied rather than overclaiming generality. The availability of both the full thesis PDF and code on GitHub increases transparency and reproducibility.

## Why It Matters
This work is directly relevant to mechanistic interpretability, offering a concrete case study of how goal representations and behavioral switching are implemented in RL agents at the circuit level. The finding that spatial gating via negative activations — rather than channel specialization — underlies multi-goal selection challenges assumptions that interpretability researchers might import from transformer-focused work, and the SAE null result is a useful data point for understanding the limits of that technique in non-transformer settings.

## Related Papers
### [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html) (2023)
This Anthropic paper introduces and applies Sparse Autoencoders (SAEs) to decompose MLP activations in language models into interpretable, monosemantic features. It is directly relevant because Sturgeon's thesis applies a similar SAE methodology to an RL agent and reaches the contrasting finding that SAEs do not reveal channel specialization for specific entities in this setting.

### [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) (2023)
This paper by Zou et al. demonstrates that high-level concepts and behaviors in neural networks can be read out and controlled via linear operations on activation space. The finding in Sturgeon's thesis that a simple uniform offset to activations can redirect agent targeting behavior is conceptually related, extending similar linear-control intuitions to RL goal-switching in a non-transformer model.
