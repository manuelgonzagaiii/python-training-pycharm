# Overloading Arithmetic on Money

> **Phase:** OOP Foundations  •  **Stage:** 13.3 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Overload + and - to combine Money values, returning a new Money
- Overload * to scale Money by an int quantity
- Implement __radd__ so sum() of Money objects works (0 + Money)
- Return NotImplemented for unsupported operands and mismatched currencies

## Python features introduced
`__add__`, `__sub__`, `__mul__`, `__radd__`, `operator overloading`, `returning new instances (immutability)`, `NotImplemented for unsupported operands`, `sum() with start=0 and __radd__`

## MiniERP increment
Add __add__/__sub__/__mul__/__radd__ to Money so line totals (price * qty) and invoice subtotals (sum of Money) compose with normal +/* operators — the arithmetic backbone of Sales & Invoicing.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Money:
    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        ...  # same-currency check, return Money(self.cents + other.cents, ...)

    def __mul__(self, qty: int) -> "Money":
        ...  # return Money(self.cents * qty, self.currency)

    def __radd__(self, other: int) -> "Money":
        ...  # support sum([...]) where start is 0
- **Test focus:** Assert Money(1500)+Money(500)==Money(2000); Money(1500)*3==Money(4500); sum([Money(100),Money(200)])==Money(300) via __radd__; mismatched currency or bad operand returns NotImplemented/raises TypeError.

</div>
