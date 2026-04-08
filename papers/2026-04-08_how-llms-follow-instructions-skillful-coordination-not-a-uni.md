---
title: "How LLMs Follow Instructions: Skillful Coordination, Not a Universal Mechanism"
authors: ['Elisabetta Rocchetti', 'Alfio Ferrara']
url: http://arxiv.org/abs/2604.06015v1
source: arxiv
published_date: 2026-04-07
topics: ['mechanistic interpretability', 'language model personas']
relevance_score: 0.72
---

## Summary
This paper investigates whether instruction-following in large language models relies on a single universal mechanism or a collection of task-specific skills. Using diagnostic probing across nine diverse tasks in three instruction-tuned models, the authors find converging evidence against a universal mechanism: general probes trained across all tasks underperform task-specific probes, cross-task transfer is weak and clusters by skill similarity, and causal ablation reveals sparse asymmetric dependencies rather than shared representations. The paper further finds that task complexity stratifies across layers—structural constraints emerge in early layers while semantic tasks emerge in later layers—and that constraint satisfaction operates as dynamic monitoring during generation rather than pre-generation planning. The authors conclude that instruction-following is better characterized as skillful coordination of diverse linguistic capabilities, with significant implications for how we understand and improve instruction-tuned models.

## About the Authors
Elisabetta Rocchetti and Alfio Ferrara are affiliated with the University of Milan, Italy. Alfio Ferrara is a faculty member whose research spans knowledge representation, semantic technologies, and NLP. The authors are not widely recognized figures in the mechanistic interpretability community, but their work is methodologically aligned with that field.

## Reliability Assessment
MEDIUM confidence. The methodology—diagnostic probing, cross-task transfer analysis, and causal ablation—is appropriate and follows established practices in mechanistic interpretability. However, the paper appears to be an arXiv preprint without confirmed peer review, and the authors are not prominent voices in this specific subfield. The claims appear proportionate to the evidence described, and the multi-pronged approach strengthens credibility, but independent replication would be valuable.

## Why It Matters
This work is directly relevant to mechanistic interpretability research, as it uses probing and causal ablation to decompose a high-level model behavior (instruction-following) into its underlying computational substrate. For researchers studying LLM personas, the finding that instruction-following is a coordination of distinct skills—rather than a unified mechanism—suggests that persona-relevant behaviors may be implemented through different circuits depending on the type of constraint being applied.

## Related Papers
### [The Internal State of an LLM Knows When It's Lying](https://arxiv.org/abs/2304.13734) (2023)
This paper uses linear probes on LLM internal representations to detect truthfulness, demonstrating that specific model behaviors can be decoded from hidden states. It connects to the Rocchetti & Ferrara paper in its use of probing to understand how LLMs represent task-relevant information internally.

### [Towards Understanding How Attention Heads Work: A Mechanistic Interpretability Study] (2022)
This line of work on identifying task-specific attention heads and circuits in transformers provides foundational methodology for the causal ablation approach used in the paper. The finding that different heads specialize in different functions supports the 'coordination of skills' framing proposed by Rocchetti & Ferrara.
