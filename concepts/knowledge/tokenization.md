---
title: Tokenization (BPE, WordPiece, SentencePiece)
created: 2026-06-30
updated: 2026-06-30
type: knowledge
tags: [tokenization, tokenizer, bpe, wordpiece, sentencepiece, llm, nlp]
links: [[transformer-architecture]], [[positional-encoding]]
---

# Tokenization

> **Tokenization**은 텍스트를 모델이 처리할 수 있는 **토큰(token)** 단위로 분할하는 과정입니다.
> LLM의 첫 번째이자 가장 중요한 전처리 단계로, 토크나이저의 품질이 모델 성능에 직접적인 영향을 미칩니다.

## 개요: 텍스트 → 토큰 → ID

```
"나는 학교에 간다"
    │
    ▼ Tokenization
    │
["나는", "학교", "에", "간다"] 또는 ["나", "는", "학교", "에", "간", "다"]
    │
    ▼ Vocabulary Lookup
    │
[342, 7891, 56, 1203] ← Token IDs
```

## Tokenizer의 세 가지 유형

### 1. Word-level Tokenizer

가장 직관적인 방식: **띄어쓰기와 구두점 기준**으로 분할.

```
"Hello, world!" → ["Hello", ",", "world", "!"]
```

| 장점 | 단점 |
|------|------|
| 해석이 직관적 | **OOV (Out-of-Vocabulary)** 문제 |
| 구현 단순 | 한국어, 중국어 등 형태소 분석 어려움 |
| | 어근/접사 같은 하위 단어 정보 손실 |
| | 매우 큰 Vocabulary 필요 (수십만) |

### 2. Character-level Tokenizer

각 문자를 하나의 토큰으로 처리.

```
"Hello" → ["H", "e", "l", "l", "o"]
```

| 장점 | 단점 |
|------|------|
| OOV 문제 없음 | **시퀀스가 너무 김** (10-20배) |
| 모든 언어 처리 가능 | 계산 비용 증가 |
| | 개별 문자만으로는 의미 파악 어려움 |

### 3. Subword Tokenizer (현대 표준)

단어와 문자 사이의 **최적점**을 찾는 방식.

```
"unbelievable" → ["un", "believ", "able"]  (BPE)
"playing"      → ["play", "ing"]           (WordPiece)
```

**현대 LLM은 모두 Subword Tokenizer를 사용합니다.**

## BPE (Byte-Pair Encoding)

### 알고리즘

GPT 시리즈에서 사용하는 가장 대표적인 Subword Tokenization 알고리즘입니다.

```python
# 1. 모든 문자를 초기 Vocabulary로 시작
vocab = {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# 2. 가장 빈번한 쌍(pair)을 반복적으로 병합
while len(vocab) < target_size:
    # 가장 많이 등장하는 인접 문자 쌍 찾기
    most_frequent_pair = find_most_frequent_pair(corpus)
    # 해당 쌍을 하나의 새로운 토큰으로 병합
    merge(most_frequent_pair)
    vocab.add(most_frequent_pair)

# 3. 최종 Vocabulary: 자주 등장하는 Subword 단위들의 집합
```

### BPE 예시

```
학습: "low", "lower", "lowest", "new", "newer", "newest"

Step 1: 'e' + 'r' → 'er' (3회 등장)
Step 2: 'er' + 's' → 'ers' (2회 등장)
Step 3: 'low' + 'er' → 'lower' (2회 등장)
...

결과 Vocabulary: 'low', 'er', 'est', 'new', 'lower', 'newer', 'newest', 'l', 'o', 'w', ...

=> "lowers" → ['low', 'er', 's']  # OOV 없이 처리 가능!
```

### BPE 사용 모델

- **GPT-2, GPT-3, GPT-4**: Byte-level BPE (문자가 아닌 바이트 단위)
- **RoBERTa**
- **LLaMA**: SentencePiece (BPE 기반)

## WordPiece

### 특징

BERT에서 사용한 Subword 알고리즘. BPE와 유사하지만 **병합 기준이 다릅니다**.

| 알고리즘 | 병합 기준 |
|----------|-----------|
| BPE | **최대 빈도수** 쌍 병합 |
| WordPiece | **우도 증가량**이 가장 큰 쌍 병합 |

### WordPiece 기준

$$ \text{score}(a, b) = \frac{\text{count}(ab)}{\text{count}(a) \times \text{count}(b)} $$

- 분자: 두 subword가 함께 등장하는 빈도
- 분모: 각각 등장하는 빈도의 곱
- **함께 등장할 확률이 높은 쌍을 병합**

