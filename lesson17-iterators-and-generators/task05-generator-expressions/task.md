# Generator expressions for filtered streams

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write generator expressions to filter and transform sale lines lazily
- Know when parentheses are optional (single function argument)
- Compare memory/behavior of a list comprehension vs a generator expression
- Feed a generator expression straight into sum()/max() without an intermediate list

## Python features introduced
`generator expressions`, `difference between [list comp] and (gen expr)`, `lazy filtering and mapping`, `generator expression as sole argument to a function (sum(... for ...))`, `memory profile of lazy vs eager`, `chaining gen-exprs into a pipeline`

## MiniERP increment
Add lazy filter helpers to the reporting module (e.g. lines for a given product SKU, lines above a price threshold) built as generator expressions, and compute a revenue total by feeding a generator expression directly into sum() — no intermediate lists allocated.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def lines_for_sku(ledger, sku):
    # TODO: return a generator expression yielding only lines whose product_sku == sku
    ...

def revenue_total(ledger):
    # TODO: sum qty * unit_price across all lines using a generator expression
    # passed directly to sum() (no list in between)
    ...

- **Test focus:** lines_for_sku returns a lazy generator (not a list) that filters correctly; revenue_total returns the right float; confirm no intermediate list is materialized (e.g. result is a generator/uses sum over a gen-expr).

</div>
