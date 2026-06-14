# The Customer Domain Class

> **Phase:** OOP Foundations  •  **Stage:** 13.6 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Independently assemble a complete domain class from the lesson's tools
- Apply validated properties, value equality/hashing, repr/str, and a factory together
- Identify a Customer by a stable id field for equality and hashing
- Reinforce the full object-design workflow on a new entity

## Python features introduced
`full class build`, `@property validation`, `__eq__/__hash__`, `__repr__/__str__`, `@classmethod factory`, `combining the phase's concepts`

## MiniERP increment
Build the Customer class (customer_id, name, email with validation) with from_dict factory, value equality/hashing on customer_id, and clean repr/str — replacing the customer dicts from earlier phases and completing the Customers module's core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Customer:
    def __init__(self, customer_id: int, name: str, email: str) -> None:
        ...  # validated email property

    @property
    def email(self) -> str: ...
    @email.setter
    def email(self, value: str) -> None: ...  # require '@'

    @classmethod
    def from_dict(cls, data: dict) -> "Customer": ...

    def __eq__(self, other: object) -> bool: ...   # by customer_id
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
- **Test focus:** Assert construction and from_dict produce equivalent customers; assert invalid email (no '@') raises; assert equality/hash key on customer_id only; assert repr is eval-able-style and str is friendly.

</div>
