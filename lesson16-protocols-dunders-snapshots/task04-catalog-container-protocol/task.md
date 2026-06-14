# Catalog: Container & Iterable Dunders

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement __len__, __getitem__, __contains__, __iter__ so a custom Catalog works with len(), [], in, and for
- Understand the difference between an iterable (__iter__) and an iterator
- Support membership tests by SKU and iteration over products
- Add __reversed__ for reverse iteration

## Python features introduced
`__len__`, `__getitem__`, `__contains__`, `__iter__`, `__reversed__`, `iterator vs iterable`, `indexing and slicing support`, `for-loop protocol`

## MiniERP increment
Adds Catalog, a first-class collection of Products that supports len(catalog), catalog[sku], product in catalog, and for product in catalog. This is the browsable product list the CLI/Web/GUI front-ends will render.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from product import Product


class Catalog:
    def __init__(self) -> None:
        self._by_sku: dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self._by_sku[product.sku.code] = product

    def __len__(self) -> int: ...
    def __getitem__(self, sku_code: str) -> Product: ...
    def __contains__(self, sku_code: str) -> bool: ...
    def __iter__(self): ...

- **Test focus:** len(catalog), catalog['SKU1'], 'SKU1' in catalog, iterating yields products, reversed() works, KeyError for missing SKU.

</div>
