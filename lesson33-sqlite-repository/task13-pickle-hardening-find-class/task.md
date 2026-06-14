# Hardening pickle: a safe snapshot loader with find_class and __getnewargs_ex__

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.13 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why `pickle.loads` on untrusted bytes is remote code execution, and that protocols / `__getstate__` do nothing to stop it
- Drive (de)serialization through the `pickle.Pickler` and `pickle.Unpickler` *classes* (writing to / reading from a `BytesIO`) instead of the module-level `dumps`/`loads` shortcuts
- Subclass `pickle.Unpickler` and override `find_class(module, name)` to enforce a class allowlist, raising `pickle.UnpicklingError` for anything not explicitly permitted
- Understand that `find_class` is the single chokepoint pickle uses to resolve every global it imports, so allowlisting there blocks `os.system`, `builtins.eval`, `subprocess.Popen`, etc.
- Implement `__getnewargs_ex__` so a `__slots__` value object with no zero-argument `__init__` can be reconstructed: pickle calls `cls.__new__(cls, *args, **kwargs)` with what you return
- Distinguish `__getnewargs_ex__` (args + kwargs, protocol >= 2) from the older positional-only `__getnewargs__`, and know when each is consulted
- See that during unpickling `__init__` is normally skipped, which is exactly why `__getnewargs_ex__` and `__getstate__/__setstate__` exist

## Python features introduced
`pickle.Pickler`, `pickle.Unpickler`, `Unpickler.find_class override`, `pickle.UnpicklingError`, `__getnewargs_ex__`, `__getnewargs__`, `__slots__ with pickle`, `object.__new__ vs __init__ during unpickling`, `frozenset / set membership allowlist`, `io.BytesIO`, `fully-qualified module.qualname identity`, `classmethod constructors`, `PEP 604 unions (X | Y) in signatures`, `raising on disallowed import`, `pickle protocol negotiation (pickle.HIGHEST_PROTOCOL)`

## MiniERP increment
Adds a hardened persistence boundary to MiniERP. Introduces `core/persistence/snapshot.py` with `dump_snapshot(state, fp)` and `load_snapshot(fp)` built on `pickle.Pickler`/`pickle.Unpickler` rather than `dumps`/`loads`. A new `SafeUnpickler(pickle.Unpickler)` overrides `find_class` to consult an `ALLOWED_CLASSES` frozenset of fully-qualified MiniERP domain names (e.g. `core.domain.Product`, `core.domain.Customer`, `core.domain.Money`, plus the snapshot container and a curated set of stdlib builtins like `builtins.dict`/`list`/`set`/`datetime.datetime`/`decimal.Decimal`); any other `module.name` (e.g. `os.system`, `builtins.eval`) raises `pickle.UnpicklingError('disallowed during unpickle: ...')`. The `Money` value object (decimal amount + currency) is reworked to use `__slots__` and a keyword-only constructor and gains `__getnewargs_ex__` so it round-trips through the safe loader without a no-arg `__init__`. This turns the earlier 'never unpickle untrusted data' warning into a concrete, tested defense for loading `.minierp` snapshot files that may have come from another machine.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** In `core/persistence/snapshot.py`:

```python
import io
import pickle
from decimal import Decimal
from datetime import datetime, date

ALLOWED_CLASSES: frozenset[str] = frozenset({
    "core.domain.Product", "core.domain.Customer", "core.domain.Money",
    "core.persistence.snapshot.Snapshot",
    "builtins.dict", "builtins.list", "builtins.tuple", "builtins.set",
    "builtins.frozenset", "builtins.str", "builtins.int", "builtins.bool",
    "builtins.NoneType",
    "decimal.Decimal", "datetime.datetime", "datetime.date",
})

class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str):
        fqn = f"{module}.{name}"
        if fqn not in ALLOWED_CLASSES:
            raise pickle.UnpicklingError(f"disallowed during unpickle: {fqn}")
        return super().find_class(module, name)

def dump_snapshot(state, fp) -> None:
    pickle.Pickler(fp, protocol=pickle.HIGHEST_PROTOCOL).dump(state)

def load_snapshot(fp):
    return SafeUnpickler(fp).load()
```

And rework `Money` in `core/domain.py`:

```python
class Money:
    __slots__ = ("amount", "currency")
    def __init__(self, *, amount: Decimal, currency: str) -> None:
        object.__setattr__(self, "amount", Decimal(amount))
        object.__setattr__(self, "currency", currency)
    def __getnewargs_ex__(self) -> tuple[tuple, dict]:
        return (), {"amount": self.amount, "currency": self.currency}
```

Learners fill in: the exact allowlist membership check, the `UnpicklingError` message, `__getnewargs_ex__` (and contrast with `__getnewargs__`), and `dump_snapshot`/`load_snapshot` wiring through `BytesIO`.
- **Test focus:** Round-trip: `dump_snapshot` then `load_snapshot` on a `Snapshot` holding `Product`/`Customer`/`Money` reconstructs equal objects, and `Money` (with `__slots__`, no no-arg `__init__`) survives the round-trip via `__getnewargs_ex__`. Security: feed the loader bytes that reference a disallowed global (craft a payload whose `__reduce__` returns `(os.system, ('echo pwned',))`, or pickle an object of a non-allowlisted class) and assert `load_snapshot` raises `pickle.UnpicklingError` *without* executing the payload (use a sentinel/flag that must remain untouched). Assert `find_class` permits an allowlisted name and rejects `os.system` / `builtins.eval` by fully-qualified name. Confirm snapshots are written/read via `pickle.Pickler`/`pickle.Unpickler` (not `dumps`/`loads`) and at `HIGHEST_PROTOCOL`. Optionally assert that a plain `pickle.loads` of the malicious payload *would* have run it, to make the contrast explicit (run in a guarded subprocess or with a harmless sentinel command).

</div>
