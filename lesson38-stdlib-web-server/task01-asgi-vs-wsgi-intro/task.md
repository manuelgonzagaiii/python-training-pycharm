# How Python apps talk to web servers (WSGI & ASGI)

> **Phase:** Networking & the Web  •  **Stage:** 38.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain the server <-> application contract and why a standard interface exists
- Read a minimal WSGI callable and a minimal ASGI app and name each parameter
- Understand why ASGI exists (websockets, long-lived async) and how it maps onto the async core built earlier
- Place http.server, wsgiref, and uvicorn on the same map

## Python features introduced
`WSGI callable signature environ+start_response`, `ASGI scope/receive/send async signature`, `the gateway concept`, `blocking vs async request handling`, `where http.server, wsgiref, uvicorn fit`

## MiniERP increment
No code change to MiniERP; this concept page frames the next four tasks (stdlib server -> WSGI -> ASGI/FastAPI) so learners know where each piece they build slots into the request pipeline.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory page — no code to complete.
# Compare:
#   def app(environ, start_response): ...          # WSGI (sync)
#   async def app(scope, receive, send): ...        # ASGI (async)
- **Test focus:** No automated check (theory task): the page ends with a self-check question contrasting the two callable signatures.

</div>
