# Why Objects? Dicts vs. Classes

> **Phase:** OOP Foundations  •  **Stage:** 11.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand the limits of dict-based records (no validation, typo-prone keys, no behavior co-located with data)
- Form a mental model of a class as a blueprint and an instance as one filled-in copy
- Understand that self is just the current instance passed as the first argument
- Preview how methods bundle behavior next to data

## Python features introduced
`class statement`, `instance vs class`, `self parameter`, `attribute access dot-notation`, `namespaces/__dict__ concept`

## MiniERP increment
Frame the refactor: the existing product dicts like {'sku': 'A1', 'name': 'Widget', 'price_cents': 1500} and the free functions that operated on them will become a Product class. No code yet — this page sets the target shape of the domain layer.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Reading task — no code to write.
# Earlier phases stored a product as a dict and passed it to functions:
#
#     product = {"sku": "A1", "name": "Widget", "price_cents": 1500}
#     def product_label(p): return f"{p['sku']} - {p['name']}"
#
# This lesson rebuilds that as a class so data and behavior live together.
- **Test focus:** No checks (theory page).

</div>
