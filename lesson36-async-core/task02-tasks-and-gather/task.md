# Concurrent awaits: tasks, gather & timeouts

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Schedule coroutines concurrently with create_task instead of awaiting them serially
- Await many results together with gather, optionally collecting exceptions instead of failing fast
- Bound a slow async operation with wait_for / asyncio.timeout and handle TimeoutError
- Cancel a task and handle CancelledError cleanly

## Python features introduced
`asyncio.create_task`, `asyncio.gather`, `return_exceptions=True`, `asyncio.wait_for`, `asyncio.timeout (async context manager)`, `asyncio.TimeoutError`, `Task cancellation / Task.cancel`, `awaiting multiple coroutines concurrently`

## MiniERP increment
Adds an async aggregate endpoint to the web core: a dashboard handler that fetches several async report fragments (sales, low-stock, recent payments) concurrently with gather and enforces a per-fragment timeout so one slow fragment cannot hang the response.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** An async build_dashboard() that create_task()s several fragment coroutines, gathers them with a timeout wrapper, and degrades gracefully on TimeoutError.
- **Test focus:** Fragments run concurrently (total time near the slowest, not the sum), a timed-out fragment is reported as partial rather than failing the whole dashboard, and cancellation is handled.

</div>
