"""Dynamic Manager Stacks with ExitStack

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from contextlib import ExitStack
from pathlib import Path
from collections.abc import Iterable

def bulk_import(paths: Iterable[Path]) -> list[str]:
    rows: list[str] = []
    with ExitStack() as stack:
        handles = [stack.enter_context(open(p)) for p in paths]
        # TODO: read each handle, extend rows; register stack.callback(...) for cleanup
        ...
    return rows
"""

# Your code here.
