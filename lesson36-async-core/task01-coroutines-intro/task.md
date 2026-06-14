# Coroutines and the event loop

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.1 of 8  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define a coroutine with async def and understand that calling it returns a coroutine object that does nothing until awaited
- Run a top-level coroutine with asyncio.run and yield control with await asyncio.sleep
- Build a correct mental model of the single-threaded event loop and cooperative scheduling
- Recognize that a blocking call (sync DB/file/CPU) inside a coroutine freezes the whole loop, motivating run_in_executor later

## Python features introduced
`async def coroutine functions`, `await expression`, `awaitables`, `asyncio.run`, `asyncio.sleep`, `event loop model (single-threaded cooperative scheduling)`, `coroutine vs function call (returns a coroutine object)`, `why blocking calls stall the loop`

## MiniERP increment
Adds docs/async.md plus erp/web/async_core.py skeleton with an async hello/health coroutine the later tasks flesh out; establishes the async entry point (asyncio.run) the web layer will use.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A minimal async main() awaiting a coroutine that returns a health payload, run via asyncio.run; a note contrasting calling vs awaiting a coroutine.
- **Test focus:** Theory task: no checks; reader runs the async health coroutine and reads the event-loop explanation.

</div>
