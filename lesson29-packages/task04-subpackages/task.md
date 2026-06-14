# Sub-packages and nested layout

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Organize a package into sub-packages (e.g. minierp.domain) each with its own __init__.py
- Import across nested levels with dotted names and relative imports
- Aggregate a sub-package's public names in its __init__.py
- Keep a clean layered layout as the codebase grows

## Python features introduced
`nested package directories`, `sub-package __init__.py`, `deep dotted names (minierp.domain.catalog)`, `import minierp.domain.catalog as ...`, `package reorganization`, `__init__ aggregation across sub-packages`

## MiniERP increment
Introduce a domain sub-package: move catalog/pricing/money under minierp/domain/ (minierp/domain/__init__.py aggregating them), leaving room for minierp.interfaces and minierp.services in later phases. The top-level minierp/__init__.py keeps re-exporting the same flat public API so callers are unaffected.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Restructured tree with minierp/domain/; learner fills the domain/__init__.py aggregation and updates relative imports one level deeper.
- **Test focus:** Assert minierp.domain.catalog imports; the flat public API on minierp is unchanged (back-compat); deep dotted imports resolve.

</div>
