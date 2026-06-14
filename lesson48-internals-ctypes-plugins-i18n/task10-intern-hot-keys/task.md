# Interning Hot Keys for Fast Identity Comparison

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.10 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why two equal strings produced at runtime (e.g. parsed from a CSV or built by concatenation) are usually NOT the same object, so `is` can be False even when `==` is True
- Use sys.intern to canonicalize a string so every equal occurrence becomes the exact same object, enabling correct and fast `is` comparison
- Measure the speedup of identity (`is`) comparison over equality (`==`) on a large number of repeated keys with time.perf_counter, and articulate when interning pays off (many repeats, long shared prefixes, hot comparison loops)
- State the cost: interned strings are never garbage-collected, so interning unbounded user input is a memory leak; intern only a bounded set of hot keys
- Connect interning to dict/set performance: interned keys can short-circuit hash-collision resolution via pointer identity

## Python features introduced
`sys.intern`, `the str interning protocol and the small/literal auto-intern caveat`, `object identity vs equality: the is operator vs ==`, `id() and CPython object identity`, `interning user-supplied (non-auto-interned) strings to force a single canonical object`, `dict/set membership and hashing with interned keys`, `time.perf_counter for micro-benchmark timing`, `weak vs strong references implication: interned strings live forever (gc/memory caveat)`, `f-string '=' self-documenting debugging for benchmark output`, `@dataclass(slots=True) field normalization in __post_init__`

## MiniERP increment
Adds a key-canonicalization layer to MiniERP's in-memory indexes. Many ERP records share a small, bounded vocabulary of repeated string keys: product SKUs, currency codes, account/ledger codes, warehouse/location codes, and audit-event names. When records are loaded (parsed from CSV/JSON import), these keys are distinct string objects per row, wasting memory and forcing full character-by-character `==` on every lookup. This task introduces `core/interning.py` with `canonical_key(value: str) -> str` that strips/upper-cases and `sys.intern`s the result, plus a `CanonicalKey` mixin used by the inventory and ledger indexes so that grouping records by SKU or currency uses interned canonical keys. A small benchmark function demonstrates the `is`-vs-`==` speedup on the loaded dataset. This makes the Reporting/Analytics grouping passes (group-by-SKU, group-by-currency) faster and lower-memory without changing any public behavior.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** """core/interning.py - canonical, interned keys for MiniERP hot lookups.

Many ERP records repeat a small, bounded set of string keys (SKUs,
currency codes, ledger codes). Strings parsed at runtime are distinct
objects even when equal, so `==` does full character comparison and the
same text is stored many times. Interning collapses every equal key to
one canonical object, letting hot loops compare with `is` and saving
memory. Interned strings are never collected, so only intern a BOUNDED
vocabulary of hot keys -- never raw, unbounded user input.
"""

from __future__ import annotations

import sys
import time
from collections.abc import Iterable
from dataclasses import dataclass, field


def canonical_key(value: str) -> str:
    """Normalize and intern a hot lookup key.

    Normalization: strip surrounding whitespace and upper-case (SKUs and
    currency codes are case-insensitive in MiniERP). Then sys.intern the
    result so every equal key becomes the SAME object.

    Returns the interned, canonical string. For two inputs that normalize
    to equal text, `canonical_key(a) is canonical_key(b)` must be True.
    """
    # TODO: normalize (strip + upper) then return sys.intern(...) of it.
    raise NotImplementedError


def count_distinct_objects(keys: Iterable[str]) -> int:
    """Return how many DISTINCT objects (by id) appear in keys.

    With interned canonical keys, many equal strings collapse to one
    object, so this count drops sharply versus the raw parsed strings.
    """
    # TODO: use a set of id(k) for k in keys, return its length.
    raise NotImplementedError


@dataclass(slots=True)
class LedgerEntry:
    """One posting in MiniERP's ledger. sku and currency are hot keys."""

    sku: str
    currency: str
    amount_cents: int

    def __post_init__(self) -> None:
        # TODO: replace self.sku and self.currency with their canonical_key
        # so every LedgerEntry shares one interned object per distinct key.
        raise NotImplementedError


def group_amounts_by_currency(entries: Iterable[LedgerEntry]) -> dict[str, int]:
    """Sum amount_cents per currency. Keys are already interned canonicals."""
    # TODO: accumulate totals into a dict keyed by entry.currency.
    raise NotImplementedError


def benchmark_is_vs_eq(key: str, haystack: list[str], rounds: int = 200_000) -> dict[str, float]:
    """Micro-benchmark identity (is) vs equality (==) against haystack.

    All of haystack and key should be interned canonicals for `is` to be
    valid. Returns {\"eq_seconds\": ..., \"is_seconds\": ...} using
    time.perf_counter. Both loops must do the same number of comparisons.
    """
    # TODO: time `== key` over haystack `rounds` times, then `is key`.
    raise NotImplementedError


if __name__ == "__main__":
    raw = [" usd ", "USD", "usd", "Eur", "EUR "]
    keys = [canonical_key(r) for r in raw]
    print(f"{count_distinct_objects(keys)=}")  # expect 2 (USD, EUR)
    same = canonical_key("usd") is canonical_key(" USD ")
    print(f"{same=}")  # expect True

- **Test focus:** Tests verify: (1) canonical_key normalizes whitespace+case AND returns an interned object such that canonical_key('usd') is canonical_key(' USD ') is True (identity, not just ==); (2) count_distinct_objects collapses equal interned keys (e.g. the 5-element raw currency list yields exactly 2 distinct ids after canonicalization, vs >2 without interning verified by a control list of non-interned f-string-built copies); (3) LedgerEntry.__post_init__ canonicalizes both sku and currency so two entries with raw 'sku-1'/'SKU-1' share the same interned objects (assert e1.sku is e2.sku); (4) group_amounts_by_currency sums correctly and its result keys are the interned canonicals; (5) benchmark_is_vs_eq returns a dict with both timing keys as positive floats and performs equal comparison counts (smoke test, not a timing assertion to stay deterministic on CI). A note in tests asserts that interning is idempotent: sys.intern(canonical_key(x)) is canonical_key(x).

</div>
