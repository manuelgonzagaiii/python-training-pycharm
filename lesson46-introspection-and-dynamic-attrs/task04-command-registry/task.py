"""Auto-build the command registry

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import inspect
from dataclasses import dataclass, field
from .introspect import ArgSpec, describe_command


@dataclass(slots=True)
class Command:
    name: str
    func: object
    args: list[ArgSpec] = field(default_factory=list)
    help: str = ""


def build_registry(*services) -> dict[str, Command]:
    """For each service, register every public method as 'service.verb'.

    Use inspect.getmembers(service, predicate=...) to find methods,
    describe_command for args, inspect.getdoc for help text.
    """
    raise NotImplementedError


def source_of(cmd: Command) -> str:
    """Return inspect.getsource of the command's function."""
    raise NotImplementedError

"""

# Your code here.
