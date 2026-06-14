# What is a module?

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 28.1 of 6  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain that a module is a singleton object produced by executing a .py file top to bottom exactly once
- Describe what 'import time' means and why top-level code runs on first import only
- Identify the module dunders __name__, __doc__, __file__ and what each holds
- Understand that importing the same module twice returns the cached object from sys.modules
- Know that CPython compiles modules to .pyc bytecode under __pycache__ and when that cache is reused

## Python features introduced
`module object`, `import statement`, `module namespace`, `__name__`, `__doc__`, `__file__`, `import-time execution`, `bytecode compilation`, `__pycache__`, `sys.modules cache`

## MiniERP increment
Frame the refactor: the whole MiniERP currently lives in one ever-growing module. This page names the file we will evolve — minierp.py — and explains that each import pulls in one cached module object. No code change yet; it sets up the mental model for the package split that follows.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A read-only concept page (task.py holds a short annotated demo: a module-level print, a function, then `print(__name__, __doc__, __file__)`), with prose explaining import-time execution, the sys.modules cache, and __pycache__/.pyc.
- **Test focus:** None (theory page; no automated checks).

</div>
