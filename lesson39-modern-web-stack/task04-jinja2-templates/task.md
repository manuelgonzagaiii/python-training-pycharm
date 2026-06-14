# Server-rendered HTML with Jinja2

> **Phase:** Networking & the Web  •  **Stage:** 39.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Configure a Jinja2 Environment with autoescaping and a loader
- Render templates with a context and use loops, conditionals, and filters
- Use template inheritance with a base layout and blocks
- Serve rendered HTML from a FastAPI route

## Python features introduced
`jinja2.Environment`, `FileSystemLoader / PackageLoader`, `template.render(context)`, `autoescape=True`, `{{ }} expressions, {% for %}/{% if %}`, `template inheritance ({% extends %}/{% block %})`, `filters (|round, |length)`, `FastAPI HTMLResponse / Jinja2Templates`

## MiniERP increment
Adds erp/web/templates/ and an HTML route in app.py: the MiniERP product list and invoice pages rendered with Jinja2 (a base layout + child pages), replacing the hand-built string HTML from Lesson 2 with safe, maintainable templates.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("erp.web", "templates"),
    autoescape=select_autoescape(),
)

def render_products_page(products) -> str:
    template = env.get_template("products.html")
    # TODO: return template.render(products=products, title='Products')
    raise NotImplementedError
# templates/base.html defines {% block content %}; products.html extends it.
- **Test focus:** Render products.html with a list and assert the output contains each product name, that autoescaping neutralizes a '<script>' name, that the {% for %} produces the right row count, and that {% extends %} pulls in the base layout's title.

</div>
