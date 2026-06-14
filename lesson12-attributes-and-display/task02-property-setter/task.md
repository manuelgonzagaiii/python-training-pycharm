# Validation with a Setter

> **Phase:** OOP Foundations  •  **Stage:** 12.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Pair a getter with a @name.setter to intercept assignment
- Store state in a backing attribute (_price_cents) behind the property
- Validate on set (reject negative prices) and raise ValueError
- Preserve a natural attribute-assignment API while enforcing rules

## Python features introduced
`@property`, `@<name>.setter`, `private backing attribute convention (_x)`, `validation on assignment`, `raising ValueError`

## MiniERP increment
Make Product.price_cents a validated property backed by _price_cents that rejects negative values, ensuring no invalid price ever enters the catalog regardless of which interface sets it.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        self.price_cents = price_cents  # goes through the setter
        ...

    @property
    def price_cents(self) -> int:
        return self._price_cents

    @price_cents.setter
    def price_cents(self, value: int) -> None:
        ...  # validate value >= 0 else raise ValueError; store in self._price_cents
- **Test focus:** Assert setting a valid price updates the backing field; assert setting a negative price raises ValueError; assert __init__ routes through the setter.

</div>
