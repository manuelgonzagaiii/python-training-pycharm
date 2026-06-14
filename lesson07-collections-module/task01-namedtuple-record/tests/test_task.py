import unittest

# TODO(author): replace with real checks.
# Test focus: ProductRecord allows name access and still unpacks/indexes as a 4-tuple; reprice returns a new record with only price_cents changed and qty/name/sku intact; _asdict round-trips the fields.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
