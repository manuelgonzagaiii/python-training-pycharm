# Product Base Class & super()

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 15.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Design a base class and call super().__init__() from subclasses
- Override methods and extend (not replace) base behavior via super()
- Understand how attributes initialized in a base are available to subclasses
- Recognize where a base method should defer to subclasses (price calculation hook)

## Python features introduced
`class inheritance`, `super().__init__()`, `method overriding`, `__init_subclass__ basics`, `abstract-ish base via NotImplementedError`, `instance attributes vs class attributes`

## MiniERP increment
Introduces product.py with a Product base (sku, name, unit_price: Money) and a price()/line_total() contract. Refactors the earlier flat product class into the root of a hierarchy the inventory module builds on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from money import Money
from sku import SKU


class Product:
    def __init__(self, sku: SKU, name: str, unit_price: Money) -> None:
        self.sku = sku
        self.name = name
        self.unit_price = unit_price

    def price(self) -> Money:
        # base price; subclasses may extend via super().price()
        return self.unit_price

    def line_total(self, qty: int) -> Money:
        # TODO: return price() * qty using Money arithmetic
        ...

- **Test focus:** Product stores fields, price() returns unit_price, line_total multiplies via Money, a subclass can call super().__init__ and super().price().

</div>
