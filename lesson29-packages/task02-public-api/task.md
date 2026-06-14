# Curating the public API with __all__

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define __all__ to declare a package's intentional public surface
- Re-export selected sub-module names from __init__.py for a flat, convenient API
- Distinguish public names from _private helpers by convention
- Control what `from minierp import *` exposes

## Python features introduced
`__all__`, `re-exporting names in __init__.py`, `public vs private (_underscore) names`, `from minierp import X`, `from minierp import *`, `package-level namespace design`

## MiniERP increment
Curate minierp's public API: __init__.py re-exports the key callables (banner, format_money, net_price, list_skus) and declares __all__, so callers write `from minierp import format_money` instead of reaching into sub-modules. Establishes the stable import surface every later phase depends on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/__init__.py with imports + a partial __all__ list; learner completes __all__ and the re-export lines. Private helpers prefixed with _ stay out of __all__.
- **Test focus:** Assert each name in __all__ is importable from minierp; `from minierp import *` exposes exactly the public names and not the _private ones.

</div>
