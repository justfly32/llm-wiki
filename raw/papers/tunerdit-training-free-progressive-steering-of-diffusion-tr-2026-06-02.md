---
source_url: https://arxiv.org/abs/2605.31590v1
ingested: 2026-06-02
type: paper
arxiv_id: 2605.31590v1
authors: Ruotong Liao, Guowen Huang, Qing Cheng
published: 2026-05-29
categories: cs.CV, cs.AI
---

# TunerDiT: Training-free Progressive Steering of Diffusion Transformer for Multi-Event Video Generation

**Authors:** Ruotong Liao, Guowen Huang, Qing Cheng
**Published:** 2026-05-29
**arXiv:** https://arxiv.org/abs/2605.31590v1
**Categories:** cs.CV, cs.AI

## Abstract

Text-to-video (T2V) generation faces challenging questions when generating videos with long horizons containing multiple events. Inspired by the intrinsics of the diffusion process, we probe video diffusion transformers (DiTs) and uncover intrinsic turning points in the DiT denoising trajectory where conditioning text affects generation from global layout to fine-grained details. Building on this finding, we present TunerDiT, a simple yet effective progressive steering method that requires no additional training for multi-event generation. TunerDiT comprises two steering handles: (1) Event-Partitioned Masking that enforces event boundaries while allowing cross-event transition bands; (2) Cross-Event Prompt Fusion that injects neighboring event semantics for late-stage refinement. We contribute a self-curated prompt suite for benchmarking multi-event generation, i.e., Meve. TunerDiT achieves state-of-the-art performance across 8 metrics and offers a tunable trade-off between video consistency and event separation, compared with other training-free methods. The improvement in text alignment increases with the event count, indicating a scaling possibility with increasing event count.
