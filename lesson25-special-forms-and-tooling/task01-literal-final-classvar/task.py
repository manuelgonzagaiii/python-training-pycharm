"""Literal, Final & ClassVar

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import Literal, Final, ClassVar
from dataclasses import dataclass

Status = Literal['draft', 'sent', 'paid', 'void']

@dataclass
class Invoice:
    TAX_RATE: ClassVar[Final[float]] = 0.12
    number: str
    status: Status = 'draft'
    def can_transition(self, to: Status) -> bool:
        # TODO: match self.status / to against allowed transitions
        ...
"""

# Your code here.
