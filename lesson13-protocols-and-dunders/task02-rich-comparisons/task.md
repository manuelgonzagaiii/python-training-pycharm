# Ordering with total_ordering

> **Phase:** OOP Foundations  •  **Stage:** 13.2 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement __lt__ (and __eq__) and let @functools.total_ordering synthesize the rest
- Understand the total_ordering contract and its minimum required methods
- Return NotImplemented for cross-type comparisons
- Sort domain objects naturally with sorted/min/max

## Python features introduced
`__lt__`, `functools.total_ordering decorator`, `rich-comparison dunders (__lt__ __le__ __gt__ __ge__)`, `NotImplemented in comparisons`, `sorted()/min()/max()`, `key vs natural ordering`

## MiniERP increment
Make Money fully orderable via @functools.total_ordering (comparing cents, same currency) and give Product a natural sort by price; reporting can now sort invoices and rank products without custom key functions.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import functools

@functools.total_ordering
class Money:
    def __eq__(self, other: object) -> bool:
        ...

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        ...  # compare cents (assume same currency)
- **Test focus:** Assert <, <=, >, >= all work though only __lt__/__eq__ are defined; assert sorted() orders Money ascending by cents; assert comparing across types returns NotImplemented / raises TypeError as expected.

</div>
