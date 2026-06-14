# Shared vs. Per-Object State

> **Phase:** OOP Foundations  •  **Stage:** 11.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish a class attribute (shared by all instances) from an instance attribute (unique per object)
- See how assigning to self.x shadows a class attribute x for that instance
- Recognize the classic mutable-class-attribute bug and why instance state belongs in __init__
- Use a class attribute for a true constant shared across the catalog

## Python features introduced
`class attributes`, `instance attributes`, `attribute shadowing`, `mutable-class-attribute pitfall`, `class-level constants`

## MiniERP increment
Add a class attribute CURRENCY = 'USD' shared by every Product, and a class-attribute count or DEFAULT_TAX_RATE constant, while keeping sku/name/price per-instance — clarifying which catalog facts are global vs. per-product.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    CURRENCY: str = "USD"      # class attribute: shared by ALL products
    DEFAULT_TAX_RATE: float = 0.0

    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        ...  # instance attributes: unique per product
- **Test focus:** Assert Product.CURRENCY is readable on both the class and an instance; assert two distinct instances share the class attribute but hold independent sku/name/price; demonstrate that setting price on one instance does not change another.

</div>
