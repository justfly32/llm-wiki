---
source_url: https://arxiv.org/abs/2607.02515v1
ingested: 2026-07-05
type: paper
arxiv_id: 2607.02515v1
authors: Haofei Xu, Rundi Wu, Philipp Henzler
published: 2026-07-02
categories: cs.CV
---

# PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

**Authors:** Haofei Xu, Rundi Wu, Philipp Henzler
**Published:** 2026-07-02
**arXiv:** https://arxiv.org/abs/2607.02515v1
**Categories:** cs.CV

## Abstract

State-of-the-art single-image 3D reconstruction methods often rely on complex hybrid architectures and loss functions, or compress geometry into latent spaces in order to leverage pre-trained latent diffusion models. In this work, we show that such architectural overhead and intricate loss formulations are unnecessary. We introduce a minimalist pixel-space Diffusion Transformer, built on a plain ViT, that operates directly on raw 3D point map patches and is conditioned on image tokens from a pre-trained DINOv3. Unlike existing latent diffusion approaches, we train our diffusion backbone entirely from scratch, eliminating the need for point map tokenizers. Despite its simplicity, our approach surpasses complex latent-based diffusion models while remaining significantly simpler than hybrid alternatives. Notably, it produces sharper geometric structure and is more robust in highly ambiguous regions, such as transparent objects.
