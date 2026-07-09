---
title: Co-LMLM: Continuous-Query Limited Memory Language Models
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [research, ai-ml]
sources: [raw/papers/co-lmlm-continuous-query-limited-memory-language-models-2026-07-10.md]
confidence: medium
---

# Co-LMLM: Continuous-Query Limited Memory Language Models

> 📄 원문: [Co-LMLM: Continuous-Query Limited Memory Language Models](https://arxiv.org/abs/2607.07707v1)
> ✍️ 저자: Yair Feldman, Linxi Zhao, Nathan Godey
> 📅 발행: 2026-07-08
> 🏷️ 카테고리: cs.CL, cs.AI, cs.LG

## 요약

Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant departure from prior reliance on relational KB and queries. CO-LMLM generates flexible vector queries at minimal cost, while still integrating human-readable and attributable retrieved knowledge into its generation. We pair this design with an annotation pipeline that tags free-form factual spans in arbitrary text, removing prior work's restriction to Wikipedia. Across pretraining on Wikipedia and FineWeb-Edu and at multiple model scales, CO-LMLM outperforms prior LMLMs and vanilla LLMs in both perplexity and factual precision. At 360M scale, this includes lower perplexity than models pretrained on 40x more data, and SimpleQA-verified performance that is in line with gpt-4o-mini and higher than Claude Sonnet 4.5.

## 원문 영어

<details>
<summary>원문 보기</summary>

Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant 

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.07707v1)
