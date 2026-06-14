"""Variadic Generics: TypeVarTuple & Unpack

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')

def as_row(*values: Unpack[Ts]) -> tuple[Unpack[Ts]]:
    # TODO: return the values as a tuple, preserving each element's type
    ...

# PEP 695 equivalent:
# def as_row[*Ts](*values: *Ts) -> tuple[*Ts]: ...
# row = as_row('A-100', Decimal('9.99'), 42)  # tuple[str, Decimal, int]
"""

# Your code here.
