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
This paper introduces novel sequence prediction algorithms grounded in stringology, achieving time/space efficiency with mistake bounds tied to stringological complexity measures—specifically the size of the smallest straight-line program generating a sequence and the number of states in a minimal automaton computing sequence symbols by position. It targets rich combinatorial sequence classes (automatic, morphic, Sturmian words) that exhibit low complexity under these measures. This is the first in a planned series advancing the 'compositional learning' programme within the learning-theoretic AI alignment agenda.

## Why It Matters
This work directly bridges agent foundations theory with practical algorithms in the compositional learning programme, a key direction in AI alignment research that seeks to understand how structured, hierarchical patterns can be efficiently learned—relevant to both alignment and compositional generalization.

## Related Papers
### [Prediction by compression] (2009)
This paper by Adrià Gascón et al. explores the connection between data compression and online sequence prediction, showing that good compressors can be converted into good predictors with bounded mistake rates. It provides a theoretical foundation linking Kolmogorov-style complexity measures to online learning, closely related to the stringological complexity measures used in Kosoy's work.

### [Grammatical compression: Compressed equivalence and other problems] (2012)
This paper by Artur Jeż and Markus Lohrey investigates straight-line programs (SLPs) as a grammar-based compression scheme and analyzes algorithmic problems on SLP-compressed strings. It establishes key complexity results for operations on SLP-represented sequences, directly underpinning the straight-line program complexity measure used in Kosoy's sequence prediction algorithms.
