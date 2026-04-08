---
title: "A survey on deep learning enabled automatic modulation classification methods: Data representations, model structures, and regularization techniques"
authors: ['Xinyu Tian', 'Qinghe Zheng', 'Binglin Li', 'Dali Qiao', 'Kan Yu', 'Zhiqing Wei', 'Bin Li', 'Haozhun Jiang', 'Xingwang Li', 'Yun Lin', 'Guan Gui']
url: https://www.semanticscholar.org/paper/14f6e166a14571302828fbc97e2c03e4f79a3baa
source: semantic_scholar
published_date: 2026-05-01
document_type: research paper
topics: ['mechanistic interpretability', 'AI safety', 'AI alignment', 'language model personas', 'emergent misalignment', 'subliminal learning', 'superposition features']
relevance_score: 0.5
---

# A survey on deep learning enabled automatic modulation classification methods: Data representations, model structures, and regularization techniques

## Overview
This is a survey paper published in the journal Signal Processing (Elsevier, 2026, Vol. 242) that comprehensively reviews deep learning (DL) methods for automatic modulation classification (AMC) in wireless communication systems. It systematically organizes the field around three core pillars: data representations, model structures, and regularization techniques used in DL-based AMC approaches from 2020-2025.

## About the Authors
Guan Gui is the senior author, an IEEE Fellow, Highly Cited Researcher, and Professor at Nanjing University of Posts and Telecommunications (NJUPT) with ~23,562 citations and an h-index of ~39+. Qinghe Zheng is an Associate Professor at Shandong Management University with research in deep learning, image processing, and AMC, who received his Ph.D. from Shandong University in 2022. Xinyu Tian is also affiliated with Shandong Management University's Department of Intelligent Engineering. Yun Lin is a full professor at Harbin Engineering University's College of Information and Communication Engineering, with ~7,891 citations and expertise in signal processing and AI for radio. Xingwang Li is an Associate Professor at Henan Polytechnic University with ~7,895 citations, listed in Stanford's World's Top 2% Scientists.

## Reliability Assessment
MEDIUM confidence. The paper is published in a reputable peer-reviewed journal (Signal Processing, Elsevier). The senior author (Guan Gui) is a well-established IEEE Fellow with high citations. However, the large author count, heavy self-citation of the group's own work, and significant overlap with a companion survey by the same team in IJIS (2025) are minor concerns. As a survey, it makes no novel empirical claims that could be falsified. The systematic review methodology is standard but the selection criteria could introduce bias toward the authors' own research direction.

## Main Goal
The primary objective is to provide a comprehensive, organized review of recent deep learning-enabled automatic modulation classification methods, categorizing them by data representation approaches, neural network model architectures, and training regularization techniques, while identifying challenges and future research directions.

## Key Findings
- Finding 1: Data representation, model structure, and regularization techniques together constitute the three core elements for improving DL-based AMC model performance, and the survey systematically categorizes existing methods along these three dimensions.
- Finding 2: The survey covers literature from the past five years (2020-2025) using a systematic multi-stage review process, screening by keywords such as AMC, DL, data representation, DL model structure, and regularization technique.
- Finding 3: Deep learning has brought new opportunities to AMC that extend beyond traditional likelihood-based and feature-based methods, with applications in both military and civilian domains including cognitive radio and spectrum sensing.

## Methodology
The authors adopted a systematic literature review methodology, searching and screening literature from 2020-2025 using targeted keywords. They transitioned through a multi-stage review process from title/abstract screening to full manuscript analysis, focusing on methods and results, and ultimately selected highly relevant literature as the basis for the review. The survey covers standard benchmark datasets such as RadioML 2016.10a and RadioML 2018.01A, and examines model architectures including CNNs, LSTMs, ResNets, CLDNNs, attention mechanisms, and transformers.

## What's Novel
Unlike prior AMC surveys that focus primarily on model architectures or general methods, this survey uniquely organizes the DL-based AMC literature around three distinct pillars: (1) data representation formats (I/Q data, constellation diagrams, spectrograms, etc.), (2) model structures (CNN, RNN, hybrid, transformer-based), and (3) regularization techniques used during training. This tripartite framework provides a more actionable guide for practitioners. The same author group (Zheng, Tian) also published a companion survey in IJIS (2025) covering traditional methods alongside DL, while this paper goes deeper into the DL-specific training pipeline.

