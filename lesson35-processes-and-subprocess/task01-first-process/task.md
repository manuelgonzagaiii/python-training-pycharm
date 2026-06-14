# Real parallelism: multiprocessing.Process

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 35.1 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run CPU-bound report aggregation in a separate OS process to bypass the GIL
- Understand why multiprocessing needs the __main__ guard and why arguments must be picklable
- Know the difference between spawn and fork start methods and why spawn is the cross-platform default
- Read a child process exit code to detect failure

## Python features introduced
`multiprocessing.Process`, `Process(target=, args=)`, `Process.start / join / is_alive / exitcode`, `__name__ == '__main__' guard requirement`, `spawn vs fork start methods`, `multiprocessing.get_context / set_start_method`, `picklability of arguments`

## MiniERP increment
Adds erp/reports/parallel.py with a compute_in_process() that offloads a CPU-heavy reporting computation (e.g. revenue rollups / margin analytics over many rows) to a child Process, proving the work runs truly in parallel rather than time-sliced.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A picklable report job run via Process(target=...); the parent joins and reads exitcode, with the required if __name__=='__main__' guard demonstrated.
- **Test focus:** The computed result matches the in-thread version, runs in a distinct PID, and a deliberately failing job yields a non-zero exitcode.

</div>
