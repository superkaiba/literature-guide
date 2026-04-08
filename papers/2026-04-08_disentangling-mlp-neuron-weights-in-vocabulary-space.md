---
title: "Disentangling MLP Neuron Weights in Vocabulary Space"
authors: ['Asaf Avrahamy', 'Yoav Gur-Arieh', 'Mor Geva']
url: http://arxiv.org/abs/2604.06005v1
source: arxiv
published_date: 2026-04-07
document_type: preprint
topics: ['mechanistic interpretability', 'superposition features']
relevance_score: 0.92
---

# Disentangling MLP Neuron Weights in Vocabulary Space

## Overview
This is an arXiv preprint introducing ROTATE, a data-free method for disentangling MLP neuron weights in transformer language models by optimizing rotations to maximize vocabulary-space kurtosis. The paper addresses the fundamental challenge of interpreting polysemantic MLP neurons without requiring forward passes over data, directly operating in weight space to recover sparse, interpretable 'vocabulary channels.'

## About the Authors
Mor Geva is an Assistant Professor at Tel Aviv University and Research Scientist at Google Research, with an h-index of 22 on Semantic Scholar (4,887 citations) and ~9,889 citations on Google Scholar. She is a leading researcher in mechanistic interpretability, known for foundational papers including 'Transformer Feed-Forward Layers Are Key-Value Memories' (EMNLP 2021, 1,093 citations) and 'Analyzing Transformers in Embedding Space' (ACL 2023). She received an EMNLP Best Paper Award (2024) and MIT Rising Star in EECS (2021). Yoav Gur-Arieh is an MS/PhD student at Tel Aviv University in Geva's lab, specializing in LLM interpretability and knowledge mechanisms, with prior work on output-centric feature descriptions and entity binding mechanisms. Asaf Avrahamy appears to be a newer researcher affiliated with Tel Aviv University, likely a student in Geva's group.

## Reliability Assessment
HIGH confidence. The senior author (Mor Geva) has an exceptional track record in exactly this subfield—MLP interpretability and vocabulary-space analysis of transformers—with highly cited foundational work. The methodology is well-motivated by established prior work from the same group. The paper includes causal ablation experiments and head-to-head comparisons rather than relying solely on qualitative examples. The institutional affiliation (Tel Aviv University + Google Research) is strong. The main caveats are that it is a preprint (not yet peer-reviewed) and the evaluation is on only two models, but neither constitutes a red flag given the quality of the research group.

## Main Goal
The authors aim to show that MLP neurons in large language models can be decomposed into interpretable sub-components ('vocabulary channels') purely from their weights—without any data or forward passes—by optimizing rotations that maximize the kurtosis of neuron weight projections onto the vocabulary space, thereby providing a scalable alternative to activation-based interpretability methods like sparse autoencoders.

## Key Findings
- Finding 1: Neurons encoding coherent, monosemantic concepts exhibit high kurtosis when projected onto the model's vocabulary via the unembedding matrix, and this statistical signature can be exploited as an optimization objective to recover sparse, interpretable directions (vocabulary channels) without any data.
- Finding 2: Ablating individual vocabulary channels selectively disables corresponding input activations or the promotion of specific concepts, demonstrating that the recovered channels are causally faithful to the neuron's actual behavior in the network.
- Finding 3: Aggregating channel-level descriptions into comprehensive neuron descriptions outperforms optimized activation-based description baselines by 2-3x in head-to-head human evaluation comparisons, validated on both Llama-3.1-8B-Instruct and Gemma-2-2B-it models.

## Methodology
The method operates entirely in weight space: for each MLP neuron, its output weight vector is projected into vocabulary space via the unembedding matrix. The authors observe that monosemantic directions produce high-kurtosis distributions over the vocabulary. ROTATE optimizes rotation matrices applied to neuron weights to maximize vocabulary-space kurtosis, effectively decomposing each polysemantic neuron into multiple sparse vocabulary channels. Experiments are conducted on Llama-3.1-8B-Instruct and Gemma-2-2B-it. Evaluation includes: (1) ablation studies showing that individual channels causally control specific input activations and output concepts, (2) head-to-head comparisons of neuron descriptions generated from channel-level aggregation versus activation-based baselines, using human evaluators and/or LLM judges. The method requires no forward passes and no training data.

## What's Novel
The key novelty is the completely data-free, weight-only approach to neuron disentanglement, which contrasts sharply with sparse autoencoders (SAEs) that require large-scale activation collection over data. The use of kurtosis in vocabulary space as the optimization signal for rotation is original—connecting a statistical property (peakedness) to monosemanticity. The method also provides a finer-grained decomposition than standard neuron-level analysis by breaking each neuron into multiple vocabulary channels, offering a middle ground between individual neurons and SAE features.

