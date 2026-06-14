"""Subclass Hooks: __init_subclass__ & __class_getitem__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: class Plugin:
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
"""

# Your code here.
