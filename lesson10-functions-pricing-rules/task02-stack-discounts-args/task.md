# Stacking Discounts with *args and **kwargs

> **Phase:** Control Flow & Functions  •  **Stage:** 10.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Accept an arbitrary number of positional discount percents with *args
- Accept open-ended named options with **kwargs
- Unpack collections into a call with * and **

## Python features introduced
`*args (variadic positional)`, `**kwargs (variadic keyword)`, `iterating *args`, `reading named options from **kwargs`, `unpacking a call with * and **`, `annotations for *args/**kwargs`

## MiniERP increment
Add stack_discounts(price, *percents, **options) to rules.py that sequentially applies each percent in *percents and reads options like clamp_floor from **kwargs, letting Sales stack promotional discounts of unknown count onto a line price.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def stack_discounts(price: float, *percents: float, **options) -> float:
    """Apply each percent in turn; honor options like clamp_floor=<min price>."""
    result = price
    for p in percents:
        ...
    floor = options.get("clamp_floor", 0.0)
    ...
- **Test focus:** Zero, one, and many percents stack multiplicatively; clamp_floor option prevents the price dropping below the floor; unpacking *list/**dict at the call site works.

</div>
