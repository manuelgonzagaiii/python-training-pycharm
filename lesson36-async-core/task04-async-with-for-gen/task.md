# Async context managers, iterators & generators

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write an async context manager (both protocol methods and @asynccontextmanager) to manage an async resource like a connection/session
- Iterate an async source with async for
- Author an async generator that yields rows/events lazily without buffering everything
- Close async generators deterministically with aclosing

## Python features introduced
`async with`, `__aenter__ / __aexit__`, `asynccontextmanager (contextlib)`, `async for`, `__aiter__ / __anext__`, `async generators (async def + yield)`, `StopAsyncIteration`, `contextlib.aclosing`

## MiniERP increment
Adds async streaming primitives to the web core: an async DB-session context manager wraps each request, and an async generator stream_audit_events() / stream_report_rows() yields audit-log or report rows incrementally so the web layer can stream large responses instead of materializing them.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** An @asynccontextmanager async_session() plus an async generator paginating rows; a consumer uses async with + async for.
- **Test focus:** The async context manager enters/exits (including on exception), async for drives the async generator to completion, and aclosing finalizes a partially-consumed generator.

</div>
