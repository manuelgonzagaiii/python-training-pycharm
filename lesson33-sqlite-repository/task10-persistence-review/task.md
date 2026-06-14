# Persistence Layer: What You Built

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.10 of 13  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Recall when to reach for SQLite vs shelve vs pickle vs JSON vs struct
- Reaffirm security rules: parametrize SQL, never unpickle untrusted data
- Remember format gotchas: csv newline='', tomllib binary+read-only, JSON has no native datetime/Decimal
- Consolidate the repository pattern and the atomic-write/backup-rotation primitives

## Python features introduced
`pathlib vs os.path tradeoffs`, `DB-API 2.0 recall`, `parametrized queries vs string formatting`, `pickle security`, `tomllib read-only/binary`, `atomic write pattern`, `csv newline requirement`, `JSON type limits`

## MiniERP increment
No code change: a knowledge check that consolidates the persistence layer (StorageLayout, repositories, import/export, config, backups) before the course moves on to the next phase.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice review. No code to write.
# Sample question:
#   Which statement is TRUE?
#   a) f-string SQL is fine if you trust your data
#   b) tomllib can write TOML files
#   c) csv files should be opened with newline=''  <- correct
#   d) pickle is safe to load from any source

- **Test focus:** Multiple-choice answers verifying recall of: csv newline='', parametrized SQL over f-strings, pickle-untrusted-data danger, tomllib being read-only and binary, and choosing SQLite vs shelve appropriately.

</div>
