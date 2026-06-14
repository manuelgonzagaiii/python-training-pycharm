# Peering into the interpreter with sys

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.1 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Measure an object's in-memory size with getsizeof and reason about overhead
- Intern frequently-repeated keys (SKUs, status codes) to save memory and speed equality
- Adjust and restore the recursion limit safely for deep report aggregation
- Read sys.flags to detect optimized/debug interpreter modes

## Python features introduced
`sys.getsizeof`, `sys.intern`, `sys.setrecursionlimit / getrecursionlimit`, `sys.flags`, `sys.getrecursionlimit guardrails`, `sys.maxsize / sys.implementation (note)`, `string interning effects on identity`

## MiniERP increment
Adds erp/diagnostics.py: a `sys-report` admin command reporting record memory footprints (getsizeof), and the inventory layer interns SKU/status strings via sys.intern so the millions of repeated codes share storage and compare by identity.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import sys


def intern_codes(codes: list[str]) -> list[str]:
    """Return the codes interned via sys.intern (so equal codes share identity)."""
    raise NotImplementedError


def deep_footprint(obj, seen: set[int] | None = None) -> int:
    """Recursive getsizeof over dict/list/tuple containers; avoid double counting via id()."""
    raise NotImplementedError


def with_recursion_limit(limit: int):
    """Context manager that sets sys.setrecursionlimit and restores it."""
    raise NotImplementedError

- **Test focus:** Tests intern_codes returns identity-equal strings for equal inputs (a is b); tests deep_footprint sums container sizes without double-counting shared objects; tests with_recursion_limit changes then restores the limit even on exception.

</div>
