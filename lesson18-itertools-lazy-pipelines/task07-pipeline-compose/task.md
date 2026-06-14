# Composing the full lazy report pipeline

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Wire filter -> group -> accumulate -> paginate stages into one pipeline
- Keep the whole pipeline lazy from source to sink
- Respect single-pass semantics when stages share a source
- See a real lazy reporting pipeline run with bounded memory

## Python features introduced
`function composition of generators`, `passing iterators between stages`, `filter()/map() builtins vs gen-exprs`, `single-pass discipline across a pipeline`, `itertools.islice for bounding`, `end-to-end lazy evaluation`

## MiniERP increment
Assemble the reporting module's headline build_report(ledger, *, sku=None, page=None) function that composes the lesson's generators (filter by SKU, group by SKU, running subtotal, paginate) into one lazy pipeline — MiniERP's reusable report engine that later CLI/Web/GUI/TUI front-ends all call.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def build_report(ledger, *, sku=None, page_no=None, page_size=50):
    """Compose the lazy stages into one report stream."""
    stream = iter(ledger)
    if sku is not None:
        stream = (ln for ln in stream if ln.product_sku == sku)
    # TODO: feed `stream` through revenue_by_sku, then page() if page_no is set
    ...

- **Test focus:** Pipeline returns correct rows for combinations of sku/page filters; stays lazy (source consumed at most once); composing stages does not break grouping/pagination; matches an eager reference implementation.

</div>
