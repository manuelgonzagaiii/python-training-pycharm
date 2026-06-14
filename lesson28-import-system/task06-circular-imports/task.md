# Avoiding circular imports

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 28.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Recognize the symptom of a circular import (ImportError / AttributeError on a partially initialized module)
- Explain why `from a import x` is more fragile than `import a` during cycles
- Break a cycle by moving an import inside a function or restructuring dependencies
- Reason about the order in which module-level code executes during a cycle

## Python features introduced
`circular import detection`, `partially-initialized module`, `ImportError on circular from-import`, `deferred / function-local import`, `import ordering`, `module-level vs in-function imports`

## MiniERP increment
Introduce two collaborating modules — catalog.py (products) and pricing.py (price/discount math) — that initially reference each other and deadlock. Fix the cycle by switching one side to a deferred function-local import, leaving MiniERP with a clean, importable catalog/pricing pair the package will absorb.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** catalog.py and pricing.py with a deliberate cycle; learner removes the cycle (e.g. function-local import in pricing) so both import cleanly. Helpers: catalog.list_skus(), pricing.net_price(sku).
- **Test focus:** Importing catalog and pricing raises no ImportError; pricing.net_price applies the discount correctly; assert no module-level cross-import deadlock remains.

</div>
