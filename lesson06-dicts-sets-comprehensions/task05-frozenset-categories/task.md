# frozenset: hashable, immutable tag sets

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that only hashable (immutable) objects can be dict keys / set elements
- Use frozenset to make a tag-combination usable as a dict key
- Build a set-of-sets, impossible with mutable sets

## Python features introduced
`frozenset`, `immutability of frozenset`, `hashability`, `frozenset as dict key`, `frozenset as set element`, `set of frozensets`, `why a regular set can't be a key`

## MiniERP increment
Adds catalog_tag_combinations(tags_index) returning a set[frozenset[str]] of the distinct tag-combinations present, the basis for a future faceted-search index keyed by tag bundles.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def catalog_tag_combinations(tags_index: dict[str, set[str]]) -> set[frozenset[str]]:
    """Return the distinct tag combinations as a set of frozensets."""
    ...
- **Test focus:** Result is a set of frozensets; identical tag combinations collapse to one element; the function works when used as a set element (proving hashability).

</div>
