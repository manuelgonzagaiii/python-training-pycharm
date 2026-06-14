# Type-based dispatch: singledispatch & singledispatchmethod

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.7 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build an open, type-dispatched serializer with singledispatch
- Register handlers for Product, Invoice, Payment without if/elif chains
- Provide a sensible default for unknown types
- Use singledispatchmethod for the same pattern inside a class

## Python features introduced
`functools.singledispatch`, `@func.register by type`, `register with type annotations`, `default/base implementation`, `functools.singledispatchmethod`, `dispatch on first argument type`, `operator.attrgetter in handlers`

## MiniERP increment
Deliver the Import/Export serialization layer: a singledispatch render() that converts each domain type (Product, Invoice, Payment, Customer) into an export row, plus a singledispatchmethod-based Exporter so new types register without touching existing code — completing the streaming-export story end to end.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import singledispatch, singledispatchmethod

@singledispatch
def render(obj):
    """Default: serialize any domain object to a dict row."""
    raise TypeError(f"no renderer for {type(obj).__name__}")

@render.register
def _(obj: Invoice):
    # TODO: return a dict row for an Invoice
    ...

# TODO: also register Product, Payment; then build an Exporter using singledispatchmethod

- **Test focus:** render dispatches to the right handler per type (Invoice/Product/Payment); the default raises for unregistered types; registration by annotation works; singledispatchmethod variant dispatches correctly inside the class.

</div>
