# Reservation Loop with while

> **Phase:** Control Flow & Functions  •  **Stage:** 8.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Choose while when the iteration count is condition-driven, not sequence-driven
- Decrement a counter safely and terminate with break
- Recognize and avoid infinite-loop pitfalls

## Python features introduced
`while loop`, `loop condition design`, `augmented assignment`, `avoiding infinite loops`, `break`, `manual counter vs for`

## MiniERP increment
Add reserve_units(available, requested) to an inventory.py module: using a while loop, draw down stock one batch at a time (batch size 10) until the request is met or stock runs out, returning units actually reserved. Models partial fulfillment for later Sales tasks.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def reserve_units(available: int, requested: int) -> int:
    """Reserve in batches of 10 via a while loop; return units actually reserved."""
    reserved = 0
    while ...:
        ...
    return reserved
- **Test focus:** Reserves exactly requested when stock suffices; caps at available when short; handles requested=0 and available=0 without looping forever.

</div>
