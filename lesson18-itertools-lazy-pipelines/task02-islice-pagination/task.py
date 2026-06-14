"""Slicing lazy streams: islice for pagination

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from itertools import islice, tee

def page(stream, page_no, size):
    """Return the rows for a 1-based page from a lazy stream, using islice."""
    start = (page_no - 1) * size
    # TODO: islice the stream from start to start+size
    ...

def count_and_preview(stream, preview_n):
    """Use tee to get both a total count and the first preview_n rows."""
    # TODO: tee the stream into two independent iterators
    ...

"""

# Your code here.