### WordPiece 사용 모델

- **BERT**
- **DistilBERT**
- **ELECTRA**

## SentencePiece (Unigram LM)

### 특징

Google이 개발한 **언어에 독립적인** Subword Tokenizer.

| 특징 | 설명 |
|------|------|
| **Raw Text 입력** | 사전 토큰화(띄어쓰기 등)가 필요 없음 |
| **언어 무관** | 한국어, 중국어, 일본어도 동일하게 처리 |
| **바이트 수준** | 모든 텍스트를 UTF-8 바이트로 처리 |

### 알고리즘 (Unigram LM 기반)

```python
# 1. 과도하게 큰 Seed Vocabulary로 시작 (모든 가능한 Subword)
vocab = initialize_seed_vocabulary(corpus)

# 2. 각 Subword의 중요도(우도 손실) 계산
for subword in vocab:
    loss = compute_likelihood_loss(subword, corpus)
    
# 3. 중요도가 낮은 Subword 제거
while len(vocab) > target_size:
    least_important = argmin(loss, vocab)
    vocab.remove(least_important)
    loss = update_loss(vocab)

# 4. 최종 Vocabulary: 가장 유용한 Subword 집합
```

### SentencePiece 사용 모델

- **LLaMA 1/2/3**
- **Mistral / Mixtral**
- **Gemma**
- **T5**
- **XLNet**

## Vocabulary 크기 비교

| 모델 | Tokenizer | Vocabulary 크기 |
|------|-----------|-----------------|
| GPT-2 | Byte-level BPE | 50,257 |
| GPT-3 | Byte-level BPE | 50,257 |
| BERT | WordPiece | 30,000 |
| LLaMA 1 | SentencePiece | 32,000 |
| LLaMA 2 | SentencePiece | 32,000 |
| LLaMA 3 | SentencePiece (개선) | **128,000** |
| Mistral | SentencePiece | 32,000 |
| GPT-4 | Byte-level BPE (개선) | ~100,000 (추정) |
| Claude 3 | 자체 Tokenizer | ~100,000 (추정) |

> **트렌드**: Vocabulary 크기가 점점 커지는 추세 → 더 적은 토큰으로 더 많은 정보 표현 가능

## 한국어 Tokenization의 특수성

한국어는 **교착어**로서 Tokenization이 특히 까다롭습니다.

### 문제점

| 특성 | 설명 | 예시 |
|------|------|------|
| **조사/어미 분리** | 단어 뒤에 붙는 다양한 조사 | "학교가", "학교를", "학교로" |
| **띄어쓰기 불일치** | 구어체에서 띄어쓰기 자주 생략 | "학교에간다" |
| **합성어** | 여러 단어가 합쳐짐 | "학교종이땡땡땡" |
| **의존명사** | 앞말과 띄어쓰지만 하나의 의미 | "할 수 있다" |

### 한국어 토크나이저 비교

| 모델 | 토크나이저 | 한국어 효율 |
|------|-----------|------------|
| GPT-4 | BPE (개선) | 좋음 (충분한 한국어 학습) |
| LLaMA 3 | SentencePiece 128K | **매우 좋음** |
| Polyglot-Ko | SentencePiece (한국어 최적화) | 최고 |
| EXAONE | 자체 한국어 토크나이저 | 최고 |
| LLaMA 2 | SentencePiece 32K | **낮음** (한국어 토큰 비효율) |

### 한국어 토큰 비효율 예시

```
"나는 학교에 간다" (영문 15자)

LLaMA 2:   ["나는", "학교", "에", "간", "다"] = 5 토큰  ← 비효율
LLaMA 3:   ["나는", "학교에", "간다"] = 3 토큰  ← 효율적
GPT-4:     ["나는", " 학교", "에", " 간다"] = 4 토큰  ← 중간
```

## Tokenizer가 모델 성능에 미치는 영향

| 요소 | 영향 |
|------|------|
| **Vocabulary 크기** | 크면 적은 토큰으로 표현 가능,但 임베딩 메모리 증가 |
| **언어 커버리지** | 특정 언어의 토큰화 효율이 해당 언어 성능에 직접 영향 |
| **숫자/코드 처리** | 숫자나 코드를 얼마나 잘 토큰화하는지 |
| **특수 문자** | 이모지, 특수 기호 처리 방식 |

## 참고

- [BPE 논문: Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909)
- [SentencePiece 논문](https://arxiv.org/abs/1808.06226)
- [[transformer-architecture]]: Transformer 전체 구조
- [[positional-encoding]]: Positional Encoding
