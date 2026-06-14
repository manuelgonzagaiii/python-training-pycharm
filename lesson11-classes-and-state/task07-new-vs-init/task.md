# __new__ vs __init__: Who Builds the Object

> **Phase:** OOP Foundations  •  **Stage:** 11.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that __new__ creates the instance and __init__ initializes it
- Override __new__ correctly (return super().__new__(cls)) and see ordering
- Learn a legitimate use of __new__: caching/interning instances by key
- Know when NOT to override __new__ (most classes never need it)

## Python features introduced
`__new__ static constructor`, `__init__ initializer`, `object.__new__`, `control flow of instance creation`, `interning / caching with __new__`

## MiniERP increment
Give Product a lightweight SKU-interning cache via __new__ so identical SKUs return the same canonical Product instance (a real catalog dedup concern), while __init__ still sets the fields — demonstrating the two-phase creation explicitly.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Product:
    _by_sku: dict[str, "Product"] = {}

    def __new__(cls, sku: str, name: str, price_cents: int) -> "Product":
        ...  # if sku in cls._by_sku: return cached; else create via super().__new__(cls)

    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        ...  # set fields; cache self in cls._by_sku
- **Test focus:** Assert constructing two Products with the same SKU returns the identical object (is); assert __new__ runs before __init__; assert a different SKU yields a different object.

</div>
