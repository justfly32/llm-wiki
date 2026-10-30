## [2026-10-31] daily-sync | 인덱스 +113/+34, 레지스트리 46개 폴더, 크론 에러 0건, 작업 변경 921개
- 인덱스: 신규 113 / 갱신 34 (텍스트 없음 스킵 1), 총 13,887개 (FTS 13,887, 원본합계 3,104.4MB). 루트별 projects 11,254 / hermes 2,096 / documents 348 / wiki 189. 전일 13,779 대비 +108(prune 5행). index.db 582.6MiB(실측 610.9MB), 전일 581.6MiB 대비 +1.0MiB
- 레지스트리: 46개 폴더 (git 19 / 로컬 27) — 신규·제거 0 (diff는 날짜·커밋수 갱신뿐, `k-shorts-automaker` 239→636파일)
- 크론 에러 24h 0건 — 4일 연속 안정. 96h 6건은 전량 10-27~10-28 HTTP 410(모델 폐기) 기분석, 신규 0. 게이트웨이 10-25 22:03 기동 후 127.5시간 무결, 마지막 RecursionError 10-20. 자기 job 헤더 직접 확인 → FAILED 아님
- 작업 변경 921개 (요약 182, AppleDouble 0): k-shorts-automaker 77 (AI 해외화제 ai04~ai10 7편 조립·`build_ai.py` 스펙 정본화·발행큐 AI06 11-01/AI10 11-02 예약, 커밋 0), my-media-agent 68 (심해 애니판30 Aoede 나레이션 전면 교체 + whisper 정렬 + 묶음01·07·08·09 재조립, 01~06 업로드 검증·01~04 replaced, 캐릭터시트_그레이니트남 동작5종, BGM 6→50곡, 미커밋 372), lotto 2, auto-trading 2, post1 1 / git 커밋 3개 저장소 (post1 fa15322, skills f43381b, memories 0734891)
- daily 페이지: concepts/daily/2026-10-31.md 생성
- captures 83.2% (3,786행·352.3MB / 전체 423.4MB, 전일 369.4MB에서 −17.1MB) — 색인 제외 승인 대기 유지

## [2026-10-30] daily-sync | 인덱스 +230/+29, 레지스트리 46개 폴더, 크론 에러 0건, 작업 변경 697개
- 인덱스: 신규 230 / 갱신 29 (텍스트 없음 스킵 12), 총 13,779개 (FTS 13,779, 원본합계 3,103.8MB). 루트별 hermes 2,091 / projects 11,154 / documents 346 / wiki 188. index.db 581.6MiB(609.9MB), 전일 580.2MiB 대비 +1.4MiB
- 레지스트리: 46개 폴더 (git 19 / 로컬 27) — 신규 1개 `k-shorts-automaker` (K-shorts 반응형 자동 파이프라인 골격, 커밋 0)
- 크론 에러 24h 0건 — 3일 연속 안정. 96h 6건은 전량 10-27~10-28 HTTP 410(모델 폐기) 기분석, 신규 0
- 작업 변경 697개 (요약 292, AppleDouble 0): my-media-agent 212 (동화법률 ep17_놀부전 최종마스터 28M·ep18_도깨비감투 A안 확정·최종 34M·stage 빌드 스크립트 12종·video_qa_gate/fc_preflight 보강, 미커밋 360), k-shorts-automaker 51, auto-trading 2, post1 1 / git 커밋 3개 저장소 (post1 5f05d9d, skills 4af7188, memories f2aeab0)
- daily 페이지: concepts/daily/2026-10-30.md 생성
- captures 83.3% (3,786행·369.4MB / 전체 443.4MB) — 색인 제외 승인 대기 유지

## [2026-10-29] daily-sync | 인덱스 +495/+125, 레지스트리 45개 폴더 (신규 html-slides 1 · 제거 windfriend-archive), 크론 에러 3건(전부 HTTP 410 모델 폐기·교체로 해소), 작업 변경 1,638개(이틀치·요약 723)
- 인덱스: 신규 495 / 갱신 125 (텍스트 없음 스킵 89), 총 13,549개 (원본 합계 3,102.8MB / index.db 580.2MiB·실측 608.4MB). 루트별 projects 10,933 / hermes 2,086 / documents 344 / wiki 186.
  - 전일 15,490 대비 **−1,941** — projects 12,894 → 10,933(−1,961). 신규 495 유입에도 순감한 것은 **prune_missing 고아 정리** 때문(10-27 `_raw`·구버전 렌더 **외장 이관 8.30GB** + archive 정리 반영). 버그 아님.
  - **index.db 596.0 → 580.2MiB (−15.8MiB)** — 600MiB 라인 아래 유지. VACUUM 회수가 신규 유입분보다 큼.
  - `car-year-lookup/captures` **3,786행 / 본문 369.4M자 = 전체 본문 442.6M자의 83.5%** → 색인 제외는 **계속 승인 대기**(크론은 정책 변경 안 함).
  - **AppleDouble `._*` 123행이 색인에 잔존**(10-28 대량 복사 부산물) — `._*` 제외도 승인 대기 후보.
- 레지스트리: **45개 폴더 (git 19 / 로컬 26)** — 신규 **`html-slides`**(~/projects, 10-28 reports/out 14파일), 제거 **`windfriend-archive`**.
- 크론 에러: 최근 24h **3건 — 전부 2026-10-28 06:00 `HTTP 410: Model deepseek-v4-flash has been deprecated.`**(Daily World News Report · Wiki Git Backup · Update personal site timestamp). 같은 원인으로 전일 05:30 **이 job 자신도 FAILED** → 10-28 daily 페이지 누락분 오늘 복원. 세 job이 같은 분에 동일 메시지로 실패 = 업스트림 모델 폐기 단일 원인(로컬 스크립트 아님). **전역 모델 `deepseek-v4.1-flash` 교체로 해소 확인**(오늘 전 실행 정상). 410은 재시도 무효 유형. **남은 리스크: `fallback_providers`가 구형 `deepseek/deepseek-v4-flash-0731`(openrouter) 지목 → 교체 승인 대기**. 게이트웨이 10-25 22:03:07 기동 후 **79.5시간 무결**, RecursionError 없음, 예방 재시작 11-01 전후.
- 작업 변경: 창이 **이틀치**(10-27 05:30~10-29 05:30, 전일 실패) — 원본 1,638 / 요약 723, 그중 AppleDouble `._*` **147개 노이즈**(실변경 576). **my-media-agent**(10-27 314 + 10-28 163 + 10-29 9): **법률 시리즈 4개를 `series/법률/`로 통합 + fcproj·스크립트 경로 일괄 치환**(`8c16ea8`), **운전자보험 20컷 최종 3연작**(`dea5fa8` 여명준 애니 아바타판 → `b5b3a49` 제목카드+아바타C+엔드카드 → `ca1818f` 효과음·자막·상반신), **발음 위험 검수기 신설 — TTS 대사 사전 점검 + ASR 역검수**(`c671ae0`), `웃기는-변호사` 시즌1 설계(세계관·아크·시놉-대사·연출계획·EP01~시즌1 대본) + `ep01_fc` FilmCraft 착수, 심해 30편 `_raw`·구버전 렌더 외장 이관(8.30GB) + BGM 10곡 교체, ep16 「벌거벗은 임금님」 기획·앵커 생성(`gen_ep16_anchors.py`), `docs/외장-아카이브-인덱스.{md,json}`·`docs/동화법률-신규3편-기획안.md`, 스킬 3건 개정(media-asset-retention·ai-video-voice-delivery·anime-series-filmcraft-structure). post1 1(`ea1d760`), html-slides 신규 14, craft-clis 11(filmcraft-cli 0.13.0 배포본), auto-trading state 2(커밋 없음), skills·memories 백업 각 2 / git 커밋 4개 저장소 15건.
- daily 페이지: concepts/daily/2026-10-29.md · **2026-10-28.md(복원)** 생성.

## [2026-10-27] daily-sync | 인덱스 +1177/+56, 레지스트리 45개 폴더 (변동 없음 — 신규 0, 5일 연속), 크론 에러 24h·96h 0건, 작업 변경 1291개
- 인덱스: 신규 1177 / 갱신 56 (텍스트 없음 스킵 7), 총 15,490개 (원본 합계 3,296.1MB / index.db 596.0MB). 루트별 projects 12,894 / hermes 2,071 / documents 340 / wiki 185.
  - 전일 14,313 대비 **+1,177 순증** — 고아 정리(prune) 감소 없이 신규 유입분이 그대로 반영. 프로젝트 대부분은 my-media-agent(심해 애니판 ep13~ep30 신규 + 영상/이미지/config).
  - **index.db 590.8MB → 596.0MB (+5.2MB)** — 신규 1,177행 대량 유입에도 **600MB 라인 아래 유지**. 신규분 다수가 바이너리(mp4/wav)·config(json)라 본문이 작았고 prune+FTS 병합+VACUUM이 회수.
  - `car-year-lookup/captures` **3,786행 / 본문 352.3MB = 전체 본문 431.7MB의 81.6%**(디스크 1.9GB) → 제외하면 200MB대지만 **정책 변경이라 승인 대기 유지**(크론은 손대지 않음). DB가 600MB를 재돌파하면 기록만 한다.
  - 원본 합계 +179.4MB(3,116.7→3,296.1MB)의 대부분은 심해 애니판 렌더·이미지·백업 — 바이너리는 본문 미추출이라 DB 영향 미미.
- 레지스트리: **45개 폴더 (git 19 / 로컬 26) — 신규 0** (5일 연속 변동 없음).
- 크론 에러: 최근 24h **0건**, 96시간 **0건**. 게이트웨이 **10-25 22:03:07 재시작 후 31시간 27분 FAILED 0건**, `RecursionError` 재발 없음. 다음 예방 재시작 권장 **11-01 전후**. 자기 job 제외 규칙 때문에 최신 실행 파일 헤더를 직접 확인(10-26_05-33-21.md 정상 종료, FAILED 마커 없음).
- 작업 변경 1,291개(원본 2,691): **my-media-agent 1,247 · 커밋 38건 · 미커밋 1 — 🎉 심해 애니판 30편 완결**(묶음 3편×10묶음). ffmpeg 파이프라인 → **FilmCraft 프로젝트 재구축**(묶음 01·02·03 규격 이식), 프리미어 예능 자막 4기법 → FilmCraft 구현 검증 + 자막 고급 3기법(트래킹·닦아내기·지진), **사고 3건 원인 규명 + 재발 방지**(캐릭터 고정 3중 방지 11:56 · 재생성본 무시 → old-source 격리 규칙 13:07 · 카드 안 바뀜 → 공용 스크립트 15:24), **배치 게이트 — 첫 1개 검수 통과해야 나머지 생성**(13:29, 사용자 지시), 자막 깜빡임 해결(FilmCraft time 프레임 내림 보정), 묶음 02(151.82초)·03(156.52초) 게이트 16/16 PASS, 묶음 04(EP10~12 침묵)·05(EP13~15 대면)·06(EP16~18 귀환)·07(EP19~21 봉인)·**묶음 08·09·10(EP22~30) 완결(02:29)**, 기술 정리 + 스킬 재구성·외장 이관. 유료 실측: 이미지 29컷 $0.576 + 인물 일관성 $0.36(승인 게이트 경유). post1 1(`a8c4c04`), auto-trading state 2(커밋 없음), skills·memories 각 1 백업.
- daily 페이지: concepts/daily/2026-10-27.md 생성.

## [2026-10-26] daily-sync | 인덱스 +745/+103, 레지스트리 45개 폴더 (변동 없음 — 신규 0, 4일 연속), 크론 에러 24h·96h 0건 (게이트웨이 10-25 22:03 재시작 후 7.5시간 무결), 작업 변경 701개
- 인덱스: 신규 745 / 갱신 103 (텍스트 없음 스킵 2,016), 총 14,313개 (원본 합계 3,116.7MB / index.db 590.8MB 실측). 루트별 projects 11,741 / hermes 2,051 / documents 337 / wiki 184.
  - 전일 13,877 대비 **+436 순증** — 신규 745에서 **고아 정리(prune) 약 309행 감소**가 반영. hermes 루트는 2,134→2,051(**−83**, 캐시·프로필 잔여 정리), projects는 11,223→11,741(+518).
  - **index.db 616.1MB → 590.8MB (−25.3MB)** — prune + FTS 병합 + VACUUM이 신규 유입분보다 크게 회수해 **600MB 라인 아래로 복귀**.
  - `car-year-lookup/captures` **3,786행 / 본문 352.3MB = 전체 본문 429.2MB의 82.1%**(디스크 1.9GB) → 제외하면 200MB대지만 **정책 변경이라 승인 대기 유지**(크론은 손대지 않음). DB가 600MB를 재돌파하면 기록만 한다.
  - 원본 합계 +114.9MB의 대부분은 **법률숏츠 렌더·백업 mp4/wav**(`v4b_final.mp4` 98MB, `v11_full.mp4` 57MB ×2 백업 폴더) — 바이너리는 본문 미추출이라 DB 영향 미미.
- 레지스트리: **45개 폴더 (git 19 / 로컬 26) — 신규 0** (4일 연속 변동 없음).
- 크론 에러: 최근 24h **0건**, 96시간 **0건**. 게이트웨이는 **10-25 22:03:07 재시작**(전일 권장일 10-27을 하루 앞당겨 이행) → 재시작 후 **7시간 27분 FAILED 0건**, `RecursionError` 재발 없음. 다음 예방 재시작 권장 **11-01 전후**. 자기 job 제외 규칙 때문에 최신 실행 파일 헤더를 직접 확인(정상 종료, FAILED 마커 없음).
- 작업 변경 701개(원본 1,215): **my-media-agent 610 · 커밋 58건 · 미커밋 0** — "표준을 코드로 고정"의 날. FilmCraft 사고 3건 원인 확정 + `fc_gate` 게이트 신설, **BGM 3중 원인 규명 + 게이트에 음량·간격 검사**, 제작 표준 과정 확립(검증을 문서→코드), 연출 설계서 `direction_sheet` 표준 양식 + 스티커 자동 배치 + BGM 덕킹, 납품 체크리스트 제정, 시네마틱 템플릿 확정(BGM 페이드아웃·엔드카드 직행·제목카드 문구 가변·아바타구간 −12dB·30MB), **BGM 라이브러리 신설 — Lyria 3 Pro 유료 6곡**, **떼인 돈 회수 3단계 광고법 통과판 시네마틱 57.00초 완성**, 캐릭터 표정·동작 5종(원본 사진 레퍼런스 + seed 고정), **폴더 구조 정리 최상위 105→21개**(사전 스냅샷 커밋) + `archive_media` 외장 이관 + `find_archived.py`, 검수 스튜디오 개편(최종본 기준 `series/<시리즈>/**/final/*.mp4` 통일·다중 선택 삭제·`ep['dir']` KeyError 500 수정·wcwidth 상태줄), `sfx_extract + variety_gfx` / skills **160→145→134개 감축**(2커밋+백업 1) · memories 1(post1 1: `faa9382`) · auto-trading state 1(커밋 없음).
- daily 페이지: concepts/daily/2026-10-26.md 생성.

