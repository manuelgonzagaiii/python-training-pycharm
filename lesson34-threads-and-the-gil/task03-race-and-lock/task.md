# Two threads, one ledger: races and Lock

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Reproduce a race condition by mutating shared MiniERP state (an in-memory stock counter / sequence) from many threads
- Protect a critical section with a Lock using the with-statement
- Understand why a re-entrant RLock is needed when a locked method calls another locked method on the same object
- Reason about lock granularity and the cost of holding a lock too long

## Python features introduced
`threading.Lock`, `Lock as context manager (with lock:)`, `threading.RLock`, `reentrant locking`, `race condition demonstration`, `critical section / mutual exclusion`

## MiniERP increment
Hardens the in-memory inventory/sequence service so concurrent stock adjustments and ID allocation are atomic: wraps the mutable counters in a Lock, and uses an RLock for the service whose public methods call each other while holding the lock.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A thread-unsafe Counter/StockLevel class plus a fixed version guarded by Lock/RLock; tests hammer it from many threads.
- **Test focus:** Unguarded version loses updates under contention; guarded version always reaches the exact expected total and never deadlocks on re-entrant calls.

</div>
