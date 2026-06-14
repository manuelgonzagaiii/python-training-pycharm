# Bytecode and __pycache__

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 28.5 of 6  •  **Type:** `output`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain that CPython compiles each module to versioned .pyc bytecode cached under __pycache__
- Read the __cached__ dunder to find a module's compiled file
- Understand when the .pyc is regenerated (source mtime/hash) and when it is reused
- Know that bytecode is an implementation detail, not a distribution format

## Python features introduced
`__pycache__ directory`, `.pyc files`, `compile()`, `compileall module`, `py_compile`, `__cached__`, `source vs bytecode`, `PYTHONDONTWRITEBYTECODE awareness`

## MiniERP increment
Add a diagnostics() routine to minierp that prints, for the current module, its source path (__file__) and compiled path (__cached__), then prints the Python implementation and version — the seed of MiniERP's future `system info` admin command.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** task.py imports minierp and prints diagnostics(): the module's __file__, __cached__, sys.version_info, and platform.python_implementation(). Learner assembles the print lines to match expected output shape.
- **Test focus:** Output task: stdout shows the labelled diagnostic lines (paths normalized/asserted by suffix so the comparison is stable across machines).

</div>
