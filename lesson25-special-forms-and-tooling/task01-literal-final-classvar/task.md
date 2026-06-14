# Literal, Final & ClassVar

> **Phase:** Modern Type System  •  **Stage:** 25.1 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Restrict a value to a closed set with Literal['draft', 'sent', 'paid'] and exhaustively match it
- Mark constants immutable to the checker with Final (module-level, class attribute, and inferred)
- Declare class-level (not per-instance) attributes with ClassVar so dataclasses treat them correctly
- Decide when Literal beats a StrEnum and when it does not

## Python features introduced
`typing.Literal`, `typing.Final`, `typing.ClassVar`, `StrEnum vs Literal trade-off`, `exhaustive match over Literal`, `module-level and attribute Final constants`

## MiniERP increment
Invoice status becomes Literal['draft' | 'sent' | 'paid' | 'void']; the dataclass gets ClassVar registries (e.g. valid transitions) and Final defaults (TAX_RATE: Final = ...). Status transitions are checked exhaustively, hardening the Sales/Invoicing module.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import Literal, Final, ClassVar
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
- **Test focus:** Tests exercise legal/illegal status transitions and confirm TAX_RATE application; a check inspects annotations to confirm status is a Literal and TAX_RATE is ClassVar/Final, and that an invalid literal would be a (documented) type error.

</div>
