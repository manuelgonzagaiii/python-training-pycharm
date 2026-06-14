# @overload, cast, assert_type & reveal_type

> **Phase:** Modern Type System  •  **Stage:** 25.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Give a function several precise signatures with @overload (e.g. get(id) -> T, get(id, default) -> T | D)
- Use cast() to assert a type the checker cannot infer, knowing it is unchecked at runtime
- Verify inferred types with assert_type and inspect them during development with reveal_type
- Understand overloads document the contract while a single untyped implementation backs them

## Python features introduced
`typing.overload`, `@overload stub + implementation pattern`, `typing.cast`, `typing.assert_type`, `reveal_type`, `guiding vs verifying inference`, `narrowing the checker's view`

## MiniERP increment
Repository.get gains @overload signatures: get(key) -> T | None and get(key, default: D) -> T | D, giving callers across all four interfaces precise return types; cast/assert_type are used to tie down a couple of dynamic spots (e.g. JSON-loaded DTOs) so the service layer stays strict.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import overload, cast, assert_type

class Repository[T]:
    @overload
    def get(self, key: str) -> T | None: ...
    @overload
    def get[D](self, key: str, default: D) -> T | D: ...
    def get(self, key, default=None):  # single impl backs both
        ...  # TODO

# raw: dict[str, object] from json.load
# dto = cast(InvoiceDTO, raw)        # assert the shape to the checker
# assert_type(repo.get('x'), 'Product | None')  # verify inference
- **Test focus:** Tests confirm get returns the right value with and without a default at runtime; an annotation/overload-count check confirms two @overload stubs exist, and assert_type/cast usages are present and runtime-harmless.

</div>
