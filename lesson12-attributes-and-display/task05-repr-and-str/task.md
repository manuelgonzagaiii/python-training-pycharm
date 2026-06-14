# __repr__ and __str__

> **Phase:** OOP Foundations  •  **Stage:** 12.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement __repr__ for an unambiguous developer-facing representation
- Implement __str__ for a friendly end-user string
- Understand str() falls back to __repr__ when __str__ is absent
- Use the eval-able 'ClassName(...)' convention and !r in f-strings

## Python features introduced
`__repr__`, `__str__`, `repr() vs str()`, `unambiguous eval-able repr convention`, `fallback of str to repr`, `!r in f-strings`

## MiniERP increment
Give Money and Product proper __repr__ (e.g. Money(cents=1500, currency='USD')) and __str__ (e.g. '$15.00'), so debugging output and user-facing displays both read cleanly across MiniERP.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Money:
    def __init__(self, cents: int, currency: str = "USD") -> None:
        self.cents = cents
        self.currency = currency

    def __repr__(self) -> str:
        ...  # f"Money(cents={self.cents!r}, currency={self.currency!r})"

    def __str__(self) -> str:
        ...  # f"${self.cents / 100:.2f}"
- **Test focus:** Assert repr(Money(...)) matches the eval-able 'Money(cents=1500, currency=\'USD\')' form; assert str(Money(...)) returns '$15.00'; assert str falls back to repr on a class defining only __repr__.

</div>
