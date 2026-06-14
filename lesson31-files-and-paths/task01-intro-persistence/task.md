# Why Persistence? From RAM to Disk

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that everything built so far is lost when the process exits
- Distinguish bytes on disk from in-memory objects (serialization vs deserialization)
- Preview the phase roadmap: paths -> files -> CSV/JSON -> config -> pickle/struct -> compression -> SQLite repository
- Learn the data-directory convention (data/, config/, exports/, backups/) MiniERP will adopt

## Python features introduced
`filesystem concepts`, `text vs binary streams`, `encodings overview (UTF-8)`, `the storage problem`, `repository pattern preview`

## MiniERP increment
Introduces the storage architecture decision: MiniERP will gain a minierp/storage package and a data/ tree. No code change yet; sets the contract every later task fills in.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Concept page only. Read the description.
# MiniERP's storage tree:
#   data/        SQLite db + snapshots
#   config/      app.toml, logging.ini
#   exports/     csv/json dumps
#   backups/     compressed archives

- **Test focus:** No checks (theory page).

</div>
