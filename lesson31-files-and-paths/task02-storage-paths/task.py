"""A StorageLayout with pathlib

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from dataclasses import dataclass
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

"""

# Your code here.
