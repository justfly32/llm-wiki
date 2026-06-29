---
source_url: https://arxiv.org/abs/2606.28321v1
ingested: 2026-06-30
type: paper
arxiv_id: 2606.28321v1
authors: Jia-Chen Zhao, Beiqi Chen, Xinyang Chen
published: 2026-06-26
categories: cs.CV
---

# StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views

**Authors:** Jia-Chen Zhao, Beiqi Chen, Xinyang Chen
**Published:** 2026-06-26
**arXiv:** https://arxiv.org/abs/2606.28321v1
**Categories:** cs.CV

## Abstract

We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framework that operates directly on uncalibrated images without requiring camera parameters. Existing methods either rely on per-scene optimization or assume known camera poses, and often entangle geometry and appearance within a unified backbone, limiting reconstruction fidelity and generalization. Our key idea is to adopt a structured representation that organizes geometry, semantic, and texture cues with explicit roles in the reconstruction process. Specifically, we introduce a pixel-aligned feature injection mechanism to enable accurate texture modeling from 2D observations, incorporate semantic-aware priors to improve global consistency, and design a camera alignment strategy to prevent information leakage and improve generalization. Experiments show that our method significantly outperforms prior approaches on challenging benchmarks. On DL3DV, our method achieves 28.045 PSNR, surpassing AnySplat (22.377) by +5.67 dB. In cross-dataset evaluation, our method achieves +1.94 dB over AnySplat on ACID and +1.72 dB on RealEstate10K. Project page: https://structsplat.github.io Code: https://github.com/J-C-Zhao/StructSplat
