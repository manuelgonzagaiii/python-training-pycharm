# Memory with tracemalloc & bytecode with dis

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Measure peak and per-line memory allocation with tracemalloc and compare snapshots
- Reduce peak memory by streaming the dataset with a generator instead of materializing a list
- Disassemble two implementations with dis to see why one does less work
- Combine memory and bytecode evidence with the earlier timing evidence

## Python features introduced
`tracemalloc.start / take_snapshot / Snapshot.compare_to / statistics('lineno')`, `tracemalloc.get_traced_memory (current vs peak)`, `generators vs lists for memory (lazy aggregation)`, `dis.dis / dis.Bytecode`, `reading bytecode to compare two implementations`, `sys.getsizeof as a complementary check`

## MiniERP increment
Add erp/perf/mem_report.py using tracemalloc to compare peak memory of list-materialized vs generator-streamed sales aggregation, and refactor the report pipeline to stream large datasets lazily. Add a short dis-based note comparing the bytecode of the old nested-filter aggregation vs the new single-pass one, completing the profiling story for MiniERP's hot path.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import tracemalloc
import dis
from erp.reporting import revenue_by_category, revenue_by_category_streaming
from erp.testdata import make_sales

tracemalloc.start()
revenue_by_category(list(make_sales(50_000)))
print('list peak', tracemalloc.get_traced_memory()[1])
# TODO: snapshot.compare_to for streaming version; dis.dis(both)

- **Test focus:** Checks confirm tracemalloc measures peak for both implementations and the streaming version has lower peak, that the streaming aggregator yields the same result as the list version, and that dis is invoked to compare the two implementations.

</div>
