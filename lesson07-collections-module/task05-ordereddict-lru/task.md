# OrderedDict: move_to_end and LRU recall

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.5 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use move_to_end to maintain a most-recently-used ordering
- Evict the least-recently-used entry with popitem(last=False)
- Know which OrderedDict features remain useful now that plain dicts keep order

## Python features introduced
`collections.OrderedDict`, `move_to_end`, `popitem(last=...)`, `order-sensitive equality vs dict`, `reordering on access`, `OrderedDict vs plain dict in 3.7+ (what's still unique)`

## MiniERP increment
Adds a tiny LRU 'recently viewed products' cache (touch(cache, sku) re-orders, evict drops the stalest) for the front-ends' UX — built on OrderedDict.move_to_end.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from collections import OrderedDict

def touch(cache: OrderedDict[str, ProductRecord], sku: str, product: ProductRecord, capacity: int) -> None:
    """Insert/refresh sku as most-recently-used; evict the LRU entry past capacity."""
    ...
- **Test focus:** touch moves an existing sku to the most-recent end; exceeding capacity evicts the least-recently-used (first) entry; access order is observable and correct.

</div>
