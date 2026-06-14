# DB-API 2.0: Connect, Execute, Fetch

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.1 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Open a SQLite connection (file and :memory:) and obtain a cursor
- Create a schema and insert/select rows with raw SQL
- Fetch results with fetchone/fetchall/fetchmany
- Understand the DB-API 2.0 shape shared by all Python databases

## Python features introduced
`sqlite3.connect`, `Connection / Cursor objects`, `cursor.execute`, `fetchone / fetchall / fetchmany`, `CREATE TABLE / INSERT / SELECT`, `connection close`, `in-memory ':memory:' db`, `DB-API 2.0 overview`

## MiniERP increment
Adds minierp/db/schema.py with the products and customers DDL and connect(layout) opening the SQLite database at layout.db_path; a create_schema(conn) call brings the real database into existence.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import sqlite3
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

- **Test focus:** Against a :memory: connection, create_schema builds the products table; an INSERT then SELECT round-trips a row; fetchone vs fetchall behave as expected.

</div>
