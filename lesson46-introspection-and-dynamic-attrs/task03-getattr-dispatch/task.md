# Dynamic dispatch with getattr/hasattr/callable

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.3 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Look up and invoke a method chosen at runtime by name (getattr) instead of an if/elif chain
- Guard lookups with hasattr and callable to avoid AttributeError and calling non-callables
- Enumerate an object's attributes with dir()/vars() and filter dunder/private names
- Understand why dynamic dispatch must be defended against arbitrary attribute names

## Python features introduced
`getattr`, `setattr`, `hasattr`, `callable`, `vars()`, `dir()`, `attribute lookup vs dict access`, `underscore-private convention filtering`

## MiniERP increment
Replaces the previous phase's hand-written CLI command switch with a generic dispatch(service, verb, **kwargs) that resolves the verb to a public callable on the service via getattr, validates it with callable(), and rejects private/dunder names — the single dispatcher all four front-ends will share.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations


def public_callables(obj) -> dict[str, object]:
    """Map public (no leading underscore) callable attribute names -> the callable.

    Use dir()/getattr()/callable(). Skip names starting with '_'.
    """
    raise NotImplementedError


def dispatch(service, verb: str, /, **kwargs):
    """Resolve `verb` on `service` and call it with kwargs.

    Raise LookupError if verb is missing, private, or not callable.
    """
    raise NotImplementedError

- **Test focus:** Tests public_callables excludes _private/__dunder and non-callable attributes; tests dispatch invokes the right method, passes kwargs through, raises LookupError for unknown/private/non-callable verbs.

</div>
