---
source_url: https://arxiv.org/abs/2607.08769v1
ingested: 2026-07-11
type: paper
arxiv_id: 2607.08769v1
authors: Weijian Chen, Weibo Yao, Yuhang Zhang
published: 2026-07-09
categories: cs.CV
---

# Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction

**Authors:** Weijian Chen, Weibo Yao, Yuhang Zhang
**Published:** 2026-07-09
**arXiv:** https://arxiv.org/abs/2607.08769v1
**Categories:** cs.CV

## Abstract

Scaling 3D Gaussian Splatting (3DGS) to large outdoor scenes is costly in both data acquisition and computation. Adopting panoramic images with equirectangular projection (ERP) can reduce capture effort via their full $360^{\circ}$ field of view, yet the resulting omnipresent visibility invalidates existing partitioning strategies that rely on local camera frustums, causing block-wise optimization to degenerate into global training. Thus, we propose PanoLOG, a two-stage coarse-to-fine framework equipped with a Geometry and Gradient-based Partitioning Strategy tailored for large-scale panoramic 3DGS reconstruction. In the global coarse stage, PanoLOG leverages sky-sphere modeling and panoramic monocular depth supervision for reliable geometry, while in the refinement stage, G$^2$PS builds adaptive bounding volumes via parallax-driven uncertainty and assigns cameras via gradient-based importance scoring. Furthermore, we construct Pano360, the first benchmark on large-scale panoramic dataset for outdoor scene reconstruction. Extensive experiments demonstrate that G$^2$PS achieves state-of-the-art rendering quality while maintaining scalable, block-parallel training. Our models, training code, and dataset are publicly available.
