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
This paper introduces 'information scope' as a new dimension for interpreting Sparse Autoencoder (SAE) features learned from CLIP vision encoders, complementing existing semantic-focused analyses. The authors observe that SAE features differ not just in what they represent semantically, but in how broadly they aggregate visual evidence—some features respond to localized, patch-specific cues while others capture global, image-level signals. To quantify this distinction, they propose the Contextual Dependency Score (CDS), a metric that separates 'local scope' features (positionally stable across spatial perturbations) from 'global scope' features (positionally variant). Experiments demonstrate that features of different information scopes have systematically different influences on CLIP's downstream predictions and confidence scores. The work establishes information scope as a critical interpretability axis beyond semantics, offering a finer-grained diagnostic lens for understanding representations encoded in SAE-derived features of vision-language models.

## About the Authors
The authors—Yusung Ro, Jaehyun Choi, and Junmo Kim—are affiliated with KAIST (Korea Advanced Institute of Science and Technology), a leading South Korean research institution. Junmo Kim is a well-established professor at KAIST with extensive work in computer vision and deep learning. The other authors are likely graduate students or postdocs in his group; they are not widely recognized individually in the mechanistic interpretability community, though their work engages seriously with that literature.

## Reliability Assessment
MEDIUM confidence. The paper appears to be an arXiv preprint without confirmed peer review, which is standard for this fast-moving field. KAIST is a credible institution with a strong computer vision track record. The methodology—proposing a quantitative score (CDS) and testing it on CLIP SAE features—seems reasonable and proportionate to the claims made. However, without peer review and given limited prior visibility of the first authors in interpretability research, independent validation of the CDS metric and experimental results would strengthen confidence.

## Why It Matters
This paper is directly relevant to mechanistic interpretability research, as it extends the SAE/superposition feature analysis toolkit beyond semantic labeling to structural properties of how features aggregate information spatially. It demonstrates that not all SAE features are equal in terms of their representational scope, which has implications for understanding how superposition and polysemanticity manifest differently for local versus global features in vision encoders. The CDS metric provides a concrete, practical tool for researchers probing internal representations of multimodal models.

## Related Papers
### [Scaling and evaluating sparse autoencoders](https://arxiv.org/abs/2406.04093) (2024)
This paper by Gao et al. (OpenAI) investigates how to scale SAEs for interpreting large language models, introducing evaluation metrics for SAE feature quality. It is directly foundational to the current work, which applies and extends SAE-based interpretability to CLIP vision encoders.

### [Multimodal Neurons in Artificial Neural Networks](https://distill.pub/2021/multimodal-neurons/) (2021)
This paper by Goh et al. (OpenAI/Clarity) identified neurons in CLIP that respond to concepts across modalities, providing early mechanistic analysis of CLIP's internal representations. It serves as an important precursor to the current work's investigation of how CLIP features aggregate visual evidence at different spatial scopes.
