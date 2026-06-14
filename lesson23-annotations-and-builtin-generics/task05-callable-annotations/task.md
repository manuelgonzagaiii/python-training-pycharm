# Typing Callables & Higher-Order Functions

> **Phase:** Modern Type System  •  **Stage:** 23.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Annotate a parameter that is itself a function using Callable[[ArgTypes], ReturnType]
- Type a key function (Callable[[Product], float]) passed to sorting/filtering helpers
- Use Callable[..., R] when the argument list is unconstrained and know the trade-off
- Connect callable typing to the strategy-style patterns already used in the OOP core

## Python features introduced
`typing.Callable / collections.abc.Callable`, `Callable[[Arg, ...], Return]`, `Callable[..., R]`, `functions as first-class typed values`, `typed key= and predicate functions`

## MiniERP increment
Reporting helpers gain typed higher-order signatures: sort_products(products, key: Callable[[Product], float]) and filter_products(products, predicate: Callable[[Product], bool]), the typed seed of the Reporting/Analytics module.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections.abc import Callable, Iterable

def sort_products(products: Iterable[Product], key: Callable[[Product], float]) -> list[Product]:
    # TODO: return sorted(products, key=key)
    ...

def filter_products(products: Iterable[Product], predicate: Callable[[Product], bool]) -> list[Product]:
    # TODO: keep products where predicate(p) is True
    ...
- **Test focus:** Tests pass lambdas/functions as key and predicate (e.g. key=lambda p: p.price, predicate by tag) and assert correct ordering/filtering; an annotation check confirms the Callable parameter types.

</div>
