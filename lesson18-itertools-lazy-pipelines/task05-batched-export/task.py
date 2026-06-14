"""Chunked streaming export with batched

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from itertools import batched
import csv, io

def export_csv_chunks(rows, header, batch_size=100):
    """Yield CSV text one batch at a time (header first), for streaming export."""
    buf = io.StringIO(); w = csv.writer(buf)
    w.writerow(header)
    for batch in batched(rows, batch_size):
        # TODO: write each row in the batch, then yield+clear the buffer's text
        ...

"""

# Your code here.
