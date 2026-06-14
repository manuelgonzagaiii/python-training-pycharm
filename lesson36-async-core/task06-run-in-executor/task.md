# Bridging blocking persistence into asyncio

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run the existing blocking (sync) persistence/reporting calls without freezing the event loop via asyncio.to_thread / run_in_executor
- Offload CPU-bound report computation to a ProcessPoolExecutor from async code
- Get the running loop correctly inside a coroutine
- Decide between to_thread (I/O-bound) and a process executor (CPU-bound) from async code

## Python features introduced
`loop.run_in_executor`, `asyncio.to_thread`, `asyncio.get_running_loop`, `wrapping blocking I/O for the event loop`, `ProcessPoolExecutor with run_in_executor for CPU-bound work`, `why not to block the loop`, `awaiting executor futures`

## MiniERP increment
Makes the async web core actually call the real (synchronous) persistence layer from earlier phases: read/write service calls run via asyncio.to_thread, and the heavy parallel report from lesson 2 is awaited through a ProcessPoolExecutor with run_in_executor, so the event loop never blocks. The async facade now fully drives the existing domain core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Async wrappers async_get_products() (to_thread) and async_build_report() (run_in_executor over a ProcessPoolExecutor) used by the server handlers.
- **Test focus:** Blocking calls run off-loop (the loop stays responsive to other tasks during the call), results match the direct sync call, and CPU-bound work runs in a separate process.

</div>
