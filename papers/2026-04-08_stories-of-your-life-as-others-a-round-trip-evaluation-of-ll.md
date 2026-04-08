---
title: "Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories Conditioned on Rich Psychometric Profiles"
authors: ['Ben Wigler', 'Maria Tsfasman', 'Tiffany Matej Hrkalovic']
url: http://arxiv.org/abs/2604.06071v1
source: arxiv
published_date: 2026-04-07
topics: ['language model personas']
relevance_score: 0.55
---

## Summary
This paper introduces a 'round-trip' evaluation paradigm for testing whether LLMs can robustly encode and decode personality information in extended text. The authors condition 10 different LLMs on real psychometric profiles from 290 human participants to generate first-person life story narratives, then use 3 independent LLM scorers to recover the original personality scores from those narratives alone. Key findings show personality recovery at a mean correlation of r = 0.750, reaching 85% of human test-retest reliability, with robustness across models from 6 different providers. The paper decomposes systematic biases to show that scoring models counteract alignment-induced defaults, and validates that personality conditioning produces behaviorally differentiated text: nine of ten coded narrative features correlate with the same features in participants' real conversations, and emotional reactivity patterns in narratives replicate in real conversational data. This goes substantially beyond prior work like PersonaLLM, which used only binary trait assignments and self-report questionnaires, by using continuous real human psychometric profiles and an external behavioral validation loop.

## About the Authors
Ben Wigler is co-founder of LoveMind AI, a startup focused on building AI companions with stable autobiographical memory and differentiable self-models; he appears to be an industry practitioner rather than a traditional academic researcher with no established h-index. Maria Tsfasman recently completed her PhD at TU Delft's Interactive Intelligence group (cited ~45 times on Google Scholar), where she studied long-term memory in conversational agents and multimodal group dynamics, and has now joined LoveMind AI to apply her research to LLMs. Tiffany Matej Hrkalovic is a postdoctoral researcher at the Jheronimus Academy of Data Science / Tilburg University (cited ~29 times on ResearchGate), specializing in social signal processing, cooperation, partner selection, and collaborative behavior in human interactions, with publications at ICMI, PLOS ONE, and IUI.

## Reliability Assessment
MEDIUM confidence. The methodology is creative and well-designed—using real human psychometric data, testing across 10 generators and 3 scorers from 6 providers, and validating against real conversational behavior—which substantially exceeds prior work's rigor. However, the paper appears to be an arXiv preprint (not yet peer-reviewed), the authors are primarily from a small AI startup (LoveMind AI) rather than established research institutions, have limited citation records, and the very high recovery correlations (r = 0.750) deserve scrutiny for potential confounds such as stereotypical trait-language mappings learned during pretraining rather than genuine personality encoding.

## Why It Matters
This paper is highly relevant to language model persona research because it provides the strongest evidence to date that personality conditioning of LLMs produces psychometrically informative representations rather than superficial trait mimicry—demonstrated through real human data, multi-model robustness, and behavioral validation against actual conversations. The round-trip methodology (encode personality → generate text → recover personality) establishes a rigorous framework for evaluating persona fidelity that could become standard, and the finding that emotional variability patterns in generated narratives replicate in real human behavior has significant implications for building psychologically grounded AI personas.

## Related Papers
### [PersonaLLM: Investigating the Ability of Large Language Models to Express Personality Traits](https://aclanthology.org/2024.findings-naacl.229/) (2024)
This NAACL Findings 2024 paper from MIT evaluates LLM personas conditioned on binary Big Five traits through self-report BFI scores, story writing tasks, and human perception experiments. It is the most direct predecessor to the reviewed paper, which extends the approach by using continuous real human psychometric profiles, a round-trip recovery paradigm, and behavioral validation against real conversations.

### [A psychometric framework for evaluating and shaping personality traits in large language models](https://www.nature.com/articles/s42256-025-01115-6) (2025)
Published in Nature Machine Intelligence by Serapio-García, Safdari et al. (Google DeepMind), this paper presents a comprehensive psychometric methodology for administering and validating personality tests on 18 LLMs, including shaping personality along desired dimensions. It establishes the foundational measurement framework that the reviewed paper builds upon by moving beyond questionnaire-based self-report to narrative generation and external recovery.
