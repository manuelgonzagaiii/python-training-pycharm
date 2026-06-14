# Finding the bottleneck: cProfile, pstats & a measured fix

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Profile a whole run with cProfile and save a .prof file
- Sort and read pstats output to find where time is actually spent (cumulative vs total)
- Apply a targeted optimization to the identified hot function
- Prove the optimization with before/after profiling and timeit numbers (no guessing)

## Python features introduced
`cProfile.run / cProfile.Profile / python -m cProfile -o out.prof`, `pstats.Stats: sort_stats('cumulative'|'tottime'), print_stats, print_callers/print_callees`, `interpreting ncalls / tottime / cumtime / percall`, `strip_dirs`, `reading a profile to locate the hot function`, `verifying an optimization by re-profiling and re-running timeit`

## MiniERP increment
Profile MiniERP's full report-generation entry point with cProfile, use pstats to confirm revenue_by_category (or its inner loop) is the hot spot, then optimize it (replace O(n*m) repeated filtering with a single-pass dict/Counter aggregation) and add tests/test_reporting_perf.py that asserts the result is unchanged. The optimized aggregator becomes MiniERP's reporting core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import cProfile, pstats
from erp.reporting import generate_report
from erp.testdata import make_sales

cProfile.run('generate_report(make_sales(20_000))', 'report.prof')
stats = pstats.Stats('report.prof').strip_dirs().sort_stats('cumulative')
stats.print_stats(10)
# TODO: optimize revenue_by_category, keep results identical, re-profile

- **Test focus:** Checks confirm the optimized aggregation produces results identical to the original (a correctness regression test), and that the implementation is now single-pass (e.g. uses a dict/Counter rather than nested filtering) so the documented speedup is real.

</div>
