# Mapping Patterns for Structured Requests

> **Phase:** Control Flow & Functions  •  **Stage:** 9.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Match dict-shaped requests by required keys
- Capture both a known field and the rest of a mapping
- Understand that mapping patterns match on subset, not exact, keys

## Python features introduced
`mapping patterns {"key": value}`, `capturing a value by key`, `**rest to capture remaining keys`, `partial-match semantics of mapping patterns`, `combining mapping with literal subpatterns`

## MiniERP increment
Add classify_request(req) to cli/dispatch.py that takes a dict request (e.g. from a Web/JSON interface) and matches mapping patterns like {'op': 'price', 'sku': sku, **rest} to extract the operation and salient fields, routing JSON-style payloads through the same logic the CLI uses.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def classify_request(req: dict) -> tuple[Command, dict]:
    """Match a dict payload with mapping patterns; capture remaining keys with **rest."""
    match req:
        case {"op": "price", "sku": sku, **rest}:
            ...
        case {"op": op}:
            ...
        case _:
            return (Command.HELP, {})
- **Test focus:** A price payload extracts sku and leftover fields via **rest; a generic {'op':...} payload routes by op; a payload missing 'op' falls to HELP.

</div>
