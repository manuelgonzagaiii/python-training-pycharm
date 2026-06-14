# Building Classes at Runtime: type(), new_class, SimpleNamespace, MappingProxyType

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create a class dynamically with type('Name', bases, ns) and with types.new_class (metaclass-aware)
- Build throwaway config/record objects with SimpleNamespace
- Expose an immutable view of an internal dict via MappingProxyType

## Python features introduced
`three-argument type(name, bases, namespace)`, `types.new_class with exec_body and a metaclass`, `types.SimpleNamespace for ad-hoc objects`, `types.MappingProxyType for read-only views`, `resolve_bases / prepare_class awareness`

## MiniERP increment
Implements make_dto(fields) that synthesizes lightweight DTO classes at runtime (used to materialize import schemas defined in a config file) via new_class so they go through PluginMeta and self-register; exposes the plugin REGISTRY to the rest of the app as a read-only MappingProxyType; uses SimpleNamespace for parsed CLI/config bundles.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from types import new_class, SimpleNamespace, MappingProxyType
from collections.abc import Mapping

def make_dto(name: str, fields: list[str]) -> type:
    def body(ns: dict) -> None:
        ns['__slots__'] = tuple(fields)
    # TODO: return new_class(name, (object,), {}, exec_body=body)
    ...

# Read-only public view of the plugin registry:
def public_registry() -> Mapping[str, type]:
    # TODO: return MappingProxyType(REGISTRY)
    ...

cfg = SimpleNamespace(verbose=True, source='products.csv')
- **Test focus:** Dynamically created class has the requested slots/bases and works as an instance; metaclass-aware creation still self-registers; MappingProxyType rejects mutation (TypeError on item assignment) while reflecting live updates; SimpleNamespace attributes round-trip.

</div>
