# Behavior Lives on the Object

> **Phase:** OOP Foundations  •  **Stage:** 11.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Move former free functions onto the class as methods
- Call one method from another through self
- Understand that a method is a function whose first argument is the instance
- Co-locate behavior with the data it operates on

## Python features introduced
`instance methods`, `self`, `methods calling other methods via self`, `returning derived values`, `method vs free-function comparison`

## MiniERP increment
Migrate the old free functions (e.g. product_label, price_display) into Product methods such as label() and price_display() returning '$15.00', so the catalog's behavior now lives on the object itself.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    CURRENCY: str = "USD"

    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        ...

    def price_display(self) -> str:
        ...  # f"${self.price_cents / 100:.2f}"

    def summary(self) -> str:
        ...  # combine label() and price_display() by calling self.<method>()
- **Test focus:** Assert price_display() formats cents as '$15.00'; assert summary() composes label() and price_display() by calling them through self.

</div>
