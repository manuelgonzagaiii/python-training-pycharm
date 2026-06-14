# Lazy attributes with cached_property

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.4 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Turn an expensive per-instance total into a cached_property
- Understand the value is computed once then stored in the instance __dict__
- Contrast cached_property (cached) with property (recomputes)
- Invalidate by `del instance.attr` and know it forbids __slots__-only classes

## Python features introduced
`functools.cached_property`, `compute-once-store-on-instance semantics`, `cached_property vs property`, `interaction with __slots__ (needs __dict__)`, `cache invalidation by deleting the attribute`, `lazy per-instance aggregates`

## MiniERP increment
Give the Invoice domain object a cached_property `total` in the sales module that lazily sums its line items once and reuses the result, so repeatedly rendering an invoice across the CLI/Web/GUI views doesn't re-sum the lines every time.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import cached_property

class Invoice:
    def __init__(self, lines):
        self.lines = list(lines)  # note: needs a normal __dict__, not slots-only

    @cached_property
    def total(self):
        """Sum line items once; cached on the instance thereafter."""
        # TODO: return sum(qty * unit_price for each line)
        ...

- **Test focus:** total computes the correct sum; the body runs only once across repeated accesses (use a counter/spy); deleting the attribute forces recompute; behaves as an instance attribute afterward.

</div>
