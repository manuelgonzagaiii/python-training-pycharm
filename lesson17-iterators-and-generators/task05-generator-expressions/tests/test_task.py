import unittest

# TODO(author): replace with real checks.
# Test focus: lines_for_sku returns a lazy generator (not a list) that filters correctly; revenue_total returns the right float; confirm no intermediate list is materialized (e.g. result is a generator/uses sum over a gen-expr).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
