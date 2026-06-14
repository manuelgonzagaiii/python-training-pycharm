# row_factory & Mapping Rows to Objects

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.4 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Access columns by name using sqlite3.Row instead of fragile positional indexing
- Write a custom row_factory that returns domain objects directly
- Read column metadata from cursor.description
- Understand type detection/converters for adapting custom types

## Python features introduced
`conn.row_factory`, `sqlite3.Row`, `indexing rows by name and position`, `custom row_factory function`, `cursor.description`, `mapping rows to dataclasses`, `register_converter / detect_types overview`

## MiniERP increment
Adds a product_row_factory to minierp.db that maps each SELECT row straight into a Product dataclass, so queries return domain objects and the service layer never touches tuples.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import sqlite3
from minierp.domain import Product

def product_row_factory(cursor, row):
    cols = [c[0] for c in cursor.description]
    data = dict(zip(cols, row))
    return Product(**_adapt(data))

def rows_as_dicts(conn, sql, params=()):
    conn.row_factory = sqlite3.Row
    ...

- **Test focus:** sqlite3.Row lets you read a column by name and index; the custom factory returns Product instances from a SELECT; cursor.description exposes column names.

</div>
