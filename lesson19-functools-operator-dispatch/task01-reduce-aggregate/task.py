"""Folding a stream with reduce

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from functools import reduce
from operator import add

def grand_total(amounts):
    """Fold a stream of amounts into one total with reduce (safe on empty)."""
    # TODO: reduce with operator.add and an initializer of 0.0
    ...

def totals_by_sku(rows):
    """Reduce (sku, amount) rows into a {sku: subtotal} dict."""
    def step(acc, row):
        # TODO: add row's amount into acc[sku] and return acc
        ...
    return reduce(step, rows, {})

"""

# Your code here.
