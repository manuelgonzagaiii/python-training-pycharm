"""Restore & Backup Rotation

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import zipfile
from pathlib import Path

def list_backups(layout) -> list[Path]:
    return sorted(layout.backups_dir.glob('minierp-*.zip'),
                  key=lambda p: p.stat().st_mtime, reverse=True)

def prune_backups(layout, keep: int = 5) -> list[Path]:
    backups = list_backups(layout)
    for old in backups[keep:]:
        old.unlink()
    ...  # return removed

"""

# Your code here.
