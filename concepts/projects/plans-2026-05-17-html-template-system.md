---
title: HTML Template System Implementation Plan
created: 2026-06-01
updated: 2026-06-01
type: concept
tags: [document, python, ai-ml, web]
sources: [raw/local/general/plans-2026-05-17-html-template-system-2026-06-01.md]
source_file: /Users/bearj/projects/docs/superpowers/plans/2026-05-17-html-template-system.md
confidence: high
links: [[specs-2026-05-17-html-template-system-design|HTML Template System 설계 문서]], [[plans-site-refinement|개인 사이트 자동화 고도화]]
---

# HTML Template System Implementation Plan

> 📁 원본: `/Users/bearj/projects/docs/superpowers/plans/2026-05-17-html-template-system.md`
> 📅 수집: 2026-06-01
> 🏷️ 카테고리: general

## 내용

# HTML Template System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enhance the PPT Generator skill with a Professional Template System for HTML generation, creating more visually consistent and professional presentations through reusable slide templates and theming.

**Architecture:** Implement a template-based HTML generation system that separates concerns into base templates, slide-specific templates, and a theme system, while maintaining backward compatibility with the existing workflow.

**Tech Stack:** Python, HTML5, CSS3 (with CSS variables), optional Jinja2 for template processing

---

### Task 1: Create Template Directory Structure

**Files:**
- Create: `PPT_Generator/templates/`
- Create: `PPT_Generator/templates/base.html`
- Create: `PPT_Generator/templates/slides/`
- Create: `PPT_Generator/templates/themes/`

- [ ] **Step 1: Create directories**

```bash
mkdir -p PPT_Generator/templates/slides PPT_Generator/templates/themes
```

- [ ] **Step 2: Commit**

```bash
git add PPT_Generator/templates/
git commit -m "feat: create template directory structure"
```

### Task 2: Implement Base Template with CSS Variables

**Files:**
- Create: `PPT_Generator/templates/base.html`

- [ ] **Step 1: Write the failing test** (we'll test that the file exists and contains expected structure)

Actually, let's follow TDD: first create a test that checks for the base template.

**Files:**
- Create: `tests/test_template_system.py`

- [ ] **Step 1: Write the failing test**

```python
import os
def test_base_template_exists():
    assert os.path.exists("PPT_Generator/templates/base.html")
    with open("PPT_Generator/templates/base.html", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "<!DOCTYPE html>" in content
        assert ":root {" in content  # CSS variables
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -c "import tests.test_template_system; tests.test_template_system.test_base_template_exists()"`
Expected: FAIL (file doesn't exist)

- [ ] **Step 3: Write minimal implementation**

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        :root {
            --color-primary: #2c3e50;
            --color-secondary: #3498db;
            --color-accent: #e74c3c;
            --color-light: #ecf0f1;
            --color-dark: #2d3436;
            --color-success: #27ae60;
            --color-warning: #f39c12;
            --font-family-base: 'Malgun Gothic', 'Arial Unicode MS', Arial, sans-serif;
            --font-size-base: 16px;
            --font-size-title: 2.2rem;
            --font-size-heading: 1.8rem;
            --spacing-unit: 20px;
            --border-radius: 

...(내용 생략)...
