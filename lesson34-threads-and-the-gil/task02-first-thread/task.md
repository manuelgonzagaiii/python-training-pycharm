# Run a report off the main thread

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create, start, and join a Thread so the caller does not block on a slow report
- Pass arguments into a thread target safely
- Understand daemon vs non-daemon threads and when the interpreter waits for a thread
- Observe that results from a thread are not returned by join() and reason about how to collect them

## Python features introduced
`threading.Thread`, `Thread(target=, args=, kwargs=)`, `Thread.start()`, `Thread.join()`, `Thread.name / Thread.daemon`, `threading.current_thread()`, `callable passed as target`

## MiniERP increment
Adds erp/reports/runner.py with run_report_in_thread(report_fn, *args) that runs an existing reporting function (e.g. the sales summary built earlier) on a background Thread so the CLI stays responsive. Stores the report result in a shared holder object the caller reads after join().

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A function that builds a Thread targeting a reporting callable, starts it, joins it, and surfaces the computed report; a daemon flag toggles whether shutdown waits.
- **Test focus:** Assert the report runs on a non-main thread, join() blocks until done, and the produced report matches the synchronous result.

</div>
