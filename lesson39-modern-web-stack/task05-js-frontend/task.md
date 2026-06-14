# A minimal JS frontend over the JSON API

> **Phase:** Networking & the Web  •  **Stage:** 39.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Serve a static single-page frontend from FastAPI
- Have the browser fetch() the JSON API and render results client-side
- Understand the JSON contract and where CORS applies
- See the full round trip: browser -> ASGI -> service -> JSON -> DOM

## Python features introduced
`serving static JS/CSS via FastAPI StaticFiles`, `a fetch()-based vanilla JS client (in a served .js asset)`, `CORS basics (CORSMiddleware)`, `JSON contract between front and back end`, `FastAPI mount of static dir`, `content-type negotiation`

## MiniERP increment
Adds erp/web/static/app.js (+ index.html): a tiny vanilla-JS SPA that lists products and submits the add-product form by calling the FastAPI JSON endpoints, completing the phase's 'simple web UI' milestone with a real browser client over the API.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

def mount_frontend(app: FastAPI) -> None:
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
    # TODO: app.mount('/', StaticFiles(directory=..., html=True), name='static')
    raise NotImplementedError
# static/app.js: fetch('/products').then(r=>r.json()).then(render)
- **Test focus:** Use the httpx/TestClient to GET / and assert index.html is served as text/html, GET /static/app.js returns the JS with the right content-type, and that a preflight OPTIONS request returns the expected CORS headers.

</div>
