# Sharing data across processes

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 35.3 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Send messages between processes with Pipe and a process-safe Queue
- Share structured progress state with a Manager (proxy dict/Namespace) guarded by a process Lock
- Share simple scalars/arrays cheaply with Value and Array
- Share a large buffer zero-copy with shared_memory.SharedMemory and a memoryview, and clean it up (close/unlink)
- Choose the right sharing mechanism for the data size and shape

## Python features introduced
`multiprocessing.Pipe`, `multiprocessing.Queue`, `multiprocessing.Manager`, `Manager().dict / list / Namespace`, `multiprocessing.Value`, `multiprocessing.Array`, `multiprocessing.Lock (process-shared)`, `multiprocessing.shared_memory.SharedMemory`, `memoryview over shared memory`

## MiniERP increment
Adds a cross-process progress channel to parallel reporting: workers report rows-processed into a Manager dict (live progress for the CLI/web), a Value tracks a global running total under a process Lock, and a large numeric matrix for analytics is passed via shared_memory instead of being pickled, with proper unlink on teardown.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Workers push progress over a Queue/Manager and accumulate into a shared Value/Array; a shared_memory block carries a big buffer between parent and children.
- **Test focus:** Aggregated shared total matches the expected sum under concurrency, the Manager dict reflects every worker's progress, and shared_memory carries the buffer correctly and is unlinked (no leaked segments).

</div>
