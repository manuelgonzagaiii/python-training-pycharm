# Alternate Constructors with @classmethod

> **Phase:** OOP Foundations  •  **Stage:** 11.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a @classmethod that receives cls and builds an instance
- Understand cls vs self and why factories use cls (subclass-friendly)
- Provide multiple named construction paths for one class
- Use a class attribute mutated through cls to track instances

## Python features introduced
`@classmethod decorator`, `cls parameter`, `alternative constructors / factory methods`, `returning cls(...)`, `class-level counter via cls`

## MiniERP increment
Add Product.from_row(cls, row) to build a Product from a CSV-style tuple/dict (mirroring the import format from earlier phases) and from_dict(cls, data), giving the catalog clean factory entry points for later Import/Export.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        ...

    @classmethod
    def from_row(cls, row: tuple[str, str, int]) -> "Product":
        ...  # return cls(*row)

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Product":
        ...  # return cls(data["sku"], data["name"], data["price_cents"])
- **Test focus:** Assert from_row builds an equivalent Product to the direct constructor; assert from_dict reads the right keys; assert the factory returns an instance of the class.

</div>
