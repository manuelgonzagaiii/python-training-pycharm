# The Repository Pattern: ProductRepository

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.5 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Encapsulate all SQL behind a ProductRepository so the rest of MiniERP is database-agnostic
- Implement add/get/list/update/delete with parametrized queries and the row_factory
- Define a Repository Protocol so an in-memory and a SQLite implementation are interchangeable
- Support pagination with ORDER BY / LIMIT / OFFSET

## Python features introduced
`repository class encapsulating SQL`, `CRUD methods (add/get/list/update/delete)`, `parametrized queries inside methods`, `context-managed connection lifecycle`, `Protocol/ABC for repository interface`, `separation of domain vs persistence`, `ORDER BY / LIMIT pagination`

## MiniERP increment
Delivers minierp/db/repository.py: ProductRepository (and a parallel CustomerRepository) implementing a Repository Protocol; the existing service layer is rewired to depend on the repository, so MiniERP's catalog now lives in SQLite end-to-end.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import sqlite3
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

- **Test focus:** add then get returns an equal Product; list paginates with limit/offset and ORDER BY; update mutates and delete removes; get on a missing sku returns None; the repo satisfies the Protocol.

</div>
