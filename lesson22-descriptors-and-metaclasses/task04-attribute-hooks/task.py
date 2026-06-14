"""Intercepting Attribute Access

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import Any

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
"""

# Your code here.
