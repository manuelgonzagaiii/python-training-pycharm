# The Exception Hierarchy, Top to Bottom

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.1 of 8  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that every exception derives from BaseException and why ordinary code should subclass Exception, not BaseException
- Read the standard exception tree and place built-ins (ValueError, KeyError, LookupError, OSError, RuntimeError) within it
- Explain why KeyboardInterrupt/SystemExit/GeneratorExit sit beside Exception and must not be swallowed by a bare except
- Recognize that an exception instance carries .args and can carry a traceback, and how its str/repr differ

## Python features introduced
`BaseException`, `Exception`, `BaseExceptionGroup`, `KeyboardInterrupt`, `SystemExit`, `GeneratorExit`, `built-in exception classes (ValueError, KeyError, LookupError, TypeError, RuntimeError, OSError)`, `exception MRO / inheritance`, `args attribute`, `with_traceback()`, `__str__ vs repr of exceptions`

## MiniERP increment
No code change yet: this page surveys the failure modes the existing MiniERP services already raise implicitly (KeyError on missing product id, ValueError on bad quantity, OSError on file import) and frames the goal of the lesson — replacing those scattered built-ins with one deliberate ERPError taxonomy.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory page only — no code to edit.
# The task description renders the full BaseException -> Exception tree
# and annotates which built-ins MiniERP currently leaks from its services.
- **Test focus:** None (theory task: no automated checking).

</div>
