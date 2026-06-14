# Concurrent bulk CSV import with ThreadPoolExecutor

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Replace hand-managed worker threads with a ThreadPoolExecutor
- Submit work and collect results/exceptions through Future objects
- Stream results as they finish with as_completed and run an ordered batch with executor.map
- Handle and aggregate per-row failures without aborting the whole import
- Reason about why a thread pool is the right tool for this I/O-bound (parse + persist) import

## Python features introduced
`concurrent.futures.ThreadPoolExecutor`, `executor.submit`, `Future`, `Future.result / Future.exception / Future.add_done_callback`, `concurrent.futures.as_completed`, `executor.map`, `with ThreadPoolExecutor() as pool:`, `max_workers tuning`

## MiniERP increment
Delivers concurrent bulk CSV import (first half of the milestone): erp/import_/bulk.py reads a products CSV and imports rows concurrently via ThreadPoolExecutor, returning a summary of succeeded/failed rows. Reuses the validation/parsing from earlier import work and the semaphore-limited persistence from the previous task.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** An import_products_concurrently(path, max_workers) that submits one Future per chunk/row, gathers results via as_completed, and aggregates an ImportReport.
- **Test focus:** All valid rows are imported, bad rows are reported individually (not fatally), the result equals the sequential import, and per-future exceptions are surfaced rather than swallowed.

</div>
