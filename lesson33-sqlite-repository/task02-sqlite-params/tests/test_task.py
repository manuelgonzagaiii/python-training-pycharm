import unittest

# TODO(author): replace with real checks.
# Test focus: Parametrized insert stores values correctly; a malicious sku string like "x'); DROP TABLE products;--" is stored literally and the table survives; executemany inserts N rows in one call.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
