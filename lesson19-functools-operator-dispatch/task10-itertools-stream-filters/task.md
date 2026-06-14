# Shaping report streams: takewhile, dropwhile, filterfalse, compress, starmap, zip_longest

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.10 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use `starmap` to apply a multi-argument function over records that are already tuples, instead of `map` + a lambda that unpacks
- Build a boolean selector with a generator expression and use `compress` to keep only the elements whose mask is truthy
- Reach for `filterfalse(pred, it)` to get the *complement* of `filter(pred, it)` without writing `not pred(x)`
- Slice a *sorted* stream by value using `takewhile` (stop at the first failure) and `dropwhile` (skip a leading run, keep the rest) — and explain why they differ from `filter`
- Align two unequal-length series for period-over-period comparison with `zip_longest(..., fillvalue=...)`, choosing a safe fill value
- Recognise that all of these return lazy one-shot iterators and decide when to materialise with `list()`/`tuple()`

## Python features introduced
`itertools.takewhile`, `itertools.dropwhile`, `itertools.filterfalse`, `itertools.compress`, `itertools.starmap`, `itertools.zip_longest`, `operator.mul / operator module callables`, `lazy iterators vs. eager list materialisation`, `predicate functions and the complement pattern (filter vs filterfalse)`, `boolean selector masks (generator expression feeding compress)`, `argument-unpacking map (starmap vs map) over tuple records`, `fill values and sentinel handling with zip_longest's fillvalue`, `consuming one-shot iterators exactly once`

## MiniERP increment
Adds a stream-shaping toolkit to the Reporting module (`minierp/reporting/streams.py`) that operates on the invoice and ledger data built in earlier Sales & Invoicing stages. Concretely the learner implements: (1) `line_totals(lines)` using `starmap` with `operator.mul` to turn `(sku, qty, unit_price)` line records into per-line subtotals; (2) `select_taxable(lines, taxable_mask)` using `compress` to keep only flagged lines, and `nontaxable(lines, pred)` using `filterfalse` to report the complement set; (3) `entries_before(ledger, cutoff)` / `entries_from(ledger, cutoff)` using `takewhile`/`dropwhile` over a date-sorted audit ledger to split opening balances from the reporting window; (4) `compare_periods(this_period, last_period)` using `zip_longest(fillvalue=Decimal('0'))` to align two monthly revenue series of different lengths into aligned `(month, current, prior, delta)` rows for a variance report. These functions become reusable building blocks the later Reporting/Analytics and Import/Export stages call when generating revenue and tax summaries.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** unittest.TestCase covering each function on small fixtures. line_totals: assert starmap result equals [qty*price...] as Decimals and that it is a lazy iterator (next() works, second pass is empty). select_taxable: mask [True,False,True] keeps lines 0 and 2; verify a too-short mask stops early (compress semantics) and a generator-expression mask works. nontaxable: complement of a predicate matches expected lines and equals the set difference vs filter. entries_before/entries_from on a date-sorted ledger: takewhile stops at first >= cutoff (won't include a later out-of-cutoff entry even if it would pass filter), dropwhile keeps the tail including any value, and concatenation of the two reconstructs the whole ledger. compare_periods: unequal lengths (this longer than last and vice versa) produce rows padded with Decimal('0'), correct delta = current - prior, and 1-based/0-based month index as specified. Include one assertion that filterfalse/takewhile differ from filter on a non-monotonic sequence to lock in the conceptual distinction.

</div>
