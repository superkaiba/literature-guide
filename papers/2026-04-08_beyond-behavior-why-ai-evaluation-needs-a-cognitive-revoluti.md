---
title: "Beyond Behavior: Why AI Evaluation Needs a Cognitive Revolution"
authors: ['Amir Konigsberg']
url: http://arxiv.org/abs/2604.05631v1
source: arxiv
published_date: 2026-04-07
topics: ['AI alignment', 'mechanistic interpretability']
relevance_score: 0.35
---

## Summary
This paper argues that AI evaluation has been epistemologically constrained by Turing's 1950 behavioral test, which implicitly committed the field to treating behavioral outputs as the only relevant evidence for intelligence attribution. The author draws a structural analogy to the behaviorist-to-cognitivist transition in psychology, arguing that just as behaviorism prevented psychologists from studying internal mental processes, AI's behavioral evaluation paradigm prevents researchers from distinguishing between systems that achieve identical outputs through fundamentally different computational mechanisms. The paper contends that this distinction—between behavioral equivalence and mechanistic equivalence—is crucial for questions of intelligence attribution, AI safety, and alignment. The proposed solution is not to abandon behavioral evidence but to supplement it with process-level, mechanistic, and internal-organizational evidence, analogous to how cognitive psychology incorporated reaction times, error patterns, and computational modeling. The implications touch directly on AI alignment and interpretability: a system that produces safe-seeming outputs through brittle or misaligned internal processes may be fundamentally different from one whose internal mechanisms are genuinely aligned, and behavioral tests alone cannot distinguish these cases.

## About the Authors
Amir Konigsberg does not appear to be a widely recognized figure in mainstream ML research publications, and detailed affiliation information is not readily available from the abstract alone. The paper appears to be a philosophical/conceptual contribution rather than an empirical ML paper, suggesting the author may have a background in philosophy of mind, cognitive science, or AI ethics rather than core ML engineering. Without further information, it is difficult to assess their track record or institutional affiliation.

## Reliability Assessment
MEDIUM confidence. The paper's argument is philosophically coherent and the analogy to the cognitive revolution in psychology is well-established in philosophy of mind literature, lending conceptual credibility. However, the author is not a recognizable figure in AI research, the paper is an arXiv preprint without confirmed peer review, and the abstract is cut off, preventing full assessment of the evidence and argumentation. The claims appear proportionate and the framing is careful rather than sensationalist, but the lack of institutional affiliation and empirical methodology (it is a conceptual/philosophical paper) warrants cautious assessment.

## Why It Matters
This paper provides a philosophical and historical foundation for why mechanistic interpretability is not merely a technical curiosity but an epistemological necessity for AI alignment—behavioral safety evaluations may be systematically insufficient to detect misalignment if the underlying computational processes are not examined. For alignment researchers, this strengthens the case that interpretability tools (e.g., circuit analysis, probing, causal intervention) are indispensable complements to behavioral benchmarks. It situates current mechanistic interpretability work within a broader scientific paradigm shift, potentially helping researchers articulate why the field needs to move beyond capability and safety benchmarks.

## Related Papers
### [Computing Machinery and Intelligence](https://doi.org/10.1093/mind/LIX.236.433) (1950)
Alan Turing's foundational paper proposing the 'imitation game' (Turing Test) as a behavioral criterion for machine intelligence. This is the primary target of critique in Konigsberg's paper, making it essential reading for understanding the epistemological commitment being challenged.

### [Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small](https://arxiv.org/abs/2211.00593) (2022)
Wang et al. present a mechanistic interpretability study identifying specific circuits in GPT-2 responsible for indirect object identification, demonstrating exactly the kind of process-level investigation Konigsberg argues is necessary. This paper exemplifies the 'cognitive revolution' in AI evaluation the author advocates for, moving beyond behavioral benchmarks to internal computational mechanisms.
