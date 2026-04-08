---
title: "Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning"
authors: ['Kui Chen', 'Jing Zhang', 'Yong Xiao', 'Minho Jo', 'Derrick Wing Kwan Ng']
url: https://www.semanticscholar.org/paper/a36c4cc380fe9f0b9501355e9cd0abd9a1849997
source: semantic_scholar
published_date: 2026-05-01
document_type: research paper
topics: ['mechanistic interpretability', 'AI safety', 'AI alignment', 'language model personas', 'emergent misalignment', 'subliminal learning', 'superposition features']
relevance_score: 0.5
---

# Completion Time Minimization for UAV-Assisted Semi-Decentralized Hybrid Federated Learning

## Overview
This is a peer-reviewed research paper accepted at IEEE Transactions on Mobile Computing (TMC) that addresses completion time minimization in UAV-assisted federated learning for large-scale IoT networks. It proposes a semi-decentralized hybrid federated learning (SDHFL) framework where a UAV serves as a mobile data center to coordinate learning across distributed IoT clusters, and formulates a non-convex MINLP optimization problem to minimize overall completion time under energy and QoS constraints.

## About the Authors
Yong Xiao is a professor at Huazhong University of Science and Technology (HUST), specializing in machine learning, game theory, distributed optimization, semantic communications, and IoT; he is associate editor of IEEE TMC and associate group leader of the IMT-2030 network intelligence group. Derrick Wing Kwan Ng is a Scientia Associate Professor at UNSW Sydney, an IEEE Fellow (Class 2021) and Highly Cited Researcher since 2018 with over 43,000 citations and an h-index of 64+, working on wireless communications resource allocation and optimization. Minho Jo is a Professor at Korea University's Department of Computer and Software Engineering, with an h-index of ~29 and over 3,200 citations, focusing on IoT, blockchain, and wireless networks. Jing Zhang is affiliated with HUST and has published on energy-efficient D2D communications and wireless-powered networks with D.W.K. Ng and Minho Jo as frequent co-authors.

## Reliability Assessment
MEDIUM-HIGH confidence. The paper is accepted at IEEE Transactions on Mobile Computing, a top-tier venue in its field (IF ~7.7). The author team includes an IEEE Fellow (Ng) and established professors at reputable institutions (HUST, UNSW, Korea University). The methodology follows standard optimization frameworks for wireless network design. However, the evaluation is simulation-only, the single-UAV assumption is somewhat restrictive, and no public discussion or independent validation of the specific results was found. The paper is highly competent within its niche but entirely outside the scope of AI safety, mechanistic interpretability, or language model research.

## Main Goal
The authors aim to design and optimize a semi-decentralized hybrid federated learning architecture that uses a UAV as a mobile aggregator to serve IoT device clusters, minimizing overall FL training completion time while satisfying UAV energy constraints, device energy constraints, and quality-of-service requirements through joint optimization of cluster selection, power allocation, and computational resource allocation.

## Key Findings
- Finding 1: The proposed SDHFL framework reveals a non-trivial tradeoff where overall completion time initially decreases and then increases as the number of devices or clusters grows, demonstrating the necessity of jointly optimizing both cluster counts and intra-cluster device allocations rather than naively adding more participants.
- Finding 2: The authors prove convergence of the SDHFL scheme and derive the minimum number of global iterations required, providing theoretical guarantees that inform the algorithm design and establish bounds on training time.
- Finding 3: A low-complexity suboptimal algorithm based on Lyapunov optimization theory is introduced for dynamic cluster selection and resource allocation, demonstrating scalability for large-scale networks and significantly reducing overall completion time compared to several baseline schemes.

## Methodology
The paper formulates a non-convex mixed-integer nonlinear programming (MINLP) problem for minimizing completion time. The system model involves a UAV acting as a mobile data center that visits IoT device clusters sequentially. Devices within clusters perform local model training and communicate with the UAV for aggregation. The MINLP is decomposed using Lyapunov optimization theory to convert long-term stochastic constraints into per-slot deterministic problems, enabling online solutions. The authors jointly optimize power allocation, device computational capability, and cluster selection. Convergence analysis derives the minimum number of global iterations. Simulation-based evaluation validates the framework against multiple baseline schemes.

## What's Novel
The key novelty lies in the 'semi-decentralized hybrid' architecture that combines intra-cluster decentralized learning with UAV-mediated global aggregation, creating a middle ground between fully centralized and fully decentralized FL. The use of a single mobile UAV as both data collector and aggregator across geographically distributed clusters, coupled with the Lyapunov-based dynamic optimization framework for joint cluster selection and resource allocation, is distinctive. The discovery of the non-monotonic relationship between device/cluster count and completion time provides a practically important design insight.

