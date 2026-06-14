# Stateless Helpers with @staticmethod

> **Phase:** OOP Foundations  •  **Stage:** 11.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a @staticmethod that takes neither self nor cls
- Decide when a helper belongs as static (no instance/class state needed)
- Group a pure utility under the class as a namespace
- Contrast static, class, and instance methods in one place

## Python features introduced
`@staticmethod decorator`, `no self/cls`, `namespacing utility functions on a class`, `when static vs class vs instance method`

## MiniERP increment
Add Product.is_valid_sku(value) as a @staticmethod validating SKU format (e.g. non-empty, alphanumeric) used by the factories and later by import validation — a pure rule that needs no instance.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    @staticmethod
    def is_valid_sku(value: str) -> bool:
        ...  # return bool(value) and value.isalnum()

    @classmethod
    def from_row(cls, row: tuple[str, str, int]) -> "Product":
        ...  # may call cls.is_valid_sku(row[0]) before constructing
- **Test focus:** Assert is_valid_sku accepts valid SKUs and rejects empty/invalid ones; assert it is callable on both the class and an instance without an instance argument.

</div>
