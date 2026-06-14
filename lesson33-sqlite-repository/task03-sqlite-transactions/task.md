# Transactions: commit, rollback & atomicity

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.3 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Group multiple statements into an atomic transaction and commit them together
- Roll back automatically on error using the connection as a context manager
- Understand isolation_level / autocommit and when changes become durable
- Handle IntegrityError from constraint violations

## Python features introduced
`conn.commit / conn.rollback`, `connection as context manager (auto-commit/rollback)`, `isolation_level`, `autocommit (3.12+)`, `BEGIN/COMMIT semantics`, `exception-driven rollback`, `savepoints overview`, `IntegrityError`

## MiniERP increment
Adds minierp.db.transaction context handling so a multi-step operation (e.g. record a sale: decrement stock + insert sale row) either fully commits or fully rolls back, guaranteeing the ledger never desyncs from inventory.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import sqlite3

def transfer_stock(conn, src_sku, dst_sku, qty) -> None:
    with conn:  # commits on success, rolls back on exception
        conn.execute('UPDATE products SET quantity = quantity - ? WHERE sku=?', (qty, src_sku))
        conn.execute('UPDATE products SET quantity = quantity + ? WHERE sku=?', (qty, dst_sku))

- **Test focus:** A successful with-block commits both updates; raising inside the block rolls back so neither update persists; a UNIQUE/PRIMARY KEY violation raises IntegrityError and leaves the table unchanged.

</div>