## Limitations & Open Questions
As a preprint, it has not undergone formal peer review. The approach assumes that projecting neuron weights into vocabulary space via the unembedding matrix is a valid lens for interpretation, which may not capture all aspects of neuron function (especially in earlier layers where vocabulary alignment may be weaker). The method focuses exclusively on MLP neurons and does not address attention heads. Kurtosis maximization may not always correspond to meaningful monosemantic concepts—high kurtosis could arise from statistical artifacts. The evaluation on only two models (Llama-3.1-8B-Instruct and Gemma-2-2B-it) limits generalizability claims. The 2-3x improvement in descriptions is measured via head-to-head comparisons, and the exact evaluation methodology (number of annotators, inter-annotator agreement, specific baselines) would need scrutiny in the full paper.

## Implications
If validated, ROTATE could provide a highly scalable building block for mechanistic interpretability that bypasses the expensive data collection and training required by SAEs. The data-free nature means it could be applied to any model with accessible weights, enabling rapid auditing and interpretation. The vocabulary channel concept could become a standard unit of analysis for MLP layers, complementing SAE features for residual streams. This work also advances the broader agenda of weight-space interpretability methods, which abstract away from input-dependent analysis.

## Critical Assessment
The paper comes from a highly credible research group. Mor Geva is a leading figure in MLP interpretability, having authored foundational papers on FFN layers as key-value memories and analyzing transformers in embedding space. The core insight—that kurtosis in vocabulary space signals monosemanticity—is elegant and well-motivated. The causal validation via ablation is a strong positive. However, several questions remain: (1) How well does this work in early vs. late layers, given that vocabulary alignment is known to be weaker in early layers? (2) How does the number of channels per neuron compare to SAE expansion factors? (3) The 2-3x improvement over activation baselines is impressive but needs careful scrutiny of the baselines used. (4) The connection between rotation optimization and the model's actual computation could be explored more deeply. The two-model evaluation is reasonable for a methods paper but leaves open questions about generalization. The data-free claim is a major practical advantage but also means the method cannot capture input-context-dependent behaviors.

## Key Terms
- **Vocabulary channel:** A sparse, interpretable direction recovered by ROTATE that represents a coherent concept within a single MLP neuron when projected into vocabulary space, enabling a neuron to be decomposed into multiple meaningful sub-components.
- **Kurtosis (in vocabulary space):** A fourth-order statistical moment measuring the 'peakedness' or tail-heaviness of a distribution. Here, high kurtosis of a neuron's weight projection onto vocabulary tokens indicates a sparse, focused distribution characteristic of monosemantic concepts.
- **Superposition:** A phenomenon where neural networks represent more features than they have neurons by encoding features as non-orthogonal directions in activation space, causing individual neurons to be polysemantic (responding to multiple unrelated concepts).
- **Monosemantic:** A neuron or direction that encodes a single coherent concept, as opposed to polysemantic neurons which activate for multiple unrelated concepts.
- **Unembedding matrix:** The final linear layer (W_U) in a transformer that maps hidden states to logits over the vocabulary. Used here to project neuron weight vectors into interpretable vocabulary space.
- **Data-free interpretability:** An approach to interpreting model internals that operates directly on model parameters/weights without requiring any forward passes over input data, making it highly scalable.

## Related Papers
### [Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913) (2021) — *Essential*
Mor Geva et al. show that FFN layers operate as key-value memories where keys detect textual patterns and values induce vocabulary distributions. This foundational paper establishes the vocabulary-space interpretation framework that ROTATE directly builds upon.
*Why relevant: Direct foundational work by the senior author. ROTATE extends the idea that FFN value vectors are interpretable in vocabulary space, adding the insight that rotation optimization can disentangle polysemantic neurons.*

### [Analyzing Transformers in Embedding Space](https://arxiv.org/abs/2209.02535) (2022) — *Essential*
Guy Dar, Mor Geva et al. present a theoretical framework for interpreting all transformer parameters by projecting them into embedding/vocabulary space, enabling input-independent (zero-pass) interpretation. Published at ACL 2023.
*Why relevant: Establishes the zero-pass, weight-space interpretability paradigm that ROTATE operates within. Both papers share the core idea of interpreting parameters in vocabulary space without forward passes.*

### [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://arxiv.org/abs/2309.08600) (2023) — *Essential*
Cunningham et al. use sparse autoencoders to decompose internal activations into interpretable, monosemantic features, addressing polysemanticity caused by superposition. The primary competing/complementary approach to the problem ROTATE addresses.
*Why relevant: The main competing methodology. SAEs require large-scale data and training; ROTATE is positioned as a data-free alternative that works in weight space rather than activation space.*

### [Decomposing MLP Activations into Interpretable Features via Semi-Nonnegative Matrix Factorization](https://arxiv.org/abs/2506.10920) (2025) — *Recommended*
Or Shafran and Mor Geva propose using SNMF to decompose MLP activations into sparse neuron combinations that outperform SAEs on causal steering while being tied to model mechanisms. Tested on Llama-3.1 and Gemma-2.
*Why relevant: A closely related concurrent work from the same lab that also decomposes MLP representations into interpretable features, but uses activation-based matrix factorization rather than weight-space rotation. Provides an important comparison point.*
