---
source_file: /Users/bearj/projects/docs/superpowers/plans/2026-05-17-html-template-system.md
ingested: 2026-06-01
sha256: f644ac2198dd
category: general
original_title: HTML Template System Implementation Plan
---

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
            --border-radius: 8px;
            --box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: var(--font-family-base);
            font-size: var(--font-size-base);
            line-height: 1.6;
            color: var(--color-dark);
            background-color: var(--color-light);
            margin: 0;
            padding: var(--spacing-unit);
        }
        .slide {
            background: white;
            margin: calc(var(--spacing-unit) * 2) 0;
            padding: var(--spacing-unit);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            min-height: 400px;
            display: flex;
            flex-direction: column;
        }
        .slide-title {
            color: var(--color-primary);
            border-bottom: 3px solid var(--color-secondary);
            padding-bottom: calc(var(--spacing-unit) / 2);
            margin-bottom: var(--spacing-unit);
            font-size: var(--font-size-title);
        }
        .slide-content {
            flex-grow: 1;
            font-size: var(--font-size-base);
            line-height: 1.8;
        }
    </style>
</head>
<body>
    <!-- Content will be injected here -->
</body>
</html>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -c "import tests.test_template_system; tests.test_template_system.test_base_template_exists()"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add PPT_Generator/templates/base.html tests/test_template_system.py
git commit -m "feat: implement base template with CSS variables"
```

### Task 3: Create Slide Template Files

**Files:**
- Create: `PPT_Generator/templates/slides/title-slide.html`
- Create: `PPT_Generator/templates/slides/content-slide.html`
- Create: `PPT_Generator/templates/slides/section-header-slide.html`

- [ ] **Step 1: Write failing test for slide templates**

```python
import os
def test_slide_templates_exist():
    templates = [
        "PPT_Generator/templates/slides/title-slide.html",
        "PPT_Generator/templates/slides/content-slide.html",
        "PPT_Generator/templates/slides/section-header-slide.html"
    ]
    for template in templates:
        assert os.path.exists(template), f"Missing template: {template}"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -c "import tests.test_template_system; tests.test_template_system.test_slide_templates_exist()"`
Expected: FAIL (files don't exist)

- [ ] **Step 3: Write minimal implementations**

Title slide template:
```html
<section class="slide slide-type-title-slide" data-slide-index="0">
    <h1 class="slide-title">{{ title }}</h1>
    {% if subtitle %}
    <p class="slide-subtitle">{{ subtitle }}</p>
    {% endif %}
</section>
```

Content slide template:
```html
<section class="slide slide-type-content-slide" data-slide-index="{{ slide_index }}">
    <h2 class="slide-title">{{ title }}</h2>
    <div class="slide-content">
        {% if content %}
        <p>{{ content }}</p>
        {% endif %}
        {% if bullet_points %}
        <ul>
        {% for point in bullet_points %}
            <li>{{ point }}</li>
        {% endfor %}
        </ul>
        {% endif %}
    </div>
</section>
```

Section header slide template:
```html
<section class="slide slide-type-section-header-slide" data-slide-index="{{ slide_index }}">
    <h2 class="slide-title section-header-title">{{ title }}</h2>
</section>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -c "import tests.test_template_system; tests.test_template_system.test_slide_templates_exist()"`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add PPT_Generator/templates/slides/title-slide.html PPT_Generator/templates/slides/content-slide.html PPT_Generator/templates/slides/section-header-slide.html tests/test_template_system.py
git commit -m "feat: create slide template files"
```

### Task 4: Modify HTML Generator to Use Template System

**Files:**
- Modify: `PPT_Generator/html_generator.py`

- [ ] **Step 1: Write failing test for template-based HTML generation**

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from PPT_Generator.html_generator import generate_html

def test_generate_html_uses_template_system():
    search_results = [
        {"title": "Test Topic - Overview", "snippet": "This is a test overview.", "url": "http://test.com"},
        {"title": "Test Topic - Features", "snippet": "These are test features.", "url": "http://test.com/features"}
    ]
    result = generate_html(search_results, "Test Topic")
    # Check that it uses template structure
    assert "<section class=\"slide\" " in result
    assert 'data-slide-index="' in result
    assert "Test Topic" in result
    assert "This is a test overview." in result
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_html_generator.py::test_generate_html_uses_template_system -v`
Expected: FAIL (doesn't use template system yet)

- [ ] **Step 3: Write implementation that uses template system**

We'll need to modify html_generator.py to:
1. Load base template
2. Load slide templates
3. Render content using the templates
4. Fallback to old method if templates fail

Let's implement a simple version first:

```python
import os
import json
from string import Template

