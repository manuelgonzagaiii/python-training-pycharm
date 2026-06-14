# What concurrency buys MiniERP (and the GIL)

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 34.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain the difference between concurrency and parallelism in plain terms
- Describe what the GIL is, why CPython has it, and exactly which workloads it does and does not slow down
- Understand that threads still give real speedups for I/O-bound work (network, disk, subprocess) even with the GIL
- Know that Python 3.14 ships an experimental free-threaded build and how to detect the GIL state at runtime
- Recognize which MiniERP operations (CSV import, report generation, email) are I/O-bound vs CPU-bound so you choose the right tool later

## Python features introduced
`threading module overview`, `Global Interpreter Lock (GIL) concept`, `sys._is_gil_enabled()`, `PEP 703 free-threading (no-GIL) build awareness`, `concurrency vs parallelism distinction`, `I/O-bound vs CPU-bound work`

## MiniERP increment
Adds a docs/concurrency.md design note and a tiny erp/concurrency/probe.py helper that reports the interpreter's threading capabilities (GIL on/off, CPU count) which later tasks import. No behavior change to the domain core yet; this frames the whole phase.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A read page plus a probe() function returning a dataclass with gil_enabled, cpu_count, and a recommended_strategy string the reader can run to see their own interpreter's stance.
- **Test focus:** Theory task: no automated checks; reader runs probe() and reads the GIL explanation.

</div>
