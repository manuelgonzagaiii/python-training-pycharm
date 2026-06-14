"""Type-based dispatch: singledispatch & singledispatchmethod

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from functools import singledispatch, singledispatchmethod

@singledispatch
def render(obj):
    """Default: serialize any domain object to a dict row."""
    raise TypeError(f"no renderer for {type(obj).__name__}")

@render.register
def _(obj: Invoice):
    # TODO: return a dict row for an Invoice
    ...

# TODO: also register Product, Payment; then build an Exporter using singledispatchmethod

"""

# Your code here.