## [2026-10-25] daily-sync | 인덱스 +316/+60, 레지스트리 45개 폴더 (변동 없음 — 신규 0, 3일 연속), 크론 에러 24h 0건 (게이트웨이 10-24 07:03 재시작 후 22.5시간 무결), 작업 변경 494개
- 인덱스: 신규 316 / 갱신 60 (텍스트 없음 스킵 3), 총 13,877개 (원본 합계 3,001.8MB / index.db 587.6MiB·실측 616.1MB). 루트별 projects 11,223 / hermes 2,134 / documents 337 / wiki 183.
  - 전일 13,994 대비 **−117** — 신규 316보다 **고아 정리(prune) 감소분이 큰 순감**. 특히 my-media-agent의 `_구버전`·재렌더 임시물 정리가 반영. index.db 586.2→587.6MiB(+1.4MB).
  - `car-year-lookup/captures` **3,786행 / 본문 352.3MB = 전체 본문 427.7MB의 82.4%**(디스크 1.9GB) → 600MB 조건 **계속 초과**(616.1MB 실측). 제외 시 200MB대. **대표님 승인 대기**(크론은 정책 변경 안 함).
- 레지스트리: **45개 폴더 (git 19 / 로컬 26) — 신규 0** (3일 연속 변동 없음).
- 크론 에러: 최근 24h **0건**. 게이트웨이 가동은 **10-24 07:03 재시작 기준 22시간 28분 FAILED 0건**(전일 기록의 "10-20 08:51 재기동"은 10-24 새벽 재기동으로 정정).
- 작업 변경 494개: **my-media-agent 434**(렌더 3편 완성 — `film01_정본.mp4` · `심해_애니홍보_1분.mp4`(129MB) · `토끼와거북이 시네마틱_최종.mp4`/`공유용30m.mp4`, film02 조립 도구 13종 + 클립 30여 컷 + `edit/전체구도_정본`·`타임라인_최종매핑`, 동화법률 **ep16 운전자보험_개미와베짱이** 옵션3 하이브리드(삽화+여명준 실사) 기획+조립, 법무법인에이블_운전자보험 쇼츠 편집 25 jsonl, `DECISIONS.md` 화면전환 8 dissolve/28 하드컷 확정, Avatar IV 컷9/27 자체음성 실패→`_구버전` 격리, **커밋 0 · 미커밋 437건**) · post1 1(`abc67b6`) · auto-trading 1(주간 매매 경과, bear 9거래일째 −0.47%) · lotto-predictor 1 / git 커밋 3개 저장소 (post1 abc67b6, skills da36aad, memories 9bcbab3).
- daily 페이지: concepts/daily/2026-10-25.md 생성.

## [2026-10-24] daily-sync | 인덱스 +339/+108, 레지스트리 45개 폴더 (변동 없음 — 신규 0, 이틀 연속), 크론 에러 24h 0건·96h 2건(전량 10-20 기분석, 신규 0 — 게이트웨이 재시작 효과 4일차), 작업 변경 480개
- 인덱스: 신규 339 / 갱신 108 (텍스트 없음 스킵 8), 총 13,994개 (원본 합계 3,004.2MB / index.db 586.2MiB·실측 614.7MB). 루트별 projects 11,216 / hermes 2,260 / documents 336 / wiki 182.
  - 전일 13,742 대비 **+252** — 신규 339에서 **고아 정리 87행 감소**가 반영된 순증. index.db 585.1→586.2MiB(+1.2MB), 원본 합계 +1.1MB. 오늘 변경이 전부 텍스트(md·py·json)라 어제의 +75.8MB(xlsx 백업) 같은 대용량 반입이 없었다.
  - `car-year-lookup/captures` **3,786행 / 본문 352.3MB = 전체 본문 427.0MB의 82.5%**(디스크 1.9GB) → "600MB 재돌파 시 EXCLUDE_PATHS" 조건 **3일 연속 초과**(614.7MB 실측). 제외 시 200MB대. **대표님 승인 대기**(크론은 정책 변경 안 함).
- 레지스트리: **45개 폴더 (git 19 / 로컬 26) — 신규 0** (이틀 연속 변동 없음 — 도구 도입 국면 종료, 기획·제작 국면).
- 크론 에러: 최근 24h **0건**, 96시간 **2건**(전량 10-20 발생분, 신규 0).
  - **✅ 게이트웨이 재시작 효과 4일차** — 10-20 08:51:30 기동 후 가동 **92.7시간**, 크론 산출물 FAILED 0건. `RecursionError` 재발 없음.
  - **대기 1건(오늘 판정)**: `주간-주식매매-진행경과-및-전망`(토 17:00) 10-17 `HTTP 429 Policy budget exceeded` 1회 실패(`failure_streak=1`) → **오늘 10-24 17:00 실행 결과로 판정**(이 동기화 05:31 이후 → 내일 보고 반영). 재발 시 시각 분산 또는 `fallback_providers` 검토.
  - **발행 운영**: 심해 A paused → **B 단독 3편/일**(17:00 업로드 → 20·21·22시 공개), 상담소 paused + 재개 예약 **10-28 06:00**. 변동 없음.
  - **남은 리스크**: 근본 코드 결함 미수정(설치본 2026-10-04 빌드) + 실패 이력 job retry 미설정 → **주 1회 게이트웨이 재시작** 예방 루틴(다음 권장일 **10-27** 전후).
  - **판정: 안정(4일 연속 에러 0)** — 조치 필요 없음.
- 작업 변경 480개: my-media-agent 357 (**프리비즈→감독 파이프라인 구축**: 전체지도·다중배우·공간연속성·머리비율 정본, 촬영계획→예측→자동편집 3단, 합격 게이트 9→13종 / **목소리 전달방식 확정** her=립싱크·rec=TTS만($0)·무대사=$0 + voice_swap(2.9배 절감)·voice_fit / **HeyGen 자체음성 실측 폐기**(F0 26~106Hz 불일관·영어 지어냄) / 심해 숏폼드라마 정본+콘티 편01~10 / 동화법률 13편 기획 / blockout_28 Blender 블록아웃), .hermes/skills 94파일·16커밋(프리비즈 교훈 회수·video-model-request-matrix·heygen-voice-endpoints), auto-trading 2(라이브 추적), lotto-predictor 2, post1 1.
  - git 커밋 4개 저장소: my-media-agent 20 · skills 16 · post1 1(`42f925b`) · memories 1(`fc02c76`).
- daily 페이지: concepts/daily/2026-10-24.md 생성

## [2026-10-23] daily-sync | 인덱스 +297/+44, 레지스트리 45개 폴더 (변동 없음 — 신규 0), 크론 에러 24h 0건·96h 3건(전량 10-20 기분석, 신규 0 — 게이트웨이 재시작 효과 3일차), 작업 변경 366개
- 인덱스: 신규 297 / 갱신 44 (텍스트 없음 스킵 6), 총 13,742개 (원본 합계 3,003.1MB / index.db 585.1MiB·실측 613.5MB). 루트별 projects 10,992 / hermes 2,235 / documents 334 / wiki 181.
  - 전일 13,447 대비 **+295**. index.db 583.1→585.1MiB(+2.1MB). 원본 합계 +75.8MB인데 DB는 +2.1MB — 신규 297개가 meta.json·analytics.json 계열 소형 파일이라 본문 증가가 작다.
  - `car-year-lookup/captures` **3,786행 / 본문 369.4MB = 전체 본문 447.0MB의 82.6%** → "600MB 재돌파 시 EXCLUDE_PATHS" 조건 **2일 연속 초과**(613.5MB). 제외 시 200MB대. **대표님 승인 대기**(크론은 정책 변경 안 함).
- 레지스트리: **45개 폴더 (git 19 / 로컬 26) — 신규 0** (전일 신규 3개 이후 첫 변동 없는 날 — 도구 도입 단계 종료, 제작 단계 진입 신호).
- 크론 에러: 최근 24h **0건**, 96시간 **3건**(전량 10-20 발생분, 신규 0).
  - **✅ 게이트웨이 재시작 효과 3일차** — 10-20 08:51:30 기동 후 가동 **68시간**, 크론 산출물 FAILED 0건. 재발 없음.
  - ✅ `daily-geek-hacker-news` **복구 확정**(10-22 08:01 `last_status=ok`, `failure_streak=0`) · ✅ `auto-trading-morning-briefing` ok 유지(streak 0).
  - **신규 관찰(경미)**: `주간-주식매매-진행경과-및-전망`(토 17:00)이 10-17 `HTTP 429 Policy budget exceeded` **1회 실패**(`failure_streak=1`)로 남아 있음 — 주간 잡이라 24/96h 창에 안 잡혀 이번이 첫 보고. 단일 실패·반복 아님 → **10-24(토) 17:00 결과로 판정**, 재발 시 시각 분산 또는 `fallback_providers` 검토.
  - **발행 운영**: 심해 A paused(10-21 지시) → **B 단독 3편/일**(17:00 업로드 → 20·21·22시 공개), 상담소 paused + 재개 예약 **10-28 06:00** 유지. 변동 없음.
  - **남은 리스크**: 근본 코드 결함 미수정(설치본 2026-10-04 빌드) + 실패 이력 job retry 미설정 → **주 1회 게이트웨이 재시작** 예방 루틴(다음 권장일 10-27 전후).
  - **판정: 안정(3일 연속 에러 0)** — 조치 필요 없음.
- 작업 변경 366개(원본 1,652): **my-media-agent 317·20커밋** — 윤서 실사 EP01~03 업로드용 마스터 완성(15.0·14.6·16.6초), **배우 연기 해결**("감정은 프롬프트가 아니라 감정이 실린 끝 앵커로 심는다"), **클립 이음새 3원칙**(15초 이하는 멀티샷 한 번 / 카메라 이동은 extend / 중복 프레임 1프레임 다듬기) + 도구 4종 신설(`check_seams.py`·`check_naturalness.py`·`heal_clip.py`·`blender_move.py`), **오픈라우터 카메라 통제 성공**($0.212 — `frame_images`=exact frame control vs `input_references`=느슨한 안내), 비용 구조 정정(청구 = 5초 블록 올림, HeyGen 요율 하드코딩 2.4배 오차 수정), 신규 시리즈 기획 2건(「웃기는 변호사」·유머-시리즈 위트반전) + 심해 30화 드라마 버전. / **car-year-lookup 4** — 대차내역 xlsx **시간 열 삽입 도구**(`insert_time_columns.py`, 원본 XML 직접 패치·sharedStrings 풀어 inlineStr 주입 + `verify_time_columns.py`). / **auto-trading 2** — 라이브 추적 갱신(국면 bear 유지). / **post1 1** — 개인사이트(`248deba`). / skills·memories 01:00 백업 각 1커밋.
- daily 페이지: concepts/daily/2026-10-23.md 생성

## [2026-10-22] daily-sync | 인덱스 +928/+124, 레지스트리 45개 폴더 (+3: blender-mcp·blender-vse-mcp·craft-clis), 크론 에러 24h 0건·96h 5건(전량 기분석 — 게이트웨이 재시작 효과 2일차, 재발 0), 작업 변경 1,079개
- 인덱스: 신규 928 / 갱신 124 (텍스트 없음 스킵 37), 총 13,447개 (원본 합계 2,927.3MB / index.db 583.1MiB·실측 611.4MB). 루트별 projects 10,723 / hermes 2,212 / documents 332 / wiki 180.
  - 전일 12,690 대비 **+757**. index.db 571.0→583.1MiB(+12.1). 원본 합계 +739MB는 **car-year-lookup inbox xlsx 백업 13개(각 ~56MB)** 때문 — 바이너리라 DB 영향 없음.
  - `car-year-lookup/captures` **3,786행 / 본문 352.3MB = 전체 본문 425.4MB의 82.8%** → "600MB 재돌파 시 EXCLUDE_PATHS" 조건 **초과**(611.4MB). 제외 시 200MB대. **대표님 승인 대기**(크론은 정책 변경 안 함).
- 레지스트리: **45개 폴더 (git 19 / 로컬 26) — 신규 3개**: `blender-mcp`(sandraschi/blender-mcp 클론), `blender-vse-mcp`(헤드리스 VSE MCP 신설), `craft-clis`(PhotoCraft 0.11.1·FilmCraft 0.9.0·VectorCraft 0.13.1 CLI).
- 크론 에러: 최근 24h **0건**, 96시간 **5건**(전량 10-18~10-20 기분석, 신규 0).
  - **✅ 게이트웨이 재시작 효과 검증** — 10-20 08:51:30 기동 후 가동 44시간, 재시작 이후 크론 산출물 누적 **137건 FAILED 0건**(10-21~10-22 실행 77건 전부 정상).
  - ✅ `auto-trading-morning-briefing` 복구(`last_status=ok`, `failure_streak=0`) · ✅ 1회성 재개 예약 2건 정상(심해 B 재개 06:05 → 본잡 10-21 17:00 completed·delivered / A 재개 12:00).
  - ⏳ `daily-geek-hacker-news`만 `last_status=error` 유지(10-20 실패분) → **10-22(목) 08:00 첫 재실행**으로 최종 복구 확인 예정.
  - **발행 운영**: 심해 A는 대표님 지시(10-21)로 **paused**(B와 공개 시각 겹침) → **B 단독 3편/일**(17:00 업로드 → 20·21·22시 공개), 상담소 paused + 재개 예약 **10-28 06:00** 활성. 중복 위험 없음.
  - **남은 리스크**: 근본 코드 결함 미수정(설치본 2026-10-04 빌드) + 실패 이력 job retry 미설정 → **주 1회 게이트웨이 재시작** 예방 루틴 권장(다음 권장일 10-27 전후).
  - **판정: 안정(재발 0)**
