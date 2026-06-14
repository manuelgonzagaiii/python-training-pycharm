# Batch Validation with while/else

> **Phase:** Control Flow & Functions  •  **Stage:** 8.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use the rare while/else to signal 'all items validated, none rejected'
- Use break to short-circuit on the first invalid item
- Use pass as an explicit do-nothing placeholder branch

## Python features introduced
`while-else clause`, `break`, `pass as a no-op placeholder`, `index-driven iteration`, `else-runs-when-no-break semantics`

## MiniERP increment
Add all_lines_valid(lines) to pricing.py: walk the cart with an index-driven while loop, break on the first line with qty<=0 or base_price<0, and use the while/else to return True only when every line passed. A pass branch documents the 'valid line, nothing to do' case.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def all_lines_valid(lines: list[tuple[str, float, int]]) -> bool:
    """True iff every line is valid; while/else returns True when none broke out."""
    i = 0
    while i < len(lines):
        sku, base_price, qty = lines[i]
        if qty <= 0 or base_price < 0:
            ...
        else:
            pass  # valid line
        i += 1
    else:
        ...
- **Test focus:** Returns True for all-valid carts (else fired); returns False on first invalid line (break taken); empty cart returns True.

</div>
