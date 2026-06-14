import unittest

# TODO(author): replace with real checks.
# Test focus: Round-trip correctness and the detect_types mechanics. Tests open an in-memory connection via open_connection(':memory:'). (1) WRITE+READ via PARSE_DECLTYPES: CREATE TABLE t(price MONEY, due DATE, ts DATETIME); INSERT a Decimal('19.99'), a date, and a datetime bound to '?' placeholders; SELECT back and assert each returned value is isinstance Decimal/date/datetime AND equals the original (not a str, not a float). (2) PARSE_COLNAMES path: SELECT a plain TEXT column aliased as 'x [MONEY]' and assert it comes back as Decimal, proving the colname converter route. (3) Fidelity: assert Decimal('19.99') survives exactly (no 19.989999... float drift) and a datetime with microseconds round-trips. (4) Assert register_erp_sqlite_types() is idempotent (calling it twice does not error and the round-trip still holds). (5) Negative: a connection opened WITHOUT detect_types returns the raw str for the same column, confirming detect_types is what activates the converters.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
