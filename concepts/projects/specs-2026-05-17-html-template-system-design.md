---
title: HTML Design Enhancement Design Document - Professional Template System
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [document, python, web]
sources: [raw/local/general/specs-2026-05-17-html-template-system-design-2026-06-01.md]
source_file: /Users/bearj/projects/docs/superpowers/specs/2026-05-17-html-template-system-design.md
confidence: high
links: [[plans-2026-05-17-html-template-system|HTML Template System 구현 계획]], [[plans-site-refinement|개인 사이트 자동화 고도화]]
---

# HTML Design Enhancement Design Document - Professional Template System

> 📁 원본: `/Users/bearj/projects/docs/superpowers/specs/2026-05-17-html-template-system-design.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: general

## 내용

# HTML Design Enhancement Design Document - Professional Template System

## Overview
This design enhances the PPT Generator skill by implementing a Professional Template System for HTML generation. Instead of ad-hoc HTML creation, the system will use reusable slide templates with consistent theming, resulting in more professional and visually consistent presentations.

## Core Concept
Replace the current ad-hoc HTML generation with a professional template system that:
1. Defines reusable slide templates (title slide, content slide, section header slide, etc.)
2. Implements a consistent visual theme with customizable colors, fonts, and spacing
3. Provides clear mapping from HTML structure to PPT slides
4. Maintains backward compatibility with existing workflow

## Template Components

### 1. Base Template (base.html)
- Defines CSS variables for theme colors, fonts, spacing
- Includes reset.css equivalent for consistent rendering
- Provides utility classes for common layout patterns

### 2. Slide Templates
- **title-slide.html**: Large title, subtitle, optional logo/date
- **content-slide.html**: Title + bullet points or paragraphs
- **two-column-slide.html**: Title + left/right content areas
- **section-header-slide.html**: Full-width section title with background
- **image-slide.html**: Title + image placeholder with caption
- **data-slide.html**: Title + table or chart container

### 3. Theme System
- CSS variables in :root for easy customization
- Predefined themes: professional, modern, academic, corporate
- Ability to override via data attributes or class modifiers

### 4. HTML Structure Convention
- Use semantic HTML5 elements with specific classes
- Each slide wrapped in `<section class="slide slide-type-[template-name]" data-slide-index="n">`
- Clear hierarchy: h1/h2 for titles, ul/ol for lists, p for paragraphs, figure for images

### 5. Benefits for PPT Conversion
- Predictable structure makes HTML→PPT mapping more reliable
- Consistent class names allow for better styling in PPT
- Template-specific conversion rules (e.g., two-column becomes side-by-side text boxes)
- Reduced need for complex HTML parsing logic

## Data Flow
User Input (Topic) → Web Search → Process Results → Template-Based HTML Generation → PPT Conversion → Output File

## Technical Approach
- Language: Python (unchanged)
- Template Engine: Jinja2 or simple string formatting (to avoid new dependencies)
- CSS: CSS3 with variables for theming
- HTML Structure: Semantic HTML5 with BEM-like naming convention
- Output: Enhanced HTML file → Improved PPT file

## File Structure Changes
```
PPT_Generator/
├── templates/
│   ├── base.html
│   ├── slides/
│   │   ├── title-slide.html
│   │   ├── content-slide.html
│   │   ├── two-column-slide.html
│   │   ├── section-header-slide.html
│   │   ├── image-slide.html
│   │   └── data-slide.html
│   └── themes/
│       ├── professional.css
│       ├── modern.css
│       ├── academic.css
│       └── corporate.css
├── web_search.py
├──

...(내용 생략)...
