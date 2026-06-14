# Absolute vs relative imports

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use absolute imports between package modules and explain their stability
- Use single-dot and double-dot relative imports for intra-package references
- Explain why a relative import raises when a module is run as a top-level script and why `python -m` fixes it
- Choose the import style consistently across a package

## Python features introduced
`absolute import (import minierp.pricing)`, `relative import (from . import money)`, `from .pricing import net_price`, `parent-package relative import (from ..)`, `leading-dot semantics`, `why relative imports fail in scripts run directly`, `package execution with -m`

## MiniERP increment
Wire the package internals with relative imports: pricing.py does `from . import money` and catalog.py does `from .pricing import net_price`, replacing the old top-level imports. MiniERP's modules now reference each other as a cohesive package, ready to be installed and moved without breakage.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Sub-modules with TODO import lines; learner converts top-level imports to relative ones. A demo runnable via `python -m minierp` shows the package entry point.
- **Test focus:** Importing minierp and its sub-modules works via the package; pricing/catalog use intra-package references; functions still compute correctly after the rewrite.

</div>