- 작업 변경 1,079개 (원본 2,288개 중): my-media-agent 468 (20커밋 — **신규 프로젝트 `심해-3년전-트레일러`**: 30편 완결 시리즈 15초 예고편(9:16·5초×3컷·Seedance 2.5) 스토리보드→클립 3개→자막/조립 배선, **사연카드 = PhotoCraft 하이브리드 패널 기본값**(620px·y1260·딤0.22, ASS 폴백), 인코딩 상향→정지화면 콘텐츠 결론으로 원복(+maxrate 9M 가드), FilmCraft vs ffmpeg Phase0 비교(5.2초/14.4MB vs 14.7초/23.0MB)·활용계획 승인 대기, 영상생성 모델 기준 검토(20종·Wan 3.0 $0.05/s), 대본 규칙(쉼표=호흡·인용 종결부호·34문장 교정), `.env` 추적 해제), blender-vse-mcp 3 (VSE MCP 15도구 신설 + README 함정), car-year-lookup 58 (표준화 3일차 — 표본 조회 세트·조회실패/X시리즈 CSV 4종·오인식 점검·작업보고서 md+docx), .hermes 71 (skills 50 — 발행 운영안·공개슬롯 20/21/22시·craft-apps-photo-film-vector 신설·blender-vse-video-editing 신설·중복 스킬 흡수(영상 7→3, 카드뉴스 4→2)), post1 1 / git 커밋 5개 저장소 (my-media-agent 20, blender-vse-mcp 3, skills 8, memories 1, post1 1)
- daily 페이지: concepts/daily/2026-10-22.md 생성

## [2026-10-21] daily-sync | 인덱스 +224/+72, 레지스트리 42개 폴더(변동 없음), 크론 에러 24h 2건·96h 6건(24h 전부 `RecursionError` — 게이트웨이 재시작으로 재발 0건, retry 미설정이 남은 리스크), 작업 변경 325개
- 인덱스: 신규 224 / 갱신 72 (텍스트 없음 스킵 11), 총 12,690개 (원본 합계 2,187.8MB / index.db 571.0MiB·실측 598.7MB). 루트별 projects 9,973 / hermes 2,208 / documents 330 / wiki 179.
  - 전일 12,468 대비 **+222**. index.db 569.4→571.0MiB(+1.6). 원본 합계 +176MB는 **car-year-lookup inbox xlsx 3개(185MB)** 때문 — 바이너리라 DB 영향 없음.
  - `car-year-lookup/captures` **3,785행 / 본문 369.3MB = 전체 본문 437.3MB의 84.5%** → "600MB 재돌파 시 EXCLUDE_PATHS" 조건 도달. 파일 삭제 없이 제외하면 200MB대. **대표님 승인 대기**.
- 레지스트리: 42개 폴더 (git 17 / 로컬 25) — **변동 없음**, 신규 0개.
- 크론 에러: 최근 24h **2건**, 96시간 **6건**, 원인 3종.
  - **`RecursionError` (에이전트 생성 단계·프레임워크)** — 10-20 08:00 `daily-geek-hacker-news`(3d0b92cb1d6e), 08:30 `auto-trading-morning-briefing`(82cb11d1c019), (96h 창) 10-20 00:10 심해 발행 A(94e321b817b7). 세 job 모두 `retry` 미설정.
  - 기존분: `HTTP 401` 키 만료 ×2 (10-18 06:00, 08:36 키 교체로 해소) · `HTTP 429` 예산 ×1 (10-17 17:00, 17:03 재시도 복구).
  - **✅ 전일 조치 필요 1번(게이트웨이 재시작) 이행 확인** — 10-20 08:51:30 SIGTERM → 08:51:31 재기동(부모 pid 838, 14일 17시간 무재시작 종료). 현재 가동 20시간 40분, 재시작 후 크론 산출물 **60건 중 FAILED 0건** → 프록시 체인 초기화 확인.
  - **대표님 조치**: 심해 발행 **A/B 분리 신설**(A 06:00 업로드→12:00·12:15·12:30 공개 / B 17:00→18:00·18:15·18:30), **상담소 발행 신설**(06:00→12:00·18:00·21:30, 심해 30편 완주까지 paused). 본잡 3개 모두 paused, **1회성 재개 예약 3건**(B 10-21 06:05 · A 10-21 12:00 · 상담소 10-25 06:00)만 활성 → 중복 발행 위험 없음.
  - **남은 리스크**: 근본 코드 결함 미수정(설치본 2026-10-04 빌드) → 가동일수 누적 시 재발. **주 1회 게이트웨이 재시작** + 실패 3종 job에 **지연 재시도 1회** 권장. `daily-geek-hacker-news` 10-20 실패분은 아직 미복구(다음 10-22 08:00), `auto-trading-morning-briefing`은 10-21 08:30 결과로 복구 확정.
  - 집계자 자기 점검: `llm-wiki-daily-sync`(28ea8625654b) 직전 실행 상태 ok, 10-19 실패분 복원 완료 상태 유지.
  - **판정: 재시작 완료 · 재발 감시 중(주의)**
- 작업 변경 325개 (원본 1,044개 중): my-media-agent 256 (20커밋 — 상담소 EP01 제작(29.8초·$0.054)·EP02~03 대본 확정·30화 재편성(1의뢰인=3편), 화면 등장 2인 고정 + 의뢰인 비노출, 사연 카드·편당 대장, 이미지 글자 금지·일관성 레퍼런스, 회차 마감 도구화, 유료 승인 사전 게이트, 발행 슬롯 간격 --step, 인증만료·시리즈 해석 버그 2건, /keys 화면, 대본 규칙 2층 분리·첫 문장 반복 차단), car-year-lookup 14 (표준화 2일차 — 기준시트·빈도/사유 분석·검토 CSV·보고서+기준서, xlsx 3개 반입), .hermes 51 (야간 백업 2, config/jobs.json, state), auto-trading 2 (라이브 리포트), post1 1 (db894f5), work 1 (llm_budget.json) / git 커밋 4개 저장소 (my-media-agent 20, post1 1, skills 1, memories 1)
- daily 페이지: concepts/daily/2026-10-21.md 생성

## [2026-10-20] daily-sync | 인덱스 +156/+231, 레지스트리 42개 폴더(변동 없음), 크론 에러 24h 1건·96h 7건(신규 `RecursionError` 1건 = 프레임워크·조치 필요), 작업 변경 412개
- 인덱스: 신규 156 / 갱신 231 (텍스트 없음 스킵 13), 총 12,468개 (원본 합계 2,011.4MB / index.db 569.4MB). 루트별 projects 9,771 / hermes 2,190 / documents 329 / wiki 178.
  - 전일 12,401 대비 +67. index.db 568.2→569.4MB(+1.2MB). `car-year-lookup/captures` 3,785행 = 본문 352.2MB로 **전체 본문 416.2MB의 84.6%** (600MB 임박, EXCLUDE_PATHS 후보 유지).
- 레지스트리: 42개 폴더 (git 17 / 로컬 25) — **변동 없음** (어제 신규 `work` 포함, 신규 0개).
- 크론 에러: 최근 24h **1건**, 96시간 **7건**, 원인 4종.
  - **신규 유형 — `RecursionError: maximum recursion depth exceeded`** (10-20 00:10 `심해 발행 진행 — 매일 00:10 다음 6편 비공개 업로드+예약`, 94e321b817b7).
    실패 지점은 job 본문이 아니라 **에이전트 생성 단계**: `_construct_cron_agent → _setup_logging → _line_buffer_piped_stdout → getattr(stream,'line_buffering')` 에서
    `process_bootstrap.__getattr__` ↔ `thread_scoped_output.__getattr__` 상호 위임으로 프레임 2배 소모. 게이트웨이 10-05 12:07부터 **14일 17시간 무재시작** → stdout 프록시 체인 누적이 원인(로그상 최초 발생).
    job은 10-19 23:14 생성, **성공 이력 0회**(failure_streak=1, retry 없음) → **10-20 예약 발행 6편 실제 누락**.
  - 기존 6건: `401` 키 만료 ×2 (10-18 06:00 Wiki Git Backup·personal site — 08:36 키 교체로 해소), `429` 예산 ×1 (10-17 17:00 주간주식 → 17:03 복구), `403` 모델차단 ×3 (10-16 16:00 ×2·20:00 로또 → 전부 재시도 복구).
  - 집계자 자기 점검: `llm-wiki-daily-sync`(28ea8625654b) 직전 실행 10-19 정상. 10-18 실패분은 10-19 실행에서 복원 완료.
  - **조치 필요** — ①게이트웨이 재시작(누적 프록시 체인 초기화) ②`심해 발행 진행` 수동 1회 재실행(오늘 몫 6편) ③해당 job에 지연 재시도 추가 ④upstream 수정(현 설치본 2026-10-04 빌드, 미포함).
- 작업 변경 412개 (원본 1,800개 중): my-media-agent 350 (20커밋 — 심해 시리즈 제작·검수 277파일, 발행 파이프라인 정비(다음 N편 자동 발행·예약 안전화·[EP번호]·재생목록·AI 사용 공개 실측), 신규 '기억 복원 상담소' 기획·캐릭터시트·30화 편성·대본 생성기 재작성 루프, 품질 게이트), .hermes 46 (local-video-production references 12개 신규/개편 + SKILL.md 9개 갱신, 야간 백업 2, memories), car-year-lookup 12 (xlsx 표준차량모델·표준열 개선 + 백업 3), auto-trading 2, post1 1 / git 커밋 4개 저장소 (my-media-agent 20, post1 1, skills 1, memories 1)
- daily 페이지: concepts/daily/2026-10-20.md 생성

## [2026-10-19] daily-sync | 인덱스 +1,339/+80, 레지스트리 42개 폴더 (+1 work), 크론 에러 24h 2건·96h 6건(전부 프로바이더 4xx, 401 키 만료 3건은 조치 필요), 작업 변경 1,441개
- 인덱스: 신규 1,339 / 갱신 80 (텍스트 없음 스킵 24), 총 12,401개 (FTS 12,401, 원본 합계 2,009.6MB / index.db 568.2MB). 루트별 projects 9,730 / hermes 2,169 / documents 326 / wiki 176.
  - 전일 11,159 대비 +1,242 — 변경 창이 **이틀치**(10-18 05:30 실행 실패)라 10-18·10-19 분이 합산 유입. index.db 557.7→568.2MB(+10.5MB).
  - **index.db 최대 용량원 = `car-year-lookup/captures`**: 3,785개 HTML(디스크 1.9GB)이 본문 352MB로 전체 본문(415MB)의 85%. 10-16 로그의 "600MB 재돌파 시 EXCLUDE_PATHS 검토" 조건에 근접(568MB) → 제외 후보 1순위. 잡음 후보 2순위 `.hermes/browser-profile/**` 33행.
- 레지스트리: 42개 폴더 (git 17 / 로컬 25) — **+1 신규: `work`** (LLM 예산 추적 단일 파일 `llm_budget.json`). my-media-agent 최근 커밋 10-19, post1 10-17.
- 크론 에러: 최근 24h 2건 / 96시간 6건, 원인 3종 — `HTTP 401` 키 만료 3건(10-18 05:30 llm-wiki-daily-sync **자신 포함**, 06:00 Wiki Git Backup·personal site 갱신), `HTTP 429 Policy budget exceeded` 1건(10-17 17:00 주간-주식매매 → 17:03 복구), `HTTP 403 Model access is disabled` 2건(10-16 16:00 주식분석·자동매매브리핑 → 20:10/20:13 복구).
  - 전부 업스트림 4xx, 로컬 스크립트 결함 0건. 401은 08:36 `auth.json` 키 교체로 해소(자동 복구 불가 유형).
  - 개선 제안: ①`fallback_providers` 등록(빈 배열, 401/403/429 자동 우회) ②키 만료 알림 ③집계자(llm-wiki-daily-sync) 자기 실패 사각지대 보완 ④17:00대 무거운 job 시각 분산.
  - **조치 필요** — 401 3건은 재시도로 안 풀리고 사람이 키를 교체해야 복구되며, 10-18 daily 페이지가 하루 공백이 됐다(10-19 실행에서 복원).
- 작업 변경 1,441개 (창 5,069개 중): my-media-agent 1,358 (창 전체 **207커밋** — 무료 음악 생성기 v1~v5·유튜브 보관함 12곡·스튜디오 대확장(프리셋·시네마룩·인트로엔딩·비용탭·연속재생)·사진 여러 장→영상·동적 자막·프리비즈 자체 구현(블렌더 없이 평면도+3D 와이어프레임)·EP20·22·23·28), .hermes 79 (스킬 신설 2: reverse-engineer-anything·local-tool-web-shell, 보강 6 + music-sourcing-and-licensing 신규, 야간 백업 2일치, config.yaml 00:30, 크론 기록), post1 1 (d4049e2), auto-trading 1 (주간 리포트), lotto-predictor 1, work 1 / git 커밋 4개 저장소
- daily 페이지: concepts/daily/2026-10-19.md 생성 + **2026-10-18.md 복원**(전일 실패분, 이틀치 창으로 재구성)

## [2026-10-17] daily-sync | 인덱스 +222/+60, 레지스트리 41개 폴더, 크론 에러 3건(동일 원인 1건·재시도 복구), 작업 변경 345개
- 인덱스: 신규 222 / 갱신 60 (텍스트 없음 스킵 17), 총 11,159개 (FTS 11,159, 원본 합계 1,998.4MB / index.db 557.7MB). 루트별 projects 8,550 / hermes 2,109 / documents 325 / wiki 175.
  - 전일 10,942 대비 +217 — my-media-agent 장면·캐릭터 이미지, car-year-lookup 백업 xlsx, 스킬 스크립트 동시 유입. index.db 557.7MB(전일 556MB, +1.7MB) 완만 증가.
- 레지스트리: 41개 폴더 (git 17 / 로컬 24) — 전일과 동일, **신규 폴더 없음**. 변동은 파일 수(car-year-lookup 5,706→5,736, lotto-predictor 19→21).
- 크론 에러 3건 — 전부 `HTTP 403 Model access is disabled`(opencode-go 프로바이더 모델 접근 차단), 10-16 16:00 Daily Stock Analysis / 16:00 auto-trading-evening-briefing / 20:00 로또-주간-예측-알림.
  - 세 건 모두 **재시도로 복구**(20:03·20:10·20:13 정상 산출물). 96시간 창에서 해당 4시간 외 에러 0건 → 단일 시간대 프로바이더 장애(반복 패턴 아님).
  - 개선 제안: `fallback_providers`가 빈 배열 → 대체 프로바이더 1개 등록 시 403 유형 자동 우회(근본 조치). 재시도 규칙 목록에 403 명시.
