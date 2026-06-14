# Defensive Input Validation at the Service Boundary

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Validate every externally supplied field at the service boundary before it touches domain state
- Convert silent bad data into explicit, well-typed ValidationError raises with actionable messages
- Use guard clauses (validate-and-raise-early) to keep the happy path flat and readable
- Apply match/case to route a field name to its specific validation rule

## Python features introduced
`raising custom exceptions`, `guard clauses / early raise`, `validating types and ranges before use`, `decimal.Decimal for money validation`, `str.strip / emptiness checks`, `match/case for dispatching validation rules`, `walrus operator in a validation guard`, `raising with structured context`

## MiniERP increment
Adds a `validate_product_payload(data)` function used by the Products service that checks sku (non-empty, normalized), name (non-empty), price (Decimal >= 0), and stock (int >= 0), raising ValidationError with the offending field on any breach. This replaces the services' previous trust-the-caller behavior with a real validation gate.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal, InvalidOperation
from errors import ValidationError

def validate_product_payload(data: dict[str, object]) -> dict[str, object]:
    """Return a cleaned payload or raise ValidationError(field=...).
    Rules: sku non-empty (stripped); name non-empty; price Decimal >= 0;
    stock int >= 0.
    """
    # TODO: guard each field with an early raise; use match/case to pick the rule;
    #       use a walrus when checking (sku := str(data.get('sku','')).strip())
    raise NotImplementedError
- **Test focus:** Each invalid field raises ValidationError naming that field; valid input returns a normalized payload; price/stock boundary values (0, negative, non-numeric) are checked.

</div>
