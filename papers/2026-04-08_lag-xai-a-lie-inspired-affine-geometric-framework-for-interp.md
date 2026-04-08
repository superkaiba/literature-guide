---
title: "LAG-XAI: A Lie-Inspired Affine Geometric Framework for Interpretable Paraphrasing in Transformer Latent Spaces"
authors: ['Olexander Mazurets', 'Olexander Barmak', 'Leonid Bedratyuk', 'Iurii Krak']
url: http://arxiv.org/abs/2604.06086v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability']
relevance_score: 0.45
---

## Summary
LAG-XAI introduces a geometric framework that models paraphrasing in transformer latent spaces as affine transformations (rotation, deformation, translation) inspired by Lie group actions, rather than discrete word substitutions. Applied to Sentence-BERT embeddings on the PIT-2015 Twitter corpus, the affine operator achieves AUC 0.7713, capturing ~80% of a nonlinear baseline's effective capacity while providing explicit geometric interpretability. The framework identifies stable invariants like a ~27.84° reconfiguration angle and near-zero deformation, suggesting local isometry in the paraphrase manifold.

## Why It Matters
This work directly addresses the black-box nature of transformer latent spaces by providing a mathematically principled, interpretable decomposition of semantic transformations—highly relevant to mechanistic interpretability research seeking to understand the geometric structure of neural representations.

## Related Papers
### [Linear Representations of Sentiment in Large Language Models](https://arxiv.org/abs/2310.15154) (2023)
This paper investigates how sentiment is encoded linearly in the activation spaces of large language models, finding that sentiment direction can be identified and manipulated as a vector. It provides empirical grounding for the 'linear representation hypothesis,' directly supporting the kind of geometric interpretability LAG-XAI pursues.

### [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084) (2019)
Sentence-BERT modifies the BERT architecture using siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared via cosine similarity. This is the core encoder used in LAG-XAI, and the paper's analysis of the semantic embedding space is foundational to the geometric framework proposed.