- 작업 변경 345개: my-media-agent 233 (20커밋 — 법률 사례 홍보 파이프라인 신설·캐릭터 시트 고정, 사례 002 제작 기준, 1:1 카드·쇼츠 가독성 5커밋, HeyGen 480p 요율 실측 정본화(3.5배 과대계산 교정), 카메라 무브·매치컷 $0 개선, 승격 480p+업스케일 3경로), car-year-lookup 30 (증빙 기반 판정·모델 표준화·OOXML 직접 패치 + 단계별 백업 4개), .hermes 77 (스킬 4개 신설: legal-case-promo·shortform-video-layout(+스크립트 2)·vehicle-model-standardization·legacy-xlsx-xml-patching / 보강 6개, Home Assistant 플러그인 신설 13파일, 야간 백업 411135f·c30efb8, config.yaml 20:02 403 대응, 크론 기록·park_watch·kanban), auto-trading 2 (실전 라이브 추적, bear·총자산 472,933), lotto-predictor 2 (1246회차·추적 15회차), post1 1 (6321e9d) / git 커밋 4개 저장소
- daily 페이지: concepts/daily/2026-10-17.md 생성

## [2026-10-16] daily-sync | 인덱스 +93/+19, 레지스트리 41개 폴더 (+1 my-media-agent), 크론 에러 0건, 작업 변경 193개
- 인덱스: 신규 93 / 갱신 19 (텍스트 없음 스킵 0), 총 10,942개 (FTS 10,942, 원본 합계 1,990.8MB / index.db 556MB). 루트별 projects 8,367 / hermes 2,078 / documents 323 / wiki 174.
  - 전일 10,849 대비 +93 — my-media-agent 신설 + 스킬 references 대량 생성분. index.db 556MB(전일 554.9MB) — 600MB 재돌파 시 `car-year-lookup/captures` EXCLUDE_PATHS 검토.
  - `build_index.py --stats` 라벨 수정: `SUM(size)`(원본 합계)를 DB 크기처럼 표기하던 것을 `원본 합계 …MB, index.db …MB`로 분리(실제 DB 실측 출력).
- 레지스트리: 41개 폴더 (git 17 / 로컬 24) — **+1 신규: `my-media-agent`** (git, justfly32/my-media-agent, 최근 커밋 10-16). 2일 연속 신규 폴더(diet-calc → my-media-agent).
- 크론 에러 0건 — 11일 연속 정상(10-05 ImportError 조치 후 회귀 없음).
- 작업 변경 193개: my-media-agent 107 (20커밋 — 쇼츠 시리즈 모드, 일관성 유지 모드+로컬 자동 점검, TTS 호흡·쉼·간격 난수화, project.json/meta.json 이력, /clean·/manual·/help·/set·/status, MarkupError·먹싱 버그 수정), .hermes 31 (스킬 4개 신설: ai-media-consistency·third-party-api-integration·install-github-python-app·interactive-cli-surface / 보강: local-video-production·stock-analysis-pipeline·paid-batch-operations·daily-memory-notion, 야간 백업 e7f85af·6cf015f, 크론 기록), auto-trading 2 (실전 라이브 추적, bear 국면 총자산 4,727,707), park-empty-watch 2, post1 1 (3a7fd19) / git 커밋 4개 저장소
- daily 페이지: concepts/daily/2026-10-16.md 생성

## [2026-10-15] daily-sync | 인덱스 +16/+15, 레지스트리 40개 폴더 (+1 diet-calc), 크론 에러 0건, 작업 변경 45개
- 인덱스: 신규 16 / 갱신 15 (텍스트 없음 스킵 4), 총 10,849개 (FTS 10,849, 1,990.1MB). 루트별 projects 8,292 / hermes 2,063 / documents 321 / wiki 173
  - 전일 10,840 대비 +9 순증. index.db 554.9MB(581,820,416 bytes, 전일 554MB) — 고아 정리·VACUUM 자동 수행 후에도 소폭 증가, 600MB 재돌파 시 `car-year-lookup/captures` EXCLUDE_PATHS 검토.
- 레지스트리: 40개 폴더 (git 16 / 로컬 24) — **+1 신규: `diet-calc`** (로컬 12개 파일, 10-11 신규 3건 이후 약 4일 만). post1 최근 커밋일만 10-13→10-14.
- 크론 에러 0건 — 10일 연속 정상(10-05 ImportError 조치 후 회귀 없음).
- 작업 변경 45개: diet-calc 12 (신규 단일페이지 식단·영양 계산기 53,797건 DB + korean-nutrition-db 스킬 신규), stock-analysis-pipeline 스킬 갱신(SKILL.md + 2026-10-14 세션노트), auto-trading 2 (실전 라이브 추적 15:45), park-empty-watch 2, post1 1 (7d5a14e), .hermes 운영 30 (야간 백업·크론 기록·curator) / git 커밋 3개 저장소 (post1 7d5a14e, skills 599ee59, memories e71fce0)
- daily 페이지: concepts/daily/2026-10-15.md 생성

## [2026-10-14] daily-sync | 인덱스 +5/+12, 레지스트리 39개 폴더, 크론 에러 0건, 작업 변경 24개
- 인덱스: 신규 5 / 갱신 12 (텍스트 없음 스킵 0), 총 10,840개 (FTS 10,840, 1,961MB). 루트별 projects 8,283 / hermes 2,066 / documents 319 / wiki 172
  - 전일 10,835 대비 +5 — car-year-lookup captures 대량 유입(10-13) 이후 정상 증분으로 복귀. index.db 554MB(전일 580MB, 소폭 감소 — 고아 정리 + VACUUM 자동 수행).
- 레지스트리: 39개 폴더 (git 16 / 로컬 23) — 전일과 동일, 신규 폴더 없음 (post1 최근 커밋일만 10-12→10-13 갱신)
- 크론 에러 0건 — 9일 연속 정상(10-05 ImportError 조치 후 회귀 없음).
- 작업 변경 24개: stock-analysis-pipeline 스킬 갱신(SKILL.md 88KB + 2026-10-13 세션노트, kanban stock-analysis 보드), auto-trading 2 (실전 라이브 추적 15:45), park-empty-watch 2 (park_watch 로그/상태), post1 1 (8e6b8c7 개인사이트), .hermes 운영 21 (야간 백업·크론 기록·curator ledger) / git 커밋 3개 저장소 (post1 8e6b8c7, skills e18b994, memories 87462c5)
- daily 페이지: concepts/daily/2026-10-14.md 생성

## [2026-10-13] daily-sync | 인덱스 +3,489/+24, 레지스트리 39개 폴더, 크론 에러 0건, 작업 변경 3,513개
- 인덱스: 신규 3,489 / 갱신 24 (텍스트 없음 스킵 1,644) / 총 10,835개 파일 (FTS 10,835, 1,961MB). 루트별 projects 8,283 / hermes 2,064 / documents 317 / wiki 171
  - 전일 7,346 대비 +3,489 — **대부분 car-year-lookup/captures 증빙 자료(5,549개, HTML 3,785+JPG 1,764, 1.9GB) 한 번에 유입** (12일 20:00 이후 생성). 실제 작업 산출물이라 bloat 아님. 단 index.db 580MB로 급증 — 10-05 정리(590→93MB) 후 최대치. 추후 DB 비대 시 EXCLUDE_PATHS에 `car-year-lookup/captures` 추가 고려.
- 레지스트리: 39개 폴더 (git 16 / 로컬 23) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 8일 연속 정상(10-05 ImportError 조치 후 회귀 없음).
- 작업 변경 3,513개: car-year-lookup 3,512 (captures 증빙 5,549개 + 열람/업로드/검증 임시 스크립트 + 연식캡처현황 CSV), auto-trading 2 (실전 라이브 추적), post1 1 (db0cb62 개인사이트) / git 커밋 3개 저장소 (post1 db0cb62, skills 4960d8a, memories dce14ab)
- daily 페이지: concepts/daily/2026-10-13.md 생성

## [2026-10-12] daily-sync | 인덱스 +41/+22, 레지스트리 39개 폴더, 크론 에러 0건, 작업 변경 79개
- 인덱스: 신규 41 / 갱신 22 (텍스트 없음 스킵 12) / 총 7,346개 파일 (FTS 7,346, 390.7MB). 루트별 projects 4,801 / hermes 2,061 / documents 314 / wiki 170
  - 전일 7,305 대비 +41 — 정상 증분 (projects 기반 확장, bloat 아님)
- 레지스트리: 39개 폴더 (git 16 / 로컬 23) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 7일 연속 정상(10-05 ImportError 조치 후 회귀 없음).
- 작업 변경 79개: build-plan 12커밋 (로컬 AI 제거→opencode-go 단일 백엔드, Vercel 서버리스 api/ai.ts 배포 정상화 glm-5.3-flash, LLM 설정 화면·자료실 탭·더블클릭 실행), sangga-tax-calc 20파일 (상가 세무 가이드 15종), post1 1 (9e6d32e), geomdan-design-contract 2, auto-trading 1 (주간 리포트) / git 커밋 4개 저장소 (build-plan 12, post1 9e6d32e, skills fb45550, memories e47cc38)
- daily 페이지: concepts/daily/2026-10-12.md 생성

## [2026-10-11] daily-sync | 인덱스 +79/+16, 레지스트리 39개 폴더, 크론 에러 0건, 작업 변경 12개
- 인덱스: 신규 79 / 갱신 16 (텍스트 없음 스킵 5) / 총 7,305개 파일 (FTS 7,305, 390.3MB). 루트별 projects 4,771 / hermes 2,051 / documents 314 / wiki 169
  - 전일 7,226 대비 +79 — 대부분 build-plan 신규 폴더(세금 레이어 소스·테스트) 유입, bloat 아님
- 레지스트리: 39개 폴더 (git 16 / 로컬 23) — 전일 36 대비 **+3 신규**
  - build-plan (git, justfly32/build-plan) — 10-10 세금 레이어 + 로컬 AI 백엔드 통합 (11커밋)
  - geomdan-design-contract (local) — 인천 검단구 표준 반영
  - sangga-tax-calc (local) — 상가주택 세금 계산기 (build-plan 세금 레이어와 동일 도메인 — 정본 구분 확인 권장)
- 크론 에러 0건 — 6일 연속 정상(10-05 ImportError 조치 후 회귀 없음).
- 작업 변경 12개: build-plan 11커밋 (로컬 AI 우선 전환·세금 레이어·인쇄리포트 세금 세부담, test:report 14항목 통과), post1 1 (5eb1e34) / git 커밋 4개 저장소 (build-plan 11, post1 5eb1e34, skills 14046ba, memories 522385b)
- daily 페이지: concepts/daily/2026-10-11.md 생성

## [2026-10-10] daily-sync | 인덱스 +17/+21, 레지스트리 36개 폴더, 크론 에러 0건, 작업 변경 48개
- 인덱스: 신규 17 / 갱신 21 (텍스트 없음 스킵 3) / 총 7,226개 파일 (FTS 7,226, 389.0MB). 루트별 projects 4,705 / hermes 2,040 / documents 313 / wiki 168
  - 전일 7,209 대비 +17 — 정상 증분, bloat 없음
