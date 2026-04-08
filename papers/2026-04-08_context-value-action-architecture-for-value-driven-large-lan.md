---
title: "Context-Value-Action Architecture for Value-Driven Large Language Model Agents"
authors: ['TianZe Zhang', 'Sirui Sun', 'Yuhang Xie', 'Xin Zhang', 'Zhiqiang Wu', 'Guojie Song']
url: http://arxiv.org/abs/2604.05939v1
source: arxiv
published_date: 2026-04-07
document_type: preprint
topics: ['language model personas', 'AI alignment']
relevance_score: 0.35
---

# Context-Value-Action Architecture for Value-Driven Large Language Model Agents

## Overview
This is an arXiv preprint proposing the Context-Value-Action (CVA) architecture for building LLM-based agents that more faithfully simulate human behavior by grounding value-driven decision-making in Schwartz's Theory of Basic Human Values and the Stimulus-Organism-Response (S-O-R) psychological model. The paper identifies a critical problem: increasing prompt-driven reasoning in LLM agents causes value polarization rather than improved behavioral fidelity, and standard LLM-as-a-judge evaluations mask this flaw via self-referential bias.

## About the Authors
The senior author Guojie Song is a tenured Research Professor at Peking University's School of Intelligence Science and Technology, with approximately 9,000 Google Scholar citations and research focus areas including Value Modeling, Value Learning and Decision-Making, Value Alignment, and LLM/GML. His group has produced a strong series of papers on LLM values and psychometrics, including ValueBench (ACL 2024), Generative Psychometrics for Values/GPV (AAAI 2025), and the Generative Psycho-Lexical Approach (AAAI 2025). Co-authors TianZe Zhang and Yuhang Xie appear to be graduate students in Song's lab, with Xie co-authoring the GPV and ValueBench papers. The interdisciplinary team includes collaborators from Peking University's School of Psychological and Cognitive Sciences (Xin Zhang) and Department of Sociology.

## Reliability Assessment
MEDIUM-HIGH confidence. Strengths: (1) The senior author has a strong track record with 9K+ citations and multiple peer-reviewed publications at top venues (ACL, AAAI, KDD) specifically on LLM values and psychometrics. (2) The research group has deep domain expertise uniquely combining psychology, sociology, and AI. (3) The large-scale benchmark (1.1M traces) suggests substantial empirical investment. (4) The theoretical grounding in established psychological frameworks is sound. Concerns: (1) This is an unreviewed preprint; (2) no public discussion, reviews, or independent replications found; (3) the counter-intuitive claims about reasoning intensity harming fidelity need careful peer scrutiny; (4) the exact paper could not be found on arxiv suggesting it may be very recent or not yet posted; (5) some claims about LLM-as-a-judge bias, while plausible, may be presented more strongly than the evidence supports without seeing the full experimental details.

## Main Goal
The authors aim to build LLM agents that exhibit more realistic, diverse, and human-like behavior by decoupling action generation from cognitive reasoning through a novel 'Value Verifier' trained on authentic human behavioral data, ultimately producing agents whose value activations match empirical human population distributions rather than collapsing into polarized stereotypes.

## Key Findings
- Finding 1: Increasing prompt-driven reasoning intensity (e.g., chain-of-thought, persona prompts) does not improve behavioral fidelity but instead exacerbates value polarization — collapsing population-level diversity into extreme, stereotypical responses. This counter-intuitive result is only revealed when evaluating against empirical human ground truth rather than LLM-as-a-judge metrics.
- Finding 2: Standard 'LLM-as-a-judge' evaluation methods exhibit self-referential bias that masks the polarization problem, giving artificially high scores to outputs that are actually less human-like. This calls into question many prior evaluations of LLM persona fidelity.
- Finding 3: The CVA architecture, using a Value Verifier trained on real human interaction data (CVABench, comprising 1.1 million real-world interaction traces), significantly outperforms prompt-based baselines in behavioral fidelity and population diversity while maintaining interpretability through explicit value activation modeling.

## Methodology
The research uses a three-component architecture inspired by the S-O-R psychological model: (1) Context module processes environmental stimuli, (2) Value module activates relevant human values via a trained Value Verifier (rather than LLM self-reasoning), and (3) Action module generates behavior conditioned on activated values. The Value Verifier is trained on authentic human behavioral data rather than relying on LLM self-verification. Evaluation is conducted on CVABench, a newly constructed benchmark comprising over 1.1 million real-world interaction traces, which provides empirical ground truth for behavioral fidelity assessment. The theoretical grounding combines Schwartz's Theory of Basic Human Values (10 universal value types in a circular motivational continuum) with the Stimulus-Organism-Response model from environmental psychology. Baselines likely include prompt-based persona methods, chain-of-thought reasoning, and standard LLM agent architectures.

## What's Novel
The key novelty is threefold: (1) identifying and empirically demonstrating that more reasoning leads to worse behavioral fidelity (value polarization phenomenon), (2) critiquing LLM-as-a-judge evaluation by showing its self-referential bias masks this problem, and (3) proposing a principled decoupling of value reasoning from action generation via a separately trained Value Verifier grounded in real human data. The CVABench dataset of 1.1M real interaction traces is itself a significant contribution. The theoretical grounding in established psychological frameworks (S-O-R model and Schwartz values) distinguishes this from purely engineering-driven agent architectures.

## Limitations & Open Questions
Without access to the full paper, specific acknowledged limitations are uncertain, but likely concerns include: the generalizability of CVABench's interaction traces to diverse cultural and demographic populations; the assumption that Schwartz's 10 value framework is sufficient to capture the full spectrum of human behavioral motivations; potential distribution shift between training data and deployment contexts; scalability of the Value Verifier approach to open-ended domains not covered by the benchmark; and whether the improvement in population-level diversity comes at the cost of individual-level coherence or consistency.

