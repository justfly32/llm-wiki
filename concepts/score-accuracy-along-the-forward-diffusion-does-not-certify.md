---
title: Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability in Diffusion Sampling
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [research, ai-ml, diffusion]
sources: [raw/papers/score-accuracy-along-the-forward-diffusion-does-not-certify-2026-07-13.md]
confidence: medium
---

# Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability in Diffusion Sampling

> 📄 원문: [Score Accuracy Along the Forward Diffusion Does Not Certify Numerical Stability in Diffusion Sampling](https://arxiv.org/abs/2607.08757v1)
> ✍️ 저자: Yiwei Zhou
> 📅 발행: 2026-07-09
> 🏷️ 카테고리: stat.ML, cs.LG, math.NA

## 요약

Score matching controls average error under the forward marginals, but a discretized reverse-time sampler evaluates the learned score along its own trajectory. We show that small forward-marginal error does not guarantee numerical stability. We construct a single smooth score field with arbitrarily small forward-marginal $L^2$ error. The learned reverse-time process is nonexplosive, has moments of every order, and can be arbitrarily close to the exact reverse-time process in path-space total variation. Yet its Euler--Maruyama discretizations converge in probability while every positive moment diverges. Thus weak convergence can hold even though every Wasserstein distance $W_p$, $p\ge1$, diverges.   The same failure can occur within one fixed finite neural architecture. We construct a family of bounded, globally Lipschitz denoisers for which both the forward-marginal error and the path-space total variation distance tend to zero, while their Euler--Maruyama endpoints diverge in every $W_p$. For compactly supported data, we also give a simple positive result. Projecting the learned denoiser onto a known bounded closed convex set containing the support preserves pointwise accuracy, gives grid-uniform moment bounds, and yields Wasserstein convergence under mild local regularity. Experiments with a small fixed DiT-style network show large growth along rare numerical trajectories and its suppression by denoiser projection, while overall trajectory errors remain small.

## 원문 영어

<details>
<summary>원문 보기</summary>

Score matching controls average error under the forward marginals, but a discretized reverse-time sampler evaluates the learned score along its own trajectory. We show that small forward-marginal error does not guarantee numerical stability. We construct a single smooth score field with arbitrarily small forward-marginal $L^2$ error. The learned reverse-time process is nonexplosive, has moments of every order, and can be arbitrarily close to the exact reverse-time process in path-space total var

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.08757v1)
