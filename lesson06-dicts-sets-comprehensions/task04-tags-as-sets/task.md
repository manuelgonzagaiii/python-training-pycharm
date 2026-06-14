# Product tags as sets; set algebra

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Model each product's tags as a set and dedupe automatically
- Combine tag sets with union/intersection/difference/symmetric-difference
- Test subset relationships for 'has all required tags' filtering

## Python features introduced
`set`, `set literal`, `set comprehension preview`, `add/discard/remove`, `union |`, `intersection &`, `difference -`, `symmetric difference ^`, `subset/superset <= >=`, `membership in`, `uniqueness/dedup`, `set is unordered`

## MiniERP increment
Adds a parallel tags index dict[str, set[str]] and functions products_with_all_tags / products_with_any_tags using & and | over sets — powering tag-based catalog filtering for search.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def products_with_all_tags(tags_index: dict[str, set[str]], required: set[str]) -> set[str]:
    """Return skus whose tag set is a superset of `required`."""
    ...

def products_with_any_tags(tags_index: dict[str, set[str]], wanted: set[str]) -> set[str]:
    """Return skus whose tag set intersects `wanted`."""
    ...
- **Test focus:** products_with_all_tags returns only skus whose tags >= required (superset test); products_with_any_tags returns skus with non-empty intersection; both return sets, and empty inputs behave sensibly.

</div>
