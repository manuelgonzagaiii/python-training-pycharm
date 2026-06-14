# Structured concurrency: TaskGroup & except*

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use asyncio.TaskGroup for structured concurrency where the group awaits all children and cancels siblings if one fails
- Handle the resulting ExceptionGroup with except* clauses
- Understand how TaskGroup differs from gather (all-or-nothing scoping, automatic cleanup)
- Choose TaskGroup as the default for fan-out that must not leak orphan tasks

## Python features introduced
`asyncio.TaskGroup`, `async with TaskGroup() as tg: tg.create_task(...)`, `structured concurrency guarantees`, `ExceptionGroup`, `except* (PEP 654)`, `sibling-task cancellation on failure`, `comparison with gather`

## MiniERP increment
Reimplements the dashboard fan-out (and a batch async import-notification step) with TaskGroup so any fragment failure cancels its siblings and surfaces an ExceptionGroup the handler maps to a clean partial/error response via except*; replaces the looser gather version for the must-not-leak path.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** An async build_dashboard_tg() using TaskGroup whose handler catches *ValueError / *TimeoutError separately with except*.
- **Test focus:** On one child failing, siblings are cancelled and an ExceptionGroup is raised; except* routes each error type correctly; on success all results are present.

</div>
