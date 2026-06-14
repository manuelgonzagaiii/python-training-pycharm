# Wiring Import/Export to the Database

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.6 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Import a CSV/JSON file into the database inside one transaction using the repository
- Export the database to CSV/JSON by streaming SELECT rows into a writer
- Use INSERT ... ON CONFLICT DO UPDATE (upsert) for idempotent imports
- Stream large result sets with a generator instead of fetchall

## Python features introduced
`combining csv/json modules with sqlite3`, `bulk load via executemany`, `SELECT -> writer streaming`, `transaction around an import`, `upsert (INSERT ... ON CONFLICT)`, `generator-based row streaming`, `memory-efficient export`

## MiniERP increment
Connects lesson 2's csv_io/json_io to the repository: import_csv(layout, path) loads exports into SQLite (upsert) and export_json(layout, path) streams the database back out - closing the loop on CSV/JSON import-export from real persistent storage.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def import_products(repo, conn, rows) -> int:
    with conn:  # one transaction
        for r in rows:
            conn.execute(
                'INSERT INTO products (sku,name,price_cents,quantity) VALUES (?,?,?,?) '
                'ON CONFLICT(sku) DO UPDATE SET name=excluded.name, '
                'price_cents=excluded.price_cents, quantity=excluded.quantity',
                r,
            )
    ...  # return count

def stream_products(conn):
    for row in conn.execute('SELECT * FROM products ORDER BY sku'):
        yield row

- **Test focus:** Importing the same CSV twice upserts (no duplicate rows, second values win); export streams all rows via a generator; the whole import is atomic (failure midway rolls back).

</div>
