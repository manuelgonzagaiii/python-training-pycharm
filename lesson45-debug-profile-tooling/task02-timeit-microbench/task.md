# Micro-benchmarking the hot path with timeit

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Measure a small operation reliably with timeit, using setup correctly
- Use repeat and take the minimum rather than the mean
- Compare two implementations of the same function fairly
- Recognize what timeit can and cannot tell you (no per-line attribution)

## Python features introduced
`timeit.timeit / timeit.repeat`, `timeit.Timer with setup`, `python -m timeit CLI`, `min-of-repeat methodology and why mean is misleading`, `autorange / number selection`, `avoiding setup cost leakage into the measured block`

## MiniERP increment
Add erp/perf/bench_report.py: a timeit harness that benchmarks the reporting module's revenue-by-category aggregation over a generated dataset, comparing the current implementation against a candidate (e.g. dict-accumulate vs repeated list filtering). It reports the min-of-repeat timing so the next task's optimization can be justified with numbers.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import timeit
from erp.reporting import revenue_by_category

setup = 'from erp.testdata import make_sales; sales = make_sales(10_000)'
best = min(timeit.repeat(
    stmt='revenue_by_category(sales)',
    setup=setup, repeat=5, number=10))
print(f'{best=:.4f}s')

- **Test focus:** Checks confirm the harness uses timeit.repeat (or Timer) with a setup that excludes data generation from the measured block, takes the minimum across repeats, and benchmarks the real revenue_by_category function rather than a stub.

</div>
