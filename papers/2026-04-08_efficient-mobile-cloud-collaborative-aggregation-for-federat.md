---
title: "Efficient Mobile-Cloud Collaborative Aggregation for Federated Learning With Latency Resilience"
authors: ['Wei Tang', 'Jiliang Li', 'Xiaojun Zhang', 'Yinbin Miao', 'Zhou Su', 'Robert H. Deng']
url: https://www.semanticscholar.org/paper/2f9e74a388ea3cd7cea0e25ec0955e40cf7c81dd
source: semantic_scholar
published_date: 2026-05-01
document_type: research paper
topics: ['mechanistic interpretability', 'AI safety', 'AI alignment', 'language model personas', 'emergent misalignment', 'subliminal learning', 'superposition features']
relevance_score: 0.5
---

# Efficient Mobile-Cloud Collaborative Aggregation for Federated Learning With Latency Resilience

## Overview
This is a research paper published in an IEEE journal (likely IEEE Transactions on Mobile Computing, based on the inline graphic naming convention 'li-ieq*-3642433.gif') addressing the problem of efficient and privacy-preserving secure aggregation in federated learning under network latency conditions. The paper proposes EFL-LR, a protocol that enables mobile-cloud collaborative aggregation while being resilient to high-latency clients (stragglers), reducing the computational overhead significantly compared to existing double-masking approaches.

## About the Authors
Robert H. Deng is a Professor of Computer Science at Singapore Management University (SMU) and an IEEE Fellow, AAIA Fellow, and Fellow of the Academy of Engineering Singapore, with a Computer Science h-index of 77 and over 21,800 citations, specializing in computer security, encryption, and cryptography. Yinbin Miao is a researcher at Xidian University with approximately 2,095 citations, focused on wireless network security and data privacy. Wei Tang and Jiliang Li have co-authored other FL security papers, including 'Robust and Secure Aggregation Scheme for Federated Learning' (IEEE IoT Journal, 2025), extending 2-party to 3-party computation. Zhou Su appears to be affiliated with Xi'an Jiaotong University, working on vehicular networks and federated learning security.

## Reliability Assessment
MEDIUM-HIGH confidence. The paper appears in a reputable IEEE publication venue. The senior author Robert H. Deng is a highly cited IEEE Fellow with deep expertise in applied cryptography and data security. Co-author Yinbin Miao has established credentials in network security at Xidian University. The claimed complexity improvements are concrete and verifiable. However, without seeing the full paper's proofs, concrete benchmarks, and experimental evaluation, full confidence cannot be assigned. The cryptographic building blocks (Shamir's SS, key-homomorphic PRFs) are well-understood, reducing risk of fundamental errors. No red flags detected, but this paper has zero relevance to the reviewer's stated research interests in mechanistic interpretability, AI alignment, or emergent misalignment.

## Main Goal
The authors aim to design a secure aggregation protocol for federated learning that simultaneously achieves: (1) privacy protection for late-arriving clients' gradients, (2) robustness against service interruption, and (3) computational efficiency suitable for resource-constrained mobile devices — achieving O(n log²n + d) client computation and O(n + d) server computation, which is a substantial improvement over existing double-masking methods.

## Key Findings
- Finding 1: The proposed EFL-LR protocol achieves O(n log²n + d) computation for clients and O(n + d) for the server, which is a significant reduction compared to the O(n²+nd) overhead of standard double-masking secure aggregation approaches like SecAgg (Bonawitz et al., CCS 2017).
- Finding 2: By combining Shamir's secret sharing with a key-homomorphic pseudorandom function, the protocol ensures that high-latency clients' privacy is preserved without requiring the server to learn individual masks, avoiding the traditional tradeoff between service interruption and privacy leakage.
- Finding 3: The mobile-cloud collaborative architecture delegates heavy cryptographic operations to the cloud while keeping client-side operations lightweight, making the protocol practical for real-world deployment on resource-constrained mobile devices.

## Methodology
The paper uses a cryptographic protocol design approach, combining Shamir's secret sharing (for distributing secret keys among participants) with a key-homomorphic pseudorandom function (which allows algebraic operations on PRF outputs to cancel pairwise masks). The protocol introduces a mobile-cloud collaborative architecture where computation is split between clients and a cloud helper. Security is analyzed through formal proofs in standard cryptographic models (likely honest-but-curious or semi-malicious server settings). Efficiency is evaluated through asymptotic complexity analysis comparing against prior work (SecAgg, SecAgg+, and double-masking variants), with n denoting the number of clients and d the dimension of the model gradient vector.

## What's Novel
The key innovation is addressing the specific vulnerability of pairwise masking-based secure aggregation to high-latency/straggler clients — a practical problem largely overlooked by prior work focused only on dropout tolerance. While SecAgg (Bonawitz et al.) handles dropouts by reconstructing masks via secret sharing (at O(n²) cost), EFL-LR uses key-homomorphic PRFs to enable mask cancellation without quadratic overhead, specifically targeting the latency resilience problem rather than just dropout tolerance. The mobile-cloud collaborative design is also distinctive, offloading expensive operations away from mobile clients.

## Limitations & Open Questions
Based on the abstract, the paper likely assumes a semi-honest (honest-but-curious) server model rather than a fully malicious adversary. The cloud helper introduces an additional trust assumption — clients must trust that the cloud does not collude with the server. The practical evaluation details (concrete runtime benchmarks, real network experiments, specific model architectures tested) are not described in the abstract. The protocol's security under active/Byzantine adversaries and its behavior under extreme dropout/latency ratios may also be limited.

