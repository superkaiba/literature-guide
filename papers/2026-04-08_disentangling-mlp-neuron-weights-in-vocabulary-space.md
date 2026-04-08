---
title: "Disentangling MLP Neuron Weights in Vocabulary Space"
authors: ['Asaf Avrahamy', 'Yoav Gur-Arieh', 'Mor Geva']
url: http://arxiv.org/abs/2604.06005v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability', 'superposition features']
relevance_score: 0.85
---

## Summary
ROTATE (Rotation-Optimized Token Alignment in weighT spacE) is a data-free method for decomposing MLP neuron weights in large language models into interpretable components called 'vocabulary channels.' The core insight is that monosemantic neurons exhibit high kurtosis when their weight vectors are projected onto the model's vocabulary embedding space, and by optimizing rotations of neuron weight matrices to maximize this kurtosis, the method recovers sparse, interpretable directions without requiring any forward passes or input data. Applied to Llama-3.1-8B-Instruct and Gemma-2-2B-it, the method decomposes neurons into channels that correspond to coherent semantic concepts. Ablating individual vocabulary channels selectively suppresses specific input token activations or output concept promotions, demonstrating causal faithfulness. Aggregating channel-level descriptions into full neuron descriptions outperforms activation-based baselines (which require running the model on data) by 2-3x in head-to-head comparisons, making ROTATE a scalable and efficient interpretability tool.

## About the Authors
Mor Geva is a well-known researcher in mechanistic interpretability, affiliated with Tel Aviv University and Google DeepMind, with influential prior work including the 'Transformer Feed-Forward Layers Are Key-Value Memories' paper that established the vocabulary-space projection framework for MLPs. Asaf Avrahamy and Yoav Gur-Arieh appear to be graduate students or collaborators in Geva's group; they are less individually recognized but benefit from working within an established and credible research program.

## Reliability Assessment
HIGH confidence. Mor Geva has a strong track record in this specific area of mechanistic interpretability, and the methodology builds directly on her prior foundational work on vocabulary-space projections. The claims are specific and proportionate, with quantitative comparisons (2-3x improvement over baselines) and causal ablation experiments supporting the core contributions. The data-free nature of the approach is a verifiable and meaningful property.

## Why It Matters
This paper directly addresses the superposition problem in mechanistic interpretability by providing a principled, data-free method to decompose polysemantic MLP neurons into monosemantic components, which is a core challenge in the field. The vocabulary-space projection and kurtosis-maximization approach offers a novel angle on feature disentanglement that complements existing activation-based and sparse coding methods, and its scalability (no forward passes required) makes it practical for studying large models.

## Related Papers
### [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913) (2021)
This foundational paper by Geva et al. demonstrated that MLP layers in transformers function as key-value memories, where values can be interpreted by projecting them onto the output vocabulary. ROTATE directly builds on this vocabulary-space projection framework, extending it to decompose individual neurons into sparse, interpretable channels.

### [Toy Models of Superposition](https://arxiv.org/abs/2209.11838) (2022)
This influential paper from Anthropic formally characterized the superposition hypothesis—that neural networks represent more features than they have dimensions by encoding them in overlapping, polysemantic directions. ROTATE's goal of disentangling MLP neurons into monosemantic vocabulary channels is a direct practical response to the problems identified in this work.
