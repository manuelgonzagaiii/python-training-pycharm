# LineItem and Container Dunders

> **Phase:** OOP Foundations  •  **Stage:** 13.4 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build LineItem and an Invoice that holds a list of line items
- Implement __len__ so len(invoice) returns item count
- Implement __bool__ (an empty invoice is falsy) and __iter__/__getitem__/__contains__
- Understand truthiness checks __bool__ first, then falls back to __len__

## Python features introduced
`__len__`, `__bool__`, `__getitem__`, `__contains__`, `__iter__`, `container protocol basics`, `truthiness via __bool__ then __len__`

## MiniERP increment
Introduce LineItem(product, quantity) with a computed line_total (Money) and an Invoice that contains LineItems, supporting len(invoice), iteration, indexing, `product in invoice`, and emptiness checks — the core of Sales & Invoicing.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class LineItem:
    def __init__(self, product: Product, quantity: int) -> None:
        ...
    @property
    def line_total(self) -> Money:
        ...  # product price * quantity

class Invoice:
    def __init__(self) -> None:
        self._items: list[LineItem] = []
    def add(self, item: LineItem) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __iter__(self): ...
    def __getitem__(self, index: int) -> LineItem: ...
    def __contains__(self, product: Product) -> bool: ...
- **Test focus:** Assert len(invoice) counts items; bool(empty)==False and bool(non-empty)==True; iterating yields LineItems; invoice[0] indexes; `product in invoice` works; line_total equals price*quantity as Money.

</div>
