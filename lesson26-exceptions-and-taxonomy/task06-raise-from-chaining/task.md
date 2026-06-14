# Exception Chaining: raise from, __cause__ and __context__

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Wrap a low-level exception in a domain exception while preserving the original via raise from
- Distinguish explicit chaining (__cause__) from implicit chaining (__context__) and when each appears
- Use raise from None deliberately to hide irrelevant internal causes from API consumers
- Translate library/built-in failures at the boundary so callers only ever see ERPError

## Python features introduced
`raise X from Y (explicit chaining sets __cause__)`, `implicit chaining during handling (__context__)`, `raise X from None to suppress the chain`, `__cause__ vs __context__ vs __suppress_context__`, `catching a low-level error and re-raising a domain error`, `translating built-in exceptions (KeyError/ValueError/InvalidOperation) into ERPError`

## MiniERP increment
Introduces a `lookup_product(repo, sku)` in the Products service that catches the repository's KeyError and raises `NotFoundError(...) from err`, and a price-parse path that catches Decimal's InvalidOperation and raises `ValidationError(...) from err` — giving every service a clean ERPError surface while retaining root-cause traceback for logs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal, InvalidOperation
from errors import NotFoundError, ValidationError

def lookup_product(repo: dict[str, object], sku: str):
    try:
        return repo[sku]
    except KeyError as err:
        # TODO: raise NotFoundError('product', sku) from err
        raise NotImplementedError

def parse_price(raw: str) -> Decimal:
    try:
        return Decimal(raw)
    except InvalidOperation as err:
        # TODO: raise ValidationError(..., field='price') from err
        raise NotImplementedError
- **Test focus:** Re-raised NotFoundError/ValidationError have __cause__ set to the original built-in; the suppression variant (from None) leaves __cause__ None with __suppress_context__ True.

</div>