def _load_template(template_path):
    """Load a template file and return its content."""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def generate_html(search_results: list, topic: str) -> str:
    """
    Generate HTML from search results using template system.
    
    Args:
        search_results: List of dictionaries with 'title', 'snippet', 'url'
        topic: The main topic for the presentation
        
    Returns:
        HTML string
    """
    # Try to use template system
    base_template = _load_template("PPT_Generator/templates/base.html")
    title_slide_template = _load_template("PPT_Generator/templates/slides/title-slide.html")
    content_slide_template = _load_template("PPT_Generator/templates/slides/content-slide.html")
    
    # If any template is missing, fall back to old method
    if not all([base_template, title_slide_template, content_slide_template]):
        # Fallback to original implementation
        return _generate_html_fallback(search_results, topic)
    
    # Generate slides using templates
    slides_html = ""
    
    # Title slide
    title_slide = Template(title_slide_template).substitute(
        title=topic,
        subtitle="Generated from web search results"
    )
    slides_html += title_slide
    
    # Content slides for each search result
    for i, result in enumerate(search_results):
        content_slide = Template(content_slide_template).substitute(
            title=result['title'],
            slide_index=i,
            content=result['snippet']
            # We could add bullet_points here if we had them
        )
        slides_html += content_slide
    
    # Insert slides into base template (replace <!-- Content will be injected here -->)
    # For simplicity, we'll just wrap in body tags for now
    # In a real implementation, we'd do proper template injection
    full_html = base_template.replace("<!-- Content will be injected here -->", slides_html)
    
    return full_html

