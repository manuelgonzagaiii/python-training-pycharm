"""Hardening pickle: a safe snapshot loader with find_class and __getnewargs_ex__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: In `core/persistence/snapshot.py`:

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
"""

# Your code here.
