# Define the Product Class

> **Phase:** OOP Foundations  •  **Stage:** 11.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a class with __init__ that stores instance attributes
- Understand self as the first parameter of every instance method
- Add an instance method that uses self.<attr> to compute a result
- Construct instances and read their attributes

## Python features introduced
`class statement`, `__init__ initializer`, `self`, `instance attributes`, `method definition`, `attribute assignment in __init__`

## MiniERP increment
Create the Product domain class with sku, name, and price_cents instance attributes set in __init__, plus a label() method returning 'SKU - Name'. This is the first real domain object in MiniERP.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        ...  # store sku, name, price_cents as instance attributes

    def label(self) -> str:
        ...  # return f"{self.sku} - {self.name}"
- **Test focus:** Construct a Product, assert each instance attribute is stored correctly, and assert label() returns the 'SKU - Name' format.

</div>
