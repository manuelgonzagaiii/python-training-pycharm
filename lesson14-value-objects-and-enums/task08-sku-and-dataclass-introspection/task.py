"""SKU Value Object & Dataclass Introspection

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from dataclasses import dataclass, field, fields, asdict


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

"""

# Your code here.
