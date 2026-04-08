---
title: "[Paper] Stringological sequence prediction I"
authors: ['Vanessa Kosoy']
url: https://www.alignmentforum.org/posts/EEvHYKLsq92LmQ78a/paper-stringological-sequence-prediction-i-1
source: alignment_forum
published_date: 2026-04-07
topics: ['AI alignment', 'compositional learning']
relevance_score: 0.35
---

## Summary
This paper introduces novel sequence prediction algorithms grounded in stringology (the mathematical study of strings and their properties). The algorithms are both time and space efficient, and their performance is characterized by mistake bounds tied to two specific stringological complexity measures: (1) the size of the smallest straight-line program (SLP) that generates the sequence, and (2) the number of states in the minimal automaton that computes any symbol given its position in base-k as input. These measures naturally capture the complexity of well-studied combinatorial word classes such as automatic sequences, morphic sequences, and Sturmian words. The work is positioned as the first in a series of papers forming a major advance in the 'compositional learning' programme within the learning-theoretic AI alignment agenda, aiming to bridge abstract agent foundations theory with practical, implementable algorithms.

## About the Authors
Vanessa Kosoy is an independent AI alignment researcher associated with the Alignment Forum and the Machine Intelligence Research Institute (MIRI) community, known for developing the 'learning-theoretic agenda' for AI alignment. Her prior work includes foundational research on infra-Bayesianism, logical induction-adjacent frameworks, and formal models of agency and learning. She is not affiliated with a major academic institution in the traditional sense but is a recognized figure in the theoretical AI safety research community.

## Reliability Assessment
MEDIUM confidence. Vanessa Kosoy has a solid track record in rigorous theoretical AI alignment research, and the paper's claims appear technically precise and proportionate. However, it is posted on the Alignment Forum rather than a peer-reviewed venue, so it has not undergone formal peer review. The mathematical framing (mistake bounds, stringological complexity) is standard and well-founded, which reduces risk of unfounded claims, but independent verification of the proofs would strengthen confidence.

## Why It Matters
This paper is directly relevant to compositional learning research, as it develops principled, theoretically grounded algorithms that can identify and exploit compositional structure in sequential data. For AI alignment, it advances the learning-theoretic agenda by providing concrete, efficient algorithms with formal guarantees, helping close the gap between foundational theory and practical alignment-relevant methods.

## Related Papers
### [Text Compression via Large Language Models] (2023)
This work explores the connection between sequence prediction and compression, showing that language model perplexity directly corresponds to compression performance. It connects to the SLP-based complexity measures in Kosoy's paper, as both frame sequence predictability in terms of compressibility.

### [Prediction by compression](https://dl.acm.org/doi/10.1145/1374376.1374451) (2008)
This classic paper by Charikar et al. establishes formal links between data compression (including straight-line programs) and online prediction, providing mistake bounds analogous to those Kosoy develops. It is a direct theoretical predecessor to the stringological prediction approach.
