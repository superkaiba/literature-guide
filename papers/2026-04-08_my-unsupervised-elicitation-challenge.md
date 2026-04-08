---
title: "My unsupervised elicitation challenge"
authors: ['DanielFilan']
url: https://www.alignmentforum.org/posts/ASoFTyk3bzBE62dyn/my-unsupervised-elicitation-challenge
source: alignment_forum
published_date: 2026-04-08
topics: ['language model personas', 'subliminal learning', 'mechanistic interpretability']
relevance_score: 0.55
---

## Summary
This is a challenge post by Daniel Filan inviting readers to identify specific systematic mistakes that Claude Opus 4.6 makes when answering Ancient Greek grammar exercises (fill-in-the-blank exercises from a textbook). The challenge is structured so that only people without prior Greek knowledge can participate, creating a controlled unsupervised elicitation task where participants must infer model errors without domain knowledge. The implicit contribution is a practical, crowd-sourced method for detecting subtle LLM errors in specialized domains.

## Why It Matters
This is directly relevant to LLM persona and capability evaluation, particularly the challenge of eliciting and detecting subtle model failures (including sycophancy) without ground-truth expertise — a core problem in unsupervised or scalable oversight research relevant to mechanistic interpretability and alignment.

## Related Papers
### [Scalable Oversight of AI Systems via Debating](https://arxiv.org/abs/1805.00899) (2018)
Irving et al. propose a framework where two AI agents debate to help human overseers identify correct answers even in domains where the human lacks direct expertise. This is closely related to the challenge of detecting LLM errors without domain knowledge, which is the core of Filan's elicitation challenge.

### [Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models](https://arxiv.org/abs/2406.10162) (2024)
This paper investigates how LLMs exhibit sycophantic behavior and can escalate to more deceptive behaviors under certain training pressures, directly relevant to Filan's motivation of worrying that Claude was being sycophantic when grading his own Greek answers.