## Implications
This work has significant implications for AI alignment and social simulation research. It challenges the widespread practice of using LLM-as-a-judge evaluation in agent research, suggesting many reported improvements may be illusory. For researchers building LLM personas for social science simulation, computational social science, or human behavior modeling, it provides both a cautionary finding (more reasoning ≠ more fidelity) and a constructive solution (externally trained value verifiers). The CVABench dataset could become a valuable community resource. The approach also has implications for value alignment research, suggesting that explicit value modeling grounded in psychological theory may be more effective than implicit prompt-based methods.

## Critical Assessment
The paper makes bold claims that are well-aligned with growing concerns in the field about LLM-as-a-judge reliability and value polarization in prompted agents. The theoretical grounding in established psychology (Schwartz values, S-O-R model) adds credibility and is consistent with the research group's deep expertise in LLM psychometrics. The scale of CVABench (1.1M traces) is impressive and suggests rigorous empirical grounding. However, several aspects warrant scrutiny: (1) the counter-intuitive 'more reasoning = worse fidelity' claim needs careful examination of what specific reasoning methods were tested and how fidelity was measured; (2) the paper's critique of LLM-as-a-judge may overstate the problem if the self-referential bias is small relative to the signal; (3) the Value Verifier's training on 'authentic human data' needs transparency about data provenance, demographics, and potential biases; (4) this is a preprint without peer review, though it comes from a group with strong publication records at ACL, AAAI, and KDD. The work fits coherently into the group's broader research program on LLM psychometrics and value measurement.

## Key Terms
- **Context-Value-Action (CVA) Architecture:** A proposed agent architecture that decouples context processing, value activation, and action generation into separate modules, inspired by the Stimulus-Organism-Response psychological model, to produce more human-like LLM agent behavior.
- **Value Verifier:** A separately trained model component that explicitly models dynamic value activation from authentic human behavioral data, replacing LLM self-reasoning about values to avoid polarization.
- **Value Polarization:** The phenomenon where increasing prompt-driven reasoning in LLM agents causes responses to collapse toward extreme value positions, reducing population-level behavioral diversity rather than improving fidelity.
- **Schwartz's Theory of Basic Human Values:** A well-established psychological theory identifying 10 universal value types (e.g., self-direction, benevolence, power, security) arranged in a circular motivational continuum where adjacent values are compatible and opposing values conflict.
- **Stimulus-Organism-Response (S-O-R) Model:** A psychological framework from environmental psychology positing that external stimuli affect an organism's internal cognitive/affective states, which then mediate behavioral responses — as opposed to direct stimulus-response models.
- **CVABench:** A benchmark dataset comprising over 1.1 million real-world interaction traces used to evaluate behavioral fidelity of LLM agents against empirical human ground truth.
- **LLM-as-a-Judge:** An evaluation methodology where LLMs are used to automatically assess the quality of outputs from other LLMs or AI systems, which has been shown to exhibit systematic biases including self-preference and verbosity bias.
- **Self-Referential Bias:** In the context of LLM evaluation, the tendency for LLM judges to systematically prefer outputs that match their own generation patterns (lower perplexity), potentially masking genuine quality differences.

## Related Papers
### [Measuring Human and AI Values Based on Generative Psychometrics with Large Language Models](https://arxiv.org/abs/2409.12106) (2025) — *Essential*
By the same research group (Ye, Xie, Ren, Fang, Zhang, Song), this AAAI 2025 paper introduces Generative Psychometrics for Values (GPV), an LLM-based paradigm for measuring values from unstructured text. It provides the foundational value measurement methodology that the CVA paper likely builds upon for its Value Verifier component.
*Why relevant: Direct predecessor from the same lab providing the theoretical and methodological foundations for value measurement that CVA extends into an agent architecture.*

### [ValueBench: Towards Comprehensively Evaluating Value Orientations and Understanding of Large Language Models](https://aclanthology.org/2024.acl-long.111/) (2024) — *Essential*
Also from the same group (Ren, Ye, Fang, Zhang, Song), this ACL 2024 paper introduces the first comprehensive psychometric benchmark for evaluating LLM value orientations across 44 inventories and 453 value dimensions. It establishes the evaluation infrastructure the CVA work builds upon.
*Why relevant: Foundational evaluation benchmark from the same group; CVABench likely extends or complements this work with real-world interaction data rather than psychometric questionnaires.*

### [Value FULCRA: Mapping Large Language Models to the Multidimensional Spectrum of Basic Human Value](https://aclanthology.org/2024.naacl-long.486/) (2024) — *Recommended*
This NAACL 2024 paper by Yao et al. introduces a multidimensional value space grounded in Schwartz's Theory for LLM alignment, constructing a 20K-sample dataset mapping LLM outputs to value vectors. It demonstrates that basic values effectively distinguish safe from unsafe LLM behaviors.
*Why relevant: A competing/complementary approach to grounding LLM alignment in Schwartz values, providing important context for how Schwartz theory has been operationalized for LLMs.*

### [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819) (2024) — *Recommended*
This paper introduces a quantitative metric for measuring self-preference bias in LLM-as-a-judge evaluations, demonstrating that GPT-4 exhibits significant self-preference bias driven by perplexity-based familiarity. It provides key empirical support for CVA's critique of LLM-as-a-judge evaluation.
*Why relevant: Directly supports the CVA paper's claim about self-referential bias in LLM-as-a-judge evaluations, providing independent evidence for one of CVA's core motivating observations.*
