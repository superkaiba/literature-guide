---
title: "Disentangling MLP Neuron Weights in Vocabulary Space"
authors: ['Asaf Avrahamy', 'Yoav Gur-Arieh', 'Mor Geva']
url: http://arxiv.org/abs/2604.06005v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability', 'superposition features']
relevance_score: 0.9
---

## Summary
ROTATE is a data-free method that decomposes MLP neuron weights in LLMs by optimizing rotations to maximize kurtosis in vocabulary space, recovering sparse 'vocabulary channels' that represent monosemantic concepts. Applied to Llama-3.1-8B-Instruct and Gemma-2-2B-it, it produces neuron descriptions that outperform activation-based baselines by 2-3x in head-to-head comparisons, with ablating individual channels selectively disabling corresponding behaviors.

## Why It Matters
This work directly addresses the superposition problem in MLP neurons by providing a scalable, data-free decomposition into monosemantic directions, offering a practical tool for mechanistic interpretability research that avoids costly forward passes while revealing fine-grained feature structure.

## Related Papers
### [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913) (2021)
This paper shows that MLP layers in transformers function as key-value memories where keys capture input patterns and values promote output tokens in vocabulary space. It provides the foundational framing of neurons as storing factual associations, which ROTATE builds on by decomposing these value vectors into interpretable vocabulary channels.

### [Toy Models of Superposition](https://arxiv.org/abs/2209.11169) (2022)
This foundational work demonstrates that neural networks can represent more features than they have dimensions by superposing them in the same weight space, with sparser features more likely to be represented. It directly motivates methods like ROTATE that attempt to disentangle polysemantic neurons into monosemantic components.
