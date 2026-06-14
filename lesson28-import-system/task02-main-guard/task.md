# The __main__ guard and module identity

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 28.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish a module run directly (__name__ == '__main__') from one that is imported (__name__ == the module name)
- Use the if __name__ == '__main__' guard to keep a runnable entry point that does not fire on import
- Expose reusable functions and constants at module scope without side effects at import time

## Python features introduced
`__name__ == '__main__'`, `module-as-script vs module-as-import`, `if __name__ guard`, `module-level constants`, `module docstring`, `def at module scope`

## MiniERP increment
Seed the framework codebase: create minierp.py exposing APP_NAME and VERSION constants plus a banner() function that returns the app title string, and add a `if __name__ == '__main__':` block that prints the banner. This is the single growing module the whole phase refactors; the guard ensures importing it stays side-effect free.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp.py with APP_NAME/VERSION constants, a banner() returning a formatted title, and a __main__ guard printing it. Learner fills in banner() and the guard.
- **Test focus:** Import minierp without triggering output; assert banner() returns the expected string and that importing the module does not print (capture stdout).

</div>
