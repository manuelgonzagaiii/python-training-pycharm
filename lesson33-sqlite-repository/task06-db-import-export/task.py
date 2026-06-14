"""Wiring Import/Export to the Database

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: def import_products(repo, conn, rows) -> int:
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

"""

# Your code here.
