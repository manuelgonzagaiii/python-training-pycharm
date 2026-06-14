# Grouping with groupby (and why sorting matters)

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Group sale lines by product SKU using groupby with a key function
- Learn the critical gotcha: groupby only groups CONSECUTIVE keys, so sort first
- Materialize each group's sub-iterator before moving on
- Produce per-SKU revenue subtotals from the grouped stream

## Python features introduced
`itertools.groupby`, `key function`, `groupby requires pre-sorted input`, `consuming the group sub-iterator before advancing`, `operator.itemgetter/attrgetter as key (preview)`, `sorted() with key`, `building per-group aggregates lazily`

## MiniERP increment
Add revenue_by_sku(ledger) to the reporting/analytics module: sort the line stream by SKU then groupby to emit (sku, units, subtotal) tuples — the first real aggregation report, delivered lazily group-by-group.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from itertools import groupby
from operator import attrgetter

def revenue_by_sku(ledger):
    """Yield (sku, total_units, subtotal) per product, lazily."""
    by_sku = sorted(ledger, key=attrgetter("product_sku"))  # groupby needs sorted input!
    for sku, group in groupby(by_sku, key=attrgetter("product_sku")):
        # TODO: consume `group` to sum units and subtotal, then yield the tuple
        ...

- **Test focus:** Groups are correct and complete (no SKU split across groups thanks to the sort); subtotals and unit counts are right; demonstrates that omitting the sort would mis-group; output is per-group lazy.

</div>
