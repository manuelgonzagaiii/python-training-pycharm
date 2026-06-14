# Legacy comparators: bridge old-style ordering with functools.cmp_to_key

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.11 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand the pre-Python-3 two-argument comparison protocol: a function f(a, b) returning a negative number, zero, or a positive number, and why Python 3 dropped the cmp= parameter from sort/sorted.
- Use functools.cmp_to_key to adapt such a comparator into a key object so it works with sorted(), list.sort(), min(), max(), and heapq.
- Recognise the situations where cmp_to_key is the *only* clean tool: orderings that are inherently pairwise (the relative order of two items depends on comparing them directly) and cannot be collapsed into one key= expression.
- Write the canonical sign expression (a > b) - (a < b) to turn any total order into a correct -1/0/+1 result, and chain several tie-break rules inside one comparator with early returns.
- Contrast a cmp_to_key comparator with the equivalent key= tuple, and articulate when each is appropriate (key= is faster and preferred when expressible; cmp_to_key when it is not).

## Python features introduced
`functools.cmp_to_key`, `old-style 3-way comparison functions (-1/0/+1 contract)`, `list.sort(key=...) and sorted(key=...)`, `the (n - m > 0) - (n - m < 0) sign trick as a cmp expression`, `tuple unpacking in comparator bodies`, `match/case to classify a comparison result into LESS/EQUAL/GREATER`, `datetime.date arithmetic for ageing`, `why some orderings are pairwise and cannot be written as a single key=`, `decimal.Decimal in comparisons`, `functools (recap: this module already gave us reduce, partial, lru_cache, total_ordering, singledispatch)`

## MiniERP increment
Adds a collections / dunning worklist ordering to the Reporting module. MiniERP already has Invoice records (with customer, amount due as Decimal, issue/due dates) and the ledger from earlier phases. This stage adds reporting/dunning.py with order_dunning_worklist(invoices, today) that returns the open invoices sorted into the exact priority a collections clerk works them: most overdue first, but with the business's real, legacy tie-break chain — (1) more days past due ranks higher; (2) on equal age, a larger Decimal balance ranks higher; (3) on equal age and balance, an account flagged 'priority' (VIP/contract) ranks higher than a standard account; (4) finally, ascending invoice number for stable, repeatable output. The rules were inherited as a single 2-argument comparator dunning_cmp(a, b) ported from the old VB/COBOL system; the learner keeps that pairwise comparator intact and bridges it to sorting via functools.cmp_to_key rather than rewriting it. This wires real, business-meaningful ordering into the reporting layer that the CLI 'erp dunning' report and later the web/UI worklists consume.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** """reporting/dunning.py - order the collections (dunning) worklist.

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

- **Test focus:** Verify order_dunning_worklist produces the exact clerk priority order and that dunning_cmp obeys the 3-way contract. Concrete checks: (1) dunning_cmp returns a value <0 / ==0 / >0 (assert the sign, not an exact magnitude) for representative pairs covering each rule; (2) self-comparison dunning_cmp(x, x, today=...) == 0; (3) two invoices differing only in days_past_due order most-overdue first; (4) equal age, different Decimal balances -> larger balance first (use Decimal literals to confirm no float drift); (5) equal age and balance, one priority=True -> it comes first; (6) full equality except invoice number -> ascending number; (7) a 6-8 invoice fixture exercising all four tie-breaks at once yields one deterministic expected list of invoice numbers; (8) order_dunning_worklist must not mutate the input list (pass a list, assert it is unchanged) and must return a new list; (9) sanity check that the result equals sorted(...) using functools.cmp_to_key with the same comparator (confirms the bridge was used correctly). Antisymmetry spot-check: sign(dunning_cmp(a, b)) == -sign(dunning_cmp(b, a)).

</div>
