# shelve: A Persistent Dict

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 32.7 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use shelve as a persistent key-value store backed by pickle
- Understand the writeback caching trap with mutable values
- Manage a shelf with a context manager so it syncs and closes
- Know shelve's limits (str keys, single-process) versus moving to SQLite

## Python features introduced
`shelve.open`, `shelf as dict-like store`, `writeback= behavior`, `key constraints (str keys)`, `shelf.sync / close`, `context-managed shelf`, `pickle-backed values`, `when shelve vs sqlite`

## MiniERP increment
Adds minierp/io/kv.py: a SettingsCache using shelve to persist small per-user UI preferences (last export path, page size) across CLI/GUI sessions - a lightweight store distinct from the main repository.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import shelve
from pathlib import Path

def put(db_path: Path, key: str, value) -> None:
    with shelve.open(str(db_path)) as sh:
        sh[key] = value

def get(db_path: Path, key: str, default=None):
    with shelve.open(str(db_path)) as sh:
        return sh.get(key, default)

- **Test focus:** Values persist across separate shelve.open calls; get returns default for missing keys; a mutable value updated without writeback demonstrates the caching gotcha in a controlled assertion.

</div>
