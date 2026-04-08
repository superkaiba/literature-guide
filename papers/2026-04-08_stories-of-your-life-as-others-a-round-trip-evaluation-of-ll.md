---
title: "Stories of Your Life as Others: A Round-Trip Evaluation of LLM-Generated Life Stories Conditioned on Rich Psychometric Profiles"
authors: ['Ben Wigler', 'Maria Tsfasman', 'Tiffany Matej Hrkalovic']
url: http://arxiv.org/abs/2604.06071v1
source: arxiv
published_date: 2026-04-07
topics: ['language model personas', 'AI alignment']
relevance_score: 0.45
---

## Summary
This paper introduces a 'round-trip' evaluation framework for assessing how robustly LLMs encode personality into generated text. The authors condition 10 different LLMs on real psychometric profiles (Big Five personality scores) from 290 human participants to generate first-person life story narratives, then use 3 independent LLMs to recover the original personality scores from those narratives alone. The key finding is that personality scores can be recovered at approximately 85% of human test-retest reliability (mean r=0.750), and this result holds across 6 different model providers. A notable secondary finding is that scoring models must actively counteract alignment-induced defaults (likely a tendency toward agreeable, positive outputs) to achieve accurate recovery, and content analysis confirms that conditioning produces behaviorally differentiated narratives where nine of ten coded features correlate significantly with participant data.

## About the Authors
Ben Wigler, Maria Tsfasman, and Tiffany Matej Hrkalovic are not widely recognized figures in the top-tier ML publication circuit based on available knowledge. Their affiliations are not stated in the provided metadata, and this appears to be an arXiv preprint. The combination of psychometric methodology with LLM evaluation suggests backgrounds spanning computational psychology or psycholinguistics alongside NLP.

## Reliability Assessment
MEDIUM confidence. The methodology is notably more rigorous than typical LLM personality studies—using real human psychometric data, multiple generators and scorers, and a round-trip design rather than self-report. The sample size (290 participants, 10 LLMs, 3 scorers) is reasonable. However, the paper is an arXiv preprint without confirmed peer review, the authors are not widely recognized, and institutional affiliations are unknown, making independent verification of methodology harder. The claims appear proportionate to the described evidence, which is a positive signal.

## Why It Matters
This work is directly relevant to AI alignment and persona research because it quantifies how deeply personality information is encoded versus superficially mimicked by LLMs, and surfaces the alignment tax—models have systematic biases that distort personality expression. For researchers studying AI personas, the round-trip methodology offers a more rigorous evaluation paradigm than questionnaire self-report, and the finding that alignment-induced defaults must be 'counteracted' raises important questions about how safety fine-tuning shapes model personality representations.

## Related Papers
### [Personality Traits in Large Language Models](https://arxiv.org/abs/2307.00184) (2023)
This paper investigates how personality traits manifest in LLMs and proposes methods to condition models on Big Five personality profiles. It connects directly as a predecessor work that this paper critiques for relying on questionnaire self-report rather than behavioral text generation as evaluation.

### [Narrative Identity and Personality: A Review of the Research] (2009)
A foundational review by Dan McAdams examining how personal narratives encode stable personality traits, providing the psycholinguistic theoretical grounding for why life story generation is a valid medium for personality expression and recovery.
