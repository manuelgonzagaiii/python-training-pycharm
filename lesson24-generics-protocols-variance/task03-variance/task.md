# Variance: Covariance & Contravariance

> **Phase:** Modern Type System  •  **Stage:** 24.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why list[Product] is NOT a list[Item] (invariance) while Sequence[Product] IS a Sequence[Item] (covariance)
- Define a covariant TypeVar for a read-only producer and a contravariant TypeVar for a write-only consumer
- Know that PEP 695 infers variance automatically, and how the classic covariant=/contravariant= flags map to it
- Choose Sequence/Iterable (covariant) over list (invariant) in parameters to avoid spurious errors

## Python features introduced
`covariance`, `contravariance`, `invariance`, `TypeVar(covariant=True)`, `TypeVar(contravariant=True)`, `PEP 695 inferred variance`, `why list[T] is invariant`, `Sequence covariance`

## MiniERP increment
Splits the repository surface into a covariant read-only Reader protocol-shaped producer (yields entities) and a contravariant Writer consumer (accepts entities), aligning the service layer with safe variance so a ProductReader can be used where an ItemReader is expected.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections.abc import Sequence

class Item: ...
class Product(Item): ...

# Covariant producer: returns T, never accepts it -> can be 'narrowed' safely
class Reader[T_co]:        # PEP 695 infers covariance from usage
    def get_all(self) -> Sequence[T_co]:
        ...  # TODO

# Why this is invariant and breaks:
# def widen(items: list[Item]) -> None: ...
# widen(list_of_products)   # TODO: explain the error in the task text
- **Test focus:** Tests verify a Reader[Product] is accepted where Reader[Item] is expected (covariance) and that Sequence parameters accept a list of subtype; the documented contrast shows list invariance as a (non-executed) type error.

</div>
