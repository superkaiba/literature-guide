---
title: "From Data Statistics to Feature Geometry: How Correlations Shape Superposition"
authors: ['Lucas Prieto', 'Edward Stevinson', 'Melih Barsbey', 'Tolga Birdal', 'Pedro A.M. Mediano']
url: https://arxiv.org/abs/2603.09972
source: arxiv
published_date: 2026-03-10
document_type: published
topics: ['mechanistic interpretability', 'superposition features']
relevance_score: 0.86
---

# From Data Statistics to Feature Geometry: How Correlations Shape Superposition

## Plain Language Summary

So what — why should anyone care? Standard superposition theory assumed features are independent, and interference between them is pure noise. This paper shows that real features are heavily correlated, and this changes the picture: correlated features can *constructively* interfere, helping reconstruct each other. This explains the semantic clusters and circular structures (months in a ring, related words grouping together) that have puzzled interpretability researchers. The practical upshot: feature geometry in neural networks is directly shaped by training data correlations, which matters for how sparse autoencoders should be trained and interpreted.

## About the Authors

All from **Imperial College London**. **Tolga Birdal** — Assistant Professor, UKRI Future Leaders Fellow, leads CIRCLE group. 5,000+ citations across geometric ML and 3D vision. **Pedro A.M. Mediano** — Lecturer, research spanning consciousness science and information theory, 6,000+ citations. **Lucas Prieto, Edward Stevinson, Melih Barsbey** — PhD students/junior researchers with related prior work on adversarial attacks and superposition.

## Reliability Assessment

**HIGH** — Published at ICLR 2026 (peer-reviewed, highly competitive). Uses public dataset (WikiText-103). BOWS framework well-specified. Authors from strong geometric ML background. Limitations honestly acknowledged.

## Overview

The canonical treatment of superposition (Elhage et al., 2022) assumed sparse, uncorrelated features. This paper shows that relaxing the independence assumption overturns key conclusions: when features co-occur systematically, their correlations can be exploited so interference helps rather than harms reconstruction.

## Main Goal

To develop a theory of superposition for correlated features, and show it explains empirically observed feature geometries in language models that prior uncorrelated theory could not account for.

## Key Findings

- **Constructive interference is real and exploited**: When feature covariance has rank ≤ bottleneck dimension, arranging features by co-activation enables constructive rather than destructive interference.
- **Semantic clusters arise from data statistics**: Month names cluster in circles, thematic words group together — direct reflections of corpus covariance structure.
- **ReLU plays a dual role**: Preserves signal when constructive interference dominates, suppresses false positives when only partial overlap exists.
- **Weight decay drives correlated encoding**: Tight bottlenecks + weight decay bias models toward low-rank solutions implementing correlated encoding.
- **Heterogeneous strategies coexist**: Months show circular structure while Roman numerals show near-orthogonal arrangements, at the same latent dimension.

## Methodology

Bag-of-Words Superposition (BOWS): binary bag-of-words vectors (V=10,000) from WikiText-103, context window c=20, ReLU autoencoders with tied weights. ~1.62M training samples. Analyses include linear decoder baselines, UMAP projections, R² measurements. Validated that months achieve R²=0.98±0.00015.

## What's Novel

BOWS is the first controlled superposition testbed using realistic feature correlations. Formal articulation of when interference is constructive (rank condition on covariance). First explanation of why semantic clusters and month-circles appear in LM feature spaces. Novel interpretation of weight decay as promoting constructive interference.

## Limitations & Open Questions

BOWS simplifies real LM complexity (no attention, residual streams, multi-layer dynamics). No complete theoretical characterization at intermediate correlations. Restricted to tied-weight autoencoders. Transferability to frontier models conjectured, not proven.

## Implications

Feature geometry is diagnostic of training data statistics. Current SAE training penalizing all inter-feature interference may be suboptimal. Weight decay findings have direct implications for SAE hyperparameter choices. Connects modern LM representations to classical distributional semantics.

## Critical Assessment

Well-motivated, technically solid paper filling a genuine gap in superposition theory. Main weakness is the gap between BOWS and real transformers. Authors' geometric ML expertise gives a fresh perspective. ICLR acceptance validates rigor. Most useful as theoretical scaffolding for understanding why features organize as they do.

## Key Terms

- **Superposition**: Encoding more features than dimensions by representing multiple features as overlapping directions.
- **Constructive interference**: When activating one feature improves reconstruction of correlated features.
- **BOWS**: Bag-of-Words Superposition — controlled experimental framework for studying superposition with realistic correlations.
- **Value-coding features**: Features encoding continuous quantities linearly in activation space.

## Related Papers

### [Toy Models of Superposition](https://arxiv.org/abs/2209.10652) (2022) — *Essential*
Elhage et al. Foundational work on sparse uncorrelated features. *Why relevant: This paper directly challenges its assumptions.*

### [Not All Language Model Features Are Linear](https://arxiv.org/abs/2405.14860) (2024) — *Essential*
Engels et al. Discovers circular features in GPT-2 and Mistral. *Why relevant: The exact structures this paper explains.*

### [The Geometry of Concepts: Sparse Autoencoder Feature Structure](https://arxiv.org/abs/2410.19750) (2024) — *Recommended*
Identifies multi-scale geometric structure in SAE features. *Why relevant: Complementary empirical characterization of the phenomenon this paper theorizes.*

### [Adversarial Attacks Leverage Interference Between Features in Superposition](https://arxiv.org/abs/2510.11709) (2024) — *Recommended*
Companion paper from same group showing that superposition interference drives adversarial vulnerability. *Why relevant: Direct application of this theory.*
