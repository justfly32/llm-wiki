---
source_url: https://arxiv.org/abs/2605.31597v1
ingested: 2026-06-01
type: paper
arxiv_id: 2605.31597v1
authors: Olaf Dünkel, Basavaraj Sunagad, Haoran Wang
published: 2026-05-29
categories: cs.CV
---

# SOCO: Benchmarking Semantic Object Correspondence in Vision Foundation Models

**Authors:** Olaf Dünkel, Basavaraj Sunagad, Haoran Wang
**Published:** 2026-05-29
**arXiv:** https://arxiv.org/abs/2605.31597v1
**Categories:** cs.CV

## Abstract

Measuring structured object understanding in vision foundation models remains challenging due to inconsistent evaluation protocols and limited part-level supervision. Semantic correspondence (SC) evaluates this capability by testing whether object parts can be matched across instances and categories under large variations in appearance, viewpoint, and geometry. To enable a systematic SC evaluation, we introduce SOCO, a new benchmark for Semantic Object Correspondence that introduces a taxonomy of correspondence types and provides consistent, functionally meaningful keypoint annotations across 100 categories and over 1M correspondence pairs. In addition, SOCO includes keypoint language descriptions, enabling the evaluation of large vision-language models (LVLMs) and their fine-grained part-level understanding. Comprehensive experiments reveal that (i) vision foundation backbones encode strong semantic structure but transfer correspondences poorly across related categories and only partially capture object-part position, (ii) LVLMs are stronger at text-prompted part localization than at visual-reference cross-image matching, exposing a gap between language-grounded localization and fine-grained visual correspondence, and (iii) correspondence performance predicts performance on dense downstream tasks, including segmentation, tracking, 3D pose estimation, and 3D detection, more strongly than ImageNet classification. Together, these findings position SOCO as a benchmark for structured, part-level representation quality in vision and multimodal foundation models.