- 레지스트리: 36개 폴더 (git 15 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 5일 연속 정상(10-05 PYTHONPATH 조치 후 회귀 없음).
- 작업 변경 48개(요약 48개): car-year-lookup 13 (연식범위 추정 CSV 재생성·무료사유판별 v2·별지대차내역 재작성·최종보고 md — 사고차 배치 정리 단계), lotto-predictor 2, post1 1 (f5b2768) / git 커밋 3개 저장소 (post1 f5b2768, skills 6e48fef, memories 3d5e5f5)
- daily 페이지: concepts/daily/2026-10-10.md 생성

## [2026-10-09] daily-sync | 인덱스 +389/+20, 레지스트리 36개 폴더, 크론 에러 0건, 작업 변경 576개
- 인덱스: 신규 389 / 갱신 20 (텍스트 없음 스킵 163) / 총 7,209개 파일 (FTS 7,209, 388.8MB, index.db 디스크 144.5MB). 루트별 projects 4,694 / hermes 2,037 / documents 311 / wiki 167
  - 전일 6,840 대비 +369: 대부분 car-year-lookup 증빙(captures 원본/열람용 HTML 373 + jpg + 발송 zip) — 실제 산출물로 인한 정상 성장, bloat 아님
- 레지스트리: 36개 폴더 (git 15 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 4일 연속 정상(10-05 PYTHONPATH 조치 후 회귀 없음).
- 작업 변경 576개(요약 443개): car-year-lookup 409 (사고차 214대 카히스토리 조회 완료 — 성공 152/불가 62/시트중복 4, 포인트 15,200P, 증빙 6종 zip 발송 패키징, 무료 폐차·침수 조회로 불가분 이월), auto-trading 2 (10-08 15:45 장후 코어 라이브 갱신), post1 1(car-year-lookup 증빙 캡처 385개는 captures/ 하위) / git 커밋 3개 저장소 (post1 fc78f6f, skills c86a2f4, memories 05860f5)
- daily 페이지: concepts/daily/2026-10-09.md 생성

## [2026-10-08] daily-sync | 인덱스 +44/+25, 레지스트리 36개 폴더, 크론 에러 0건, 작업 변경 116개
- 인덱스: 신규 44 / 갱신 25 (텍스트 없음 스킵 0) / 총 6,840개 파일 (FTS 6,840, 222.9MB, index.db 디스크 97.2MB). 루트별 projects 4,332 / hermes 2,033 / documents 309 / wiki 166
  - 전일 6,999 대비 -159: 색인 대상은 순증(+69)이나 prune_missing이 디스크에서 사라진 `~/.hermes` 파일(hermes 2,200→2,033) 고아 행을 정리한 결과 — 정상 동작
- 레지스트리: 36개 폴더 (git 15 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 3일 연속 정상(10-05 PYTHONPATH 오염 조치 후 회귀 없음).
- 작업 변경 116개(요약 92개): shorts-forge 56 (웹 UI 전환 — webapp.py·비밀번호 게이트·퀵터널, 삭제/휴지통·기록 삭제, 완료 텔레그램 알림, 설명란을 기획서로, 시각 없는 기획서 자동 구간, 원본 구간만 시작점, 20초 기본, ffmpeg 스케줄러 멈춤 방지), auto-trading 2 (10-07 15:45 장후 코어 라이브 갱신), post1 1 / git 커밋 4개 저장소 (shorts-forge 13커밋 a27d42a~ccf7567, post1 4046cc0, skills 820252d, memories d72858d)
- daily 페이지: concepts/daily/2026-10-08.md 생성

## [2026-10-07] daily-sync | 인덱스 +37/+14, 레지스트리 36개 폴더, 크론 에러 0건, 작업 변경 101개
- 인덱스: 신규 37 / 갱신 14 (텍스트 없음 스킵 0) / 총 6,999개 파일 (FTS 6,999, 223.8MB, index.db 디스크 98.7MB). 루트별 projects 4,327 / hermes 2,200 / documents 307 / wiki 165
- 레지스트리: 36개 폴더 (git 15 / 로컬 21) — **신규 1개: `shorts-forge`** (유튜브 롱폼 → 쇼츠 자동 생성)
- 크론 에러 0건 — 10-05 PYTHONPATH 오염(ImportError 2건) 조치(4e3da5d) 후 이틀 연속 정상, 회귀 없음 확인
- 작업 변경 101개(요약 73개): shorts-forge 50 (기획서 컷 → 롱폼 자막에서 쇼츠 후보·제목·대본 자동 생성, whisper 로컬 음성인식, 인용 검증, 내레이션 TTS+문장 자막, 알파컷 기능), auto-trading 2 (10-06 15:45 장후 코어 라이브 갱신), post1 1 / git 커밋 4개 저장소 (shorts-forge 9커밋 2f20445~0fead9d, post1 b72aa59, skills 80c74bf, memories f470245)
- daily 페이지: concepts/daily/2026-10-07.md 생성

## [2026-10-06] daily-sync | 인덱스 +7/+19, 레지스트리 35개 폴더, 크론 에러 2건, 작업 변경 43개+
- 인덱스: 신규 7 / 갱신 19 (텍스트 없음 스킵 0) / 총 6,961개 파일 (FTS 6,961). 루트별 projects 4,297 / hermes 2,195 / documents 305 / wiki 164
  - 총계 감소(17,380→6,961)는 정상: 커밋 34d9bb4에서 앱 소스·툴체인(hermes-agent/installs/tools) 색인 제외 + FTS external-content 전환 (index.db 590MB→93MB)
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 2건 (동일 원인 1건의 파급): auto-trading-intraday-alpha-pm(10-05 14:00), auto-trading-live-afterhours-core(10-05 15:45) — Hermes PYTHONPATH(3.14 site-packages)가 venv(3.11) numpy/pandas를 가려 ImportError. 커밋 4e3da5d로 이미 차단(10-05 16:02), 10-06 실행으로 회귀 검증 필요 — 3건 이상 반복 패턴은 아님
- 작업 변경 43개+ (요약 기준): auto-trading 39 (PYTHONPATH 차단, no-write 가드 검사 스크립트, 추이 CSV 무결성 문서, 라이브 추적 갱신), post1 1, pc-llm-dashboard 2, MI8_project 1 / git 커밋 5개 저장소 (post1 23697c3, auto-trading aab02c3·4e3da5d, memories 655eaea, skills 29b72bd, hermes-agent 14)
- daily 페이지: concepts/daily/2026-10-06.md 생성

## [2026-10-04] daily-sync | 인덱스 +4/+7, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 15개
- 인덱스: 신규 4 / 갱신 7 / 총 17,377개 파일 (FTS 17,118, 357.6MB)
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 안정 유지, 정상.
- 작업 변경 15개: post1 1 (커밋 b7293dc), auto-trading 1 (주간 매매 경과 리포트), lotto-predictor 1, .hermes 12 (memory 백업·cron 상태·kanban) / git 커밋 2개 저장소 (post1 b7293dc, memories 7bf243d)
- daily 페이지: concepts/daily/2026-10-04.md 생성

## [2026-09-30] daily-sync | 인덱스 +11/+24, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 39개
- 인덱스: 신규 11 / 갱신 24 / 총 17,346개 파일 (FTS 17,087, 357.4MB)
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 4일 연속 크론 안정 유지, 정상.
- 작업 변경 39개: auto-trading 12 (장후 코어 주문 81→71 전환 + NH 필수 필드 + 성과 기준자본 분리), post1 1 (커밋 c041577), .hermes 26 / git 커밋 3개 저장소 (post1 c041577, auto-trading 3개 8f44c26·8343f9c·116decf, memories 2b82997)
- daily 페이지: concepts/daily/2026-09-30.md 생성

## [2026-09-23] daily-sync | 인덱스 +27/+74, 레지스트리 34개 폴더, 크론 에러 0건, 작업 변경 110개
- 인덱스: 신규 27 / 갱신 74 / 총 17,094개 파일 (FTS 16,838, 352.8MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음 (post1 커밋 09-22, car-year-lookup 로컬 파일 수 10→31 증가)
- 크론 에러 0건 — 전일(09-22) card-news-supabase-sync curl 타임아웃은 재발 없음, 정상.
- 작업 변경 110개: MI8_project 55 (카드뉴스 md 발행), car-year-lookup 20 (카히스토리 직접조회 flood check + 기웅 fill + 피해차량 연식추정 CSV v2), auto-trading 2, post1 1, .hermes 32 / git 커밋 2개 저장소 (post1 e6908b1, memories a8ef8e0)
- daily 페이지: concepts/daily/2026-09-23.md 생성

## [2026-09-15] daily-sync | 인덱스 +6/+66, 레지스트리 34개 폴더, 크론 에러 3건, 작업 변경 76개
- 인덱스: 신규 6 / 갱신 66 / 총 17,031개 파일 (FTS 16,775, 351.8MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 3건 — 전부 card-news-supabase-sync (20:50/02:02/03:18) 상태 정리 단계 curl DELETE 10s 타임아웃. 발행·업로드·SEO는 성공하고 cleanup만 실패. 조치 필요.
- 작업 변경 76개: MI8_project 55 (카드뉴스 md 발행), auto-trading 2, post1 1 (git 커밋 bd910d8), .hermes 18 / git 커밋 2개 저장소 (post1 bd910d8, memories 9844886)
- daily 페이지: concepts/daily/2026-09-15.md 생성

## [2026-09-14] daily-sync | 인덱스 +3/+149, 레지스트리 34개 폴더, 크론 에러 0건, 작업 변경 159개
- 인덱스: 신규 3 / 갱신 149 / 총 17,025개 파일 (FTS 16,769, 351.7MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 정상. (4일 연속 에러 0건으로 안정 상태 유지)
- 작업 변경 159개: MI8_project 141 (카드뉴스 md 54 + .seo.json 93 등), auto-trading 1 (주간 시장 분석 보고), post1 1 (git 커밋 6bbae10), .hermes 16 / git 커밋 2개 저장소 (post1 6bbae10, memories 1e814bd)
- daily 페이지: concepts/daily/2026-09-14.md 생성

## [2026-09-13] daily-sync | 인덱스 +6/+64, 레지스트리 34개 폴더, 크론 에러 0건, 작업 변경 78개
- 인덱스: 신규 6 / 갱신 64 / 총 17,022개 파일 (FTS 16,766, 351.7MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 정상. (3일 연속 에러 0건으로 안정 상태)
- 작업 변경 78개: MI8_project 53 (카드뉴스 md 발행), auto-trading 1 (주간 매매 경과 보고), lotto-predictor 1, post1 1 (git 커밋 a4b686a), .hermes 22 / git 커밋 2개 저장소 (post1 a4b686a, memories a1fb6ef)
- daily 페이지: concepts/daily/2026-09-13.md 생성

## [2026-09-12] daily-sync | 인덱스 +7/+66, 레지스트리 34개 폴더, 크론 에러 0건, 작업 변경 79개
- 인덱스: 신규 7 / 갱신 66 / 총 17,016개 파일 (FTS 16,760, 351.6MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 정상. (전일 card-news-supabase-sync PUT 타임아웃은 재발 없음)
- 작업 변경 79개: MI8_project 52 (카드뉴스 md 발행), auto-trading 4, lotto-predictor 2, post1 1 (git 커밋 85b05a6), .hermes 20 / git 커밋 2개 저장소 (post1 85b05a6, memories 3fec7b9)
- daily 페이지: concepts/daily/2026-09-12.md 생성

## [2026-09-11] daily-sync | 인덱스 +8/+70, 레지스트리 34개 폴더, 크론 에러 1건, 작업 변경 84개
- 인덱스: 신규 8 / 갱신 70 / 총 17,009개 파일 (FTS 16,753, 351.5MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 (card-news-supabase-sync 04:30 상태 동기화 PUT curl 타임아웃 10초) — 빌드/SEO/naver_blog 업로드는 정상, 마지막 status.json PUT만 실패. 09-10의 bs4 50건은 해소됨.
- 작업 변경 84개: MI8_project 53 (카드뉴스 md 신규), auto-trading 4, post1 1 (git 커밋 17a9de1), .hermes 26 / git 커밋 2개 저장소 (post1 17a9de1, memories 12a817c)
- daily 페이지: concepts/daily/2026-09-11.md 생성

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-09-10] daily-sync | 인덱스 +5/+13, 레지스트리 34개 폴더 (변동 없음), 크론 에러 50건, 작업 변경 34개
- 인덱스: 신규 5 / 갱신 13 / 총 17,001개 파일 (FTS 16,745, 351.4MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일(09-09)과 동일, 신규 폴더 없음
- 크론 에러 50건 (1개 job — card-news-supabase-sync, 전일과 동일한 bs4 누락):
  - `ModuleNotFoundError: No module named 'bs4'` — `sync-card-news.sh`가 `~/.hermes/hermes-agent/venv/bin/python3`로 `fetch-pending-content.py` 실행 시 bs4 미설치
  - ✅ **조치 완료:** `pip install beautifulsoup4` → import 검증 통과. 다음 2분 주기 실행부터 해소.
- 작업 변경: 34개 (auto-trading 4 / MI8_project 1 / post1 1 / .hermes 28)
- git 커밋: post1 `b8a72ca`, memories `38dc025`
- 새 daily 페이지: concepts/daily/2026-09-10.md

## [2026-09-09] daily-sync | 인덱스 +743/+2503, 레지스트리 34개 폴더 (변동 없음), 크론 에러 60건, 작업 변경 3651개
- 인덱스: 신규 743 / 갱신 2503 / 총 16,996개 파일 (FTS 16,740, 351.3MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 60건 (7개 job, ⚠️ 조치 필요):
  - card-news-supabase-sync 50건 — `ModuleNotFoundError: bs4` (fetch-pending-content.py, failure_streak 528) → `hermes-agent/venv`에 beautifulsoup4 설치 필요
  - opencode-go 라우팅 9건 (naver keepalive 5, auto-trading-briefing/daily-geek/wiki-backup/personal-site 각 1) — `missing x-opencode-session`
  - seo-monitor-search 1건 — `model deepseek-v4-flash HTTP 400`
- 작업 변경 3651개: MI8_project 56 (카드뉴스 md), auto-trading 4, post1 1 / .hermes 3205 (hermes-agent v0.21.1) / git 커밋 4개 저장소 (post1 53b7577, memories d93e64b·ee55f51, hermes-agent 20개)
- daily 페이지: concepts/daily/2026-09-09.md 생성 (09-08 페이지 누락)

## [2026-09-07] daily-sync | 인덱스 +3/+155, 레지스트리 34개 폴더 (변동 없음), 크론 에러 0건, 작업 변경 154개
- 인덱스: 신규 3 / 갱신 155 / 총 16,253개 파일 (FTS 15,998, 357.3MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 — 정상 운영 (전일 대비 소멸/유지)
- 작업 변경 154개: MI8_project 141 (카드뉴스/seo.json), post1 1 (git 커밋 75dc47b), enterprise-search 1, auto-trading 1 / .hermes 10 / git 커밋 2개 저장소 (post1 75dc47b, memories e7e4580)
- daily 페이지: concepts/daily/2026-09-07.md 생성

## [2026-09-06] daily-sync | 인덱스 +8/+65, 레지스트리 34개 폴더 (변동 없음), 크론 에러 1건, 작업 변경 68개
- 인덱스: 신규 8 / 갱신 65 / 총 16,250개 파일 (FTS 15,995, 357.2MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건: card-news-supabase-sync (00:21) — 상태 동기화 status.json PUT curl 10s 타임아웃(단발). **전일 50건 대량 반복 402 결제 오류 소멸 → Supabase 과금 이슈 해소로 판단**, 스크립트 미수정 상태에서 기존 타임아웃 유형으로 회귀. 1건이라 3건 초과 반복 패턴 아님. 제안: 상태 동기화 PUT 타임아웃 상향+재시도/비치명 처리
- 작업 변경 68개: MI8_project 53 (카드뉴스 md), post1 1 (git 커밋 43be202), enterprise-search 1, auto-trading 1, lotto-predictor 1 / .hermes 11 / git 커밋 2개 저장소 (post1 43be202, memories 7a32180)
- daily 페이지: concepts/daily/2026-09-06.md 생성

## [2026-09-05] daily-sync | 인덱스 +20/+71, 레지스트리 34개 폴더 (+1: car-year-lookup), 크론 에러 50건 (조치 필요), 작업 변경 86개
- 인덱스: 신규 20 / 갱신 71 / 총 16,242개 파일 (FTS 15,987, 357.2MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — **신규 로컬 폴더 +1: car-year-lookup** (차량 연식 조회, 10개 파일 변경 감지)
- 크론 에러 50건: card-news-supabase-sync (05:01~05:28, 3분 간격) — 전부 `Error 402: Payment Required`. 전일 타임아웃(09-04)에서 **결제/요금제 문제로 유형 전환** + 3분 간격 무한 반복 루프 = 명백한 반복 패턴(**3건 초과, 조치 필요**). Supabase 대시보드 Billing/Credits 확인 + 연속실패 회로차단 제안
- 작업 변경 86개: MI8_project 52 (카드뉴스 md), car-year-lookup 10 (신규), auto-trading 4, lotto-predictor 2, post1 1 / .hermes 17 / git 커밋 2개 저장소 (post1 8f14fec, memories bf8f97c)
- daily 페이지: concepts/daily/2026-09-05.md 생성

## [2026-09-04] daily-sync | 인덱스 +4393/+3202, 레지스트리 33개 폴더 (변동 없음), 크론 에러 1건, 작업 변경 9069개
- 인덱스: 신규 4393 / 갱신 3202 / 총 16,222개 파일 (FTS 15,967, 356.9MB) — 대부분 hermes-agent 내부 코드(20커밋, schema v30) 반영
- 레지스트리: 33개 폴더 (git 13 / 로컬 20) — 전일 대비 신규 폴더 없음 (post1 커밋 09-03 갱신, web-crawler-work 파일수 14→23)
- 크론 에러 1건: card-news-supabase-sync (05:18) — status.json PUT curl 10초 타임아웃 (상태 정리 단계만 실패, 콘텐츠 발행 정상). 과거 08-24~08-30 반복 이력 재발. 08-30 재시도 래퍼 조치에도 재발 → 타임아웃 상향 + non-fatal 처리 제안
- 작업 변경 9069개: .hermes 7558 (hermes-agent 20커밋), projects 65 (MI8_project 53 카드뉴스 md, web-crawler-work 7, post1 1), git 커밋 3개 저장소 (post1 4b0248e, hermes-agent 20, memories 10a44fe)
- daily 페이지: concepts/daily/2026-09-04.md 생성

## [2026-09-03] daily-sync | 인덱스 +32/+67, 레지스트리 33개 폴더 (+1: web-crawler-work), 크론 에러 1건, 작업 변경 94개
- 인덱스: 신규 32 / 갱신 67 / 총 11,829개 파일 (FTS 11,584, 306.5MB)
- 레지스트리: 33개 폴더 (git 13 / 로컬 20) — **신규 로컬 폴더 +1: web-crawler-work** (부동산 아파트 지도/타일 크롤링, map.html/tiles_SG.json/cl_apt.json)
- 크론 에러 1건: auto-trading-live-daily (14:15) — ZeroDivisionError (live.py:397, 가격 데이터 부족 px=0) / 근본 원인 IGW40023 모의투자 가격 API 미지원. 커밋 d5e9d12로 ZeroDivisionError 방어 반영
- 작업 변경 94개: MI8_project 52 (카드뉴스 md + .published_slugs.txt), web-crawler-work 14 (신규), auto-trading 4, post1 1 / .hermes 23 / git 커밋 3개 저장소 (post1 3652c4a, auto-trading d5e9d12, memories e28019e)
- daily 페이지: concepts/daily/2026-09-03.md 생성

## [2026-09-02] daily-sync | 인덱스 +11/+76, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 81개
- 인덱스: 신규 11 / 갱신 76 / 총 11,797개 파일 (FTS 11,552, 306.2MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건: card-news-supabase-sync (04:52) — curl -X DELETE .status.json 10초 타임아웃 (Storage 정리 단계, 삭제만 실패 / 업로드는 정상)
- 작업 변경 81개: MI8_project 53 (카드뉴스 md 본문 + .published_slugs.txt), auto-trading 7, post1 1 / .hermes 20 / git 커밋 3개 저장소 (post1 2db23c7, auto-trading e3cce6b, memories fe73cc9)
- daily 페이지: concepts/daily/2026-09-02.md 생성

## [2026-09-01] daily-sync | 인덱스 +26/+69, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 87개
- 인덱스: 신규 26 / 갱신 69 / 총 11,786개 파일 (FTS 11,541, 306.0MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일까지 재발하던 card-news-supabase-sync 타임아웃 및 keepalive 이슈 모두 미발생
- 작업 변경 87개: MI8_project 74 (카드뉴스 md 본문 + .published_slugs.txt + .seo.json), auto-trading 4, post1 1 / .hermes 8 / git 커밋 2개 저장소 (post1 5330cb7, memories c010173)
- daily 페이지: concepts/daily/2026-09-01.md 생성

## [2026-08-31] daily-sync | 인덱스 +3/+149, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 148개
- 인덱스: 신규 3 / 갱신 149 / 총 11,760개 파일 (FTS 11,515, 304.1MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일까지 재발하던 card-news-supabase-sync 타임아웃 및 keepalive 이슈 모두 미발생
- 작업 변경 148개: MI8_project 141 (카드뉴스 SEO .seo.json 대량 회귀 + md 본문), post1 1 (git 커밋 b45ff1f), auto-trading 1 / git 커밋 2개 저장소 (post1 b45ff1f, memories bcfc828)
- daily 페이지: concepts/daily/2026-08-31.md 생성

## [2026-08-30] daily-sync | 인덱스 +5/-0, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 67개
- 인덱스: 신규 5 / 갱신 67 / 총 11,757개 파일 (FTS 11,512, 304.1MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 — card-news-supabase-sync (05:00, Supabase `.status.json` curl PUT 타임아웃 10초). **7일 창(08-24~30)에서 6회 재발** — PUT/DELETE 교차, 간헐 절정 구간 (08-26·27 소멸 후 3일 연속 재발). 단건이라 "3건 이상 반복" 기준은 미달이나 명백한 재발성 패턴 → 재시도 래퍼(타임아웃 30초 + --retry/지수 백오프) 명시적 조치 제안.
- 작업 변경 67개: MI8_project 53 (카드뉴스 md + 발행 slug), lotto-predictor 2, auto-trading 1, post1 1 / .hermes 10 / git 커밋 2개 저장소 (post1 9d632af, memories 8300425)

## [2026-08-28] daily-sync | 인덱스 +9/-0, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 81개
- 인덱스: 신규 9 / 갱신 66 / 총 11,745개 파일 (FTS 11,500, 303.9MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 — card-news-supabase-sync (05:20, Supabase `.status.json` curl PUT 타임아웃 10초). 5일 창(08-24~28)에서 이 원인 4회 재발성 간헐 이슈 (08-26·27 소멸 후 재발). 단건이라 "3건 이상 반복" 기준은 미달, 관찰 유지 + 재시도 규칙 추가 권장.
- 작업 변경 81개: MI8_project 65 (카드뉴스 md + 발행 slug), auto-trading 4 (트랙 리포트), post1 1 / .hermes 11 / git 커밋 2개 저장소 (post1 99550fe, memories 278e56d)

## [2026-08-27] daily-sync | 인덱스 +4/-0, 레지스트리 32개 폴더, 크론 에러 3건 (조치 필요), 작업 변경 68개
- 인덱스: 신규 4 / 갱신 64 / 총 11,736개 파일 (FTS 11,491, 303.8MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 3건 — **단일 유형 반복 (조치 필요)**: naver-session-hourly-keepalive 2회 (23:00, 00:00) + daily-memory-to-notion 1회 (00:00), 전부 `HTTP 401: Model ox-alpha-free is not supported` — 크론 job이 지원되지 않는 모델(ox-alpha-free)로 지정됨
- 작업 변경 68개: MI8_project 51 (카드뉴스 md + 발행 slug), auto-trading 4 (트랙 리포트), post1 1 / .hermes 12 / git 커밋 2개 저장소 (post1 de32ddf, memories 3c29952)

## [2026-08-26] daily-sync | 인덱스 +6/-0, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 70개
- 인덱스: 신규 6 / 갱신 69 / 총 11,731개 파일 (FTS 11,486, 303.7MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일 반복되던 card-news-supabase-sync 타임아웃 소멸, 경과 관찰 유지
- 작업 변경 70개: MI8_project 52 (카드뉴스 md + 발행 slug), auto-trading 4 (트랙 리포트), post1 1 / .hermes 13 / git 커밋 2개 저장소 (post1 f5aa224, memories c62e7c6)

## [2026-08-25] daily-sync | 인덱스 +5/-0, 레지스트리 32개 폴더, 크론 에러 4건, 작업 변경 67개
- 인덱스: 신규 5 / 갱신 69 / 총 11,725개 파일 (FTS 11,480, 303.7MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 4건 — **2개 유형 (조치 필요)**: card-news-supabase-sync 2회 (23:30, 23:52, Supabase 상태 동기화 curl PUT 타임아웃 10초 — 48h 내 동일 원인 3회 반복, 미해결), telecom-3sa-daily-news + auto-trading-morning-briefing 2건 (08:30, HTTP 401 Insufficient balance — opencode.ai 워크스페이스 결제 잔액 부족)
- 작업 변경 67개: MI8_project 54 (카드뉴스 md), auto-trading 4, post1 1 (git 커밋 e0320fa) / git 커밋 2개 저장소

## [2026-08-24] daily-sync | 인덱스 +4/+149, 레지스트리 32개 폴더, 크론 에러 1건 (card-news-supabase-sync 타임아웃), 작업 변경 149개

## [2026-08-23] daily-sync | 인덱스 +5/+68, 레지스트리 32개 폴더, 크론 에러 17건 (inference config drift unpinned), 작업 변경 72개

## [2026-06-01] create | Wiki initialized
- Domain: Personal knowledge base
- Structure created with SCHEMA.md, index.md, log.md
- Karpathy LLM Wiki pattern: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## [2026-06-01] ingest | Karpathy LLM Wiki from https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## [2026-06-01] lint | 1 issues found

## [2026-06-01] batch_ingest | PC files: 60 new, 10 skip, 0 fail

## [2026-06-01] batch_ingest | PC files: 0 new, 70 skip, 0 fail

## [2026-06-01] lint | 4 issues found

## [2026-06-02] batch_ingest | PC files: 3 new, 69 skip, 0 fail

## [2026-06-02] lint | 4 issues found

## [2026-06-03] batch_ingest | PC files: 2 new, 72 skip, 0 fail

## [2026-06-03] lint | 4 issues found

## [2026-06-04] batch_ingest | PC files: 2 new, 74 skip, 0 fail

## [2026-06-04] lint | 4 issues found

## [2026-06-05] batch_ingest | PC files: 2 new, 76 skip, 0 fail

## [2026-06-05] lint | 4 issues found

## [2026-06-07] batch_ingest | PC files: 3 new, 78 skip, 0 fail

## [2026-06-07] lint | 4 issues found

## [2026-06-08] batch_ingest | PC files: 3 new, 80 skip, 0 fail

## [2026-06-08] lint | 4 issues found

## [2026-06-09] batch_ingest | PC files: 3 new, 82 skip, 0 fail

## [2026-06-09] lint | 3 issues found

## [2026-06-10] lint | 3 issues found

## [2026-06-10] batch_ingest | PC files: 3 new, 80 skip, 0 fail

## [2026-06-10] lint | 3 issues found

## [2026-06-11] batch_ingest | PC files: 2 new, 87 skip, 0 fail

## [2026-06-11] lint | 3 issues found

## [2026-06-11] lint | 3 issues found

## [2026-06-12] batch_ingest | PC files: 8 new, 88 skip, 0 fail

## [2026-06-12] lint | 3 issues found

## [2026-06-13] batch_ingest | PC files: 2 new, 96 skip, 0 fail

## [2026-06-13] lint | 3 issues found

## [2026-06-13] ingest | us-stock-tax from file: /Users/bearj/documents/tax-research/us-stock-tax.md

## [2026-06-13] ingest | jp-stock-tax from file: /Users/bearj/documents/tax-research/jp-stock-tax.md

## [2026-06-13] ingest | eu-stock-tax from file: /Users/bearj/documents/tax-research/eu-stock-tax.md

## [2026-06-13] ingest | kr-stock-tax from file: /Users/bearj/documents/tax-research/kr-stock-tax.md

## [2026-06-13] ingest | real-estate-tax from file: /Users/bearj/documents/tax-research/real-estate-tax.md

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 3 issues found

## [2026-06-13] lint | 2 issues found

## 2026-06-13
- llm-wiki 대규모 재구성: 164개 → 84개 페이지
- 논문/뉴스 107개 → raw/archive/ 이동
- concepts/ 카테고리별 폴더 생성 (projects/knowledge/learnings/daily/)
- 84개 파일 wikilink 연결 완료
- 세제 조사 5개 knowledge/ 에 ingest + 상호 크로스레퍼런스
- devbox.md 추가 (추천글 정리)
- SCHEMA.md 업데이트: 구조 + 추천글 정리 규칙
- index.md 재작성: 카테고리별 분류

## [2026-06-14] lint | 2 issues found

## [2026-06-15] sync | Daily sync executed
- 2 changed files detected: world_news_20260614.md, world_news_20260615.md
- All external content → skipped (not added to concepts/)
- Daily page created: concepts/daily/2026-06-15.md
- index.md updated

## [2026-06-15] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-16] lint | 2 issues found

## [2026-06-17] lint | 2 issues found

## [2026-06-17] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-18] lint | 2 issues found

## [2026-06-20] lint | 2 issues found

## [2026-06-20] lint | 2 issues found

## [2026-06-20] lint | 2 issues found

## [2026-06-21] lint | 2 issues found

## [2026-06-22] lint | 2 issues found

## [2026-06-22] lint | 2 issues found

## [2026-06-23] lint | 2 issues found

## [2026-06-23] lint | 2 issues found

## [2026-06-24] lint | 2 issues found

## [2026-06-24] lint | 2 issues found

## [2026-06-25] sync | daily 2026-06-24 updated, 8 new work items
- Updated: concepts/daily/2026-06-24.md — added 6/24 work summary (주식 분석, 뉴스, 사이트 배포, 칸반)
- Skipped: world_news_20260625.md (external content → raw/archive only)
- Index updated: Daily section added

## [2026-06-25] lint | 2 issues found

## [2026-06-26] sync | 2 new pages, 1 skipped
- New: concepts/daily/2026-06-25.md — 6/25 work log (주식 분석, 뉴스, 사이트 배포, 칸반)
- New: concepts/knowledge/code-edu-lab-curriculum.md — Code Edu Lab 4스택 커리큘럼 요약
- Skipped: world_news_20260626.md (external content → not synced to concepts)
- Index updated: 2 new entries in Concepts section

## [2026-06-26] lint | 2 issues found

## [2026-06-26] lint | 2 issues found

## [2026-06-27] lint | 2 issues found

## [2026-06-29] lint | 2 issues found

## [2026-06-30] lint | 2 issues found

## [2026-07-07] lint | 2 issues found

## [2026-07-07] lint | 2 issues found

## [2026-07-08] lint | 2 issues found

## [2026-07-09] lint | 2 issues found

## [2026-07-09] lint | 2 issues found

## [2026-07-11] lint | 2 issues found

## [2026-07-11] lint | 2 issues found

## [2026-07-12] lint | 2 issues found

## [2026-07-13] lint | 2 issues found

## [2026-07-13] lint | 2 issues found

## [2026-07-13] lint | 2 issues found

## [2026-07-14] lint | 2 issues found

## [2026-07-15] lint | 2 issues found

## [2026-07-16] lint | 2 issues found

## [2026-07-16] lint | 2 issues found

## [2026-07-16] lint | 2 issues found

## [2026-08-09] daily-sync | 작업 변경 감지 75개, daily 페이지 갱신 (2026-08-09.md 생성)
- collect_work.py 신규 도입: ~/projects + ~/.hermes 작업 변경 감지 파이프라인
- llm-wiki-daily-sync 크론 프롬프트 교체 (외부 수집 금지 → 작업 내역 수집)

## [2026-08-09] lint | 2 issues found

## [2026-08-09] wiki-v4 | 위키 전면 재구축 (외부 콘텐츠 삭제 → Hermes 작업 인덱스)
- 기존 raw 2,448 + concepts 266 + entities 10 삭제 (git 태그 legacy-wiki-2026-08-09로 보존)
- build_index.py: 10,806개 작업 파일 FTS5 인덱싱 (5.4초)
- search.py: FTS5 + RAG 답변 CLI
- web.py: /api/search 통합 검색
- SCHEMA.md v2 재작성, llm-wiki 스킬 v4 업데이트

## [2026-08-09] cron-errors | collect_cron_errors.py 도입, 24h 내 에러 8건 분석 기록
- collect_cron_errors.py 신규: 크론 output에서 최근 24h FAILED/Error 수집
- llm-wiki-daily-sync 프롬프트에 에러 분석 단계 추가 (패턴 분석 + 개선 제안)
- 8건 분석: naver-session-hourly-keepalive 5회 반복 (Broken pipe) — 재시도 적용 검토 대상

## [2026-08-09] personal-sites | 개인 사이트 폴더 내역 기록 (중복 방지)
- concepts/projects/personal-sites.md 신규 생성: justfly32.github.io(포트폴리오) / post1(활동로그) / personal-site(구 프로토타입) 3개 폴더 역할·위치·갱신방식 정리
- index.md 카탈로그 등록 (Total pages: 1)
- 목적: personal-site→post1 진화 구조를 기록해 폴더 중복 생성 방지

## [2026-08-09] project-registry | 프로젝트 폴더 레지스트리 도입 (중복 방지 시스템)
- generate_project_registry.py 신규: ~/projects + justfly32.github.io 스캔 → concepts/projects/project-registry.md 자동 생성 (36개 폴더, git 11/로컬 25)
- 중복 유사 후보 6그룹 식별: 건강관리(elderly-health×2), GIF(simpli×5), 대시보드(system×3), PPT(html2pptx/PPT_Generator), 개인사이트(personal-site/post1), 코딩교육(code-edu×3)
- hermes-orchestration 스킬에 "코딩 전 레지스트리 조회" 필수 규칙 추가
- 갱신 명령: python3 ~/wiki/scripts/generate_project_registry.py

## [2026-08-09] project-registry-cleanup | 비정본 7개 폴더 삭제 (휴지통 이동)
- 정리 3개 그룹(건강관리·코딩 교육·GIF) 비정본 확정 후 삭제: elderly-health, code-tutorial, code-express, simple-anim-maker, simpli-video-maker, animation-maker, stickman-gif-creator
- 삭제 방식: ~/.Trash/hermes-removed-20260809/ 로 이동 (복구 가능), code-tutorial은 GitHub 원격 백업 존재
- 사전 검증: 크론/스크립트/포트폴리오(justfly32.github.io) 참조 없음 확인 후 삭제
- 레지스트리 갱신: 36 → 29개 폴더 (git 9/로컬 20), CANONICAL 3개 정본만 유지 (elderly-health-care, code-edu-lab, simpli-gif-maker)
- generate_project_registry.py에 REMOVED 섹션 + 삭제 기록 표 추가, index.md 설명 갱신

## [2026-08-09] registry-auto | llm-wiki-daily-sync에 레지스트리 자동 재생성 추가
- llm-wiki-daily-sync 크론(매일 05:30) 프롬프트에 Step 1.5 추가: generate_project_registry.py 실행
- 새 폴더 생성 시 ~/projects 스캔 → project-registry.md 자동 갱신 (다음 날 05:30 반영)
- 최종 보고에 레지스트리 폴더 수 + 신규 폴더 이름 포함하도록 변경
- llm-wiki 스킬 SKILL.md 크론 섹션에도 반영 (1~6단계로 재구성)

## [2026-08-09] dashboard-merge | 대시보드 3종 → pc-llm-dashboard 단일 통합
- 배경: system-dashboard / system-monitor-dashboard / openclaw-token-dashboard 3개가 동일 기능 복제본임을 확인 (라우트 동일, 같은 날 생성)
- 기능 정체성 확정: PC 상태 확인 + LLM 사용량 확인 → 폴더명을 기능 기준 pc-llm-dashboard로 신설
- 코드 베이스: openclaw-token-dashboard(리팩토링 완료, useMemo/fetchStats) 채택, system-dashboard와 diff 비교 후 고유 기능 없음 확인
- 검증: npm install + build 성공, dev 서버 기동 (API 4010 / Vite 5175), health·system-status·hermes-stats(3.4억 토큰/1,877세션)·openclaw-stats 정상 응답, title PC·LLM 대시보드로 변경
- 기존 3개 폴더 → ~/.Trash/hermes-removed-20260809/ 이동
- 레지스트리: 29 → 27개, CANONICAL에 pc-llm-dashboard 등록, 대시보드 그룹 중복 후보 제거

## [2026-08-09] personal-site-move | justfly32.github.io를 projects로 이동
- 사용자 발견: 개인 사이트 폴더가 home 직속(~/justfly32.github.io)에 있어 projects와 분산
- 이동: ~/justfly32.github.io → ~/projects/justfly32.github.io (git remote/branch 그대로, clean 상태)
- 참조 확인: post1 크론은 /Users/bearj/projects/post1 사용(무관), jobs.json의 justfly32는 URL 텍스트뿐 → 파일 경로 참조는 레지스트리 EXTRA_DIRS뿐
- generate_project_registry.py: EXTRA_DIRS 비움(projects 스캔으로 자동 포함), 규칙 문구를 "개인 사이트 포함 projects 통일"로 변경
- personal-sites.md: 위치/규칙 갱신 (home 직속 금지 추가)
- 레지스트리: 27 → 28개 폴더 (justfly32.github.io가 git 프로젝트로 합류, git 10개)

## [2026-08-09] enterprise-search | 사내 파일 검색 PoC 구축
- 신규 프로젝트: ~/projects/enterprise-search (Next.js 16 + FastAPI + SQLite/Supabase RLS)
- FileAccessor 인터페이스 (DRM 무관 추상화): LocalFileAccessor 구현, 파수/마크애니/MIP는 제품 확정 후 추가 예정
- 인덱서: FTS5(bm25) + n-gram 벡터(cosine) 하이브리드, mtime 증분
- 권한 모델: 파일별 ACL(dept/role/users) → 검색 단계 차단 (Glean Permission Mirroring 원칙)
- 검증: CLI 5개 시나리오 + 브라우저 E2E — 일반 직원 급여 차단, 법무팀 계약서 접근, admin 전체 접근, RAG 답변(월 1,500만원/건당 300만원) + 출처 표기
- 배운 점: HTTP 헤더 한글 불가 → 사용자 컨텍스트는 body 전달 (브라우저 fetch 제약), Next 15.4.1→16.3.0 필요 (Node22 호환)
- schema/supabase.sql: documents + file_acl + RLS + pgvector (운영용)

## [2026-08-10] daily-sync | 인덱스 +43/-162, 레지스트리 29개 폴더, 크론 에러 7건, 작업 변경 271개
- 인덱스: 신규 43 / 갱신 162 / 총 11,120개 파일 (FTS 10,880)
- 레지스트리: 28 → 29개 폴더 (git 11 / 로컬 18) — enterprise-search 신규 합류
- 크론 에러 7건: naver-session-hourly-keepalive 4 (2일 연속 반복, 조치 필요), Broken pipe 5 / empty stream 2
- 작업 변경 271개: MI8_project 138, enterprise-search 51, pc-llm-dashboard 25, justfly32.github.io 2, post1 1 / git 커밋 3개 저장소 22건
## [2026-08-11] daily-sync | 인덱스 +8/+67, 레지스트리 29개 폴더, 크론 에러 10건, 작업 변경 70개
- 인덱스: 신규 8 / 갱신 67 / 총 11,128개 파일 (FTS 10,888)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 10건: naver-session-hourly-keepalive 5 (3일 연속 반복, 조치 필요), Broken pipe 6 (09:08~10:10 집중) / empty stream 3, llm-wiki-daily-sync 1건은 오탐
- 작업 변경 70개: MI8_project 50 (카드뉴스 md), post1 1 / git 커밋 1건
## [2026-08-12] daily-sync | 인덱스 +7/+64, 레지스트리 29개 폴더, 크론 에러 8건, 작업 변경 66개
- 인덱스: 신규 7 / 갱신 64 / 총 11,135개 파일 (FTS 10,895)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 8건 (오탐 1 제외 실질 7): naver-session-hourly-keepalive 5 (4일 연속 반복, 조치 필요), Broken pipe 5 (09:09~10:09 집중, 2일 연속 동일 창) / empty stream 2, llm-wiki-daily-sync 1건은 오탐 (2일 연속)
- 작업 변경 66개: MI8_project 50 (카드뉴스 md), post1 1 / git 커밋 1건
## [2026-08-13] daily-sync | 인덱스 +12/+58, 레지스트리 29개 폴더, 크론 에러 8건, 작업 변경 76개
- 인덱스: 신규 12 / 갱신 58 / 총 11,147개 파일 (FTS 10,907)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 8건 (오탐 1 제외 실질 7): naver-session-hourly-keepalive 4 (5일 연속 반복, 조치 필요), Broken pipe 5 (09:09~10:09 3건 집중, 3일 연속 동일 창) / empty stream 2, seo-optimizer-daily 1건 신규 출현 (21:09), llm-wiki-daily-sync 1건은 오탐 (3일 연속)
- 작업 변경 76개: MI8_project 61 (카드뉴스 md), post1 1 (git 커밋 fe70f18) / git 커밋 1건

## [2026-08-15] daily-sync | 인덱스 +10/+61, 레지스트리 29개 폴더, 크론 에러 10건, 작업 변경 66개
- 인덱스: 신규 10 / 갱신 61 / 총 11,165개 파일 (FTS 10,925)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 10건 (오탐 1 제외 실질 9): naver-session-hourly-keepalive 6 (7일 연속 반복 + 전일 3→6 2배 급증, 조치 필요), Broken pipe 9건 전부 (01:08~21:09 전 시간대 확산, 09:09 3건/21:09 2건 동시), seo-optimizer-daily 2일 연속 21:09 동일 시각 재발, llm-wiki-daily-sync 1건 오탐 (5일 연속)
- 작업 변경 66개: MI8_project 50 (카드뉴스 md), lotto-predictor 2, post1 1 (git 커밋 073dc53) / git 커밋 1건

## [2026-08-14] daily-sync | 인덱스 +7/+57, 레지스트리 29개 폴더, 크론 에러 7건, 작업 변경 73개
- 인덱스: 신규 7 / 갱신 57 / 총 11,155개 파일 (FTS 10,915)
- 레지스트리: 29개 폴더 (git 11 / 로컬 18) — 전일과 동일, 신규 폴더 없음
- 크론 에러 7건 (오탐 1 제외 실질 6): naver-session-hourly-keepalive 3 (6일 연속 반복, 조치 필요), Broken pipe 5 (09:08~10:09 4건 집중 3일 연속 + 01:09 확산), card-news-supabase-sync 1건 신규 (Duplicate KeyAlreadyExists), llm-wiki-daily-sync 1건 오탐 (4일 연속)
- 작업 변경 73개: MI8_project 62 (카드뉴스 md 54 + 이미지 11), post1 1 (git 커밋 3911341) / git 커밋 1건

## [2026-08-16] daily-sync | 인덱스 +218/+64, 레지스트리 31개 폴더, 크론 에러 9건, 작업 변경 277개
- 인덱스: 신규 218 / 갱신 64 / 총 11,383개 파일 (FTS 11,138, 298.6MB)
- 레지스트리: 31개 폴더 (git 12 / 로컬 19) — 전일 29개에서 +2. 신규: auto-trading (git, 한국 주식 자동매매, 최근 커밋 2026-08-16), auto-trading-research (로컬)
- 크론 에러 9건 (오탐 1 제외 실질 8): naver-session-hourly-keepalive 5 (8일 연속 반복, 조치 필요, Broken pipe 4 + empty stream 1, 09~13시 집중 + 01:09 확산), seo-monitor-search 1 (10:09), telecom-3sa-daily-news 1 (09:09), card-news-supabase-sync 1 (Duplicate KeyAlreadyExists 03:11, 2일 간격 재발), llm-wiki-daily-sync 1건 오탐 (6일 연속)
- 작업 변경 277개: auto-trading 190 (git 커밋 20건: 금 10% 동적 리밸런스, bear_recovery_days 15→0, 5년 백테스트), MI8_project 50 (카드뉴스 md), auto-trading-research 2 (신규), post1 1 (git 커밋 a1fb013), lotto-predictor 1 / git 커밋 21건 (2개 저장소)

## [2026-08-17] daily-sync | 인덱스 +32/+159, 레지스트리 31개 폴더, 크론 에러 2건, 작업 변경 195개
- 인덱스: 신규 32 / 갱신 159 / 총 11,415개 파일 (FTS 11,170, 299.0MB)
- 레지스트리: 31개 폴더 (git 12 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 2건 (오탐 1 제외 실질 1): naver-session-hourly-keepalive 1 (Broken pipe 01:09, 9일 연속 반복, 조치 필요 — 전일 5건→1건 급감), llm-wiki-daily-sync 1건 오탐 (7일 연속)
- 작업 변경 195개: MI8_project 147 (카드뉴스 .seo.json — 전일 50→147 급증), auto-trading 13 (git 커밋 7건: trading-rules.md 단일 문서, 장중 체크 10시+14시, 트레일링 스톱 10% 확정), post1 1 (git 커밋 9763644) / git 커밋 8건 (2개 저장소)

## [2026-08-18] daily-sync | 인덱스 +230/+71, 레지스트리 32개 폴더 (신규: slide-master), 크론 에러 오탐 1건→수정, 작업 변경 306개 (MI8 77, slide-master 65, post1 커밋 1)

## [2026-08-19] daily-sync | 인덱스 +29/+68, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 105개
- 인덱스: 신규 29 / 갱신 68 / 총 11,674개 파일 (FTS 11,429, 303.2MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건: card-news-supabase-sync (Duplicate KeyAlreadyExists 23:20, 주 3회 이상 재발, 조치 필요)
- 작업 변경 105개: MI8_project 64 (카드뉴스 md), auto-trading 20 (git 커밋 77012b2: NHPLUG 라이브 연동), post1 1 (git 커밋 d26b40f) / git 커밋 2건 (2개 저장소)

## [2026-08-21] daily-sync | 인덱스 +10/+78, 레지스트리 32개 폴더, 크론 에러 2건, 작업 변경 83개
- 인덱스: 신규 10 / 갱신 78 / 총 11,704개 파일 (FTS 11,459, 303.5MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 2건: (1) card-news-supabase-sync 03:21 — Supabase status.json DELETE curl 10초 타임아웃(TimeExpired), (2) auto-trading 16:05 — NHPLUG 22642 주문가격 입력 불가 (시간외 71, 커밋 8a2f7e3으로 수정 완료)
- 작업 변경 83개: MI8_project 52 (카드뉴스 md), auto-trading 11 (git 커밋 8건: 장후코어 81 정합, bull_hold 매도 억제, --no-save), post1 1 (git 커밋 978ee99) / git 커밋 3개 저장소

## [2026-08-22] daily-sync | 인덱스 +7/+67, 레지스트리 32개 폴더, 크론 에러 16건, 작업 변경 69개
- 인덱스: 신규 7 / 갱신 67 / 총 11,711개 파일 (FTS 11,466, 303.6MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 16건 — **모두 동일 유형 (인퍼런스 설정 drift, unpinned, 조치 필요)**: naver-session-hourly-keepalive 15회(매시간 14:00~05:00), auto-trading-evening-briefing 1회. 원인: 글로벌 설정 migrate(provider opencode-go→openrouter, model deepseek-v4-flash→deepseek/deepseek-v4-flash-0731) 후 unpinned 작업 안전 차단. 해결: 각 job을 `cronjob action=update`로 pin.
## [2026-09-21] daily-sync | 인덱스 +6/+152, 레지스트리 34개 폴더, 크론 에러 0건, 작업 변경 163개
- 인덱스: 신규 4 / 갱신 63 / 총 17,055개 파일 (FTS 16,799, 352.0MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 2건 (card-news-supabase-sync 05:21 상태 정리 PUT 10s 타임아웃 — 4일 연속 재발, 조치 필요 / seo-monitor-analyze 09-19 19:00 HTTP 530 업스트림 오류 단발)
- 작업 변경 72개: MI8_project 53 (카드뉴스 md), auto-trading 1, lotto-predictor 1, post1 1 (git 커밋 df2d110), .hermes 16 / git 커밋 2개 저장소 (post1 df2d110, memories 86095db)
- daily 페이지: concepts/daily/2026-09-20.md 생성

- 작업 변경 69개: MI8_project 51 (카드뉴스 md), auto-trading 4, lotto-predictor 2, post1 1 (git 커밋 cc3f963) / git 커밋 2개 저장소

## [2026-08-20] daily-sync | 인덱스 +0/+55, 레지스트리 32개 폴더, 크론 에러 0건, 작업 변경 96개
- 인덱스: 신규 0 / 갱신 55 / 총 11,694개 파일 (FTS 11,449, 303.3MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 0건 (정상) — 전일까지 재발하던 card-news-supabase-sync Duplicate 미발생
- 작업 변경 96개: MI8_project 52 (카드뉴스 md), auto-trading 14 (git 커밋 7건: 장중/장후 모드 분리, env별 분리, ops-runbook), post1 1 (git 커밋 0ce483a) / git 커밋 3개 저장소

## [2026-08-29] daily-sync | 인덱스 +7/+65, 레지스트리 32개 폴더, 크론 에러 1건, 작업 변경 68개
- 인덱스: 신규 7 / 갱신 65 / 총 11,752개 파일 (FTS 11,507, 304.0MB)
- 레지스트리: 32개 폴더 (git 13 / 로컬 19) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 (card-news-supabase-sync 05:02 상태 정리 DELETE curl 타임아웃 10초) — 콘텐츠 업로드/SEO 정상, 정리 단계만 실패
- 작업 변경 68개: MI8_project 52 (카드뉴스 md), auto-trading 4, lotto-predictor 2, post1 1 (git 커밋 df5514f), .hermes 9 / git 커밋 2개 저장소 (post1 df5514f, memories 1ccdcae)
- daily 페이지: concepts/daily/2026-08-29.md 생성

## [2026-09-18] daily-sync | 인덱스 +6/+65, 레지스트리 34개 폴더, 크론 에러 1건, 작업 변경 76개
- 인덱스: 신규 6 / 갱신 65 / 총 17,045개 파일 (FTS 16,789, 351.9MB)
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 전일과 동일, 신규 폴더 없음
- 크론 에러 1건 (card-news-supabase-sync 23:48) — 상태 정리 단계 curl DELETE 10s 타임아웃. 발행·업로드·SEO·네이버 미리보기는 성공, cleanup만 실패. (상위 2일 + 오늘: 09-15 3건 / 09-17 2건 / 09-18 1건 — DELETE 타임아웃 반복 재발, max-time 상향 + 실패 시 continue 제안)
- 작업 변경 76개: MI8_project 53 (카드뉴스 md 51 재발행 + .seo-context), auto-trading 2 (라이브 추적), post1 1 (git 커밋 e067289), .hermes 20 / git 커밋 2개 저장소 (post1 e067289, memories d87567b)
- daily 페이지: concepts/daily/2026-09-18.md 생성

## [2026-09-17] daily-sync | 인덱스 +8/+75, 레지스트리 34개 폴더, 크론 에러 12건(모델 프로바이더 연결 10 + card-news DELETE 타임아웃 2), 작업 변경 79개

## [2026-09-19] daily-sync | 인덱스 +6/+67, 레지스트리 34개 폴더, 크론 에러 1건, 작업 변경 78개
- 인덱스: 신규 6 / 갱신 67, 총 17,051개 (FTS 16,795). 루트별 hermes 12,411 / projects 4,101 / documents 276 / wiki 263
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 신규 폴더 없음
- 크론 에러 1건 (card-news-supabase-sync 09-18 23:56) — 상태 정리 단계 curl PUT(.status.json status=completed) 10s 타임아웃. 51개 발행·업로드·SEO·네이버 미리보기는 성공, update_status()만 실패. (상위 3일: 09-15 3건 / 09-17 2건 / 09-18 1건+오늘 — PUT/DELETE 모두 반복 재발, 3일 연속 → 조치 필요, max-time 상향 + 실패 시 continue 제안)
- 작업 변경 78개: MI8_project 52 (카드뉴스 md 51 재발행 + .published_slugs), auto-trading 4 (LiveEngine ma_rsi 누락 버그 수정 863258c + 전략 이중 구조 문서화 2d5d976), post1 1 (커밋 fcfdde2), lotto-predictor 1, .hermes 20 / git 커밋 3개 저장소 (post1 fcfdde2, auto-trading 2, memories 1a3bb69)
- daily 페이지: concepts/daily/2026-09-19.md 생성

## [2026-09-22] daily-sync | 인덱스 +6/+64, 레지스트리 34개 폴더, 크론 에러 1건, 작업 변경 72개
- 인덱스: 신규 6 / 갱신 64, 총 17,067개 (FTS 16,811). 루트별 hermes 12,418 / projects 4,103 / documents 280 / wiki 266
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 신규 폴더 없음
- 크론 에러 1건 (card-news-supabase-sync 09-22 00:22) — 상태 정리 단계 curl PUT(.status.json) 10s 타임아웃. 51개 발행·업로드·SEO·네이버 미리보기는 성공, update_status()만 실패. 지난 3일간 동일 job 같은 패턴 재발 (09-15 3건 / 09-17 2건 / 09-18 1건 + 오늘) → 4일 연속 → 조치 필요 (curl max-time 상향 + 실패 시 continue)
- 작업 변경 72개: MI8_project 55 (카드뉴스 md 51 재발행 + published_slugs), auto-trading 2, post1 1, .hermes 14 / git 커밋 2개 저장소 (post1 027fe36, memories c54a773)
- daily 페이지: concepts/daily/2026-09-22.md 생성

## [2026-09-24] daily-sync | 인덱스 +25/-0, 레지스트리 34개 폴더, 크론 에러 2건, 작업 변경 104개

## [2026-09-26] daily-sync | 인덱스 +8/+70, 레지스트리 34개 폴더, 크론 에러 5건, 작업 변경 89개
- 인덱스: 신규 8 / 갱신 70, 총 17,127개 (FTS 16,871, 355.4MB). 루트별 hermes 12,430 / projects 4,142 / documents 286 / wiki 269
- 레지스트리: 34개 폴더 (git 13 / 로컬 21) — 신규 폴더 없음
- 크론 에러 5건 (전부 09-25 발생, 오늘 미발생) — 동일 유형 `RuntimeError: agent reported failure`(빈 메시지): Daily World News / Wiki Git Backup / personal site notify (06:00), telecom-3sa-daily-news / auto-trading-morning-briefing (08:30). 서로 다른 job이 동일 시각대 동일 RuntimeError → 일시적 인퍼런스/프로바이더 장애 추정. 3건 반복 패턴은 아니나 동일 유형 다발 → 주시 (지연 재시도, 실행시간대 분산 제안)
- 작업 변경 89개: MI8_project 53 (카드뉴스 md ~50 재발행 + .published_slugs + 재개_가이드), lotto-predictor 2, post1 1, auto-trading 1, .hermes 32 / git 커밋 3개 저장소 (MI8_project 3cfa37bd, post1 528ca88, memories 0a9f827)
- daily 페이지: concepts/daily/2026-09-26.md 생성

## [2026-09-27] daily-sync | 인덱스 +151/+11, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 175개
- 인덱스: 신규 151 / 갱신 11 (텍스트 없음 스킵 4), 총 17,278개 (FTS 17,019, 356.7MB). 루트별 hermes 12,439 / projects 4,282 / documents 287 / wiki 270
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — **+1 신규: my-local-agent** (git 프로젝트로 등록, 사내 LLM 업무도우미)
- 크론 에러 0건 — 전일(09-25) 5건 RuntimeError 다발 이후 완전 회복 확인.
- 작업 변경 175개: my-local-agent 146 (워크플로우 자동화 v0.29~v0.33 — 예약 자동실행·대량반복·엑셀 내보내기·workflow.from_history), post1 1, auto-trading 1 / git 커밋 3개 저장소 (my-local-agent 20개: 3fd1eb2 등, post1 fd0b7ff, memories 5b70b99)
- daily 페이지: concepts/daily/2026-09-27.md 생성

## [2026-09-28] daily-sync | 인덱스 +46/+42, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 104개
- 인덱스: 신규 46 / 갱신 42 (텍스트 없음 스킵 0), 총 17,324개 (FTS 17,065, 357.2MB). 루트별 hermes 12,443 / projects 4,320 / documents 290 / wiki 271
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 신규 폴더 없음
- 크론 에러 0건 — 2일 연속 안정 (09-24~25 인퍼런스/타임아웃 다발 이후 회복 유지)
- 작업 변경 104개: my-local-agent 75 (v0.45.0~v0.46.0 — 시작 전 묻기·부분 수정·백그라운드 UX, 빈 업무 후보+오류 4회 중단, 감시 폴더 쓰기+무인 실패 원인 보존 + 현장 체크리스트 §11~12), post1 1, auto-trading 1 / git 커밋 3개 저장소 (my-local-agent 20개: 6201f2e 등, post1 31bc814, memories 93c64cc)
- daily 페이지: concepts/daily/2026-09-28.md 생성

## [2026-10-02] daily-sync | 인덱스 +14/+9, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 32개
- 인덱스: 신규 14 / 갱신 9 (텍스트 없음 스킵 0), 총 17,367개 (FTS 17,108, 357.6MB). 루트별 hermes 12,465 / projects 4,328 / documents 299 / wiki 275
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 신규 폴더 없음 (전일과 동일)
- 크론 에러 0건 — 6일 연속 크론 안정 유지, 정상.
- 작업 변경 32개: park_watch (주차 감시) 스크립트 하루 5회 수정 보강(백업: 1042/1043_bigo/1046_37/1137_step/1139_holiday, 최종 17:37) + 상태 파일 3종, post1 1 (커밋 bce81f2), auto-trading 리포트 2 (라이브 추적 데이터 자동 갱신), 스킬 2건(korean-brokerage-trading-api + backtest-live-parity.md 신규, park-empty-spot-watch) / git 커밋 2개 저장소 (post1 bce81f2, memories a6a3341)
- daily 페이지: concepts/daily/2026-10-02.md 생성

## [2026-10-01] daily-sync | 인덱스 +6/+26, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 43개
- 인덱스: 신규 6 / 갱신 26 (텍스트 없음 스킵 0), 총 17,352개 (FTS 17,093, 357.5MB). 루트별 hermes 12,453 / projects 4,328 / documents 297 / wiki 274
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 신규 폴더 없음
- 크론 에러 0건 — 5일 연속 안정
- 작업 변경 43개: auto-trading 16 (백테스트 복구 — 시뮬레이터 NH 모의투자 도메인 시세 미호출, 실행라벨 거짓 표시 수정, 유니버스 SK하이닉스→KB금융), post1 1, lotto-predictor 1 / git 커밋 3개 저장소 (post1 0c00444, auto-trading 3, memories 856563f)
- daily 페이지: concepts/daily/2026-10-01.md 생성
- 인덱스: 신규 11 / 갱신 19 (텍스트 없음 스킵 0), 총 17,335개 (FTS 17,076, 357.3MB). 루트별 hermes 12,446 / projects 4,324 / documents 293 / wiki 272
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 신규 폴더 없음
- 크론 에러 0건 — 3일 연속 안정
- 작업 변경 32개: car-year-lookup 9 (카히스토리 직접 조회 — 캡처·연식 채우기·현황 갱신, 조회금지 가짜목록 분리), auto-trading 2 (실시간 매매 기록), post1 1 / git 커밋 2개 저장소 (post1 76b24ee, memories 40d8989)
- daily 페이지: concepts/daily/2026-09-29.md 생성

## [2026-10-05] daily-sync | 인덱스 +3/+6, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 14개
- 인덱스: 신규 3 / 갱신 6 (텍스트 없음 스킵 0), 총 17,380개 (FTS 17,121, 357.7MB). 루트별 hermes 12,469 / projects 4,331 / documents 302 / wiki 278
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 신규 폴더 없음
- 크론 에러 0건 — 안정 상태 계속.
- 작업 변경 14개: post1 1 (개인사이트 업데이트, 커밋 b635432), auto-trading 1 (주간 시장 분석 리포트), .hermes 메모리/크론 상태 백업 (커밋 ae821c0) / git 커밋 2개 저장소 (post1 b635432, memories ae821c0)
- daily 페이지: concepts/daily/2026-10-05.md 생성

## [2026-10-03] daily-sync | 인덱스 +6/+10, 레지스트리 35개 폴더, 크론 에러 0건, 작업 변경 20개
- 인덱스: 신규 6 / 갱신 10 (텍스트 없음 스킵 0), 총 17,373개 (FTS 17,114, 357.6MB). 루트별 hermes 12,467 / projects 4,329 / documents 301 / wiki 276
- 레지스트리: 35개 폴더 (git 14 / 로컬 21) — 신규 폴더 없음
- 크론 에러 0건 — 7일 연속 크론 안정 유지, 정상.
- 작업 변경 20개: post1 1 (개인사이트 업데이트, 커밋 fbe8758), auto-trading 2 (실전 라이브 추적 리포트 자동 갱신), lotto-predictor 2 (로또 추적기+예측), .hermes 메모리 백업 (커밋 94a5212) / git 커밋 2개 저장소 (post1 fbe8758, memories 94a5212)
- daily 페이지: concepts/daily/2026-10-03.md 생성
