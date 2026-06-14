# Subclass Hooks: __init_subclass__ & __class_getitem__

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use __init_subclass__ to run code each time a subclass is defined and accept class-level keyword args
- Auto-register subclasses into a registry without writing a metaclass
- Implement __class_getitem__ so a class supports SomeClass[param] subscription

## Python features introduced
`__init_subclass__(cls, **kwargs)`, `class-keyword arguments (class C(Base, key=val))`, `validating/registering subclasses without a metaclass`, `__class_getitem__ for MyClass[...] subscription`, `types.GenericAlias awareness`

## MiniERP increment
Gives the Plugin base class an __init_subclass__(cls, *, name) that auto-registers each plugin subclass by name into a registry dict, and a __class_getitem__ so Report['sales'] resolves a parametrized variant — the lighter-weight precursor to the metaclass registry in the next task.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Plugin:
    registry: dict[str, type["Plugin"]] = {}
    def __init_subclass__(cls, *, name: str | None = None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        key = name or cls.__name__.lower()
        # TODO: Plugin.registry[key] = cls
        ...
    def __class_getitem__(cls, item: str):
        # TODO: return cls.registry[item]
        ...

# Usage: class SalesReport(Plugin, name='sales'): ...
- **Test focus:** Defining a subclass (with or without name=) registers it under the right key; class-keyword args are consumed correctly; Plugin['sales'] returns the registered subclass; super().__init_subclass__ still called.

</div>
