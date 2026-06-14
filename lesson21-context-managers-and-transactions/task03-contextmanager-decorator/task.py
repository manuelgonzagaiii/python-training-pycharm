"""Generator-based Managers with @contextmanager

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from contextlib import contextmanager
from collections.abc import Iterator

current_actor: str = "system"

@contextmanager
def switch_actor(name: str) -> Iterator[str]:
    global current_actor
    previous = current_actor
    current_actor = name
    try:
        yield name
    finally:
        # TODO: restore current_actor = previous
        ...
"""

# Your code here.
