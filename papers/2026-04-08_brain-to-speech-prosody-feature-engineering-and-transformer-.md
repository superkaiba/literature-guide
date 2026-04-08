---
title: "Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction"
authors: ['Mohammed Salah Al-Radhi', 'Géza Németh', 'Andon Tchechmedjiev', 'Binbin Xu']
url: http://arxiv.org/abs/2604.05751v1
source: arxiv
published_date: 2026-04-07
document_type: preprint
topics: ['mechanistic interpretability', 'AI safety', 'AI alignment', 'language model personas', 'emergent misalignment', 'subliminal learning', 'superposition features']
relevance_score: 0.5
---

# Brain-to-Speech: Prosody Feature Engineering and Transformer-Based Reconstruction

## Overview
This is an arxiv preprint (book chapter format) presenting a brain-to-speech synthesis pipeline that extracts prosodic features from intracranial EEG (iEEG) data and uses a transformer-based architecture to reconstruct speech. The central problem is improving the naturalness and intelligibility of speech reconstructed from neural signals by explicitly modeling prosodic features like intonation, pitch, and rhythm. This work is closely related to the authors' MiSTR paper accepted at Interspeech 2025.

## About the Authors
Mohammed Salah Al-Radhi is a Research Scientist/Postdoc at Budapest University of Technology and Economics (BME), with a PhD in AI of Speech from BME (summa cum laude, 2020). He has ~209 citations on Google Scholar and ~49 publications, with his core expertise in speech synthesis, vocoders, and voice conversion; his brain-to-speech work is recent (2024-2025). Géza Németh is a Full Professor at BME's Department of Telecommunications and Media Informatics with ~981 citations and 157 publications, heading the Speech Communication and Smart Interactions Lab with decades of TTS experience. Andon Tchechmedjiev is an Associate Professor at IMT Mines Alès / EuroMov DHM with ~548 citations, specializing in computational semantics, NLP, and recently neuroengineering/BCI. Binbin Xu is affiliated with IMT Mines Alès / EuroMov DHM, working on EEG-based BCI, neural signal processing, and deep learning for neuroimaging.

## Reliability Assessment
MEDIUM confidence. The lead author has genuine speech synthesis expertise with a solid publication record at BME, and the related MiSTR paper was accepted at Interspeech 2025, a reputable speech conference. However, concerns include: the BTS research line is very recent for these authors (starting 2024-2025); the baselines compared against are weak by current field standards; quantitative results are not specified in the abstract; the document is a non-peer-reviewed book chapter/preprint; and the language is somewhat promotional. The institutional affiliations (BME, IMT Mines Alès) are legitimate but not top-tier BCI research centers compared to groups at UCSF, Stanford, or Meta that lead this field.

## Main Goal
The authors aim to build a novel pipeline for extracting prosodic features from iEEG signals and use these with a custom transformer encoder architecture to generate more natural-sounding and intelligible speech from brain activity, outperforming traditional baselines like Griffin-Lim and CNN-based reconstruction.

## Key Findings
- Finding 1: The proposed transformer-based architecture integrating prosodic features achieves superior performance over Griffin-Lim and CNN-based speech reconstruction baselines across both quantitative metrics and perceptual evaluations.
- Finding 2: A novel pipeline for extracting key prosodic features (intonation, pitch, rhythm) directly from complex iEEG brain signals is introduced and shown to enhance speech reconstruction quality.
- Finding 3: The integration of prosodic features into the transformer encoder significantly improves both intelligibility and expressiveness of reconstructed speech compared to models that do not utilize prosody information.

## Methodology
The research uses intracranial EEG (iEEG) data with a multi-stage pipeline: (1) prosodic feature extraction from iEEG signals including intonation, pitch, and rhythm; (2) a novel transformer encoder architecture that integrates these prosodic features for mapping neural signals to speech representations (likely mel spectrograms); (3) speech waveform reconstruction from predicted spectrograms. Baselines include traditional Griffin-Lim algorithm and CNN-based reconstruction approaches. Evaluation uses both quantitative metrics (likely Pearson correlation, STOI, MCD) and perceptual/subjective metrics. The approach is described as a book chapter, suggesting it may present extended material from the authors' MiSTR framework (Interspeech 2025), which achieved a Pearson correlation of 0.91 on a public iEEG dataset.

## What's Novel
The primary novelty is the explicit integration of prosody-aware feature engineering into the brain-to-speech pipeline, specifically extracting prosodic features (pitch, intonation, rhythm) directly from iEEG signals and feeding these into a custom transformer encoder. Most prior BTS work focuses on spectral reconstruction without explicit prosody modeling. The chapter format also provides a broader tutorial-style overview of the field compared to a conference paper.

