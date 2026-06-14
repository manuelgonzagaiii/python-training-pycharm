# A StorageLayout with pathlib

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 31.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build paths portably with the / operator instead of string concatenation
- Create the data/config/exports/backups tree idempotently with mkdir(parents=True, exist_ok=True)
- Decompose and recompose filenames using stem/suffix/with_suffix
- Resolve a root directory and derive child paths relative to it

## Python features introduced
`pathlib.Path`, `Path / operator`, `Path.home / Path.cwd`, `Path.mkdir(parents, exist_ok)`, `Path.exists / is_dir / is_file`, `Path.name / stem / suffix / parent / parts`, `Path.with_suffix / with_name`, `Path.resolve / expanduser`, `PurePath vs Path`, `Path.relative_to`

## MiniERP increment
Adds minierp/storage/layout.py with a StorageLayout dataclass that, given a root Path, exposes .data_dir, .config_dir, .exports_dir, .backups_dir, the db_path, and an ensure() method that creates the whole tree. All later tasks build on these paths.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass
from pathlib import Path

@dataclass(slots=True)
class StorageLayout:
    root: Path

    @property
    def data_dir(self) -> Path:
        ...  # root / 'data'

    @property
    def db_path(self) -> Path:
        ...  # data_dir / 'minierp.sqlite3'

    def ensure(self) -> 'StorageLayout':
        ...  # mkdir every dir, return self

- **Test focus:** Given a tmp_path root, ensure() creates data/config/exports/backups; db_path ends with minierp.sqlite3 and lives under data_dir; properties return Path objects composed with /.

</div>
