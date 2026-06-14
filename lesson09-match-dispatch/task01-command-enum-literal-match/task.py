"""Literal and Capture Patterns

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from enum import StrEnum


class Command(StrEnum):
    ADD = "add"
    PRICE = "price"
    DISCOUNT = "discount"
    REPORT = "report"
    HELP = "help"


def normalize_verb(token: str) -> Command:
    """Map a raw token to a Command via match/case; unknown -> HELP."""
    match token.strip().lower():
        case "add":
            return Command.ADD
        case _:
            ...
"""

# Your code here.
