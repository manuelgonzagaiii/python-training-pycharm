# Bounded & Constrained Type Vars

> **Phase:** Modern Type System  •  **Stage:** 24.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Constrain a type parameter with an upper bound (T: Entity) so the body may call Entity methods on values of T
- Distinguish a bound (any subtype of Entity) from constraints (exactly one of a fixed set, e.g. TypeVar('N', int, float))
- Express both in PEP 695 syntax (def f[T: Entity], def g[N: (int, float)]) and classic TypeVar form
- Use a bound to require that repository entities expose an .id

## Python features introduced
`TypeVar bound=`, `TypeVar with value constraints`, `PEP 695 'T: Bound' bound syntax`, `upper bounds vs constraints distinction`, `using a bound to call methods on T`

## MiniERP increment
Defines an Entity base (has .id: str) and re-parameterizes the repository/service helpers as bounded generics [T: Entity], so save_all and reindex can read entity.id generically. Numeric helpers (e.g. round_money) use a constrained TypeVar over (int, float, Decimal-like).

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Entity:
    id: str

# Bounded: T must be Entity or a subclass -> we may read .id
def index_by_id[T: Entity](items: list[T]) -> dict[str, T]:
    # TODO: build {item.id: item}
    ...

# Constrained: N is exactly one of these types
def clamp[N: (int, float)](value: N, lo: N, hi: N) -> N:
    # TODO: return value bounded to [lo, hi]
    ...
- **Test focus:** Tests run index_by_id over Product/Customer (both Entity subclasses) and clamp over ints and floats; a check confirms calling .id inside the bounded function works and that a non-Entity argument would be a type error (documented, not executed).

</div>
