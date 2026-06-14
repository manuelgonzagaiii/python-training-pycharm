import unittest

# TODO(author): replace with real checks.
# Test focus: Catalog stores valid products and rejects invalid ones (empty sku or negative price/qty) by raising on __setitem__; valid inserts are retrievable via [] and `in`; the .data backing dict stays consistent.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
