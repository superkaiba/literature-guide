---
title: "Beyond Semantics: Disentangling Information Scope in Sparse Autoencoders for CLIP"
authors: ['Yusung Ro', 'Jaehyun Choi', 'Junmo Kim']
url: http://arxiv.org/abs/2604.05724v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability', 'superposition features']
relevance_score: 0.55
---

## Summary
This paper introduces 'information scope' as a new interpretability dimension for SAE features in CLIP vision encoders, distinguishing between localized patch-level features and global image-level features. The authors propose the Contextual Dependency Score (CDS) to quantify this distinction by measuring how consistently features respond under spatial perturbations. They demonstrate that features with different information scopes have systematically different influences on CLIP's predictions and confidence.

## Why It Matters
This work extends mechanistic interpretability of SAEs beyond semantic labeling to include a spatial/scope axis, offering richer diagnostic tools for understanding how superposition and feature geometry manifest in vision-language models. It directly advances the toolkit for analyzing what individual SAE features actually encode.

## Related Papers
### [Scaling and evaluating sparse autoencoders](https://arxiv.org/abs/2406.04093) (2024)
This paper from Anthropic scales SAEs to large language models and proposes automated evaluation metrics for SAE feature quality, including sparsity and reconstruction fidelity. It provides foundational methodology for training and assessing SAEs that subsequent work like this CLIP paper builds upon.

### [Decomposing and Editing Predictions by Modeling Model Computation](https://arxiv.org/abs/2404.11534) (2024)
This paper proposes methods for attributing model predictions to internal components, examining how individual features and circuits contribute to outputs. It is relevant as a complementary approach to understanding feature influence on model confidence and predictions, which this CLIP SAE paper also investigates.
