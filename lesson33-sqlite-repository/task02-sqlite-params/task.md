# Parametrized Queries & SQL Injection

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.2 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Always bind values with ? or named placeholders, never f-strings, to prevent injection
- Insert many rows efficiently with executemany
- Use named placeholders with dict parameters for readable INSERTs
- Recognize and reject the unsafe string-formatting pattern

## Python features introduced
`? placeholders (qmark)`, `named :name placeholders`, `executemany`, `passing tuples/dicts as params`, `why string formatting is unsafe`, `executescript`, `SQL injection demonstration`

## MiniERP increment
Adds parametrized insert_product(conn, product) and bulk_insert(conn, products) (executemany) to minierp.db, so seeding the catalog from a CSV import is safe and fast.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import sqlite3

def insert_product(conn, sku, name, price_cents, quantity) -> None:
    conn.execute(
        'INSERT INTO products (sku, name, price_cents, quantity) VALUES (?, ?, ?, ?)',
        (sku, name, price_cents, quantity),
    )

def bulk_insert(conn, rows) -> None:
    ...  # executemany

- **Test focus:** Parametrized insert stores values correctly; a malicious sku string like "x'); DROP TABLE products;--" is stored literally and the table survives; executemany inserts N rows in one call.

</div>
