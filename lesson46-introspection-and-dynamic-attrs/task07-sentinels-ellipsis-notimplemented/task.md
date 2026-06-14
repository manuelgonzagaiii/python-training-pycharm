# Sentinels: Ellipsis, NotImplemented, NotImplementedError

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.7 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a unique MISSING sentinel to distinguish 'absent' from 'None' in ERP fields
- Return NotImplemented from a rich-comparison to let Python try the reflected op
- Raise NotImplementedError for not-yet-implemented abstract service methods
- Use ... as a placeholder body and in type stubs, and know it is the Ellipsis singleton

## Python features introduced
`Ellipsis / ... literal`, `sentinel object() pattern`, `NotImplemented (singleton) vs NotImplementedError (exception)`, `__eq__ returning NotImplemented`, `is-comparison for singletons`, `abstract-method stub with ...`, `raise NotImplementedError for abstract behavior`

## MiniERP increment
Adds a MISSING sentinel used by ERP partial-update / patch operations (so PATCH can tell 'leave field unchanged' from 'set to None'), and makes Money.__eq__ return NotImplemented for foreign types so comparisons stay correct.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations


class _Missing:
    """Unique sentinel distinct from None. Use `is MISSING` to test."""
    __slots__ = ()
    def __repr__(self) -> str: return "MISSING"


MISSING = _Missing()


def apply_patch(record: dict, **changes) -> dict:
    """Return updated copy: keys whose value is MISSING are left unchanged;
    an explicit None overwrites with None."""
    raise NotImplementedError


class Money:
    def __init__(self, cents: int): self.cents = cents
    def __eq__(self, other) -> bool:
        """Compare by cents with another Money; return NotImplemented otherwise."""
        raise NotImplementedError
    def __hash__(self) -> int: return hash(self.cents)

- **Test focus:** Tests apply_patch leaves MISSING fields untouched while applying None/real values; asserts MISSING is not None and is its own type; tests Money.__eq__ returns NotImplemented (checked via the internal op or comparison fallback) for non-Money and equality works between Money instances.

</div>
