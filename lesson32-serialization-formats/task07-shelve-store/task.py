"""shelve: A Persistent Dict

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import shelve
from pathlib import Path

def put(db_path: Path, key: str, value) -> None:
    with shelve.open(str(db_path)) as sh:
        sh[key] = value

def get(db_path: Path, key: str, default=None):
    with shelve.open(str(db_path)) as sh:
        return sh.get(key, default)

"""

# Your code here.
