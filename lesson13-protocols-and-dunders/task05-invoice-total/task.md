# Compose the Invoice Total

> **Phase:** OOP Foundations  •  **Stage:** 13.5 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compute an invoice total by summing LineItem line_totals with sum()
- Reuse Money arithmetic and __radd__ from the operators task
- Reuse Money.__format__/__str__ to render the total
- See how small well-behaved objects compose into larger ones

## Python features introduced
`@property computed total`, `sum() over objects using __radd__`, `operator overloading reuse`, `__str__/__format__ reuse`, `object composition`

## MiniERP increment
Add Invoice.total (a Money) computed by summing line_totals, plus a __str__ that renders the invoice with each line and the formatted grand total — delivering a printable invoice for CLI/Web/GUI later.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Invoice:
    @property
    def total(self) -> Money:
        ...  # sum((item.line_total for item in self._items), Money(0))

    def __str__(self) -> str:
        ...  # render each line + f"TOTAL: {self.total}"
- **Test focus:** Assert total equals the summed line_totals as Money; assert an empty invoice totals Money(0); assert __str__ includes each line and the formatted total.

</div>
