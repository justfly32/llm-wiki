---
title: Program-as-Weights: A Programming Paradigm for Fuzzy Functions
created: 2026-07-06
updated: 2026-07-06
type: concept
tags: [research, ai-ml, programming, optimization]
sources: [raw/papers/program-as-weights-a-programming-paradigm-for-fuzzy-functio-2026-07-06.md]
confidence: medium
---

# Program-as-Weights: A Programming Paradigm for Fuzzy Functions

> 📄 원문: [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](https://arxiv.org/abs/2607.02512v1)
> ✍️ 저자: Wentao Zhang, Liliana Hotsko, Woojeong Kim
> 📅 발행: 2026-07-02
> 🏷️ 카테고리: cs.LG, cs.AI, cs.CL

## 요약

Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (PAW), in which a 4B compiler trained on FuzzyBench, a 10M-example dataset we release, emits parameter-efficient adapters for a frozen, lightweight interpreter. A 0.6B Qwen3 interpreter executing PAW programs matches the performance of direct prompting of Qwen3-32B, while using roughly one fiftieth of the inference memory and running at 30 tokens/s on a MacBook M3. PAW reframes the foundation model from a per-input problem solver into a tool builder: invoked once per function definition, it produces a small reusable artifact whose subsequent calls per function application are cheap and offline.

## 원문 영어

<details>
<summary>원문 보기</summary>

Many everyday programming tasks resist clean rule-based implementation, such as alerting on important log lines, repairing malformed JSON, or ranking search results by intent, and are increasingly outsourced to large language model APIs at the cost of locality, reproducibility, and price. We propose fuzzy-function programming: compiling such a function from a natural-language specification into a compact, locally-executable neural artifact. We instantiate this paradigm with Program-as-Weights (P

</details>

## 관련

- [arXiv 원문 보기](https://arxiv.org/abs/2607.02512v1)
