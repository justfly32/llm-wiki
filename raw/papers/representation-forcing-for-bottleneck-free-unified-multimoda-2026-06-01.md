---
source_url: https://arxiv.org/abs/2605.31604v1
ingested: 2026-06-01
type: paper
arxiv_id: 2605.31604v1
authors: Yuqing Wang, Zhijie Lin, Ceyuan Yang
published: 2026-05-29
categories: cs.CV
---

# Representation Forcing for Bottleneck-Free Unified Multimodal Models

**Authors:** Yuqing Wang, Zhijie Lin, Ceyuan Yang
**Published:** 2026-05-29
**arXiv:** https://arxiv.org/abs/2605.31604v1
**Categories:** cs.CV

## Abstract

Unified multimodal models (UMMs) aim to handle perception and generation in a single model. Yet existing UMMs still rely on a frozen, separately pretrained VAE for image generation, imposing a structural bottleneck. Naively removing it introduces a quality gap, as the model must learn both high-level structure and low-level details from raw pixels. In this paper, we propose Representation Forcing (RF), a technique that closes this gap by making representation prediction a native capability of the model. Concretely, RF forces the decoder to autoregressively predict visual representations as intermediate tokens before pixels; these tokens then stay in context to guide pixel diffusion within the same backbone. By turning representations from perception outputs into generation targets, RF eliminates the need for any external generative latent space. We find that RF benefits both understanding and generation. On image generation, our pixel-space model with RF matches state-of-the-art VAE-based unified models. On image understanding, pixel-space RF generally outperforms its VAE-based variant. Together, these results offer an effective step toward end-to-end, bottleneck-free UMMs.
