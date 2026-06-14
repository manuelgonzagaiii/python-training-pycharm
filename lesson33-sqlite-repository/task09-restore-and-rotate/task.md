# Restore & Backup Rotation

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.9 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Restore a database by extracting an archive into a temp dir then atomically replacing the live db
- Verify archive integrity before restoring (testzip)
- List backups sorted newest-first via glob + mtime
- Implement a retention policy that deletes all but the N most recent backups

## Python features introduced
`extractall to a temp dir`, `shutil.copy2 / os.replace restore`, `sorting backups by mtime/name`, `glob for backups/*.zip`, `retention policy (keep N newest)`, `pathlib unlink`, `zipfile testzip integrity check`

## MiniERP increment
Completes the backup subsystem: minierp.backup.restore_backup(layout, archive) and prune_backups(layout, keep=5), so MiniERP can recover from a backup and bound disk usage - the persistence milestone is fully delivered.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import zipfile
from pathlib import Path

def list_backups(layout) -> list[Path]:
    return sorted(layout.backups_dir.glob('minierp-*.zip'),
                  key=lambda p: p.stat().st_mtime, reverse=True)

def prune_backups(layout, keep: int = 5) -> list[Path]:
    backups = list_backups(layout)
    for old in backups[keep:]:
        old.unlink()
    ...  # return removed

- **Test focus:** list_backups returns newest-first; prune_backups(keep=N) deletes exactly the oldest beyond N and returns them; restore extracts to temp and os.replaces the live db; a corrupted zip is caught by testzip before any restore happens.

</div>
