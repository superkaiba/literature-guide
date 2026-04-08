---
title: "Beyond Behavior: Why AI Evaluation Needs a Cognitive Revolution"
authors: ['Amir Konigsberg']
url: http://arxiv.org/abs/2604.05631v1
source: arxiv
published_date: 2026-04-07
document_type: preprint
topics: ['AI alignment', 'mechanistic interpretability']
relevance_score: 0.45
---

# Beyond Behavior: Why AI Evaluation Needs a Cognitive Revolution

## Overview
This is a philosophical/theoretical preprint posted on arXiv (cs.AI; cs.HC) that argues AI evaluation has been overly constrained by Turing's behaviorist epistemology since 1950. It draws a structural analogy between the behaviorist-to-cognitivist transition in psychology and proposes that AI needs an equivalent 'cognitive revolution' in its evaluative framework, moving beyond purely behavioral assessments to examine internal computational processes and mechanisms.

## About the Authors
Amir Konigsberg holds a PhD from Princeton University / Hebrew University of Jerusalem in Rationality and Interactive Decision Theory, combining philosophy, psychology, and game theory. He teaches at Tel Aviv University as an adjunct professor and is primarily known as a technology entrepreneur—he co-founded Twiggle (e-commerce NLP, $35M+ funding) and has been involved in multiple AI-related companies. His Google Scholar profile shows approximately 55 total citations across 11 publications, with an h-index that appears to be in the low single digits. His academic research interests span epistemology, embodied cognition, belief revision, and artificial consciousness, but his publication record in peer-reviewed AI venues is limited.

## Reliability Assessment
LOW confidence. While the philosophical argument is coherent and interesting, several factors reduce confidence: (1) This is an unreviewed arXiv preprint, not peer-reviewed; (2) The author's primary career is in tech entrepreneurship, not active AI research, with a modest academic publication record (~55 citations total); (3) The paper is purely conceptual with no empirical component; (4) It does not adequately engage with the existing mechanistic interpretability literature that already operationalizes the shift being called for; (5) The argument space (Turing test critique, behavioral vs. internal evaluation) is well-trodden, and the paper's incremental novelty over prior work (especially Johnson-Laird & Ragni 2023 and Chollet 2019) is unclear; (6) No evidence of discussion or uptake in the research community was found.

## Main Goal
The paper argues that Turing's 1950 decision to reduce the question of machine intelligence to behavioral indistinguishability was not merely pragmatic but constituted a deep epistemological commitment that has constrained AI research for seven decades. The author seeks to show that behavioral evaluation alone is insufficient for the construct claims AI researchers wish to make (e.g., about intelligence, reasoning, understanding), and proposes a post-behaviorist evaluative framework analogous to the cognitive revolution in psychology.

## Key Findings
- Finding 1: Turing's behavioral test was not just a practical simplification but an epistemological commitment about what counts as evidence for intelligence—one that became embedded in AI's evaluative infrastructure and rendered questions about internal processes and mechanisms 'unaskable.'
- Finding 2: There is a structural parallel between AI's current evaluative stance and pre-cognitive-revolution behaviorism in psychology: just as behaviorism prevented productive questions about internal mental processes, AI's behavioral evaluation prevents distinguishing systems that achieve identical outputs through fundamentally different computational processes.
- Finding 3: The field requires an epistemological transition—not abandoning behavioral evidence, but supplementing it with analysis of process, mechanism, and internal organization—to support the construct claims (about intelligence, understanding, reasoning) that the field currently wishes to make.

## Methodology
This is a purely conceptual/philosophical paper. It employs historical analysis of Turing's 1950 paper and the subsequent embedding of behavioral evaluation in AI, draws structural analogies to the history of psychology (behaviorism to cognitivism), and articulates a philosophical argument for what a 'post-behaviorist epistemology' for AI would entail. No empirical experiments, datasets, or computational models are involved.

## What's Novel
The paper's novelty lies in framing Turing's test not as a flawed benchmark to be replaced, but as an epistemological commitment that structurally constrains what questions the field can ask—analogous to the historiography of psychology's cognitive revolution. While many have criticized the Turing test, this paper focuses on the deeper epistemological infrastructure rather than proposing a specific replacement test. It bridges philosophy of science, history of psychology, and AI evaluation in a way that relatively few papers do.

## Limitations & Open Questions
As a purely philosophical/conceptual paper, it offers no empirical validation, no concrete operationalization of the proposed 'post-behaviorist' evaluation framework, and no case studies demonstrating how such evaluation would work in practice. The analogy between psychology's cognitive revolution and AI may be strained—AI systems are engineered artifacts whose internals are in principle fully accessible (unlike biological brains in the 1950s). The paper also does not engage substantively with the active mechanistic interpretability research community, which is already pursuing many of the questions the paper claims are 'unaskable.' The argument may also oversimplify Turing's original intent, which remains a subject of scholarly debate.

