---
title: CUDA 커널을 실행하면 어떤 일이 발생하는가?
created: 2026-06-30
updated: 2026-06-30
type: concept
tags: [news]
sources: [raw/articles/hn-what-happens-when-you-run-a-cuda-kernel-2026-06-30.md]
confidence: medium
source_type: hn
---

# CUDA 커널을 실행하면 어떤 일이 발생하는가?

> 📰 원문: [What happens when you run a CUDA kernel?](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/)
> 🔥 HN Score: 188 | By: mezark | 💬 Comments: 22
> 🔗 HN Discussion: https://news.ycombinator.com/item?id=48718863

## 요약

CUDA 커널을 실행하면 어떻게 되는가 블로그 글 소개 *:hover]:brightness-75 md:opacity-80 [&#38;>*]:cursor-pointer" data-astro-cid-lgn464si> 블로그 글 소개 *:hover]:brightness-75 md:opacity-80 [&#38;>*]:cursor-pointer" data-astro-cid-lgn464si> 이 페이지에서 다루는 내용 nvcc로 프로그램 컴파일하기 호스트가 GPU를 실행하는 방법 GPU로 이동하기 명령어 단위로 살펴보기 워프(warp)가 실행 가능해진다는 것의 의미 데이터 로드하기 CPU로 돌아가기 전체 경록 부록: 런치 내부를 들여다보는 방법 인터포지션 훅(Interposition hook) 푸시버퍼 커맨드 스트림

## 원문 영어

<details>
<summary>원문 보기</summary>

What happens when you run a CUDA kernel Blog Talks About *:hover]:brightness-75 md:opacity-80 [&#38;>*]:cursor-pointer" data-astro-cid-lgn464si> Blog Talks About *:hover]:brightness-75 md:opacity-80 [&#38;>*]:cursor-pointer" data-astro-cid-lgn464si> On This Page Compiling our program with nvcc How the host triggers the GPU Getting it onto the GPU Instruction by instruction What does it mean for a warp to be eligible? Loading the data Back to the CPU The whole path Appendix: how to look inside th

</details>

## HN 토론

- [HN 댓글 보기](https://news.ycombinator.com/item?id=48718863)
- [원문 기사 읽기](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/)
