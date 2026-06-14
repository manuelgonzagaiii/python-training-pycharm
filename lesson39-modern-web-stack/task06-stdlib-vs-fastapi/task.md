# Stdlib vs FastAPI: what the framework bought us

> **Phase:** Networking & the Web  •  **Stage:** 39.6 of 6  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Articulate exactly which boilerplate FastAPI removed versus the stdlib server
- Map each stdlib piece (routing, body parsing, status codes, validation, docs) to its framework equivalent
- Judge when reaching for the stdlib server is still the right call
- Consolidate the WSGI/ASGI mental model from the whole phase

## Python features introduced
`recap: BaseHTTPRequestHandler vs FastAPI routing`, `manual JSON vs pydantic validation`, `WSGI vs ASGI`, `manual 404/422 vs HTTPException/automatic validation`, `no-docs vs automatic OpenAPI`, `sync threading vs async ASGI`

## MiniERP increment
No code change: a knowledge check that closes the phase by comparing erp/web/api.py (stdlib) against erp/web/app.py (FastAPI) so learners can justify the dependency they just added.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice knowledge check — no code to write.
# Q: Which of these did FastAPI provide automatically that the
#    BaseHTTPRequestHandler version required us to hand-write?
#    (validation / OpenAPI docs / status codes / routing — pick all that apply)
- **Test focus:** Choice task: correct options identify automatic request validation (pydantic/422), automatic OpenAPI docs, and declarative routing/response models as framework-provided, while raw socket/header writing remains stdlib's job.

</div>
