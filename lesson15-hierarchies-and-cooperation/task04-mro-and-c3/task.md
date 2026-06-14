# Reading the MRO & C3 Linearization

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 15.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read a class's method resolution order via __mro__
- Predict the C3 linearization of a diamond hierarchy
- Understand that super() walks the MRO of the *instance's* type, not the literal parent
- Recognize what makes an MRO inconsistent (the TypeError Python raises)

## Python features introduced
`__mro__ / mro()`, `C3 linearization rules`, `diamond inheritance`, `super() follows MRO not parent`, `type.mro()`, `TypeError on inconsistent MRO`

## MiniERP increment
Adds a small diagnostics helper mro_names(cls) used by developer tooling/tests to verify the entity hierarchy resolves as intended, and documents the cooperative-init contract for all entities.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def mro_names(cls: type) -> list[str]:
    # TODO: return the names of classes in cls.__mro__, in order
    ...


def calls_in_order(instance) -> list[str]:
    # Given an entity that records each cooperative __init__ via a
    # class attribute log, return the order classes were initialized.
    # TODO
    ...

- **Test focus:** mro_names returns the C3 order for a diamond (e.g. ['Invoice','Timestamped','Identified','Entity','object']), and cooperative __init__ runs each class exactly once in MRO order.

</div>
