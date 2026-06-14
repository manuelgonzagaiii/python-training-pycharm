"""@transaction via __enter__/__exit__ (MILESTONE)

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import copy
from types import TracebackType

class Transaction:
    def __init__(self, repo: "Repository") -> None:
        self.repo = repo
        self._snapshot: object | None = None
    def __enter__(self) -> "Repository":
        self._snapshot = copy.deepcopy(self.repo.state)
        return self.repo
    def __exit__(self, exc_type: type[BaseException] | None,
                 exc: BaseException | None, tb: TracebackType | None) -> bool:
        # TODO: if exc_type is not None: restore self.repo.state from snapshot
        #       always clear snapshot; return False to propagate
        ...
"""

# Your code here.