## Limitations & Open Questions
As a survey paper, it does not introduce new experimental results or methods. The systematic review is limited to a five-year window (2020-2025), potentially missing influential earlier foundational work. The paper primarily covers methods validated on synthetic RadioML benchmark datasets rather than real-world over-the-air deployments, which may limit generalizability claims. The coverage of emerging approaches such as foundation models, state space models (Mamba), and federated learning for AMC may be limited given the rapidly evolving field.

## Implications
This survey provides a structured reference for researchers entering the DL-based AMC field, helping them identify which data representations, model architectures, and regularization strategies are most effective for their use case. It is relevant for cognitive radio, spectrum sensing, dynamic spectrum access, and military signal intelligence applications. The identified future directions could guide research funding and focus areas in 6G-era communications.

## Critical Assessment
This is a well-structured survey from authors with deep domain expertise in AMC. The three-pillar organizational framework (data, model, regularization) is a useful contribution over previous surveys. The paper is published in Signal Processing (Elsevier), a reputable peer-reviewed journal with strong standing in the signal processing community. However, the author list is large (11 co-authors), and the paper heavily self-cites prior work from the same group (multiple references to Zheng et al. and Tian et al.). The overlap with their earlier companion survey in IJIS (2025) on similar topics raises questions about incremental novelty. The paper does not appear to have generated significant discussion in the ML/AI safety community, as it falls entirely outside the alignment/interpretability domain. For an ML researcher focused on mechanistic interpretability or AI safety, this paper has essentially zero relevance.

## Key Terms
- **Automatic Modulation Classification (AMC):** The task of automatically identifying the modulation scheme (e.g., BPSK, QPSK, QAM) of an unknown received wireless signal, critical for cognitive radio and spectrum management.
- **I/Q Data:** In-phase and Quadrature components of a received radio signal, commonly used as raw input representation for deep learning-based AMC models.
- **RadioML Dataset:** A family of benchmark datasets (e.g., RadioML 2016.10a, 2018.01A) created by O'Shea et al. using GNU Radio, containing synthetic radio signals with various modulations and SNR levels for AMC research.
- **Cognitive Radio:** A radio system that can dynamically sense and adapt to its electromagnetic environment, automatically adjusting communication parameters like modulation scheme for efficient spectrum utilization.
- **Regularization Techniques:** Methods used during model training (e.g., dropout, data augmentation, weight decay, prior regularization) to prevent overfitting and improve generalization performance of deep learning models.
- **CLDNN:** Convolutional Long Short-term Deep Neural Network, a hybrid architecture combining CNN feature extraction with LSTM temporal modeling, widely used in AMC tasks.

## Related Papers
### [Convolutional Radio Modulation Recognition Networks](https://arxiv.org/abs/1602.04105) (2016) — *Essential*
The foundational paper by O'Shea et al. that first applied CNNs to raw I/Q radio signals for modulation classification and introduced the RadioML datasets. This pioneered the DL-based AMC field that the survey covers.
*Why relevant: Foundational work that started the DL-based AMC field; introduced the RadioML benchmark datasets used by virtually all work reviewed in this survey.*

### [Automatic Modulation Classification: A Deep Architecture Survey](https://ieeexplore.ieee.org/document/9576081) (2021) — *Essential*
A prior comprehensive survey by Huynh-The et al. in IEEE Access that reviews deep architectures for AMC, covering fundamental DL concepts and their application to modulation pattern recognition. This is the main competing/predecessor survey.
*Why relevant: Primary competing survey that this paper updates and extends with a different organizational framework (data/model/regularization vs. architecture-centric).*

### [Recent Advances in Automatic Modulation Classification Technology: Methods, Results, and Prospects](https://onlinelibrary.wiley.com/doi/10.1155/int/4067323) (2025) — *Recommended*
A companion survey by Zheng, Tian et al. (same core author group) published in International Journal of Intelligent Systems, covering AMC methods across three categories: likelihood-based, feature-based, and deep learning methods.
*Why relevant: Companion survey from the same research group providing broader context including traditional methods; helps understand the overlap and differentiation with the current paper.*

### [DL-PR: Generalized automatic modulation classification method based on deep learning with priori regularization](https://www.sciencedirect.com/science/article/abs/pii/S0952197623002853) (2023) — *Recommended*
A method paper by Zheng, Tian et al. proposing a deep learning prior regularization approach for AMC that incorporates prior knowledge of SNR distributions during training to improve generalization.
*Why relevant: A primary research contribution from the same author group, directly relevant to the regularization pillar of the survey and likely a key method reviewed within it.*
