# sys.path, sys.modules, and the module cache

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 28.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Describe how the interpreter searches sys.path to locate a module
- Prove that two imports of the same module return the identical cached object via sys.modules and id()
- Use importlib.reload to force re-execution and observe when state resets
- Understand that import side effects happen exactly once per process

## Python features introduced
`sys.path`, `sys.modules`, `module caching / singletons`, `importlib.reload`, `id() to prove identity`, `module attribute access`, `first-import side effects`

## MiniERP increment
Add a load counter to minierp: a module-level _LOADS list (or counter) bumped at import time, plus a module_info() function returning the module's __name__, __file__, and whether it is already cached in sys.modules. This instrumentation makes the caching behavior visible and feeds the later 'package diagnostics' command.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp.py gains module_info() reporting __name__/__file__ and `'minierp' in sys.modules`; a tiny demo imports twice and compares id(). Learner implements module_info().
- **Test focus:** Assert importing minierp twice yields the same object (id equal); module_info() reports the correct __name__ and that the module is present in sys.modules.

</div>
