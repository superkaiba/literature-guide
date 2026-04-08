---
title: "Finding Belief Geometries with Sparse Autoencoders"
authors: ['Matthew Levinson']
url: https://arxiv.org/abs/2604.02685
source: arxiv
published_date: 2026-04-03
document_type: preprint
topics: ['mechanistic interpretability', 'superposition features']
relevance_score: 0.87
---

# Finding Belief Geometries with Sparse Autoencoders

## Plain Language Summary

So what — why should anyone care? There's a theory that language models develop internal "belief states" — probabilistic estimates about hidden aspects of the world — organized as geometric simplices in activation space. This has been proven in tiny toy models, but does it survive in real, billion-parameter LLMs? This paper builds a search pipeline using sparse autoencoders to hunt for simplex-shaped geometric clusters in Gemma-2-9B and finds 5 clusters that pass statistical tests for genuine belief-encoding. It's one of the first empirical validations that LLMs may develop structured probabilistic world models, not just next-token statistics.

## About the Authors

**Matthew Levinson** — Solo author with no identified institutional affiliation. Likely an independent researcher or someone from an alignment research training program (MATS, PIBBSS). No Google Scholar profile or prior publication record found.

## Reliability Assessment

**MEDIUM** — Technically serious exploratory preprint with sound null hypothesis testing (zero null clusters passed validation). However: single author with no affiliation, single model (Gemma-2-9B), modest effect sizes (R² margins 0.16–0.24, steering score 0.419), and only 1 of 5 clusters achieves convergent passive + causal evidence. Best treated as suggestive evidence warranting follow-up.

## Overview

This paper asks whether large language models develop internal geometric structures encoding probabilistic beliefs about hidden discrete states — structure predicted by theory and found in toy HMM-trained transformers. The author builds a four-stage pipeline using SAE feature clustering, simplex fitting, geometric selection, and dual validation.

## Main Goal

To determine whether belief-state simplex geometry emerges in large-scale LLMs trained on natural language, and to build a principled pipeline for detecting and validating such structures.

## Key Findings

- **Pipeline validated on synthetic ground truth**: Successfully recovered all 5 generative components of a toy HMM-trained transformer (mean R² = 0.61)
- **13 priority clusters identified in Gemma-2-9B**: Far exceeding null cluster baseline (0 null clusters passed)
- **Five clusters show significant barycentric predictive advantage**: Wilcoxon p < 10⁻¹⁴ for strongest cases
- **One cluster achieves convergent evidence**: Cluster 768_596 (likely encoding grammatical person) has both passive prediction and causal steering alignment
- **Phantom vertices common**: Most clusters have simplex vertices without corresponding SAE features

## Methodology

Four-stage pipeline: (1) k-subspace clustering of SAE decoder directions, (2) AANet simplex fitting for barycentric coordinates, (3) priority cluster selection by geometric consistency, (4) dual validation via barycentric predictive advantage test and causal steering test.

## What's Novel

First systematic search for belief-state simplex geometry in a large-scale LLM via SAEs. The barycentric predictive advantage test is a novel diagnostic distinguishing genuine mixture encoding from geometric coincidence.

## Limitations & Open Questions

Single model and layer. Modest effect sizes. No ground-truth labels for natural language. Most clusters show dissociated passive/causal evidence. SAE quality dependent.

## Implications

If confirmed, significant evidence that LLMs spontaneously develop structured probabilistic world models. Belief-state representations accessible via SAEs could be monitored or steered for safety.

## Critical Assessment

Technically careful and honest about limitations. The dissociation between passive and causal evidence in most clusters is a significant weakness. The most defensible interpretation: something geometrically interesting is happening, consistent with but not yet proven to be belief-state geometry. A valuable exploratory contribution.

## Key Terms

- **Belief state**: Probability distribution over discrete hidden states, maintained as observations arrive.
- **Simplex geometry**: The shape formed by probability distributions over n states — a (n-1)-dimensional simplex.
- **Barycentric coordinates**: Coordinates within a simplex expressing a point as a weighted combination of vertices.
- **AANet**: Archetypal Analysis Network for fitting simplices to data distributions.

## Related Papers

### [Transformers Represent Belief State Geometry in their Residual Stream](https://arxiv.org/abs/2405.15943) (2024) — *Essential*
Shai et al. The foundational paper demonstrating belief-state geometry in transformer residual streams. *Why relevant: Directly motivates this extension to large-scale LLMs.*

### [Constrained Belief Updates Explain Geometric Structures in Transformer Representations](https://arxiv.org/abs/2502.01954) (2025) — *Essential*
Piotrowski et al. Explains why transformers develop simplex geometry via constrained Bayesian belief updating. *Why relevant: Essential theoretical context.*

### [The Geometry of Concepts: Sparse Autoencoder Feature Structure](https://arxiv.org/abs/2410.19750) (2024) — *Recommended*
Demonstrates geometric structure in SAE feature dictionaries. *Why relevant: Directly relevant methodology for searching for geometric structure in SAE features.*
