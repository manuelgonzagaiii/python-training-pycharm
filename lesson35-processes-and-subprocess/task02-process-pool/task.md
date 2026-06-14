# Parallel reports with ProcessPoolExecutor & Pool

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 35.2 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Fan out independent CPU-bound report partitions across all cores with ProcessPoolExecutor and the same Future API learned for threads
- Compare it with the classic multiprocessing.Pool (map/imap/apply_async)
- Understand why worker functions must be importable top-level functions (pickling), unlike with thread pools
- Tune chunksize to amortize per-task overhead

## Python features introduced
`concurrent.futures.ProcessPoolExecutor`, `executor.map across processes`, `multiprocessing.Pool`, `Pool.map / Pool.imap / Pool.apply_async`, `AsyncResult`, `chunksize tuning`, `picklable top-level worker functions`

## MiniERP increment
Upgrades parallel reporting: month-end analytics are partitioned (per product category / per month) and computed across a ProcessPoolExecutor, then merged. The same reporting service that ran on threads now scales across cores for the heavy path; the job runner picks thread vs process pool based on whether the job is I/O- or CPU-bound.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A top-level partition_worker(part) plus a driver that maps it over partitions with ProcessPoolExecutor and reduces the results; a Pool-based variant for contrast.
- **Test focus:** Parallel result equals the sequential reduction, work is distributed across multiple PIDs, and an unpicklable closure is shown to fail (teaching the constraint).

</div>
