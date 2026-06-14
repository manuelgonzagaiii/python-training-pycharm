import unittest

# TODO(author): replace with real checks.
# Test focus: Tests verify: (1) canonical_key normalizes whitespace+case AND returns an interned object such that canonical_key('usd') is canonical_key(' USD ') is True (identity, not just ==); (2) count_distinct_objects collapses equal interned keys (e.g. the 5-element raw currency list yields exactly 2 distinct ids after canonicalization, vs >2 without interning verified by a control list of non-interned f-string-built copies); (3) LedgerEntry.__post_init__ canonicalizes both sku and currency so two entries with raw 'sku-1'/'SKU-1' share the same interned objects (assert e1.sku is e2.sku); (4) group_amounts_by_currency sums correctly and its result keys are the interned canonicals; (5) benchmark_is_vs_eq returns a dict with both timing keys as positive floats and performs equal comparison counts (smoke test, not a timing assertion to stay deterministic on CI). A note in tests asserts that interning is idempotent: sys.intern(canonical_key(x)) is canonical_key(x).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
