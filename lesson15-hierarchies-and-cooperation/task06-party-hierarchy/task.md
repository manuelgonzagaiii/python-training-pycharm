# Party Hierarchy: Customer & Supplier

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 15.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a second hierarchy (Party -> Customer, Supplier) reusing Timestamped/Identified mixins
- Compose value objects (Address) into entities
- Provide cooperative __repr__ that shows the id from a mixin
- Keep the base Party agnostic while subclasses add credit limit / lead time

## Python features introduced
`inheritance + mixins together`, `super() with keyword forwarding`, `overriding __str__/__repr__ cooperatively`, `abstract base placeholder method`, `encapsulating Address value object`

## MiniERP increment
Adds party.py: Party base plus Customer (credit_limit: Money, addresses) and Supplier (lead_time_days). Customers feed the Sales/Invoicing module; Suppliers feed inventory replenishment. Both are timestamped, identified entities.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from address import Address
from money import Money
from mixins import Timestamped, Identified


class Party(Timestamped, Identified):
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        super().__init__(**kwargs)


class Customer(Party):
    def __init__(self, name: str, credit_limit: Money, **kwargs) -> None:
        # TODO: store credit_limit, call super().__init__, manage addresses
        ...

- **Test focus:** Customer/Supplier inherit id and timestamps via the mixin chain, credit_limit/lead_time stored, addresses managed correctly, __repr__ includes id, isinstance(customer, Party) holds.

</div>
