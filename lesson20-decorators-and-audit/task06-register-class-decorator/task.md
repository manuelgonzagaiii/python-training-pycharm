# Class Decorators: @register_service

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a decorator that receives a class and registers it in a module-level dict keyed by a name attribute
- Attach a derived attribute (e.g. a slug) onto the class without subclassing
- Understand that class decorators run once at class-definition time

## Python features introduced
`class decorators (callable taking and returning a class)`, `mutating/annotating a class object`, `adding methods/attributes to a class at decoration time`, `returning the same vs a replacement class`, `difference between decorating a class and a function`

## MiniERP increment
Introduces a first, decorator-based service registry: @register_service('products') tags each ERP service class so a dispatcher can look services up by name. This foreshadows the metaclass-driven plugin registry built in Lesson 3 and contrasts the two registration techniques.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import TypeVar

T = TypeVar('T', bound=type)
SERVICES: dict[str, type] = {}

def register_service(name: str):
    def decorate(cls: T) -> T:
        # TODO: SERVICES[name] = cls; cls.service_name = name; return cls
        ...
    return decorate
- **Test focus:** Decorated class appears in SERVICES under the given name; the class gains the expected name attribute; the original class object is returned (identity preserved).

</div>
