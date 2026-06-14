# SKU Value Object & Dataclass Introspection

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.8 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Inspect a dataclass at runtime with fields() and read field metadata
- Serialize a dataclass with asdict()/astuple() and understand recursion into nested dataclasses
- Use default_factory for mutable defaults (e.g. tags list)
- Destructure a dataclass in match/case using its auto-generated __match_args__

## Python features introduced
`dataclasses.fields()`, `dataclasses.asdict / astuple`, `field(default_factory=...)`, `field(compare=False) / field(metadata=...)`, `dataclass __match_args__`, `match/case destructuring a dataclass`

## MiniERP increment
Adds SKU (code + checksum) and shows generic serialization of any value object via asdict, which the future Import/Export module will reuse. Establishes the introspection helpers (to_dict) used across the domain.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass, field, fields, asdict


@dataclass(frozen=True, slots=True)
class SKU:
    code: str
    tags: tuple[str, ...] = field(default_factory=tuple, compare=False)

    def __post_init__(self) -> None:
        # TODO: validate code is non-empty alphanumeric; normalize to upper-case
        ...


def describe(value) -> dict:
    # TODO: use match/case to recognize SKU/Money/Address, else asdict()
    ...

- **Test focus:** SKU validates/normalizes code, equality ignores tags (compare=False), asdict serializes nested value objects, describe() destructures via match/case and falls back to asdict.

</div>
