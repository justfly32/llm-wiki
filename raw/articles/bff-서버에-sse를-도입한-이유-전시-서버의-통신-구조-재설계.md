---
title: "BFF 서버에 SSE를 도입한 이유: 전시 서버의 통신 구조 재설계"
source: 우아한형제들 Tech
url: https://techblog.woowahan.com/26507/
date: 2026-07-28
lang: ko
type: reference
tags: [feed, 우아한형제들-tech]
---

# BFF 서버에 SSE를 도입한 이유: 전시 서버의 통신 구조 재설계

> Source: [우아한형제들 Tech](https://techblog.woowahan.com/26507/)  
> Date: 2026-07-28

들어가며 배달의민족에서 음식을 주문할 때 카테고리를 누르면 만나는 화면, 바로 가게목록입니다. 사용자가 가게를 탐색하는 첫 관문이자, 가장 트래픽이 많은 지면 중 하나입니다. 이 글은 그 가게목록 지면의 통신 구조를 재설계한 이야기입니다. 클라이언트가 여러 서버에 각각 요청을 보내던 구조를 하나의 API로 통합하고(1지면 1API), 통합이 만들어낼 병목을 SSE(Server-Sent Events) 스트리밍으로 풀어낸 두 번의 의사결정 과정을 소개합니다. &#8216;가게목록&#8217;이 [&#8230;]
The post BFF 

---
*전문 보기: [BFF 서버에 SSE를 도입한 이유: 전시 서버의 통신 구조 재설계](https://techblog.woowahan.com/26507/)*