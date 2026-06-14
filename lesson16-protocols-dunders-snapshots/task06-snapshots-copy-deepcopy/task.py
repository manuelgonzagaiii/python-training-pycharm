"""Snapshots: copy, deepcopy & custom hooks

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import copy


class Invoice:
    def __init__(self, number: str) -> None:
        self.number = number
        self.lines: list = []

    def __deepcopy__(self, memo: dict) -> "Invoice":
        # TODO: build a clone; use copy.deepcopy(self.lines, memo)
        # and register self in memo to handle shared references
        ...

    def snapshot(self) -> "Invoice":
        return copy.deepcopy(self)

"""

# Your code here.