## Implications
For alignment and mechanistic interpretability researchers, this paper provides a philosophical grounding for why examining AI internals (not just behavior) is essential. It supports the legitimacy of interpretability research by framing it as a necessary epistemological shift. However, the mechanistic interpretability community is already pursuing this program empirically—the paper's contribution is more in framing and articulation than in enabling new technical work. For safety, the argument that behaviorally equivalent systems can have fundamentally different internal processes is directly relevant to alignment concerns about deceptive alignment and mesa-optimization.

## Critical Assessment
The paper's core argument—that behavioral evaluation alone is insufficient—is well-established and widely shared in the philosophy of AI, cognitive science, and the mechanistic interpretability community. The historical analogy to psychology's cognitive revolution is interesting but potentially oversimplified. The paper does not appear to engage with the extensive existing mechanistic interpretability literature (Olah et al., Elhage et al., Conmy et al., etc.) that is already operationalizing the very shift the paper calls for. The argument also does not address Hendrycks' (2025) counter-position that mechanistic interpretability may be fundamentally intractable for large models. The Turing test critique space is quite crowded (Chollet 2019, Johnson-Laird & Ragni 2023, Feather et al. 2025, Block's Blockhead, Searle's Chinese Room), and the paper's incremental contribution over this prior work—particularly over Johnson-Laird & Ragni's very similar argument—needs clearer articulation. The paper is single-authored by an entrepreneur/adjunct professor rather than a full-time academic researcher, which is neither disqualifying but also means it lacks the institutional review rigor of lab-embedded work.

## Key Terms
- **Behavioral epistemology:** The epistemological stance that only observable behavior (inputs/outputs) constitutes valid evidence for attributing intelligence or cognitive properties to a system, as opposed to examining internal processes or mechanisms.
- **Cognitive revolution:** The paradigm shift in psychology from behaviorism (studying only observable behavior) to cognitivism (studying internal mental representations and processes), which occurred primarily in the 1950s-1970s. The paper argues AI needs an analogous shift.
- **Construct validity:** The degree to which a test or evaluation actually measures the theoretical construct (e.g., intelligence, understanding, reasoning) it claims to measure. The paper argues behavioral tests lack construct validity for intelligence claims.
- **Process-level evaluation:** Assessment of an AI system based not just on its outputs but on the computational processes, mechanisms, and internal representations it uses to produce those outputs.
- **Behavioral equivalence:** The condition where two systems produce identical outputs for the same inputs, while potentially using fundamentally different internal computational processes—a key problem the paper identifies with purely behavioral evaluation.

## Related Papers
### [On the Measure of Intelligence](https://arxiv.org/abs/1911.01547) (2019) — *Essential*
François Chollet argues that measuring AI skill at specific tasks falls short of measuring intelligence, proposes defining intelligence as skill-acquisition efficiency, and introduces the ARC benchmark. Foundational critique of behavioral/skill-based AI evaluation.
*Why relevant: Directly precedes and overlaps with Konigsberg's argument: Chollet also critiques behavioral/skill-based evaluation as insufficient for intelligence claims and proposes going beyond output performance. However, Chollet proposes a concrete benchmark rather than a philosophical framework.*

### [What Should Replace the Turing Test?](https://spj.science.org/doi/10.34133/icomputing.0064) (2023) — *Essential*
Johnson-Laird and Ragni propose replacing the Turing test with a three-step framework: testing AI in psychological experiments, testing its understanding of its own reasoning, and examining the cognitive adequacy of its source code.
*Why relevant: Makes a very similar argument to Konigsberg's paper—that behavioral evaluation is insufficient and AI should be evaluated on internal reasoning processes—but provides a more concrete operationalization. The key competitor/predecessor in this argument space.*

### [Brain-Model Evaluations Need the NeuroAI Turing Test](https://arxiv.org/abs/2502.16238) (2025) — *Recommended*
Feather et al. argue that behavioral similarity is insufficient for evaluating brain models and propose the 'NeuroAI Turing Test' requiring representational convergence between AI model activations and biological brain activity, not just behavioral indistinguishability.
*Why relevant: Makes the same core argument—behavioral similarity is insufficient, internal representations matter—but from the neuroscience/NeuroAI perspective with concrete metrics and evaluation criteria. Demonstrates the argument is being operationalized in adjacent fields.*

### [The Misguided Quest for Mechanistic AI Interpretability](https://ai-frontiers.org/articles/the-misguided-quest-for-mechanistic-ai-interpretability) (2025) — *Recommended*
Dan Hendrycks argues that mechanistic interpretability has failed to provide useful insights into AI behavior due to flawed foundational assumptions, and advocates for top-down representation engineering instead of bottom-up circuit analysis.
*Why relevant: Provides a direct counterargument to the 'look inside the system' approach that Konigsberg advocates. If mechanistic interpretability of large models is intractable, as Hendrycks argues, then the post-behaviorist evaluation program Konigsberg proposes may face fundamental practical barriers.*
