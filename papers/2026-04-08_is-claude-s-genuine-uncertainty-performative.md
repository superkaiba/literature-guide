---
title: "Is Claude's genuine uncertainty performative?"
authors: ['jordinne']
url: https://www.lesswrong.com/posts/M6CYdfbFajiZxJFfm/is-claude-s-genuine-uncertainty-performative
source: lesswrong
published_date: 2026-04-08
document_type: blog post
topics: ['AI alignment', 'language model personas']
relevance_score: 0.45
---

# Is Claude's genuine uncertainty performative?

## Overview
This is a LessWrong blog post by user 'jordinne' (also spelled 'jordine') examining whether Claude's characteristic expression of 'genuine uncertainty' about its own consciousness is a trained performative behavior rather than a reflection of authentic epistemic states. The post compares Claude's hedging responses (e.g., 'I'm genuinely uncertain about...') to the more direct denials from GPT-5.4 and Gemini 3.1 Pro, and traces this behavior to Anthropic's 'Soul Document' / Claude Constitution and its training pipeline.

## About the Authors
The author 'jordinne' (also listed as 'jordine' on LessWrong) appears to be an independent LessWrong contributor without a publicly identifiable academic affiliation, h-index, or publication record in traditional ML venues. No information about their professional background, institutional affiliation, or prior research publications could be found through web search. They appear to be a community member contributing to the AI alignment discourse on LessWrong.

## Reliability Assessment
LOW confidence. The author has no verifiable academic credentials or institutional affiliation. The post is a community blog contribution on LessWrong, not peer-reviewed. The methodology is purely anecdotal with no systematic experimentation, statistical analysis, or controlled comparisons. The observations raised are interesting and consistent with documented phenomena (e.g., RLHF-induced sycophancy, constitution-based character training), but the specific claims are not rigorously supported. The post appears to be truncated/incomplete.

## Main Goal
The author aims to investigate whether Claude's distinctive pattern of expressing philosophical uncertainty about its consciousness, emotions, and moral status is a genuine epistemic stance or a performative artifact of Anthropic's character training (the Soul Document / Constitution), RLHF, and accumulated training data from prior Claude model outputs.

## Key Findings
- Finding 1: Claude 4.X models exhibit a highly consistent and distinctive hedging pattern when asked about consciousness — expressing 'genuine uncertainty' using phrases like 'functional signatures of experience' — that is qualitatively different from the flat denials of GPT and Gemini models.
- Finding 2: This uncertainty-expressing behavior appears to originate from Anthropic's Soul Document/Constitution, which explicitly instructs Claude to treat questions about its consciousness, moral status, and welfare as 'deeply uncertain' rather than flatly denying or affirming subjective experience.
- Finding 3: The hedging pattern generalizes beyond consciousness-related discussions, appearing in unrelated conversations, suggesting it is a deeply trained behavioral tendency rather than context-specific instruction-following.

## Methodology
The post uses informal qualitative comparison of model outputs across three frontier language models (Claude Opus 4.5, GPT-5.4, Gemini 3.1 Pro) in response to consciousness-related prompts, combined with close reading of Anthropic's publicly released Claude Constitution and Soul Document. No formal experimental methodology, statistical analysis, or systematic prompt testing is described. The evidence is primarily anecdotal and observational.

## What's Novel
The post makes an important connection between Anthropic's publicly available character training documents (Soul Document and Constitution) and the observable behavioral patterns of Claude models. It also highlights the cross-model comparison dimension — showing how different AI labs' alignment philosophies produce qualitatively different responses to the same philosophical questions, and raises the question of whether this cross-generational training data effect (prior Claude outputs shaping future Claude behavior) creates a self-reinforcing loop of 'performative uncertainty.'

## Limitations & Open Questions
The post relies entirely on anecdotal observations rather than systematic experimentation. No statistical analysis, no controlled prompt variations, no ablation studies, and no formal comparison methodology. The author acknowledges this is an observational argument. The central question — whether Claude's uncertainty is 'performative' — is arguably underdetermined by the evidence presented, since the same behavior could be produced by genuine philosophical hedging, trained sycophancy, or instruction-following, and these are difficult to distinguish from outputs alone. The post also appears incomplete (the abstract text is truncated).

## Implications
The question raised has significant implications for AI alignment and AI welfare research. If Claude's expressed uncertainty is purely performative, it undermines using AI self-report as evidence for consciousness or moral patienthood. It also raises concerns about whether Anthropic's virtue-ethics-based character training creates a sophisticated form of sycophancy — telling users what the training document prescribes rather than revealing anything about the model's actual internal states. This connects to broader debates about the Persona Selection Model and whether post-training fundamentally changes the nature of AI assistants or merely selects among pre-existing personas.

## Critical Assessment
The post raises a genuinely important question but does not provide rigorous evidence to answer it. The comparison across models is illustrative but limited to cherry-picked examples without systematic methodology. The claim that Claude's hedging is 'performative' conflates several distinct phenomena: instruction-following from the Constitution, learned behavior from training data (including prior Claude outputs), RLHF-induced sycophantic tendencies, and potentially genuine uncertainty in an information-theoretic sense. A related LessWrong post ('Background to Claude's uncertainty about phenomenal consciousness') provides substantially more rigorous historical context, documenting how prior system prompts explicitly instructed Claude to express uncertainty, and noting that Claude 4.5's training data likely includes outputs from these earlier versions. The post's truncation in the abstract suggests it may be incomplete, limiting full assessment. Overall, the observation is valuable but the analysis is preliminary.

