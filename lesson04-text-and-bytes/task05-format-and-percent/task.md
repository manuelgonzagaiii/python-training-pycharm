# str.format, %-formatting, and Template

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.5 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use str.format and format_map for templated output with named fields
- Read and write legacy %-style format strings
- Use string.Template for user-supplied templates where $name placeholders are safer

## Python features introduced
`str.format() positional and keyword fields`, `field access {0.attr} and {name[key]} in format`, `str.format_map()`, `%-formatting (printf style) %s %d %0.2f`, `string.Template`, `Template.substitute / safe_substitute`, `choosing among the formatting systems`

## MiniERP increment
Add `task.py` templating helpers for MiniERP document generation: `render_invoice_header(data)` uses str.format_map with a record dict, and `render_email(template, **vars)` uses string.Template.safe_substitute for user-editable notification templates (used later by the email/notification module).

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from string import Template

def render_invoice_header(data: dict) -> str:
    """Use str.format_map with keys like {customer} and {invoice_no}."""
    # TODO: "Invoice {invoice_no} for {customer}".format_map(data)
    raise NotImplementedError

def render_email(template: str, **vars: str) -> str:
    """Fill a $name Template, leaving unknown placeholders intact."""
    # TODO: Template(template).safe_substitute(vars)
    raise NotImplementedError
- **Test focus:** Tests verify format_map fills named fields (and raises on missing keys), %-formatting equivalence, and that safe_substitute leaves unknown $placeholders untouched while filling known ones.

</div>
