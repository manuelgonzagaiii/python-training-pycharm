# A Money Value Object

> **Phase:** OOP Foundations  •  **Stage:** 12.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Design a small value object that wraps a single concept (money in cents)
- Combine __init__, a property, and a classmethod factory learned so far
- Avoid float money bugs by storing integer cents
- Prepare a reusable currency type for prices, totals, and payments

## Python features introduced
`class as value object`, `dataclass-free plain class`, `int-cents storage`, `computed properties`, `@classmethod factory from_dollars`, `encapsulating units`

## MiniERP increment
Introduce a Money class (integer cents + currency) with a from_dollars classmethod and a dollars property; Product.price will reference Money, unifying currency handling across catalog, invoices, and payments.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Money:
    def __init__(self, cents: int, currency: str = "USD") -> None:
        ...

    @classmethod
    def from_dollars(cls, amount: float, currency: str = "USD") -> "Money":
        ...  # round to nearest cent

    @property
    def dollars(self) -> float:
        ...  # self.cents / 100
- **Test focus:** Assert from_dollars(15.0) stores 1500 cents; assert the dollars property returns 15.0; assert currency defaults to 'USD' and is preserved.

</div>
