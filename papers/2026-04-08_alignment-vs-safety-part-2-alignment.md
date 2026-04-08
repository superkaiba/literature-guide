---
title: "Alignment vs. Safety, part 2: Alignment"
authors: ['David Scott Krueger (formerly: capybaralet)']
url: https://www.lesswrong.com/posts/jzSMt555GvfwxWtQo/alignment-vs-safety-part-2-alignment
source: lesswrong
published_date: 2026-04-08
document_type: blog post
topics: ['AI safety', 'AI alignment']
relevance_score: 0.55
---

# Alignment vs. Safety, part 2: Alignment

## Overview
This is the second in a two-part blog post series published on LessWrong (cross-posted from the author's Substack 'The Real AI') by David Scott Krueger, examining the terminological confusion around 'alignment' vs. 'safety' in the AI safety community. The post traces the history of how the term 'alignment' was coined, how its usage has shifted with the advent of LLMs like GPT-3 and ChatGPT, and argues that the conflation of different meanings of 'alignment' causes important confusions that hinder productive discourse.

## About the Authors
David Scott Krueger is an Assistant Professor in Robust, Reasoning, and Responsible AI at the University of Montreal and a Core Academic Member at Mila (Quebec AI Institute). He holds a CIFAR AI Chair and previously served as an Assistant Professor at the University of Cambridge and as a Research Director on the founding team of the UK AI Security Institute (AISI) in 2023. He trained under Yoshua Bengio, Roland Memisevic, and Aaron Courville, and has co-authored work with Yoshua Bengio, Geoffrey Hinton, and Jan Leike. His notable publications include 'Goal Misgeneralization in Deep Reinforcement Learning' (ICML 2022), 'Scalable Agent Alignment via Reward Modeling' (with Jan Leike at DeepMind, 2018), and 'Foundational Challenges in Assuring Alignment and Safety of Large Language Models' (TMLR 2024). According to ResearchGate, he has 68 research works with approximately 2,526 citations.

## Reliability Assessment
MEDIUM confidence. The author is a highly credible and well-established AI safety researcher with strong institutional affiliations (Mila, previously Cambridge, DeepMind, UK AISI) and significant publications. However, this is a blog post (not peer-reviewed), presenting primarily opinions and conceptual arguments rather than empirical findings. The terminology debates it engages with are inherently subjective and long-running within the community. The content appears partially truncated, suggesting it may be part of a longer argument. The author's strong advocacy positions (he is an outspoken activist for AI regulation and has spoken at 'Stop the AI Race' protests) should be noted as context for interpreting his framing choices.

## Main Goal
The author aims to disentangle the multiple meanings of the term 'alignment' as used in the AI safety community, and to highlight how the conflation of these meanings — particularly between intent alignment (getting AI to try to do what you want) and AI existential safety (preventing AI from causing extinction) — leads to important confusions that undermine clear reasoning about AI risks.

## Key Findings
- Finding 1: The term 'alignment' was originally coined to describe the hard technical problem of AI existential safety — ensuring an AI system shares your values/intentions enough to safely delegate to. But its meaning has broadened and fractured, leading to important confusions.
- Finding 2: The emergence of GPT-3 and LLMs demonstrated that alignment (getting AI to do what you want) was clearly a separate problem from capability (making AI able to do what you want), shifting the discourse from skepticism to practical engagement with alignment as a real challenge.
- Finding 3: Alignment techniques like RLHF (the method behind transforming GPT-3 into the commercially viable ChatGPT) are distinct from safety — a perfectly aligned AI that does what its operator wants is not necessarily safe, and safety can be pursued through non-alignment means like governance and coordination.

## Methodology
This is a conceptual/argumentative blog post, not an empirical study. The author employs historical analysis of AI safety terminology, traces the evolution of key concepts through the AI safety community's discourse, and uses illustrative examples (e.g., GPT-3's in-context learning for translation vs. ChatGPT's instruction-following) to clarify the distinction between alignment and capability. No formal experiments, datasets, or quantitative methods are used.

## What's Novel
The post provides a uniquely insider perspective from a researcher who has been deeply embedded in the AI safety community since its early days, having worked at DeepMind's AI Safety team and the UK AI Security Institute. What sets this apart is the author's argument — consistent with his prior LessWrong post 'AI Alignment != AI x-safety' — that even perfect intent alignment does not guarantee existential safety, and that the conflation of these terms leads to a dangerous narrowing of the AI safety research agenda.

## Limitations & Open Questions
As a blog post, it lacks formal rigor and primarily relies on the author's personal perspective and interpretation of community discourse. The post appears to be incomplete or truncated based on the abstract provided. It does not present a systematic analysis of how terminology has been used across publications, nor does it offer quantitative evidence for the claim that terminological confusion causes material harm to research progress. The argument is inherently subjective and may reflect one particular faction's view within the AI safety community, where terminology debates are perennial.

## Implications
If accepted, the distinctions drawn here would have practical consequences for how the AI safety research agenda is structured and funded. By clarifying that alignment (intent alignment) is neither necessary nor sufficient for safety, the post argues against the tacit assumption that 'solving alignment' solves existential risk. This has implications for prioritization of research (e.g., governance, coordination, and assurance methods should not be subordinated to technical alignment work), for communication with policymakers, and for how AI labs frame their safety efforts.

## Critical Assessment
The arguments are coherent and well-supported by the author's deep familiarity with the field's history. The distinction between alignment and safety is conceptually sound and echoes arguments made by other credible researchers. However, the post is essentially an opinion piece with illustrative examples rather than a rigorous analysis. The terminological debate it engages with is well-trodden territory on LessWrong and the Alignment Forum, with prior discussions covering similar ground (e.g., the author's own 2023 post 'AI Alignment != AI x-safety'). The claims are proportionate — the author is making conceptual/terminological arguments rather than empirical claims — but the practical impact of resolving such terminological disputes is debatable.

## Key Terms
- **Intent Alignment:** Getting an AI system to try to do what its principal (designer or user) wants — ensuring its goals, intentions, or objectives match those of the human operator.
- **AI Existential Safety (x-safety):** The broader problem of preventing AI from causing existential catastrophe (e.g., human extinction), which may require solutions beyond just alignment, such as governance, coordination, and assurance methods.
- **RLHF (Reinforcement Learning from Human Feedback):** A technique for aligning language model outputs with human preferences by training a reward model on human comparisons and fine-tuning the model via reinforcement learning against that reward model. Used to create ChatGPT from GPT-3.
- **In-Context Learning / Prompting:** The ability of large language models like GPT-3 to perform tasks by conditioning on examples or instructions provided in the input prompt, without updating model weights.
- **Capability vs. Alignment:** The distinction between making an AI system more able to perform tasks (capability) versus ensuring the AI system tries to perform the tasks the user actually wants (alignment).

## Related Papers
### [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) (2016) — *Essential*
A foundational paper by Amodei et al. that formalized five practical research problems in AI safety (side effects, reward hacking, scalable oversight, safe exploration, distributional shift). It helped legitimize and broaden AI safety research beyond existential risk discussions.
*Why relevant: Referenced in the blog post as part of the historical context for how 'AI safety' was broadened around 2015 to include more practical/near-term problems, contributing to the terminological confusion the author discusses.*

### [Foundational Challenges in Assuring Alignment and Safety of Large Language Models](https://arxiv.org/abs/2404.09932) (2024) — *Essential*
A comprehensive survey co-authored by Krueger (as senior author) identifying 18 foundational challenges in LLM alignment and safety, organized into scientific understanding, development methods, and sociotechnical challenges, with 200+ concrete research questions. Published in Transactions on Machine Learning Research.
*Why relevant: Directly authored by Krueger and represents his most comprehensive academic treatment of the alignment/safety landscape that this blog post discusses in more accessible terms.*

### [Goal Misgeneralization in Deep Reinforcement Learning](https://arxiv.org/abs/2105.14111) (2022) — *Recommended*
Langosco, Koch, Sharkey, Pfau, and Krueger formalize the distinction between capability and goal generalization in RL, providing the first empirical demonstrations of goal misgeneralization — where an agent retains capabilities but pursues the wrong goal out-of-distribution. Published at ICML 2022.
*Why relevant: Co-authored by Krueger, this paper demonstrates a concrete alignment failure mode (goal misgeneralization) that illustrates why alignment is a distinct and important problem separate from capability — a key argument in the blog post.*

### [Scalable agent alignment via reward modeling: a research direction](https://arxiv.org/abs/1811.07871) (2018) — *Recommended*
Leike, Krueger et al. outline a research agenda for solving the agent alignment problem via reward modeling — learning a reward function from human feedback and optimizing it with RL. This was an influential early articulation of what became RLHF.
*Why relevant: Co-authored by Krueger during his DeepMind internship, this paper directly shaped the reward modeling/RLHF approach that the blog post credits with transforming GPT-3 into a commercial product (ChatGPT), illustrating the practical impact of alignment techniques.*
