# A Metaclass-Driven Plugin Registry (MILESTONE)

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a PluginMeta(type) whose __new__ registers each concrete plugin class into a central registry
- Use __prepare__ to capture declaration-order metadata for the class body
- Understand when a metaclass is warranted over __init_subclass__ (controlling class creation itself, not just reacting to it)

## Python features introduced
`custom metaclass (class Meta(type))`, `type.__new__ / __init__ in a metaclass`, `metaclass __call__ controlling instance creation`, `__prepare__ returning an ordered/custom namespace`, `metaclass vs __init_subclass__ trade-offs`, `isinstance/issubclass interplay with metaclasses`

## MiniERP increment
Delivers the phase milestone: the metaclass-backed plugin registry in core/plugins.py. Report, Exporter, and ImportAdapter base classes use PluginMeta so every new reporting/export/import plugin self-registers by subclassing alone — the dispatcher discovers plugins with no central wiring, completing the Reporting and Import/Export extensibility story.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections import OrderedDict

REGISTRY: dict[str, type] = {}

class PluginMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        return OrderedDict()  # capture declaration order
    def __new__(mcls, name, bases, ns, *, key: str | None = None, **kw):
        cls = super().__new__(mcls, name, bases, dict(ns), **kw)
        if bases:  # skip the abstract base itself
            # TODO: REGISTRY[key or name.lower()] = cls
            ...
        return cls

class Plugin(metaclass=PluginMeta):
    ...
- **Test focus:** Concrete subclasses auto-register under the right key; the abstract base does NOT register; __prepare__'s namespace preserves declaration order; instances are correct isinstance of base and metaclass type.

</div>
