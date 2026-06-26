---
source_url: https://arxiv.org/abs/2606.03992v1
ingested: 2026-06-04
type: paper
arxiv_id: 2606.03992v1
authors: Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch
published: 2026-06-02
categories: cs.CV, cs.RO
---

# Exploring Easy Boosts for Lidar Semantic Scene Completion

**Authors:** Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch
**Published:** 2026-06-02
**arXiv:** https://arxiv.org/abs/2606.03992v1
**Categories:** cs.CV, cs.RO

## Abstract

This paper investigates "free lunch" strategies to boost the performance of lidar semantic scene completion (SSC) without requiring complex architectural redesigns. We first demonstrate that endowing input point clouds with semantic pseudo-labels from off-the-shelf segmentors significantly improves the performance of existing architectures. By evaluating these models against an oracle, we establish that high-quality semantic priors are a primary driver of mIoU gains. Furthermore, we equip the input lidar scan with visibility information that distinguishes between empty and unknown spaces, which provides a secondary performance boost across the tested architectures. Using these simple enhancements, we observe that older models remain competitive with state-of-the-art systems, and can even outperform them. Our code is available at https://github.com/astra-vision/SSC-Priors.
