# try / except / else / finally Control Flow

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Place recovery, success, and cleanup logic in the correct clause (except vs else vs finally)
- Order except clauses from most specific to most general so the right handler wins
- Use finally for guaranteed cleanup that runs on success, exception, and early return alike
- Avoid the bare-except anti-pattern and know when a bare raise re-raises the active exception

## Python features introduced
`try/except/else/finally`, `multiple except clauses ordered specific-to-general`, `except with tuple of types`, `exception aliasing (except E as e)`, `else clause semantics (runs only when no exception)`, `finally clause semantics (always runs, even on return/raise)`, `bare except pitfalls`, `re-raising with a bare raise`

## MiniERP increment
Adds a `safe_load_dataset(path)` helper to the import/export pathway that wraps file reading in try/except/else/finally: except maps OSError to a friendly message, else parses only on success, finally guarantees the file handle/resource is released and a load-attempt counter is updated. This hardens the existing data-loading entry point used by services.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from pathlib import Path

_load_attempts = 0

def safe_load_dataset(path: str | Path) -> list[str]:
    """Read lines from `path`. Return [] if the file is missing/unreadable.
    Always increment the module-level _load_attempts counter, on success OR failure.
    Parse (split into lines) ONLY when the read succeeded.
    """
    global _load_attempts
    # TODO: try -> read; except OSError -> return []; else -> split lines;
    #       finally -> bump _load_attempts
    raise NotImplementedError
- **Test focus:** Verify else runs only on success, finally always increments the counter (success, missing-file, and unreadable cases), and OSError is caught while unrelated errors propagate.

</div>
