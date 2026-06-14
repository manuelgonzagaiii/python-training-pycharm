"""The Repository Pattern: ProductRepository

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import sqlite3
from typing import Protocol
from minierp.domain import Product

class ProductRepo(Protocol):
    def add(self, p: Product) -> None: ...
    def get(self, sku: str) -> Product | None: ...
    def list(self, limit: int = 50, offset: int = 0) -> list[Product]: ...

class SqliteProductRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.row_factory = ...
    # implement add/get/list/update/delete

"""

# Your code here.
