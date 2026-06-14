# PEP 448: spread/unpacking in calls and literals

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.7 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Spread iterables into list/tuple/set literals and dicts into one another
- Pass a sequence as positional args with * and a dict as keyword args with **
- Merge several catalogs/configs in a single expression
- Forward arbitrary args through a wrapper function

## Python features introduced
`* unpacking in calls`, `** unpacking in calls`, `PEP 448 generalized unpacking`, `merge literals {**a, **b}`, `[*a, *b] and (*a, *b)`, `{*a, *b} set merge`, `*args/**kwargs forwarding`, `combine multiple iterables in one literal`

## MiniERP increment
Adds merge_catalogs(*catalogs) (one [*c1, *c2, ...] expression) and build_product(**fields) that constructs a ProductRecord via ** unpacking from an import dict — the glue the Import/Export phase will lean on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def merge_catalogs(*catalogs: list[ProductRecord]) -> list[ProductRecord]:
    """Concatenate any number of catalogs using a single starred-spread literal."""
    ...

def build_product(**fields) -> ProductRecord:
    """Build a ProductRecord from keyword fields using ** unpacking."""
    ...
- **Test focus:** merge_catalogs flattens all inputs in order and works with zero/one/many catalogs; build_product constructs the correct record from a fields dict passed via **.

</div>
