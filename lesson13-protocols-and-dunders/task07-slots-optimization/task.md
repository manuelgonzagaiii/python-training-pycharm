# Locking Down Memory with __slots__

> **Phase:** OOP Foundations  •  **Stage:** 13.7 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Add __slots__ to fix the allowed attribute set and drop per-instance __dict__
- Understand the memory savings for many small objects (whole catalogs/invoices)
- See that __slots__ blocks accidental typo attributes by raising AttributeError
- Know the tradeoffs: no dynamic attributes, interaction with properties and subclassing

## Python features introduced
`__slots__`, `absence of __dict__`, `memory footprint reduction`, `AttributeError on stray attributes`, `slots vs dynamic attributes tradeoff`, `slots interaction with properties/inheritance`

## MiniERP increment
Add __slots__ to Money, Product, LineItem, and Customer (the high-cardinality domain objects) to shrink memory and prevent typo'd attributes — finalizing the shared domain layer that all four MiniERP interfaces will build on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Money:
    __slots__ = ("cents", "currency")
    def __init__(self, cents: int, currency: str = "USD") -> None:
        self.cents = cents
        self.currency = currency

# For classes with properties, slot the BACKING fields, e.g.:
class Product:
    __slots__ = ("sku", "name", "_price_cents", "_discount_cents")
- **Test focus:** Assert a slotted instance has no __dict__; assert setting an undeclared attribute raises AttributeError; assert declared attributes and properties still work; assert backing fields (not property names) are slotted correctly.

</div>
