"""DB-API 2.0: Connect, Execute, Fetch

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import sqlite3
from pathlib import Path

SCHEMA = '''
CREATE TABLE IF NOT EXISTS products (
  sku TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  price_cents INTEGER NOT NULL,
  quantity INTEGER NOT NULL DEFAULT 0
);
'''

def connect(db_path: Path) -> sqlite3.Connection:
    return sqlite3.connect(db_path)

def create_schema(conn) -> None:
    conn.executescript(SCHEMA)

"""

# Your code here.
