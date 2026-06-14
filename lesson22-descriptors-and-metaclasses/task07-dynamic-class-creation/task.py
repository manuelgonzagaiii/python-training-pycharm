"""Building Classes at Runtime: type(), new_class, SimpleNamespace, MappingProxyType

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from types import new_class, SimpleNamespace, MappingProxyType
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
"""

# Your code here.
