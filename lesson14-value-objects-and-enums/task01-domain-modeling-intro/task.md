# Why a Domain Model? Entities vs Value Objects

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.1 of 8  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish an entity (has identity, e.g. a Customer) from a value object (defined by its data, e.g. Money)
- Understand why value objects should be immutable and hashable
- See the road map of the domain layer that all four MiniERP interfaces will share
- Recall the difference between == (equality) and is (identity) and how __eq__/__hash__ relate

## Python features introduced
`class vs instance`, `identity vs equality`, `mutability vs immutability`, `__eq__ / __hash__ overview`, `id()`, `is vs ==`

## MiniERP increment
Establishes the design vocabulary and a diagram of the target domain model (Product hierarchy, Party hierarchy, Money/SKU/Address value objects, status enums, repositories) that the rest of the phase implements. No code change required; sets direction for the evolving codebase.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** """Read-only concept page. No code to write.

MiniERP domain layer overview:
  Entities (have identity):     Product, Customer, Invoice, Payment
  Value objects (no identity):  Money, SKU, Address, Quantity
  Enums (closed sets):          OrderStatus, PaymentMethod, Permission

You will build these over this phase. They become the shared core
for the CLI, Web, Desktop (tkinter) and Text (curses) interfaces.
"""

- **Test focus:** No checking (theory page). Reading only.

</div>
