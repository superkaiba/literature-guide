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
LAG-XAI introduces a geometric framework for interpreting paraphrasing in transformer latent spaces by modeling paraphrase transitions as affine transformations (rotation, deformation, translation) on a semantic manifold rather than discrete word substitutions. The framework uses a mean-field approximation inspired by local Lie group actions to decompose these transformations into interpretable components. Experiments on the PIT-2015 Twitter paraphrase corpus encoded with Sentence-BERT achieve an AUC of 0.7713, capturing roughly 80% of a non-linear baseline's effective discriminative capacity (AUC 0.8405) while remaining fully parametrically interpretable. A key empirical finding is 'linear transparency': a stable reconfiguration angle of ~27.84° and near-zero deformation suggesting local isometry in the paraphrase manifold. Cross-domain generalization is demonstrated via validation on a separate TURL dataset, supporting the framework's broader applicability.

## About the Authors
The authors — Olexander Mazurets, Olexander Barmak, Leonid Bedratyuk, and Iurii Krak — appear to be affiliated with Ukrainian academic institutions (likely Kyiv-based, given Krak's known association with Taras Shevchenko National University of Kyiv and the Institute of Cybernetics). They are not widely recognized figures in the core mechanistic interpretability or NLP communities, and their prior work appears focused on applied mathematics and computational linguistics rather than mainstream deep learning interpretability.

## Reliability Assessment
MEDIUM confidence. The methodology is mathematically coherent and the empirical claims are modest and proportionate to the evidence presented. However, the authors are not prominent in the interpretability or NLP fields, the paper is an arXiv preprint without confirmed peer review, and the experimental scope is limited to one relatively small and noisy corpus (PIT-2015 Twitter) with a single encoder (Sentence-BERT). The Lie group motivation is somewhat loosely applied — the 'mean-field approximation' framing is suggestive rather than formally rigorous — which may limit reproducibility and theoretical depth.

## Why It Matters
For mechanistic interpretability research, this paper offers a mathematically grounded approach to decomposing transformer representations into geometric primitives, connecting latent space structure to human-interpretable transformations. The use of Lie group theory to characterize semantic operations aligns with broader efforts to find structured, algebraic explanations for neural network computations, and the 'linear transparency' finding echoes work on linear representation hypotheses in LLMs.

## Related Papers
### [Language Models Represent Space and Time](https://arxiv.org/abs/2310.02207) (2023)
This paper demonstrates that large language models develop linear representations of spatial and temporal concepts in their embedding spaces. It connects directly to LAG-XAI's 'linear transparency' finding by providing evidence that semantic structure in transformer latent spaces is often geometrically regular and linearly decodable.

### [Linguistic Regularities in Continuous Space Word Representations](https://aclanthology.org/N13-1090/) (2013)
Mikolov et al.'s classic paper showing that word embedding spaces exhibit linear algebraic structure (e.g., king - man + woman ≈ queen), foundational to the idea that semantic transformations can be modeled as geometric operations. LAG-XAI extends this intuition to paraphrasing via affine transformations on sentence-level embeddings.
