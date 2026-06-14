# Signaling workers: Event and Condition

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use an Event as a one-shot or repeatable broadcast flag to pause/resume or stop the report worker pool
- Use a Condition to make workers wait until a buffer/state predicate holds, then notify them
- Understand why you re-check the predicate in a while loop after wait()
- Implement a clean, cooperative shutdown rather than killing threads

## Python features introduced
`threading.Event`, `Event.set / clear / wait / is_set`, `threading.Condition`, `Condition.wait / notify / notify_all`, `Condition used with a predicate (while not ready: cond.wait())`, `graceful shutdown flag`, `spurious-wakeup-safe waiting`

## MiniERP increment
Adds a coordinated lifecycle to the job runner: a shutdown Event that tells all report workers to stop after draining, and a Condition that lets workers block until the job buffer is non-empty or capacity frees up. The runner now starts, pauses, resumes, and stops cleanly.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A worker pool that waits on a Condition for available work and watches a shutdown Event; start/pause/resume/stop methods drive them.
- **Test focus:** Setting the shutdown Event stops all workers after the backlog drains; Condition consumers never busy-wait and wake correctly when notified.

</div>
