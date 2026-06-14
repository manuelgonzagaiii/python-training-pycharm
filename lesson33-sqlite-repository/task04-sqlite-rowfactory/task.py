"""row_factory & Mapping Rows to Objects

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import sqlite3
from minierp.domain import Product

def product_row_factory(cursor, row):
    cols = [c[0] for c in cursor.description]
    data = dict(zip(cols, row))
    return Product(**_adapt(data))

def rows_as_dicts(conn, sql, params=()):
    conn.row_factory = sqlite3.Row
    ...

"""

# Your code here.
