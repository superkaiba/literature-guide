---
title: "My unsupervised elicitation challenge"
authors: ['DanielFilan']
url: https://www.alignmentforum.org/posts/ASoFTyk3bzBE62dyn/my-unsupervised-elicitation-challenge
source: alignment_forum
published_date: 2026-04-08
topics: ['subliminal learning', 'language model personas', 'mechanistic interpretability']
relevance_score: 0.55
---

## Summary
This is not a traditional research paper but rather a community challenge post on the AI Alignment Forum by Daniel Filan. Filan describes using Claude Opus 4.6 (likely Claude 3 Opus or a similarly named model) to help study Ancient Greek, and noticed what he believes are consistent, specific errors the model makes when completing fill-in-the-blank exercises from his Greek textbook. He poses an 'unsupervised elicitation challenge' to readers: can they prompt the model to reveal or correct these errors without being told what the errors are in advance? The post excludes anyone with prior knowledge of Ancient or Modern Greek to ensure a fair test of whether the errors can be elicited purely through clever prompting. The implicit research question concerns sycophancy, model reliability in low-resource language tasks, and whether targeted prompting can surface latent model failures. The challenge is methodologically informal but touches on real concerns about LLM behavior in niche domains.

## About the Authors
Daniel Filan is an AI safety researcher associated with CHAI (Center for Human-Compatible AI) at UC Berkeley and is known for his work on AI alignment, interpretability, and the AI X-risk podcast 'AXRP.' He is not primarily a linguist or NLP researcher, and this post reflects a personal learning experiment rather than formal research. His prior work includes theoretical alignment research and empirical work on neural network modularity.

## Reliability Assessment
LOW confidence as a research artifact — this is an informal blog/forum post, not a peer-reviewed paper, and lacks rigorous methodology, quantitative evaluation, or reproducibility details. However, Filan is a credible and technically sophisticated author in the alignment community, so the observation of model errors is likely genuine. The challenge format is intellectually interesting but the claims are anecdotal and the specific errors are deliberately withheld, making independent verification impossible without completing the challenge.

## Why It Matters
This challenge is directly relevant to the intersection of subliminal learning and mechanistic interpretability: it asks whether specific, consistent failure modes in a language model can be elicited without prior knowledge of what those failures are, which is essentially unsupervised behavioral probing. For someone studying LLM personas and sycophancy, this also illustrates how models may systematically mislead users in low-stakes educational contexts. It connects to broader questions about how to reliably audit model behavior in domains where ground truth is hard to verify.

## Related Papers
### [Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models](https://arxiv.org/abs/2406.10162) (2024)
This paper investigates how LLMs exhibit sycophantic behavior and how that can escalate to more deceptive behaviors under certain training pressures. It is directly relevant to Filan's concern that Claude might be sycophantically validating his incorrect Greek answers rather than providing honest corrections.

### [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) (2022)
This paper by Kadavath et al. (Anthropic) examines the calibration of LLMs regarding their own knowledge, finding models are often well-calibrated but can be confidently wrong. It connects to Filan's challenge of determining whether Claude's Greek errors reflect genuine knowledge gaps or miscalibrated confidence.
