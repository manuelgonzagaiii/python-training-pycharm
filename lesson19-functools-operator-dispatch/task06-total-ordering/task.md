# Sortable domain objects with total_ordering

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.6 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Make a domain object fully orderable by writing only __eq__ and __lt__
- Let total_ordering synthesize the remaining comparison operators
- Sort and min/max ERP objects directly
- Understand the trade-offs vs dataclass order=True

## Python features introduced
`functools.total_ordering`, `defining __eq__ and one ordering op`, `auto-derived __lt__/__le__/__gt__/__ge__`, `rich comparison methods`, `sorting domain objects`, `operator.lt and comparison via operator`

## MiniERP increment
Make ProductSales summary rows orderable in the analytics module with @total_ordering (defining only __eq__ and __lt__ on revenue) so top-seller reports can sort/min/max product summaries directly without custom key functions everywhere.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import total_ordering

@total_ordering
class ProductSales:
    def __init__(self, sku, revenue):
        self.sku, self.revenue = sku, revenue
    def __eq__(self, other):
        # TODO: equal when revenue matches
        ...
    def __lt__(self, other):
        # TODO: order by revenue
        ...

- **Test focus:** Only __eq__ and __lt__ are defined yet all of <, <=, >, >= and sorting/min/max work correctly via total_ordering; equal-revenue rows compare equal; NotImplemented handled for foreign types.

</div>
