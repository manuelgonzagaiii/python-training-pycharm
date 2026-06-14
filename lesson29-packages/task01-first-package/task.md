# From modules to a package

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.1 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create a package by placing modules in a directory with an __init__.py
- Explain how a package's __init__.py runs when the package is first imported
- Reference sub-modules with dotted names (minierp.catalog)
- Understand __path__ and how it differs from a plain module's __file__

## Python features introduced
`package directory`, `__init__.py`, `package vs module`, `sub-modules`, `dotted module names`, `package __name__ / __path__`, `regular package semantics`

## MiniERP increment
Create the `minierp/` package and move the existing modules into it: minierp/__init__.py, minierp/catalog.py, minierp/pricing.py, minierp/money.py. This is the structural milestone of the phase — MiniERP is now a package you `import minierp` rather than a single file.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Pre-made minierp/ folder; learner places catalog/pricing/money inside and writes minierp/__init__.py setting __version__ and importing the sub-modules so `import minierp` works.
- **Test focus:** Assert `import minierp` succeeds, minierp.catalog and minierp.pricing are importable sub-modules, and minierp.__version__ is a string.

</div>
