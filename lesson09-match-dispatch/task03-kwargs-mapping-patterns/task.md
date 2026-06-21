# Stage 3: mapping patterns for structured requests

The same command can arrive not as a token list but as a **dict** — for example a JSON
payload from the web interface: `{"op": "price", "sku": "A-001", "qty": 2}`. `match` handles
that shape too, with **mapping patterns**, so the CLI and the web layer can funnel through
the same routing logic.

## Matching a dict by its keys

```
match req:
    case {"op": "price", "sku": sku}:
        ...        # matches any dict that HAS op == "price" and a "sku" key
```

Two things make mapping patterns behave differently from sequence patterns:

- They match on **the keys you name and ignore the rest**. `{"op": "price", "sku": sku}`
  matches a dict that has at least those keys with `op` equal to `"price"`; extra keys like
  `"qty"` do not stop the match. (Sequence patterns, by contrast, care about the full
  length.)
- A value position can be a **literal** to constrain it (`"op": "price"`) or a **capture**
  to pull it out (`"sku": sku` binds the SKU). You can mix both in one pattern.
- `**rest` captures the keys you did *not* name into a new dict — the mapping equivalent of
  the star pattern.

## Your task

In `dispatch.py`, finish `classify_request(req)`. The discount, generic, and fallback cases
are written. Fill in the **first** case: match a request whose `op` is `"price"` and which
has a `"sku"` key, binding the SKU and capturing any remaining keys with `**rest`.

## Worked example

```
>>> import dispatch
>>> dispatch.classify_request({"op": "price", "sku": "A-001", "qty": 2})
('price', {'sku': 'A-001', 'qty': 2})
>>> dispatch.classify_request({"op": "report"})
('report', {})
>>> dispatch.classify_request({})
('help', {})
```

## What the check verifies, and what it leaves to you

- Enforced: a `price` request is recognized and its SKU is extracted; other operations route
  by their `op`; a dict with no `op` falls back to `help`.
- Your free choice: exactly which extra fields you carry forward in the returned dict is up
  to you, as long as the operation is identified and the SKU is available for a price request.

<div class="hint" title="If you are stuck">

The pattern is `case {"op": "price", "sku": sku, **rest}:`. The literal `"price"` constrains
the operation; `sku` captures the value; `**rest` scoops up whatever else was in the dict.

</div>

Reference: Python documentation, "The match statement" (mapping patterns) at docs.python.org.