## Limitations & Open Questions
The paper appears to consider a single UAV scenario, which limits scalability for very large geographic areas. The UAV must sequentially visit clusters, introducing inherent latency. The simulation-based evaluation may not fully capture real-world channel dynamics, UAV flight mechanics, and device heterogeneity. The convergence analysis likely relies on standard assumptions (e.g., bounded gradients, Lipschitz smoothness) that may not hold in all practical settings. The suboptimal algorithm, while low-complexity, does not provide provable optimality gaps for the MINLP problem.

## Implications
This work is relevant for deploying federated learning in infrastructure-limited IoT environments (disaster zones, rural areas, military operations) where UAVs can provide mobile communication infrastructure. The non-trivial tradeoff finding has practical implications for network planning—blindly adding more devices or clusters can worsen performance. The Lyapunov-based approach offers a template for online resource management in other UAV-assisted distributed learning scenarios. For the wireless communications community, this contributes to the growing intersection of UAV communications and distributed machine learning.

## Critical Assessment
The paper addresses a relevant and timely problem at the intersection of UAV communications, federated learning, and IoT. The MINLP formulation and Lyapunov-based decomposition follow established wireless optimization methodology and appear rigorous. The convergence analysis adds theoretical value. However, the paper is primarily a wireless communications / resource optimization contribution rather than a machine learning one—the 'learning' component is somewhat generic and the focus is on communication and computation resource management. The simulation-based validation is standard for this field but lacks real-world experimental deployment. The assumption of a single UAV is somewhat limiting. The paper fits well within the IEEE TMC scope and the strong author team lends credibility. This paper has no relevance to mechanistic interpretability, AI safety, AI alignment, language model personas, emergent misalignment, subliminal learning, or superposition features—it is entirely outside the reviewer's core research interests.

## Key Terms
- **Semi-Decentralized Hybrid Federated Learning (SDHFL):** A FL architecture that combines intra-cluster decentralized training among IoT devices with UAV-mediated inter-cluster global model aggregation, creating a hybrid between fully centralized and fully decentralized approaches.
- **MINLP (Mixed-Integer Nonlinear Programming):** An optimization problem class involving both continuous and integer decision variables with nonlinear objective or constraint functions; here used to formulate the joint cluster selection, power allocation, and resource optimization problem.
- **Lyapunov Optimization:** A framework from stochastic network optimization that converts long-term time-averaged constraints into per-slot deterministic optimization problems using virtual queues, enabling online decision-making without future knowledge.
- **Straggler Effect:** A phenomenon in distributed computing/FL where the overall round completion time is dictated by the slowest participating device, causing delays that impede model convergence.
- **Quality of Service (QoS):** Performance metrics (e.g., minimum data rates, maximum latency) that must be maintained for each device or cluster during the FL training process while optimizing overall completion time.

## Related Papers
### [Communication-Efficient Learning of Deep Networks from Decentralized Data](https://proceedings.mlr.press/v54/mcmahan17a.html) (2017) — *Essential*
The foundational FedAvg paper by McMahan et al. introducing the Federated Averaging algorithm for training deep networks across decentralized data on mobile devices, demonstrating 10-100x communication reduction versus synchronized SGD.
*Why relevant: The seminal federated learning paper that this work builds upon; SDHFL extends the basic FL framework to a semi-decentralized UAV-assisted architecture with resource optimization.*

### [Adaptive UAV-Assisted Hierarchical Federated Learning: Optimizing Energy, Latency, and Resilience for Dynamic Smart IoT](https://arxiv.org/abs/2503.06145) (2025) — *Recommended*
Proposes a hierarchical FL architecture with energy-constrained UAVs as mobile aggregators for smart IoT, jointly optimizing learning configuration, bandwidth allocation, and device-to-UAV association using augmented Lagrangian and TD3-based reinforcement learning.
*Why relevant: A closely related and more recent work addressing the same UAV-assisted hierarchical FL problem with different optimization approaches (DRL-based vs. Lyapunov-based), enabling direct methodological comparison.*

### [Communication-Efficient Device Scheduling for Federated Learning Using Lyapunov Optimization](https://arxiv.org/abs/2503.00569) (2025) — *Recommended*
Derives convergence bounds for FL with arbitrary device participation probabilities and develops a Lyapunov drift-plus-penalty based client selection and power allocation algorithm, achieving up to 8.5x speedup over uniform selection.
*Why relevant: Uses the same core Lyapunov optimization methodology for FL device scheduling and power allocation, providing a direct methodological reference for the optimization approach used in this paper.*

### [Decentralized Federated Learning for UAV Networks: Architecture, Challenges, and Opportunities](https://arxiv.org/abs/2104.07557) (2021) — *Recommended*
Proposes a Decentralized FL architecture for UAV Networks (DFL-UN) that enables FL within UAV networks without a central entity, addressing single points of failure in centralized UAV FL systems.
*Why relevant: Foundational work on decentralized FL in UAV networks that motivates and contextualizes the semi-decentralized approach taken in this paper; provides the architectural baseline the authors seek to improve upon.*
