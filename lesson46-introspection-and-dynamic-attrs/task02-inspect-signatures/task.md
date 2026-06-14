# Read service signatures with inspect

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.2 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Extract a callable's parameters, kinds, defaults and annotations programmatically
- Distinguish required from optional params via Parameter.empty
- Use Signature.bind to validate caller-supplied args before invoking a service
- Generate per-command usage/help strings from signatures alone

## Python features introduced
`inspect.signature`, `inspect.Signature / inspect.Parameter`, `Parameter.kind (POSITIONAL_OR_KEYWORD, KEYWORD_ONLY, VAR_POSITIONAL, VAR_KEYWORD)`, `Parameter.default / Parameter.empty`, `Parameter.annotation`, `Signature.bind / bind_partial`, `inspect.getfullargspec contrast`

## MiniERP increment
Adds erp/introspect.py with describe_command(func) returning structured argument metadata for any ERP service method (e.g. products.add(name, price, qty=0)). CLI help and Web API parameter docs will be generated from this instead of duplicated docstrings.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** Tests describe_command against functions with positional, keyword-only, defaulted, var-args and annotated params; asserts required/default/annotation are read correctly; tests bind_args accepts valid calls (with defaults applied) and raises TypeError for missing/extra args.

</div>
