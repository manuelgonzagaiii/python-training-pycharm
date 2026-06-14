# Recursion and the Recursion Limit

> **Phase:** Control Flow & Functions  •  **Stage:** 10.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a recursive function with a correct base case
- Reason about stack depth and the interpreter recursion limit
- Decide when recursion is clearer than a loop and when it risks RecursionError

## Python features introduced
`recursion (function calling itself)`, `base case and recursive case design`, `call stack reasoning`, `sys.getrecursionlimit / setrecursionlimit`, `RecursionError`, `recursion vs iteration tradeoffs`

## MiniERP increment
Add expand_bundle(catalog, sku, qty) to rules.py that recursively explodes a product bundle (a product whose components are themselves products, possibly bundles) into flat (sku, qty) leaf lines, with cycle/depth protection referencing sys.getrecursionlimit — the final pricing primitive enabling MiniERP to price composite kit products.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import sys


def expand_bundle(catalog: list[dict], sku: str, qty: int = 1, _depth: int = 0) -> list[tuple[str, int]]:
    """Recursively flatten a bundle into leaf (sku, qty) lines.
    Base case: a non-bundle product. Guard against runaway depth."""
    if _depth > 50:
        raise RecursionError("bundle nesting too deep")
    ...
- **Test focus:** Flat product returns one line; one- and multi-level bundles flatten with multiplied quantities; over-deep/cyclic nesting raises RecursionError via the depth guard.

</div>
