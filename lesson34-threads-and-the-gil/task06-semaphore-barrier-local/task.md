# Throttling, rendezvous & per-thread state

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Limit concurrency to N with a (Bounded)Semaphore so report jobs do not exhaust a scarce resource (e.g. DB connections / file handles)
- Use a Barrier to make a fixed set of worker threads start a batch phase together
- Store per-thread state (a per-thread DB connection / scratch buffer / request id) in threading.local without locks
- Explain why BoundedSemaphore catches release-without-acquire bugs

## Python features introduced
`threading.Semaphore`, `threading.BoundedSemaphore`, `threading.Barrier`, `Barrier.wait / parties / BrokenBarrierError`, `threading.local`, `thread-local storage`, `resource-pool / rate-limit pattern`

## MiniERP increment
Adds a connection/permit pool: report and import workers must acquire a BoundedSemaphore permit before touching the persistence layer, capping concurrent DB access. Each worker keeps its own persistence handle in threading.local. A Barrier synchronizes a multi-phase month-end batch so all workers finish phase 1 before any begins phase 2.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A permit-limited resource pool, a threading.local connection cache, and a Barrier-coordinated two-phase batch run.
- **Test focus:** Concurrent access never exceeds the semaphore limit; each thread sees its own local handle; the barrier releases all parties simultaneously and raises BrokenBarrierError if a party aborts.

</div>
