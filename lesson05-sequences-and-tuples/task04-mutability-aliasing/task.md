# Aliasing traps: copies vs references

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 5.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- See that assigning a list does NOT copy it — both names alias one object
- Use [:], list(), or .copy() to take a shallow copy before mutating
- Understand why storing records as tuples prevents accidental shared-state edits
- Use is/id() to reason about object identity vs equality

## Python features introduced
`reference semantics`, `aliasing`, `is vs ==`, `id()`, `shallow copy via list() and slicing [:]`, `list.copy`, `shared-reference bug`, `tuple immutability as a safeguard`

## MiniERP increment
Adds snapshot_catalog(catalog) returning an independent shallow copy so callers (later: reports, the web layer) can read a stable view without mutating the source. Hardens the catalog against aliasing bugs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def snapshot_catalog(catalog: list[Product]) -> list[Product]:
    """Return a shallow copy: mutating the result must not change the original."""
    ...
- **Test focus:** snapshot_catalog returns a different list object (distinct id) with equal contents; appending to the snapshot leaves the original length unchanged.

</div>
