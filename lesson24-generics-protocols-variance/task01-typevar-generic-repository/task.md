# TypeVar & a Generic Repository[T]

> **Phase:** Modern Type System  •  **Stage:** 24.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Declare a TypeVar and parameterize a class with Generic[T] (classic form)
- Write the same class with PEP 695 'class Repository[T]:' inline syntax and see they are equivalent
- Make methods (add, get, all) carry the element type T so a Repository[Product] yields Product
- Understand that one generic implementation removes the need for per-entity repository classes

## Python features introduced
`TypeVar`, `typing.Generic`, `Generic[T] base class`, `PEP 695 class Repo[T] syntax`, `generic methods`, `type parameter scoping`

## MiniERP increment
Introduces the cornerstone of the data layer: a single Repository[T] (in-memory dict-backed) that the Products, Customers, Sales and Payments modules all instantiate as Repository[Product], Repository[Customer], etc. Replaces ad-hoc per-entity stores from the OOP phase with one typed container.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # PEP 695 inline form (target 3.14):
class Repository[T]:
    def __init__(self) -> None:
        self._items: dict[str, T] = {}
    def add(self, key: str, item: T) -> None:
        ...  # TODO
    def get(self, key: str) -> T | None:
        ...  # TODO
    def all(self) -> list[T]:
        ...  # TODO

# Classic equivalent (also accepted by checkers):
# from typing import Generic, TypeVar
# T = TypeVar('T'); class Repository(Generic[T]): ...
- **Test focus:** Tests build Repository[Product] and Repository[Customer], add/get/all round-trip; a static-flavored check (and reveal-style assertion via get_type_hints on the methods) confirms T is threaded through get's return type.

</div>
