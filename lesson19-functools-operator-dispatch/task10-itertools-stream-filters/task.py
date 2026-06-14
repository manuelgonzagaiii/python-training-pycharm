"""Shaping report streams: takewhile, dropwhile, filterfalse, compress, starmap, zip_longest

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
from collections.abc import Callable, Iterable, Iterator
from decimal import Decimal
from itertools import compress, dropwhile, filterfalse, starmap, takewhile, zip_longest
from operator import mul

# An invoice line is a tuple record: (sku, qty, unit_price)
type Line = tuple[str, int, Decimal]
# A ledger entry is (iso_date, amount); the ledger is sorted ascending by date.
type Entry = tuple[str, Decimal]


def line_totals(lines: Iterable[Line]) -> Iterator[Decimal]:
    """Per-line subtotal qty*unit_price. Use starmap so the (qty, price)
    columns are passed positionally to operator.mul (ignore the sku column)."""
    # TODO: starmap(mul, ...) over (qty, unit_price) pairs.
    ...


def select_taxable(lines: Iterable[Line], taxable_mask: Iterable[bool]) -> Iterator[Line]:
    """Keep only lines whose parallel mask value is truthy. Use compress."""
    ...


def nontaxable(lines: Iterable[Line], is_taxable: Callable[[Line], bool]) -> Iterator[Line]:
    """The complement of filter(is_taxable, lines). Use filterfalse, not `not`."""
    ...


def entries_before(ledger: Iterable[Entry], cutoff: str) -> Iterator[Entry]:
    """Opening run: entries strictly before cutoff. Ledger is date-sorted, so
    use takewhile to stop at the first entry that reaches the cutoff."""
    ...


def entries_from(ledger: Iterable[Entry], cutoff: str) -> Iterator[Entry]:
    """Reporting window: drop the leading run before cutoff with dropwhile,
    keep everything from the cutoff onward."""
    ...


def compare_periods(
    this_period: Iterable[Decimal], last_period: Iterable[Decimal]
) -> Iterator[tuple[int, Decimal, Decimal, Decimal]]:
    """Align two monthly revenue series of possibly different lengths into
    (month_index, current, prior, delta) rows. Use zip_longest with a
    Decimal('0') fillvalue so a missing month is treated as zero."""
    ...

"""

# Your code here.
