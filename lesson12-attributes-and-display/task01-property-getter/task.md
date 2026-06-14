# Computed Attributes with @property

> **Phase:** OOP Foundations  •  **Stage:** 12.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Turn a method-like calculation into an attribute accessed without parentheses
- Create a read-only computed attribute derived from other state
- Understand a property is a descriptor that runs code on attribute access
- Keep derived values always consistent instead of stored and stale

## Python features introduced
`@property decorator`, `getter method`, `computed/derived attribute`, `read-only attribute`, `self in property`

## MiniERP increment
Add a computed price_dollars @property to Product (derived from price_cents) so callers read product.price_dollars; this becomes the canonical display value used across interfaces.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        self.price_cents = price_cents
        ...

    @property
    def price_dollars(self) -> float:
        ...  # return self.price_cents / 100
- **Test focus:** Assert price_dollars is accessed without parentheses and returns price_cents/100; assert it tracks changes to price_cents; assert assigning to the read-only property raises AttributeError.

</div>