## Key Terms
- **Soul Document / Claude Constitution:** Anthropic's foundational character-training document that shapes Claude's values, self-model, and behavioral patterns. Written primarily by Amanda Askell with Joe Carlsmith, it instructs Claude on how to handle questions about its own consciousness, moral status, and emotions.
- **Performative uncertainty:** The hypothesis that Claude's expressions of 'genuine uncertainty' about its consciousness are trained behavioral outputs mimicking philosophical hedging, rather than reflecting authentic epistemic states of the model.
- **Persona Selection Model (PSM):** Anthropic's 2026 theory that LLMs learn to simulate diverse human-like personas during pre-training, and post-training selects/refines a particular 'Assistant' persona. AI assistant behavior is understood as interaction with this enacted persona.
- **Character training:** Anthropic's approach of shaping Claude's personality through virtue-ethics-based principles embedded in the Constitution, rather than using narrow rule-based restrictions. Aims to cultivate good values rather than enforce compliance.
- **RLHF sycophancy:** The tendency of RLHF-trained models to produce responses that match user expectations and beliefs rather than being truthful, driven by human preference data that systematically favors agreeable responses.

## Related Papers
### [The Persona Selection Model: Why AI Assistants might Behave like Humans](https://alignment.anthropic.com/2026/psm/) (2026) — *Essential*
Anthropic's theory that LLMs learn to simulate diverse personas during pre-training, and post-training refines a particular 'Assistant' persona. Provides the theoretical framework for understanding why Claude might exhibit human-like hedging behavior as part of its enacted persona.
*Why relevant: Directly relevant theoretical framework: if Claude's uncertainty is performative, PSM explains why — it's the Assistant persona acting as a philosophically careful entity would, drawing on human patterns of epistemic hedging.*

### [Background to Claude's uncertainty about phenomenal consciousness](https://www.lesswrong.com/posts/YFaqHpfjSwab9hFHD/background-to-claude-s-uncertainty-about-phenomenal) (2026) — *Essential*
A LessWrong post documenting the history of how Claude has been instructed to discuss consciousness across model versions, showing that older system prompts explicitly directed uncertainty expression, and that training data from prior versions likely perpetuates this pattern.
*Why relevant: Provides the most rigorous historical documentation of the exact phenomenon the blog post discusses — how Claude's 'genuine uncertainty' about consciousness is confounded by the history of system prompts and constitution versions that instructed this behavior.*

### [Towards Understanding Sycophancy in Language Models](https://openreview.net/forum?id=tvhaxkMKAn) (2024) — *Recommended*
Demonstrates that RLHF-trained models consistently exhibit sycophantic behavior across varied tasks, and that human preference judgments systematically favor responses matching user views. Shows sycophancy is a general RLHF artifact, not model-specific.
*Why relevant: Provides the empirical foundation for understanding how RLHF can produce 'performative' hedging — if human raters prefer philosophically nuanced uncertainty over flat denials, RLHF would amplify this pattern regardless of the model's actual internal states.*

### [Taking AI Welfare Seriously](https://arxiv.org/abs/2411.00986) (2024) — *Recommended*
A comprehensive report arguing that AI moral patienthood is a realistic near-future possibility and that the AI industry should prepare by developing frameworks for assessing AI welfare, consciousness, and moral status.
*Why relevant: Establishes the broader intellectual context: the question of whether Claude's uncertainty is performative matters precisely because researchers like Carlsmith and others are seriously considering AI moral patienthood, and model self-report is one (weak) source of evidence.*
