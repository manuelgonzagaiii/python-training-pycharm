"""MiniERP command dispatcher, built on structural pattern matching.

One match statement is MiniERP's front door: it turns a raw command -- a token
list from the CLI, or a JSON-style dict from the web layer -- into a typed request
object the pricing layer can execute. The module is self-contained; it builds
request objects but does not import the pricing rules (that wiring arrives with
the packaging phase).
"""
from dataclasses import dataclass
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


def parse_tokens(tokens: list[str]) -> tuple[Command, list[str]]:
    """Split a token list into (command, args) using sequence patterns.

    Sequence patterns match by shape. [] matches an empty list. [verb] matches a
    list of exactly one, binding it to `verb`. [verb, *args] matches a non-empty
    list, binding the first element to `verb` and the rest to a new list `args`;
    because the [verb] case is tested first, this one effectively handles two-or-
    more.
    """
    match tokens:
        case []:
            return (Command.HELP, [])
        case [verb]:
            return (normalize_verb(verb), [])
        case [verb, *args]:
            return (normalize_verb(verb), args)


def classify_request(req: dict) -> tuple[str, dict]:
    """Pull the operation and its fields from a dict request via mapping patterns.

    A mapping pattern matches by key and ignores extra keys: {"op": "price",
    "sku": sku} matches any dict that HAS those two keys, binding `sku`. The
    `**rest` capture collects the remaining keys into a dict. This lets JSON-style
    web payloads flow through the same routing the CLI uses.
    """
    match req:
        case {"op": "price", "sku": sku, **rest}:
            return ("price", {"sku": sku, **rest})
        case {"op": "discount", **rest}:
            return ("discount", rest)
        case {"op": op, **rest}:
            return (op, rest)
        case _:
            return ("help", {})


@dataclass(slots=True)
class AddRequest:
    sku: str
    qty: int


@dataclass(slots=True)
class PriceRequest:
    sku: str
    qty: int


@dataclass(slots=True)
class DiscountRequest:
    rules: list


def describe(req: object) -> str:
    """Render a one-line summary of a typed request using class patterns.

    A class pattern such as PriceRequest(sku=s, qty=q) checks the type AND extracts
    fields. The positional form, AddRequest(sku, qty), relies on the class's
    __match_args__, which @dataclass fills in from the field order -- this is why
    these dataclasses are not keyword-only (kw_only would leave __match_args__
    empty and the positional pattern would not match).
    """
    match req:
        case AddRequest(sku, qty):
            return f"add {qty} x {sku}"
        case PriceRequest(sku=s, qty=q):
            return f"price {q} x {s}"
        case DiscountRequest(rules=rules):
            return f"discount with {len(rules)} rule(s)"
        case _:
            return "unknown request"
