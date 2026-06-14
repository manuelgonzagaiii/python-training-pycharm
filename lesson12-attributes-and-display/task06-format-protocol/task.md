# Custom Format Specs with __format__

> **Phase:** OOP Foundations  •  **Stage:** 12.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement __format__ to support f-string format specs like f'{money:full}'
- Parse a custom format_spec and branch with match/case
- Delegate to built-in formatting for numeric specs
- Understand how f-strings call __format__ under the hood

## Python features introduced
`__format__ method`, `format() builtin`, `format_spec parsing`, `f-string format spec dispatch`, `match/case on spec`, `format(self.cents, spec) delegation`

## MiniERP increment
Add Money.__format__ supporting specs such as '' (default '$15.00'), 'full' ('15.00 USD'), and 'cents' ('1500'), giving the Reporting/Analytics layer flexible currency rendering from a single object.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Money:
    def __format__(self, spec: str) -> str:
        match spec:
            case "" | "short":
                ...  # "$15.00"
            case "full":
                ...  # "15.00 USD"
            case "cents":
                ...  # "1500"
            case _:
                ...  # format(self.cents / 100, spec) or raise ValueError
- **Test focus:** Assert f'{m}' gives '$15.00', f'{m:full}' gives '15.00 USD', f'{m:cents}' gives '1500'; assert an unknown numeric spec delegates or an invalid one raises ValueError.

</div>
