# Dict views and the | merge operator

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Iterate a dict with .items() and understand views are dynamic
- Merge two dicts with | and |= and know that the right operand wins on conflicts
- Compare the | operator with the {**a, **b} spread form

## Python features introduced
`dict.keys/values/items views`, `live view semantics`, `iterating items()`, `dict union operator |`, `in-place |=`, `PEP 584`, `later-key-wins merge rule`, `dict() and {**a, **b} merging`

## MiniERP increment
Adds apply_overrides(base, overrides) that merges a price/qty override dict onto the base index with |, used later when importing updated catalog data. Reports can now overlay changes without mutating the source.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def apply_overrides(base: dict[str, Product], overrides: dict[str, Product]) -> dict[str, Product]:
    """Return a new dict where overrides replace matching base entries (| merge)."""
    ...
- **Test focus:** apply_overrides returns a merged dict where overlapping keys take the override value and non-overlapping keys from both survive; the original base dict is not mutated.

</div>
