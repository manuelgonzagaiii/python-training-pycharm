"""The Descriptor Protocol

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import Any

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
"""

# Your code here.
