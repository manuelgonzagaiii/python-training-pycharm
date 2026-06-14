# Any vs. the Collection ABCs

> **Phase:** Modern Type System  •  **Stage:** 23.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Know that Any opts out of type checking and should be a last resort, not a default
- Choose abstract collection types (Iterable, Iterator, Sequence, Mapping) for parameters to accept the widest reasonable input
- Apply 'be liberal in what you accept (Iterable), be precise in what you return (list)'
- Import the runtime-subscriptable ABCs from collections.abc and understand their relationship to typing aliases

## Python features introduced
`Any`, `typing.Iterable`, `typing.Iterator`, `typing.Sequence`, `typing.Mapping`, `collections.abc generics`, `accept-broad / return-narrow principle`, `why Any disables checking`

## MiniERP increment
Service helpers (e.g. total_inventory_value, index_products) are typed to accept Iterable[Product] and Mapping[str, Product] and to return concrete lists/dicts, making the service layer composable with any container the four interfaces pass in.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections.abc import Iterable, Mapping
from typing import Any

def total_inventory_value(products: Iterable[Product]) -> float:
    # TODO: sum price * total_stock for each product
    ...

def index_products(products: Iterable[Product]) -> dict[str, Product]:
    # TODO: build {sku: product}
    ...

def raw_payload() -> Any:  # demonstrates the escape hatch (and its cost)
    ...
- **Test focus:** Tests pass a generator (not a list) into total_inventory_value to prove Iterable acceptance, verify the dict built by index_products, and a check confirms parameters are typed as abstract collections rather than concrete list.

</div>
