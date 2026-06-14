"""Read service signatures with inspect

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import inspect
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ArgSpec:
    name: str
    required: bool
    default: object | None
    annotation: str


def describe_command(func) -> list[ArgSpec]:
    """Return one ArgSpec per parameter of `func` using inspect.signature.

    Skip 'self'. required is True when the parameter has no default.
    annotation is the str form, or '' when empty.
    """
    raise NotImplementedError


def bind_args(func, /, *args, **kwargs) -> dict[str, object]:
    """Use Signature.bind + apply_defaults; raise TypeError on a bad call."""
    raise NotImplementedError

"""

# Your code here.
