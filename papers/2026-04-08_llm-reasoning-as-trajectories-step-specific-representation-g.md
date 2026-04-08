---
title: "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals"
authors: ['Lihao Sun', 'Hang Dong', 'Bo Qiao', 'Qingwei Lin', 'Dongmei Zhang', 'Saravan Rajmohan']
url: http://arxiv.org/abs/2604.05655v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability']
relevance_score: 0.55
---

## Summary
This paper analyzes large language models' chain-of-thought (CoT) reasoning by characterizing it as a structured trajectory through representation space. The authors demonstrate that mathematical reasoning proceeds through functionally ordered, step-specific subspaces that become increasingly separable with layer depth, and importantly, this geometric structure exists in base models before any reasoning-specific training. Reasoning training (e.g., RLVR-style fine-tuning) primarily accelerates convergence toward termination-related subspaces rather than creating new representational organization. A key finding is that correct and incorrect reasoning trajectories diverge systematically only at late reasoning steps, enabling mid-reasoning prediction of final answer correctness with ROC-AUC up to 0.87. Building on this, the authors introduce 'trajectory-based steering,' an inference-time intervention that corrects reasoning errors and controls output length by guiding activations toward derived 'ideal' trajectories, establishing geometric trajectory analysis as a practical tool for interpreting and controlling LLM reasoning.

## About the Authors
The authors are affiliated with Microsoft Research (Qingwei Lin, Dongmei Zhang, Saravan Rajmohan are well-known Microsoft Research figures, with Rajmohan also associated with work at UC Davis and Microsoft). Lihao Sun, Hang Dong, and Bo Qiao appear to be researchers within the Microsoft ecosystem. The group has prior work on LLM reliability, monitoring, and systems, though this paper represents a more interpretability-focused direction for some of them.

## Reliability Assessment
MEDIUM confidence. The paper is from a credible institutional group (Microsoft Research) with researchers who have established track records in LLM evaluation and systems. The methodology—probing representational geometry, ROC-AUC evaluation, and inference-time steering—is sound and specific enough to be falsifiable. However, this appears to be an arXiv preprint without confirmed peer review, and some claims (e.g., ROC-AUC of 0.87 for mid-reasoning correctness prediction) would benefit from broader benchmark validation across model families.

## Why It Matters
This paper is directly relevant to mechanistic interpretability as it reveals how reasoning processes are geometrically organized in representation space, offering a structured lens for understanding what LLMs 'do' during multi-step reasoning without relying solely on behavioral analysis. The finding that correctness signals emerge in late-stage representations—and can be used for inference-time steering—connects to broader efforts to localize and intervene on specific computations within transformers. It also contributes to understanding how training shapes (or doesn't fundamentally reorganize) internal representations.

## Related Papers
### [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting](https://arxiv.org/abs/2305.04388) (2023)
This paper investigates whether chain-of-thought explanations faithfully reflect the internal computations of LLMs, finding systematic cases where stated reasoning diverges from the actual factors driving predictions. It connects to this work by motivating the need to study internal representations rather than just output text to understand LLM reasoning.

### [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) (2023)
This paper introduces representation engineering, which characterizes high-level cognitive phenomena (honesty, emotion, reasoning) as directions in LLM activation space and enables control via linear interventions. It is closely related as both papers use representational geometry to interpret and steer LLM behavior, with the current work extending this to step-wise reasoning trajectories.
