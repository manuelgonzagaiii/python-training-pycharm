"""Legacy comparators: bridge old-style ordering with functools.cmp_to_key

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: """reporting/dunning.py - order the collections (dunning) worklist.

This stage continues the MiniERP guided project. Reuse the Invoice model and
Decimal money handling introduced in earlier phases.

The ordering rules below were ported verbatim from the company's legacy system
as a single TWO-ARGUMENT comparator. A 2-arg comparator returns a NEGATIVE
number if a should sort before b, ZERO if they tie, and a POSITIVE number if a
should sort after b. Python 3's sorted()/list.sort() no longer accept a `cmp=`
argument - they only take `key=`. functools.cmp_to_key is the standard bridge:
it wraps a 2-arg comparator into a key object.

DO NOT rewrite dunning_cmp as a key= tuple. The point of this task is to keep a
legacy pairwise comparator intact and adapt it. (As an exercise, parts of this
chain ARE key-expressible - but treat the comparator as a black box you must
bridge.)
"""
from __future__ import annotations

import functools
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class Invoice:
    number: int            # invoice number, unique, used as final stable tie-break
    customer: str
    balance: Decimal       # amount still due
    due: date              # date the invoice was due
    priority: bool = False # True for VIP / contract accounts


def days_past_due(invoice: Invoice, today: date) -> int:
    """How many days overdue (negative if not yet due)."""
    return (today - invoice.due).days


def dunning_cmp(a: Invoice, b: Invoice, *, today: date) -> int:
    """Legacy 2-arg comparator. Return <0, 0, or >0 (a vs b).

    Priority chain (first difference wins):
      1. MORE days past due sorts FIRST.
      2. else LARGER balance sorts FIRST.
      3. else priority account sorts FIRST (True before False).
      4. else SMALLER invoice number sorts FIRST (stable, repeatable).

    TODO: implement using the sign expression (x > y) - (x < y) for each rule,
    returning as soon as a rule produces a non-zero result. Remember rules 1-3
    are 'bigger first' (descending) so you must flip the sign.
    """
    # Your code here.
    raise NotImplementedError


def order_dunning_worklist(invoices, today: date) -> list[Invoice]:
    """Return invoices ordered for the collections clerk.

    TODO: use functools.cmp_to_key to adapt dunning_cmp (which needs `today`)
    into a key= for sorted(). functools.partial or a small lambda/closure will
    help bind `today`.
    """
    # Your code here.
    raise NotImplementedError

"""

# Your code here.
