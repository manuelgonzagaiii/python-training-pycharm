import unittest

# TODO(author): replace with real checks.
# Test focus: TaxRule instances are callable and compute tax, UnitOfWork commits buffered changes on clean exit and discards them when an exception propagates, __exit__ returns False so exceptions are not swallowed, parenthesized with-block works.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
