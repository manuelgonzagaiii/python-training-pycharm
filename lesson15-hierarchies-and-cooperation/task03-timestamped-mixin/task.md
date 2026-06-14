# Mixins & Multiple Inheritance

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 15.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a mixin (Timestamped) that participates in cooperative __init__ via super().__init__(**kwargs)
- Combine a mixin with a domain class through multiple inheritance
- Understand why every cooperative __init__ must call super() and forward **kwargs
- Order base classes correctly (mixin before/after the domain base)

## Python features introduced
`multiple inheritance`, `mixin classes`, `cooperative super() across a chain`, `**kwargs pass-through in __init__`, `datetime.datetime / UTC`, `class composition order`

## MiniERP increment
Adds an audit-friendly Timestamped mixin (created_at/updated_at) and an Identified mixin (uuid id). Entities like Customer and Invoice mix these in, giving every record creation/modification metadata for the future Audit log module.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from datetime import datetime, UTC
from uuid import uuid4


class Timestamped:
    def __init__(self, **kwargs) -> None:
        self.created_at = datetime.now(UTC)
        self.updated_at = self.created_at
        super().__init__(**kwargs)  # cooperative: pass the rest along

    def touch(self) -> None:
        self.updated_at = datetime.now(UTC)


class Identified:
    def __init__(self, **kwargs) -> None:
        self.id = str(uuid4())
        super().__init__(**kwargs)

- **Test focus:** A class mixing in Timestamped + Identified + a base initializes all attributes through one super() chain, touch() updates updated_at, id is unique per instance, kwargs reach the base.

</div>
