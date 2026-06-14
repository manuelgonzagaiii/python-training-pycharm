"""A Metaclass-Driven Plugin Registry (MILESTONE)

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from collections import OrderedDict

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
"""

# Your code here.
