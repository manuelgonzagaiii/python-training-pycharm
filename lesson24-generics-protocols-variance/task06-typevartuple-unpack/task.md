# Variadic Generics: TypeVarTuple & Unpack

> **Phase:** Modern Type System  •  **Stage:** 24.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Declare a TypeVarTuple (*Ts) to capture a variable number of type arguments
- Use Unpack / the *Ts star form to type a function that preserves a heterogeneous tuple's shape
- Write tuple[*Ts] returns so a transform keeps each column's type in a report row
- Use both PEP 695 [*Ts] and the classic TypeVarTuple('Ts')/Unpack forms

## Python features introduced
`TypeVarTuple`, `typing.Unpack`, `PEP 646 variadic generics`, `PEP 695 def f[*Ts] syntax`, `tuple[*Ts] / tuple[Unpack[Ts]]`, `typing a heterogeneous fixed-shape tuple row`

## MiniERP increment
Types the reporting layer's row pipeline: a function that takes a heterogeneous record tuple (e.g. tuple[str, Decimal, int]) and returns the same shape, used to assemble typed analytics rows without collapsing every column to a single common type.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')

def as_row(*values: Unpack[Ts]) -> tuple[Unpack[Ts]]:
    # TODO: return the values as a tuple, preserving each element's type
    ...

# PEP 695 equivalent:
# def as_row[*Ts](*values: *Ts) -> tuple[*Ts]: ...
# row = as_row('A-100', Decimal('9.99'), 42)  # tuple[str, Decimal, int]
- **Test focus:** Tests build rows of mixed types and assert the returned tuple equals the inputs in order; a get_type_hints/structure check documents that element types are preserved (shape kept) rather than widened to a single type.

</div>
