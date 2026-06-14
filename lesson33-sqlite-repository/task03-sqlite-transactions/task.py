"""Transactions: commit, rollback & atomicity

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import sqlite3

def transfer_stock(conn, src_sku, dst_sku, qty) -> None:
    with conn:  # commits on success, rolls back on exception
        conn.execute('UPDATE products SET quantity = quantity - ? WHERE sku=?', (qty, src_sku))
        conn.execute('UPDATE products SET quantity = quantity + ? WHERE sku=?', (qty, dst_sku))

"""

# Your code here.
