# Namespace packages for plugins

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain how a namespace package (no __init__.py) lets multiple directories contribute to one import name
- Contrast regular packages with namespace packages and know when each is appropriate
- Discover modules under a namespace with pkgutil.iter_modules
- Reason about __path__ spanning multiple locations

## Python features introduced
`PEP 420 namespace packages`, `package with NO __init__.py`, `splitting one logical package across directories`, `__path__ on namespace packages`, `implicit namespace discovery`, `pkgutil iteration`

## MiniERP increment
Add a `minierp.plugins` namespace package (no __init__.py) and a tiny report plugin module inside it, plus a loader that uses pkgutil.iter_modules to discover plugins by name. This gives MiniERP an extension point reporting/export modules will populate in later phases.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/plugins/ as a namespace package with one demo plugin; learner writes discover_plugins() using pkgutil.iter_modules over the namespace's __path__.
- **Test focus:** discover_plugins() finds the demo plugin by name; importing a plugin module works; the namespace has no __init__.py yet still resolves.

</div>
