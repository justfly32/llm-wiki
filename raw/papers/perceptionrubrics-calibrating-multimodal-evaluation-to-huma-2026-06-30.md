---
source_url: https://arxiv.org/abs/2606.28322v1
ingested: 2026-06-30
type: paper
arxiv_id: 2606.28322v1
authors: Yana Wei, Hongbo Peng, Yanlin Lai
published: 2026-06-26
categories: cs.CV
---

# PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception

**Authors:** Yana Wei, Hongbo Peng, Yanlin Lai
**Published:** 2026-06-26
**arXiv:** https://arxiv.org/abs/2606.28322v1
**Categories:** cs.CV

## Abstract

We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 12,000 instance-specific rubrics. These criteria are derived from golden captions constructed via a novel Circular Peer-Review consensus pipeline and then distilled into a dual-stream system of Must-Right (essential facts) and Easy-Wrong (fine-grained details) rubrics. Crucially, PerceptionRubrics implements a Gated Scoring mechanism: unlike linear averages, failure on mandatory visual facts triggers sharp binary penalties. Extensive evaluation yields critical insights: (1) The Reliability Gap: models often verify fragmented elements correctly yet fail strict conjunctive constraints, exposing brittleness in dense domains; (2) Open-Closed Stratification: contrary to reasoning trends, we reveal a persistent 8% perception deficit between open-source and proprietary frontiers; and (3) Human-Aligned Rigor: our gated metrics substantially out-align conventional benchmarks, validating that strict perceptual fidelity is the prerequisite for reliable generation.