def _generate_html_fallback(search_results: list, topic: str) -> str:
    """Fallback to original HTML generation method."""
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic}</title>
    <style>
        body {{ font-family: 'Malgun Gothic', 'Arial Unicode MS', Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        h1, h2, h3 {{ color: #333; }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .content {{ max-width: 800px; margin: 0 auto; }}
        .section {{ margin-bottom: 30px; padding: 20px; border-left: 4px solid #007cba; }}
        .references {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; font-size: 0.9em; }}
        .url {{ color: #0066cc; word-break: break-all; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{topic}</h1>
        <p>Generated from web search results</p>
    </div>
    <div class="content">
        <div class="section">
            <h2>Overview</h2>
            <p>This presentation contains information about {topic} gathered from web search results.</p>
        </div>
"""
    
    # Add sections for each search result
    for i, result in enumerate(search_results):
        html += f"""        <div class="section">
            <h2>{result['title']}</h2>
            <p>{result['snippet']}</p>
            <p><strong>Source:</strong> <a href="{result['url']}" class="url">{result['url']}</a></p>
        </div>
"""
    
    html += """    </div>
    <div class="references">
        <h2>References</h2>
        <p>Information gathered from:</p>
        <ul>
"""
    
    for result in search_results:
        html += f'            <li><a href="{result["url"]}" class="url">{result["title"]}</a></li>\n'
    
    html += """        </ul>
    </div>
</body>
</html>"""
    
    return html
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_html_generator.py::test_generate_html_uses_template_system -v`
Expected: PASS

- [ ] **Step 5: Add test for fallback behavior when templates missing**

```python
def test_generate_html_fallback_when_templates_missing():
    # Temporarily rename template directory to simulate missing templates
    import os
    if os.path.exists("PPT_Generator/templates"):
        os.rename("PPT_Generator/templates", "PPT_Generator/templates_backup")
    
    try:
        search_results = [{"title": "Test", "snippet": "Test", "url": "http://test.com"}]
        result = generate_html(search_results, "Test Topic")
        # Should still generate valid HTML
        assert "<!DOCTYPE html>" in result
        assert "Test Topic" in result
    finally:
        # Restore template directory
        if os.path.exists("PPT_Generator/templates_backup"):
            os.rename("PPT_Generator/templates_backup", "PPT_Generator/templates")
```

- [ ] **Step 6: Run fallback test**

Run: `pytest tests/test_html_generator.py::test_generate_html_fallback_when_templates_missing -v`
Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add PPT_Generator/html_generator.py tests/test_html_generator.py
git commit -m "feat: modify html generator to use template system"
```

### Task 5: Enhance PPT Converter to Leverage Template Classes (Optional)

**Files:**
- Modify: `PPT_Generator/ppt_converter.py`

- [ ] **Step 1: Write failing test for improved PPT conversion**

Actually, let's keep it simple for now and note that the existing converter should work with the new HTML structure since we're using semantic HTML with clear classes.

We'll just ensure the converter doesn't break.

- [ ] **Step 2: Commit** (if we make changes)

For now, we'll skip this task as the existing converter should work with the new structure.

### Task 6: Write Tests for New Functionality

**Files:**
- Modify: `tests/test_html_generator.py`
- Create: `tests/test_template_system.py` (already started)

- [ ] **Step 1: Add comprehensive tests**

We've already started some tests. Let's add a few more:

```python
def test_generate_html_contains_css_variables():
    search_results = [{"title": "Test", "snippet": "Test", "url": "http://test.com"}]
    result = generate_html(search_results, "Test Topic")
    # Check that CSS variables from base template are present
    assert "--color-primary:" in result
    assert "--font-family-base:" in result

def test_generate_html_has_correct_slide_count():
    search_results = [
        {"title": "Result 1", "snippet": "Snippet 1", "url": "http://example.com/1"},
        {"title": "Result 2", "snippet": "Snippet 2", "url": "http://example.com/2"},
        {"title": "Result 3", "snippet": "Snippet 3", "url": "http://example.com/3"}
    ]
    result = generate_html(search_results, "Test Topic")
    # Count slide sections
    slide_count = result.count('<section class="slide"')
    assert slide_count == len(search_results) + 1  # +1 for title slide

def test_generate_html_includes_all_search_content():
    search_results = [
        {"title": "First Result", "snippet": "First snippet content", "url": "http://first.com"},
        {"title": "Second Result", "snippet": "Second snippet content", "url": "http://second.com"}
    ]
    result = generate_html(search_results, "Test Topic")
    assert "First Result" in result
    assert "First snippet content" in result
    assert "Second Result" in result
    assert "Second snippet content" in result
```

- [ ] **Step 2: Run new tests**

Run: `pytest tests/test_html_generator.py -v`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_html_generator.py
git commit -m "feat: add comprehensive tests for template system"
```

### Task 7: Final Integration and Verification

**Files:**
- Modify: Any files as needed based on testing
- Create: Example usage documentation

- [ ] **Step 1: Run full integration test**

```python
# Test the full pipeline
from PPT_Generator.web_search import search_topic
from PPT_Generator.html_generator import generate_html
from PPT_Generator.ppt_converter import convert_html_to_ppt

topic = "Test Integration"
search_results = search_topic(topic, num_results=3)
assert len(search_results) > 0

html_content = generate_html(search_results, topic)
assert len(html_content) > 1000  # Reasonable length

success = convert_html_to_ppt(html_content, "test_integration.pptx")
assert success == True

import os
assert os.path.exists("test_integration.pptx")
file_size = os.path.getsize("test_integration.pptx")
assert file_size > 10000  # Should be a reasonable PPT size

# Cleanup
os.remove("test_integration.pptx")
```

- [ ] **Step 2: Run integration test**

Run: `python3 -c "
import sys
sys.path.insert(0, '.')
from PPT_Generator.web_search import search_topic
from PPT_Generator.html_generator import generate_html
from PPT_Generator.ppt_converter import convert_html_to_ppt

topic = 'Test Integration'
search_results = search_topic(topic, num_results=3)
assert len(search_results) > 0, 'No search results'

html_content = generate_html(search_results, topic)
assert len(html_content) > 1000, f'HTML too short: {len(html_content)}'

success = convert_html_to_ppt(html_content, 'test_integration.pptx')
assert success == True, 'PPT conversion failed'

import os
assert os.path.exists('test_integration.pptx'), 'PPT file not created'
file_size = os.path.getsize('test_integration.pptx')
assert file_size > 10000, f'PPT too small: {file_size} bytes'

os.remove('test_integration.pptx')
print('All integration tests passed!')
"`
Expected: PASS (prints "All integration tests passed!")

- [ ] **Step 3: Commit**

```bash
git add .
git commit -m "feat: complete HTML template system implementation"
```

### Task 8: Update Skill Documentation (Optional)

**Files:**
- Modify: `.claude/skills/ppt-generator/SKILL.md`

- [ ] **Step 1: Update documentation to mention template system**

Actually, we'll keep the skill documentation simple and just note that it generates professional presentations.

- [ ] **Step 2: Commit** (if we make changes)

For now, we'll leave the skill documentation as is since the external interface hasn't changed.

---