---
source_url: https://arxiv.org/abs/2606.06470v1
ingested: 2026-06-08
type: paper
arxiv_id: 2606.06470v1
authors: Senmiao Wang, Tiantian Fang, Haoran Zhang
published: 2026-06-04
categories: cs.LG, cs.AI
---

# PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training

**Authors:** Senmiao Wang, Tiantian Fang, Haoran Zhang
**Published:** 2026-06-04
**arXiv:** https://arxiv.org/abs/2606.06470v1
**Categories:** cs.LG, cs.AI

## Abstract

We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training. The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning. After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead. We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-training, for both the AdamW and Muon optimizers. Theoretically, we justify this spectrum-control principle by proving that uniformly bounding each layer's singular values ensures geometric convergence of gradient descent to global minima, for certain deep linear networks. Our code is available at https://github.com/Empath-aln/PC-layer.
