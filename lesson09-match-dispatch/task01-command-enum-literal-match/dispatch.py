"""MiniERP command dispatcher, built on structural pattern matching.

One match statement is MiniERP's front door: it turns a raw command -- a token
list from the CLI, or a JSON-style dict from the web layer -- into a typed request
object the pricing layer can execute. The module is self-contained; it builds
request objects but does not import the pricing rules (that wiring arrives with
the packaging phase).
"""
from enum import StrEnum


class Command(StrEnum):
    """The verbs MiniERP understands. StrEnum (Python 3.11+) makes each member a
    real string, so Command.ADD == 'add' and it prints as 'add' -- ideal for a CLI.
    """
    ADD = "add"
    PRICE = "price"
    DISCOUNT = "discount"
    REPORT = "report"
    HELP = "help"


def normalize_verb(token: str) -> Command:
    """Map a raw command word to a Command, defaulting anything unknown to HELP.

    A match statement compares `token` against each case top to bottom. The
    literal patterns (case "add":) match an exact value; the wildcard `_` at the
    end matches everything left over, which is how the default is expressed.
    """
    match token:
        case "add":
            return Command.ADD
        case "price":
            return Command.PRICE
        case "discount":
            return Command.DISCOUNT
        case "report":
            return Command.REPORT
        case _:
            return Command.HELP
