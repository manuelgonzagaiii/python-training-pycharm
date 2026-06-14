# Folding a stream with reduce

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.1 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Fold a stream into a single value with reduce()
- Always supply an initializer for safety on empty streams
- Recognize when sum/min/max are clearer than reduce
- Combine reduce with operator functions instead of lambdas

## Python features introduced
`functools.reduce`, `reduce with initializer`, `binary reducer functions`, `reduce vs sum/min/max`, `operator module (operator.add, operator.mul)`, `reducing into an accumulator dict`

## MiniERP increment
Add grand_total(report_rows) and totals_by_sku(rows) to the analytics module using functools.reduce — folding the lazy report stream into a grand total and into an accumulator dict of per-SKU subtotals, the canonical reduce-based aggregation.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import reduce
from operator import add

def grand_total(amounts):
    """Fold a stream of amounts into one total with reduce (safe on empty)."""
    # TODO: reduce with operator.add and an initializer of 0.0
    ...

def totals_by_sku(rows):
    """Reduce (sku, amount) rows into a {sku: subtotal} dict."""
    def step(acc, row):
        # TODO: add row's amount into acc[sku] and return acc
        ...
    return reduce(step, rows, {})

- **Test focus:** grand_total returns the correct sum and 0.0 on empty input (initializer used); totals_by_sku accumulates per-SKU subtotals correctly; operator.add path matches a manual loop.

</div>
