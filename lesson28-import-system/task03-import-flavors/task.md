# import, from-import, and as

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 28.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Choose between `import x`, `from x import y`, and aliasing with `as`
- Explain how each form binds names into the importing namespace
- Understand why `from x import *` is discouraged and how __all__ would control it
- Read tracebacks that reference qualified vs unqualified names

## Python features introduced
`import module`, `from module import name`, `from module import name as alias`, `import module as alias`, `qualified vs unqualified names`, `binding names into the local namespace`, `from module import *`, `__all__ teaser`

## MiniERP increment
Split a tiny helper out: add a money.py module with a format_money(cents) -> str helper, then import it into minierp.py three ways across the demo (plain import, from-import, aliased) so the banner/report code can format currency. This is the first multi-module step toward the package.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** money.py with format_money(cents); minierp.py imports it. Learner writes format_money and uses each import flavor where indicated.
- **Test focus:** Assert format_money(123456) == '$1,234.56'; verify minierp can call it via the chosen import; check both modules import cleanly.

</div>
