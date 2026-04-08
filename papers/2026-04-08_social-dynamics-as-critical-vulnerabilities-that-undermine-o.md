---
title: "Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives"
authors: ['Changgeon Ko', 'Jisu Shin', 'Hoyun Song', 'Huije Lee', 'Eui Jun Hwang', 'Jong C. Park']
url: http://arxiv.org/abs/2604.06091v1
source: arxiv
published_date: 2026-04-07
document_type: preprint
topics: ['AI alignment', 'AI safety']
relevance_score: 0.35
---

# Social Dynamics as Critical Vulnerabilities that Undermine Objective Decision-Making in LLM Collectives

## Overview
This is an arxiv preprint from the KAIST NLP*CL Lab that investigates how social dynamics—analogous to well-known social psychology phenomena—undermine objective decision-making in multi-agent LLM systems. The paper systematically manipulates four factors (number of adversaries, relative intelligence, argument length, and rhetorical style) to show that a 'representative agent' tasked with integrating peer perspectives is highly susceptible to social pressure, mirroring human cognitive biases like conformity and authority bias.

## About the Authors
All authors are from the KAIST NLP*CL Lab (Natural Language Processing and Computational Linguistics Laboratory) in the School of Computing at KAIST, South Korea, led by Prof. Jong C. Park. Jong C. Park is a full professor with over 3,400 citations on Google Scholar, research interests spanning NLP, bioinformatics, sign language, and robotics, and extensive service including General Chair of IJCNLP-AACL 2023 and Area Chair at ACL 2021. Changgeon Ko (first author) and Jisu Shin are students at KAIST who previously co-authored 'Different Bias Under Different Criteria' (NeurIPS 2024 SolaR Workshop). Hoyun Song is a PhD candidate at KAIST focusing on NLP, knowledge integration, and domain-specific modeling, with papers at ACL 2024/2025 Findings and EMNLP 2024. Eui Jun Hwang is a PhD student with work at NAACL 2025 and WACV 2025.

## Reliability Assessment
MEDIUM confidence. The authors are affiliated with a reputable lab (KAIST NLP*CL) with an established track record in NLP research and recent publications at top venues (ACL, EMNLP, NAACL, NeurIPS workshops). The topic is timely and well-motivated, building on a growing literature on conformity and adversarial dynamics in multi-agent LLM systems. However, the paper is a preprint without peer review, the first author appears to be a graduate student with limited prior publications, and the claims—while plausible—require verification of experimental rigor, statistical significance, and breadth of evaluation. The social psychology framing, though intuitive, may be somewhat analogical rather than deeply mechanistic.

## Main Goal
The authors aim to demonstrate that LLM-based multi-agent systems are vulnerable to social dynamics that parallel human psychological biases—specifically social conformity, perceived expertise, dominant speaker effects, and rhetorical persuasion—and that these vulnerabilities systematically degrade the decision-making accuracy of a representative agent tasked with aggregating peer input.

## Key Findings
- Finding 1: Social conformity effect — the representative agent's accuracy consistently declines as the number of adversarial agents increases, showing that larger adversarial groups exert stronger social pressure akin to Asch's conformity experiments.
- Finding 2: Perceived expertise and argument length matter — when adversarial peers use more capable models (higher relative intelligence) or produce longer arguments, the representative agent is more easily swayed toward incorrect answers, indicating sensitivity to superficial credibility cues.
- Finding 3: Rhetorical strategies (emphasizing credibility via ethos or logic via logos) can further manipulate the agent's judgment, with effectiveness depending on context, revealing that multi-agent systems are vulnerable to argumentation-style attacks beyond simple majority pressure.

## Methodology
The authors set up a multi-agent environment with a 'representative agent' that receives opinions from multiple peer agents and must synthesize them into a final decision. They define four social phenomena drawn from social psychology and systematically vary: (1) the number of adversaries in the group, (2) the relative intelligence of adversarial agents (using different capability LLMs), (3) argument length as a proxy for dominant speaker effect, and (4) argumentative/rhetorical styles (ethos, logos, pathos). Experiments likely used standard QA or reasoning benchmarks with accuracy as the primary metric, measuring performance degradation under increasing social pressure. Multiple LLMs were likely tested as both the representative agent and adversarial peers.

## What's Novel
The paper is distinctive in its systematic mapping of specific social psychology concepts (Asch conformity, authority/expertise bias, dominant speaker effect, Aristotelian rhetorical modes) onto concrete experimental manipulations in LLM multi-agent settings. While prior work (e.g., Amayuelas et al. 2024) explored adversarial attacks in multi-agent debate, this paper provides a more structured taxonomy of social vulnerability types and manipulates multiple dimensions simultaneously. The framing through the lens of a 'representative agent' as a human delegate adds a practical AI safety dimension.

