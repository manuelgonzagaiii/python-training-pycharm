"""Lazy attributes with cached_property

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from functools import cached_property

class Invoice:
    def __init__(self, lines):
        self.lines = list(lines)  # note: needs a normal __dict__, not slots-only

    @cached_property
    def total(self):
        """Sum line items once; cached on the instance thereafter."""
        # TODO: return sum(qty * unit_price for each line)
        ...

"""

# Your code here.
