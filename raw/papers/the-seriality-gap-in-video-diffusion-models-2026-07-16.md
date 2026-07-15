---
source_url: https://arxiv.org/abs/2607.13031v1
ingested: 2026-07-16
type: paper
arxiv_id: 2607.13031v1
authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu
published: 2026-07-14
categories: cs.LG, cs.CV
---

# The Seriality Gap in Video Diffusion Models

**Authors:** Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu
**Published:** 2026-07-14
**arXiv:** https://arxiv.org/abs/2607.13031v1
**Categories:** cs.LG, cs.CV

## Abstract

When one ball strikes another, then another, video models should predict the consequences of each bounce. In controlled experiments on multi-ball hard-sphere dynamics, we find that the performance of standard bidirectional video diffusion degrades as the causal chain lengthens, even when provided more denoising steps. In a length-matched single-ball control, where ball-ball interactions are absent, the degradation largely disappears, isolating dependent-event structure rather than video length as the cause. Across intervention studies, methods that increase effective serial computation improve performance disproportionately, including autoregressive/blockwise generation and architectural depth. We identify this pattern as the seriality gap: a mismatch between tasks requiring growing serial computation and video diffusion models whose denoising loop does not provide scalable serial compute. We then prove that, for deterministic video prediction, denoising steps do not add serial computation beyond the backbone, indicating a structural obstacle for video diffusion on serial reasoning and simulation tasks.
