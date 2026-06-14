"""Endless and concatenated streams: count, cycle, chain

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from itertools import count, chain

def numbered_stream(*ledgers):
    """Yield (row_no, line) starting at row 1, across all ledgers, lazily."""
    combined = chain(*ledgers)            # one lazy stream over every ledger
    # TODO: pair each line with an incrementing row number from count(1)
    ...

"""

# Your code here.
