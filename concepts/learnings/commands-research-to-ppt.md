---
title: Research to PPT Command
created: 2026-06-01
updated: 2026-06-13
type: concept
tags: [ai-ml, programming, research, python, web]
sources: [raw/local/ai-ml/commands-research-to-ppt-2026-06-01.md]
source_file: /Users/bearj/projects/.claude/commands/research-to-ppt.md
confidence: high
links: [[commands-weather-orchestrator|Weather Orchestrator Command]], [[rules-presentation|Presentation Rules]], [[site-refinement-learnings|Site Refinement Learnings]]
---

# Research to PPT Command

> 관련: [[specs-2026-05-17-html-template-system-design|HTML 템플릿 시스템 설계]], [[plans-2026-05-17-html-template-system|HTML 템플릿 시스템 구현 계획]]을 참고하세요.

> 📁 원본: `/Users/bearj/projects/.claude/commands/research-to-ppt.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: ai-ml

## 내용

# Research to PPT Command

Researches a topic via web search, creates a rich HTML presentation, and converts it to PowerPoint.

## Description
Searches the web for comprehensive information about a topic, generates a dark-themed HTML slide deck, and converts it to a `.pptx` file. Uses the existing `PPT_Generator/ppt_converter.py` for PPT conversion.

## Usage
`/research-to-ppt [topic]`

## Pipeline
1. **Web Search** — Use the WebSearch tool to find 5-8 high-quality sources about the topic
2. **Content Compilation** — Extract key facts, statistics, trends, and insights from search results
3. **HTML Generation** — Create a dark-themed HTML file with slide sections (compatible with `ppt_converter.py`)
4. **PPT Conversion** — Run `python3 -c "import sys; sys.path.insert(0, 'PPT_Generator'); from ppt_converter import convert_html_to_ppt; convert_html_to_ppt(open('PATH.html').read(), 'PATH.pptx')"`
5. Return paths to both `.html` and `.pptx` files

## HTML Structure Requirements
The HTML must follow this exact format for `ppt_converter.py` compatibility:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Topic Name</title>
    <style>/* dark theme CSS - can use base.html from PPT_Generator/templates/ */</style>
</head>
<body>
    <!-- 1. Title Slide -->
    <section class="slide slide-type-title-slide">
        <div class="glow-orb glow-orb-blue"></div>
        <h1 class="slide-title">Topic Name</h1>
        <p class="slide-subtitle">웹 기반 자동 생성 프레젠테이션</p>
        <div class="slide-meta">Generated via Web Research</div>
    </section>

    <!-- 2. Overview Slide -->
    <section class="slide slide-type-section-header-slide">
        <span class="section-header-badge badge-blue">개요</span>
        <h2 class="slide-title">Overview</h2>
    </section>

    <!-- 3-N. Content Slides (one per search result) -->
    <section class="slide slide-type-content-slide accent-blue">
        <h2 class="slide-title">Result Title</h2>
        <div class="slide-content">
            <p>Key paragraph from search result...</p>
        </div>
        <ul class="bullet-list">
            <li>Bullet point 1</li>
            <li>Bullet point 2</li>
        </ul>
        <div class="slide-footer"><span>Source URL</span></div>
    </section>

    <!-- Thank You Slide -->
    <section class="slide slide-type-thankyou">
        <h1 class="slide-title">감사합니다</h1>
        <p class="slide-subtitle">질문이 있으시면 말씀해 주세요</p>
    </section>
</body>
</html>
```

### Accent Color Classes
- `accent-blue` — first content slide
- `accent-green` — second content slide
- `accent-orange` — third content slide
- Cycle through: blue → green → orange → blue → ...

### Section Header Badge Classes
- `badge-blue`, `badge-green`, `badge-orange` — cycle same as accent

## Behavior
1. If no topic provided, prompts user for a topic
2. Searches web for comprehensive information using WebSearch tool
3. Generates HTML file following the structure above (save as `PPT_Generator

...(내용 생략)...
