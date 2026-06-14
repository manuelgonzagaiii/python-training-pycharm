# Role Permissions with IntFlag

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Model combinable permissions with enum.IntFlag and compose them with bitwise OR
- Test for a granted permission with & and the in operator
- Understand why Flag values are powers of two and how auto() supplies them
- Contrast IntFlag (combinable) with IntEnum (single value) and StrEnum

## Python features introduced
`enum.IntFlag`, `enum.Flag`, `bitwise combination (| & ^ ~)`, `auto() for power-of-two flags`, `membership test (in)`, `Flag.NONE / boolean truthiness of flags`, `enum.IntEnum contrast`

## MiniERP increment
Adds Permission (READ, WRITE, REFUND, MANAGE_USERS, EXPORT) for the Users & Roles module. Roles will be expressed as combined IntFlag values, ready for the later auth/audit features.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from enum import IntFlag, auto


class Permission(IntFlag):
    NONE = 0
    READ = auto()
    WRITE = auto()
    REFUND = auto()
    MANAGE_USERS = auto()
    EXPORT = auto()

    # TODO: define class-level role constants, e.g.
    # CLERK = READ | WRITE  ;  ADMIN = everything
    def grants(self, needed: "Permission") -> bool:
        # TODO: return True if self contains all bits in `needed`
        ...

- **Test focus:** Combining flags with | works, grants() checks containment with &, ADMIN grants every permission, NONE is falsy, a flag value is a power of two.

</div>
