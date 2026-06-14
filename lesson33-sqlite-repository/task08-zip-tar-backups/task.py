"""Backups: zipfile & tarfile Archives

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import zipfile
from datetime import datetime, timezone
from pathlib import Path

def make_zip_backup(layout) -> Path:
    stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
    target = layout.backups_dir / f'minierp-{stamp}.zip'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(layout.db_path, arcname=layout.db_path.name)
        ...  # add exports
    return target

"""

# Your code here.
