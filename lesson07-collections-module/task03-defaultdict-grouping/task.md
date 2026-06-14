# defaultdict: grouping without setdefault

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.3 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Group products by category with defaultdict(list) — cleaner than setdefault
- Choose the right default_factory (list vs set vs int)
- Understand the access side-effect (reading a missing key creates it)
- Convert a defaultdict back to a plain dict for output

## Python features introduced
`collections.defaultdict`, `default_factory (list, set, int)`, `auto-creating missing keys`, `defaultdict vs dict.setdefault`, `nested defaultdict`, `converting back to a plain dict`

## MiniERP increment
Re-implements grouping as group_by_category_dd(catalog) using defaultdict(list) and adds tag_to_skus(tags_index) using defaultdict(set) — an inverted index from tag to the SKUs carrying it, used by search.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from collections import defaultdict

def group_by_category_dd(catalog: list[ProductRecord]) -> dict[str, list[ProductRecord]]:
    """Group by category code using defaultdict(list); return a plain dict."""
    ...

def tag_to_skus(tags_index: dict[str, set[str]]) -> dict[str, set[str]]:
    """Inverted index tag -> set of skus, using defaultdict(set)."""
    ...
- **Test focus:** group_by_category_dd matches the earlier setdefault grouping and returns a plain dict; tag_to_skus inverts the mapping so each tag points to exactly the skus that have it.

</div>