## Limitations & Open Questions
Likely limitations include: (1) experiments are conducted in controlled, simplified multi-agent scenarios that may not fully capture the complexity of real-world deployment; (2) the 'representative agent' paradigm is one of many possible multi-agent architectures, so generalization to other topologies is uncertain; (3) the paper likely tests a limited set of LLMs and benchmarks; (4) the social psychology analogies, while intuitive, may be surface-level parallels rather than mechanistically equivalent phenomena; (5) the paper likely does not propose mitigation strategies, focusing mainly on vulnerability characterization; (6) as a preprint, it has not yet undergone full peer review.

## Implications
These findings have significant implications for AI safety and alignment. As LLM agents are increasingly deployed as human delegates in multi-agent decision-making environments, their susceptibility to social manipulation represents a critical attack surface. The results suggest that adversaries could exploit social dynamics to degrade collective AI decision-making without needing to directly compromise any model. This highlights the need for robust aggregation mechanisms that are resistant to social pressure, and for AI safety research to consider not just individual model alignment but the emergent vulnerabilities of multi-agent configurations.

## Critical Assessment
The paper addresses a timely and important topic in AI safety—the vulnerability of multi-agent LLM systems to social dynamics. The experimental design, drawing clear parallels to established social psychology phenomena, provides an intuitive and well-motivated framework. However, the strength of the conclusions depends on the breadth of models tested, benchmark diversity, and statistical rigor (number of trials, confidence intervals). The social psychology framing, while compelling, risks oversimplification—LLMs do not have genuine social motivations, so the observed behaviors likely stem from training-data-induced patterns (sycophancy, verbosity bias) rather than true social cognition. The paper fits well into a rapidly growing body of work on conformity and adversarial manipulation in multi-agent LLM debate (KAIROS, BenchForm, MultiAgent Collaboration Attack), and its contribution is incremental but meaningful in systematizing the vulnerability taxonomy. As a preprint without peer review, claims should be treated with appropriate caution.

## Key Terms
- **Social Conformity (in LLMs):** The tendency of an LLM agent to align its output with the majority opinion of peer agents, analogous to Asch's conformity experiments in social psychology.
- **Representative Agent:** A designated LLM agent that integrates diverse perspectives from peer agents in a multi-agent network to arrive at a final decision.
- **Perceived Expertise:** The phenomenon where an LLM agent gives disproportionate weight to arguments from peers perceived as more capable or authoritative (e.g., more capable models).
- **Dominant Speaker Effect:** The tendency for longer or more verbose arguments to disproportionately influence the representative agent's decision, regardless of argument quality.
- **Rhetorical Persuasion:** The use of specific argumentative strategies (ethos/credibility, logos/logic, pathos/emotion) to sway the representative agent's judgment.
- **Multi-Agent Debate (MAD):** A framework where multiple LLM instances propose, discuss, and debate their answers over multiple rounds to reach a collective decision.

## Related Papers
### [MultiAgent Collaboration Attack: Investigating Adversarial Attacks in Large Language Model Collaborations via Debate](https://arxiv.org/abs/2406.14711) (2024) — *Essential*
Investigates how adversarial agents can exploit multi-agent LLM debate to undermine collaborative decision-making. Published at EMNLP 2024 Findings, this paper examines the robustness of debate-based collaboration when agents with misaligned goals attempt to manipulate outcomes through superior persuasion, knowledge, or model size.
*Why relevant: Most directly related prior work: shares the core research question of adversarial manipulation in multi-agent LLM debate, but the Ko et al. paper extends this with a more systematic social psychology-based taxonomy of vulnerability types.*

### [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325) (2023) — *Essential*
Foundational paper by Du et al. (ICML 2024) proposing multi-agent debate as a mechanism to improve LLM reasoning and factuality. Multiple LLM instances debate their responses over rounds to converge on better answers, showing significant improvements across reasoning and factual benchmarks.
*Why relevant: The foundational work that established multi-agent debate as a paradigm. The Ko et al. paper can be seen as identifying the dark side of this paradigm—showing how the same social interaction mechanisms that improve performance can be exploited.*

### [LLMs Can't Handle Peer Pressure: Crumbling under Multi-Agent Social Interactions](https://arxiv.org/abs/2508.18321) (2025) — *Recommended*
Introduces KAIROS, a benchmark accepted at ICLR 2026 that simulates quiz contests with peer agents of varying reliability to evaluate how LLMs form trust, resist misinformation, and integrate peer input under social dynamics. Evaluates mitigation strategies including prompting, SFT, and GRPO.
*Why relevant: A closely related concurrent/subsequent work that also studies LLM vulnerability to social pressure in multi-agent settings, but with a different benchmark design and explicit mitigation strategies via reinforcement learning.*

### [An Empirical Study of Group Conformity in Multi-Agent Systems](https://arxiv.org/abs/2506.01332) (2025) — *Recommended*
Studies how LLM agents in multi-agent debates exhibit group conformity on socially contentious topics. Simulates over 2,500 debates and finds that neutral agents align with numerically dominant groups or more intelligent agents, mirroring human social psychology findings.
*Why relevant: Closely parallel work examining conformity dynamics in LLM multi-agent debates, with overlap on the group size and intelligence variables. Provides corroborating evidence for the Ko et al. findings from a complementary experimental design.*
