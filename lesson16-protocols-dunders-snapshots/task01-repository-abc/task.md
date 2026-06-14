# Abstract Repository with abc.ABC

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.1 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define an abstract base class with abc.ABC and @abstractmethod
- Understand that instantiating a class with unimplemented abstractmethods raises TypeError
- Provide a concrete in-memory subclass implementing the full contract
- Combine @property with @abstractmethod

## Python features introduced
`abc.ABC`, `@abc.abstractmethod`, `abstractmethod prevents instantiation`, `concrete subclass must implement all abstracts`, `@property + @abstractmethod`, `TypeError on instantiating abstract class`

## MiniERP increment
Adds repository.py with an abstract Repository[T] contract (add/get/list/remove) and a concrete InMemoryRepository used to store Products, Customers, Invoices. This is the persistence seam the future SQLite/Web layers will swap behind.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from abc import ABC, abstractmethod


class Repository[T](ABC):
    @abstractmethod
    def add(self, key: str, item: T) -> None: ...

    @abstractmethod
    def get(self, key: str) -> T: ...

    @abstractmethod
    def list(self) -> list[T]: ...


class InMemoryRepository[T](Repository[T]):
    # TODO: implement all abstract methods over a dict
    ...

- **Test focus:** Instantiating Repository directly raises TypeError, InMemoryRepository implements every abstractmethod, add/get/list/remove behave correctly, missing key raises KeyError.

</div>
