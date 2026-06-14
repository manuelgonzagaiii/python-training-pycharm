# The Descriptor Protocol

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.1 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement a reusable Field descriptor with __get__/__set__/__set_name__
- Use __set_name__ to learn the attribute name and pick a private storage slot
- Distinguish data descriptors (define __set__/__delete__) from non-data ones and know they win over instance __dict__

## Python features introduced
`__get__(self, obj, objtype)`, `__set__(self, obj, value)`, `__set_name__(self, owner, name)`, `data vs non-data descriptors`, `storing per-instance state under a private key`, `descriptor lives on the class, data lives on the instance`

## MiniERP increment
Introduces core/fields.py with a base Field descriptor that backs domain attributes with validated storage, replacing ad-hoc __init__ checks in Product/Customer with declarative class-level fields.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import Any

class Field:
    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.slot = f"_{name}"
    def __get__(self, obj: Any, objtype: type | None = None) -> Any:
        if obj is None:
            return self
        # TODO: return getattr(obj, self.slot)
        ...
    def __set__(self, obj: Any, value: Any) -> None:
        # TODO: setattr(obj, self.slot, self.validate(value))
        ...
    def validate(self, value: Any) -> Any:
        return value
- **Test focus:** Reading/writing the attribute round-trips through the private slot; __set_name__ captures the right name; accessing the descriptor on the class (obj is None) returns the descriptor itself.

</div>
