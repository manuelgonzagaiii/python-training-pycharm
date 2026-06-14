# Per-request context with contextvars

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Carry per-request data (current user, role, correlation/request id) implicitly across awaits with a ContextVar
- Set and restore a ContextVar using its Token (reset) around a request scope
- Understand that each asyncio.Task gets its own copy of the context, so concurrent requests do not bleed into each other
- Contrast contextvars with threading.local and know why contextvars is the async-correct choice

## Python features introduced
`contextvars.ContextVar`, `ContextVar.set / get / default`, `Token and ContextVar.reset(token)`, `contextvars.copy_context`, `context propagation across await points`, `context isolation per asyncio.Task`, `contrast with threading.local`

## MiniERP increment
Adds an ambient request context to the async server: a middleware-style wrapper sets current_user / request_id ContextVars per connection so the audit-log and service layer can read the acting user without threading it through every call signature, and concurrent requests stay isolated. This unifies the audit-log identity story across the async core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A request_context(user, request_id) helper setting ContextVars (with reset via Token), and audit/service code that reads them via get(); the server sets context per client.
- **Test focus:** Concurrent tasks each see their own user/request_id (no leakage), reset restores the prior value after the scope, and the audit log records the correct acting user per request.

</div>
