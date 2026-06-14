# Nested Patterns and the Full Dispatcher

> **Phase:** Control Flow & Functions  •  **Stage:** 9.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compose sequence, mapping, and class patterns to one level deep and beyond
- Design a single match that handles the whole command surface
- See how structural matching replaces sprawling if/elif chains

## Python features introduced
`nested patterns (patterns inside patterns)`, `sequence-inside-mapping and class-inside-sequence`, `combining literal+capture+guard nesting`, `exhaustive-style match design`, `match as the single dispatch entry point`

## MiniERP increment
Add dispatch(request) to cli/dispatch.py — the phase's milestone entry point — matching nested shapes like ['add', sku, qty] and {'op': 'discount', 'rules': [*rules]} and PriceRequest(...) in one match, producing the typed request object that the pricing layer in Lesson 3 will execute. Wire main.py to call dispatch() so MiniERP has a working command front door.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def dispatch(request) -> object:
    """Single match/case entry point over CLI lists, dict payloads, and request objects."""
    match request:
        case ["add", sku, qty]:
            ...
        case {"op": "discount", "rules": [*rules]}:
            ...
        case PriceRequest() as req:
            return req
        case _:
            ...
- **Test focus:** List, dict, and object forms each route to the correct typed request; nested rules list is captured; malformed input yields a HELP/error sentinel.

</div>
