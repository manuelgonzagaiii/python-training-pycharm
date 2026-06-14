# Backups: zipfile & tarfile Archives

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.8 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Bundle the database and exports into a single .zip with compression
- Create a gzip-compressed .tar.gz archive with tarfile
- List and extract archive members safely
- Name backups with a UTC timestamp for ordering

## Python features introduced
`zipfile.ZipFile`, `ZIP_DEFLATED`, `zip writestr / write / namelist / extractall`, `tarfile.open modes (w:gz)`, `tarfile add / extractall`, `archive members`, `datetime-stamped filenames`, `shutil.make_archive`

## MiniERP increment
Delivers minierp/backup/archive.py: make_backup(layout) producing backups/minierp-YYYYMMDD-HHMMSS.zip (db + exports + config) and a tar.gz variant - the backup half of the persistence milestone.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import zipfile
from datetime import datetime, timezone
from pathlib import Path

def make_zip_backup(layout) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    target = layout.backups_dir / f'minierp-{stamp}.zip'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(layout.db_path, arcname=layout.db_path.name)
        ...  # add exports
    return target

- **Test focus:** make_zip_backup creates an archive whose namelist includes the db and exports; extractall into a tmp dir reproduces the files byte-for-byte; a tarfile w:gz variant round-trips; the filename carries a parseable timestamp.

</div>