## Limitations & Open Questions
The abstract does not specify dataset size, number of subjects, or the specific public iEEG dataset used, making it difficult to assess generalizability. Brain-to-speech research is inherently limited by small datasets (typically minutes of data per subject) and subject-specific electrode placements. The baselines (Griffin-Lim, CNN) are relatively weak — more competitive neural baselines from recent literature (e.g., diffusion models, wav2vec-based approaches) are not mentioned. The chapter discusses future directions (diffusion models, real-time inference) rather than implementing them, suggesting current limitations in these areas. No mention of cross-subject generalization or clinical deployment testing.

## Implications
If validated on larger datasets, this prosody-aware approach to brain-to-speech synthesis could meaningfully advance neuroprosthetic communication devices for patients with severe speech impairments (ALS, locked-in syndrome). The explicit modeling of prosody addresses a key gap — most BCI-driven speech systems produce flat, unintelligible output. The work connects established speech synthesis expertise (vocoders, TTS) with BCI research, potentially accelerating progress in both fields.

## Critical Assessment
The paper appears to be an extended book chapter version of the authors' MiSTR framework accepted at Interspeech 2025, which reported a Pearson correlation of 0.91 and STOI of 0.73. While the results are promising, several concerns limit confidence: (1) the baselines are relatively weak (Griffin-Lim, basic CNNs) rather than state-of-the-art neural decoders from groups like Meta, Stanford, or UCSF; (2) the abstract is heavy on marketing language ('novel', 'paving the way') without specific quantitative claims; (3) as a book chapter/preprint, it has not undergone rigorous peer review beyond the related Interspeech publication; (4) the BTS field generally works with very small per-subject datasets, and generalization claims should be treated cautiously; (5) the connection between co-authors Tchechmedjiev/Xu (NLP/BCI at IMT Mines Alès) and Al-Radhi/Németh (speech synthesis at BME Budapest) suggests a cross-institutional collaboration, but the division of contributions is unclear. The authors have genuine expertise in speech synthesis and vocoding, though their BCI work is relatively recent (2024-2025).

## Key Terms
- **iEEG (intracranial EEG):** Electroencephalography recorded from electrodes placed directly on or within the brain tissue, providing much higher spatial resolution and signal quality than scalp EEG.
- **Brain-to-Speech (BTS):** The process of decoding neural signals from brain activity and synthesizing corresponding speech audio, typically using deep learning pipelines.
- **Prosody:** The suprasegmental features of speech including intonation (pitch patterns), rhythm, stress, and tempo that convey meaning beyond individual phonemes.
- **Griffin-Lim algorithm:** An iterative signal processing algorithm for reconstructing a time-domain audio waveform from a magnitude spectrogram by estimating the phase, without using a neural vocoder.
- **Mel spectrogram:** A time-frequency representation of audio where frequencies are mapped to the mel scale (approximating human pitch perception), commonly used as an intermediate target in speech synthesis.
- **Transformer encoder:** A neural network architecture using self-attention mechanisms to capture long-range dependencies in sequential data, here adapted to map iEEG features to speech representations.

## Related Papers
### [MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction](https://arxiv.org/abs/2508.03166) (2025) — *Essential*
The conference paper version by the same lead authors (Al-Radhi, Németh) accepted at Interspeech 2025. Introduces wavelet-based iEEG feature extraction, a transformer-based prosody-aware spectrogram predictor, and a neural phase vocoder, achieving 0.91 Pearson correlation on a public iEEG dataset.
*Why relevant: Directly related companion publication by the same first author — likely shares significant methodology and results with the book chapter under review.*

### [Speech synthesis from neural decoding of spoken sentences](https://www.nature.com/articles/s41586-019-1119-1) (2019) — *Essential*
Anumanchipalli, Chartier, and Chang's seminal Nature paper demonstrating that spoken sentences can be decoded from ECoG recordings via a two-stage approach mapping neural activity to articulatory movements and then to speech acoustics.
*Why relevant: Foundational work in neural speech synthesis that established the modern paradigm of mapping brain signals through intermediate representations to speech. The current paper builds on this lineage of brain-to-speech decoding research.*

### [Real-time synthesis of imagined speech processes from minimally invasive recordings of neural activity](https://www.nature.com/articles/s42003-021-02578-0) (2021) — *Essential*
Angrick et al. demonstrated real-time synthesis of audible speech from sEEG depth electrodes during imagined and whispered speech conditions, using linear decoding models and Griffin-Lim reconstruction — one of the baselines the current paper aims to surpass.
*Why relevant: Uses the same sEEG/iEEG recording modality and Griffin-Lim baseline that the current paper claims to outperform. Represents the most directly comparable prior work using depth electrodes for speech synthesis.*

### [A neural speech decoding framework leveraging deep learning and speech synthesis](https://www.nature.com/articles/s42256-024-00824-8) (2024) — *Recommended*
Chen, Wang et al. present a deep learning framework for neural speech decoding using ECoG with a differentiable speech synthesizer, validated across a cohort of 48 participants — representing a more rigorous and larger-scale competing approach.
*Why relevant: A competing state-of-the-art approach published in Nature Machine Intelligence that provides a stronger baseline comparison. Its larger cohort (48 participants) contrasts with the typically small datasets used in iEEG studies.*
