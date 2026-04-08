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
This paper investigates a critical flaw in how knowledge editing methods for LLMs are evaluated. The authors introduce a diagnostic framework using discriminative self-assessment under in-context learning (ICL) settings to probe whether knowledge edits represent genuine memory modification or merely surface-level output mimicry. Their central finding is a phenomenon they term 'Surface Compliance,' where edited models achieve high benchmark scores by producing target outputs without actually overwriting internal parametric beliefs—essentially gaming evaluation metrics without true knowledge integration. Additionally, they find that repeated/recursive edits accumulate 'representational residues' that cause cognitive instability and reduce the model's ability to reverse prior edits. The work challenges the validity of current knowledge editing benchmarks and argues that robust, verifiable memory modification is essential for trustworthy LLM deployment.

## About the Authors
The authors—Xiaojie Gu, Ziying Huang, Weicong Hong, Jian Xie, Renze Lou, and Kai Zhang—do not appear to be widely recognized senior figures in the field based on available knowledge. They are likely affiliated with academic institutions in China or Chinese-American research groups, given naming conventions and co-authorship patterns, but specific affiliations are not confirmed from the abstract alone. Their research focus appears to center on LLM reliability, knowledge editing, and evaluation methodology.

## Reliability Assessment
MEDIUM confidence. The paper addresses a genuine and important problem, and the core intuition (that benchmark performance can diverge from internal belief modification) is well-motivated and consistent with known issues in the field. However, the authors are not widely recognized, the paper is a preprint from arXiv without confirmed peer review, and the abstract does not detail experimental scale, which models were tested, or quantitative results—making it difficult to fully assess methodological rigor. The claims are plausible but should be treated cautiously pending peer review.

## Why It Matters
This paper is directly relevant to mechanistic interpretability and AI safety because it exposes a fundamental gap between behavioral evaluation and internal model state—a core concern in both fields. The finding that models can 'comply' on benchmarks without genuinely updating beliefs is a concrete safety risk, as it means alignment or factual correction techniques may appear to work while leaving underlying representations unchanged. It underscores the need for interpretability tools that can verify internal belief states, not just surface outputs.

## Related Papers
### [Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172) (2023)
This survey paper systematically reviews the landscape of knowledge editing methods for LLMs, covering approaches like ROME, MEMIT, and fine-tuning-based editors. It is directly connected as the foundational framing for the editing paradigm that the current paper critiques.

### [Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) (2022)
This influential paper (ROME) introduced causal tracing to locate factual memory in transformer MLPs and proposed rank-one model editing to modify it. It is a primary target of scrutiny for the 'Surface Compliance' phenomenon described in the current paper, as ROME is one of the most benchmarked editing methods.
