# Auto-build the command registry

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.4 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Walk every public method of a service with inspect.getmembers and a predicate
- Attach signature metadata and the cleaned docstring (getdoc) to each command
- Expose getsource so an admin can view a command's implementation from the CLI
- Produce one registry consumed identically by CLI, Web and TUI

## Python features introduced
`inspect.getmembers`, `inspect.getmembers with predicates (isfunction/ismethod)`, `inspect.getdoc`, `inspect.getsource`, `building lookup dicts from members`, `combining signature + docstring metadata`

## MiniERP increment
Builds erp/registry.py: build_registry(*services) returns name -> Command(method, argspecs, help) covering Products, Customers, Sales, Payments. This registry becomes the canonical command catalog; `help` and Web `/commands` are generated from it.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** Tests build_registry discovers all public methods of multiple fake services under 'service.verb' keys, populates args via describe_command and help via getdoc; tests source_of returns the function body text; verifies private methods are excluded.

</div>
