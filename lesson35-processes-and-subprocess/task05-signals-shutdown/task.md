# Catching signals for graceful shutdown

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 35.5 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Install a SIGINT/SIGTERM handler so the long-running job runner shuts down gracefully instead of dying mid-job
- Understand that signal handlers run only in the main thread and must do minimal work (just set a flag/Event)
- Relate SIGINT to KeyboardInterrupt and restore default behavior when needed
- Avoid unsafe work inside a handler and hand off to the worker loop

## Python features introduced
`signal module`, `signal.signal handler registration`, `signal.SIGINT / SIGTERM`, `KeyboardInterrupt relationship to SIGINT`, `main-thread-only handler constraint`, `signal.raise_signal`, `re-entrancy / async-signal-safety caveats`, `setting a shutdown Event from a handler`

## MiniERP increment
Wires the report-job runner's CLI entry point to handle SIGINT/SIGTERM: the handler sets the shutdown Event from lesson 1 so workers finish their current job and drain the queue before exit, giving MiniERP a clean Ctrl-C / kill story for batch runs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** An install_handlers(shutdown_event) that registers handlers flipping the Event; the runner loop checks it between jobs.
- **Test focus:** Raising SIGINT/SIGTERM (via signal.raise_signal) sets the Event and triggers a drain-then-stop without losing in-flight jobs; handler does no heavy work.

</div>
