# ChainMap: layered config and multi-location stock

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.6 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Stack multiple mappings so lookups fall through from most- to least-specific
- Layer per-warehouse overrides over a default stock map without copying
- Use new_child to add a scratch layer; know writes only touch the top map

## Python features introduced
`collections.ChainMap`, `lookup falls through layers`, `first-map-wins`, `new_child`, `maps attribute`, `writes hit only the first map`, `ChainMap for layered settings`

## MiniERP increment
Adds effective_stock(default_levels, *warehouse_overrides) returning a ChainMap so a SKU resolves to its warehouse-specific level or the default — the multi-location inventory view, also reused later for layered config (defaults < file < env).

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from collections import ChainMap

def effective_stock(default_levels: dict[str, int], *overrides: dict[str, int]) -> ChainMap:
    """Layer overrides over defaults; earlier overrides win on conflicts."""
    ...
- **Test focus:** effective_stock resolves a sku to the highest-priority layer that defines it, falling back to defaults; an override layer shadows the default; keys present only in defaults still resolve.

</div>
