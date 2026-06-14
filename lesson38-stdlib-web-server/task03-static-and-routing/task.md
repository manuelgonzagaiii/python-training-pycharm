# Serving HTML and decoding form posts

> **Phase:** Networking & the Web  •  **Stage:** 38.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Serve an HTML page and correct Content-Type from a handler
- Decode an application/x-www-form-urlencoded POST body
- Escape user-supplied text before embedding it in HTML
- Use mimetypes and pathlib to serve static assets safely

## Python features introduced
`serving text/html responses`, `SimpleHTTPRequestHandler comparison`, `mimetypes.guess_type`, `urllib.parse.parse_qs on form bodies`, `application/x-www-form-urlencoded`, `html.escape for safe output`, `pathlib for locating static files`

## MiniERP increment
Adds erp/web/ui.py and erp/web/static/: a minimal server-rendered HTML UI — a product list page and an 'add product' form that POSTs back to the API handler. Gives MiniERP its first browser-visible screen, still pure stdlib.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import html, mimetypes
from pathlib import Path
from urllib.parse import parse_qs

STATIC = Path(__file__).parent / "static"

def render_products(products) -> str:
    """Return an HTML table of products with every field html.escape-d."""
    rows = "".join(
        f"<tr><td>{html.escape(p.name)}</td><td>{p.price}</td></tr>"
        for p in products
    )
    # TODO: wrap rows in a full <html> document
    raise NotImplementedError

def parse_form(body: bytes) -> dict[str, str]:
    """Decode an urlencoded form body into a flat dict (first value per key)."""
    # TODO: parse_qs then take [0] of each list
    raise NotImplementedError
- **Test focus:** Assert render_products escapes a malicious name like '<script>' so it cannot inject markup; assert parse_form decodes name=Widget&price=9.99 into the right dict; GET the UI page through the server and assert it returns text/html with the product name present.

</div>
