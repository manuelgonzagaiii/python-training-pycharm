# Intercepting Attribute Access

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use __getattr__ to provide dynamic/virtual attributes only when normal lookup fails
- Override __setattr__ to enforce a write policy (e.g. reject unknown fields) without recursing
- Customize __dir__ so tooling/REPL shows the virtual attributes; know the cost of __getattribute__

## Python features introduced
`__getattr__ (fallback for missing attrs)`, `__getattribute__ (intercepts ALL access)`, `__setattr__`, `__delattr__`, `__dir__`, `avoiding infinite recursion via super().__setattr__/object.__getattribute__`

## MiniERP increment
Adds a Record base (core/record.py) used by lightweight value objects: __getattr__ exposes extra/custom fields stored in a dict, __setattr__ enforces that known descriptor fields go through validation while custom keys land in the extras dict, and __dir__ advertises both — powering flexible Import/Export rows.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import Any

class Record:
    def __init__(self) -> None:
        object.__setattr__(self, "_extra", {})
    def __getattr__(self, name: str) -> Any:
        # called ONLY when normal lookup fails
        extra = object.__getattribute__(self, "_extra")
        # TODO: return extra[name] or raise AttributeError(name)
        ...
    def __setattr__(self, name: str, value: Any) -> None:
        # TODO: if name is a descriptor on type(self): super().__setattr__(...)
        #       else store in self._extra (avoid recursion!)
        ...
    def __dir__(self) -> list[str]:
        # TODO: return base dir + list(self._extra)
        ...
- **Test focus:** Known fields validate via descriptors; unknown fields go to extras and are retrievable; __getattr__ raises AttributeError for truly-missing names; __dir__ lists virtual fields; no infinite recursion on set/get.

</div>
