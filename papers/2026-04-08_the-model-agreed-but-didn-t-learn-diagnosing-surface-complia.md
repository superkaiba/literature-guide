---
title: "The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models"
authors: ['Xiaojie Gu', 'Ziying Huang', 'Weicong Hong', 'Jian Xie', 'Renze Lou', 'Kai Zhang']
url: http://arxiv.org/abs/2604.05995v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability', 'AI safety']
relevance_score: 0.55
---

## Summary
This paper introduces a diagnostic framework to evaluate whether knowledge editing in LLMs produces genuine memory modification or merely surface-level output mimicry. Using discriminative self-assessment under in-context learning settings, the authors reveal a phenomenon called 'Surface Compliance,' where edited models achieve high benchmark scores without truly overwriting internal beliefs. They also show that repeated edits accumulate representational residues, causing cognitive instability and reducing reversibility of memory states.

## Why It Matters
For mechanistic interpretability and AI safety researchers, this work exposes a critical gap between behavioral benchmarks and actual internal model states, suggesting that current knowledge editing evaluations may give false assurances about model reliability and controllability—a core concern for trustworthy AI deployment.

## Related Papers
### [Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172) (2023)
This paper provides a comprehensive survey of knowledge editing methods for LLMs, categorizing approaches such as locate-and-edit, meta-learning, and memory-based methods. It also outlines evaluation criteria including efficacy, generalization, and locality, which are precisely the benchmarks this paper critiques as insufficient for verifying genuine memory modification.

### [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) (2022)
This foundational paper introduces ROME, a method for locating factual knowledge in MLP layers of GPT models using causal tracing and performing surgical weight edits. It is a key prior work that the Surface Compliance findings directly challenge, as high editing success rates on standard prompts may not reflect true parametric belief change.