## Implications
This work addresses a critical practical bottleneck in deploying secure aggregation for federated learning at scale on mobile devices. By reducing client computation from quadratic to near-linear in the number of participants while handling stragglers gracefully, it makes privacy-preserving FL more feasible for real-world mobile applications (e.g., Google Keyboard, mobile health). The latency resilience aspect is particularly important for heterogeneous network environments with varying client capabilities.

## Critical Assessment
The paper addresses a genuine and important problem in practical federated learning deployment. The asymptotic complexity improvements are meaningful, especially the reduction to O(n log²n + d) from O(n² + nd) for clients. However, the abstract alone does not reveal concrete benchmark results, and asymptotic improvements may not always translate to practical gains for typical FL deployment sizes (e.g., n=100-1000). The combination of Shamir's secret sharing with key-homomorphic PRFs is technically sound but well-established in the cryptographic literature. The paper appears to be published in a reputable IEEE venue. The author team combines strong cryptography expertise (Robert H. Deng, Yinbin Miao) with systems/FL knowledge, lending credibility. This paper is solidly within the applied cryptography/systems security domain and is NOT relevant to mechanistic interpretability, AI alignment, emergent misalignment, or language model safety research.

## Key Terms
- **Secure Aggregation:** A cryptographic protocol that allows a server to compute the sum of clients' private inputs (e.g., model gradients) without learning any individual client's contribution, using techniques like pairwise masking and secret sharing.
- **Pairwise Masking:** A technique where each pair of clients agrees on a random mask; when all masks are summed, they cancel out, revealing only the aggregate. If a client drops out, its masks must be reconstructed via secret sharing.
- **Double Masking:** An enhancement to pairwise masking where each client adds a second independent mask to protect against the server learning individual masks during dropout recovery, providing both robustness and privacy at higher computational cost.
- **Key-Homomorphic Pseudorandom Function (PRF):** A PRF where the output satisfies algebraic properties with respect to the key: PRF(k1, x) * PRF(k2, x) = PRF(k1+k2, x), enabling efficient cancellation of masks without reconstructing individual keys.
- **Shamir's Secret Sharing:** A (t,n)-threshold scheme where a secret is split into n shares such that any t shares can reconstruct the secret, but fewer than t shares reveal nothing about it.
- **Latency Resilience:** The ability of a protocol to maintain both security and correctness when some clients arrive late or experience high network latency, as opposed to merely tolerating complete dropouts.
- **Federated Learning (FL):** A distributed machine learning paradigm where multiple clients collaboratively train a model by sharing only local model updates (gradients) with a central server, keeping raw training data on-device.

## Related Papers
### [Practical Secure Aggregation for Privacy-Preserving Machine Learning](https://dl.acm.org/doi/10.1145/3133956.3133982) (2017) — *Essential*
The foundational work by Bonawitz et al. (Google) that introduced the first practical secure aggregation protocol for federated learning using pairwise masking and Shamir's secret sharing, with O(n²+nd) client computation. This is the primary baseline the EFL-LR paper improves upon.
*Why relevant: This is the seminal work establishing pairwise masking-based secure aggregation for FL. EFL-LR directly addresses the quadratic computation bottleneck and latency vulnerability of this protocol.*

### [Secure Single-Server Aggregation with (Poly)Logarithmic Overhead](https://dl.acm.org/doi/10.1145/3372297.3417885) (2020) — *Essential*
Bell, Bonawitz et al. improved upon the original SecAgg by replacing the complete communication graph with a k-regular graph, achieving polylogarithmic per-client communication and computation. This represents the state-of-the-art efficiency improvement prior to EFL-LR.
*Why relevant: A key competing approach that also reduces the quadratic overhead of SecAgg. EFL-LR's O(n log²n + d) complexity should be compared against this work's polylogarithmic bounds to assess the novelty of the improvement.*

### [Robust and Secure Aggregation Scheme for Federated Learning](https://www.semanticscholar.org/paper/Robust-and-Secure-Aggregation-Scheme-for-Federated-Tang-Li/81b7d880d2af7ca3c1b56b12d323dd3f5f3b0994) (2025) — *Recommended*
A closely related paper by the same lead authors (Wei Tang, Jiliang Li, Yinbin Miao) proposing a 3-party computation scheme for FL aggregation that resists abnormal termination and colluding poisoning attacks. Published in IEEE Internet of Things Journal.
*Why relevant: Directly from the same research group, showing their broader research program on secure FL aggregation. Provides context for understanding the authors' approach and threat models.*

### [CESA: Communication Efficient Secure Aggregation Scheme via Sparse Graph in Federated Learning](https://www.sciencedirect.com/science/article/abs/pii/S1084804524001747) (2024) — *Recommended*
Proposes a communication-efficient secure aggregation scheme that transforms the fully-connected client graph into a sparse graph based on a minimal spanning tree, reducing key exchange overhead while maintaining security. Represents an alternative approach to reducing SecAgg's communication costs.
*Why relevant: An alternative approach to improving secure aggregation efficiency using graph-theoretic techniques rather than key-homomorphic PRFs, providing a useful comparison point for the mobile-cloud collaborative approach of EFL-LR.*
