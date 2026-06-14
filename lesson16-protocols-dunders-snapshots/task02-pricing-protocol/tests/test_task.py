import unittest

# TODO(author): replace with real checks.
# Test focus: Strategies satisfy PricingStrategy without subclassing, isinstance(strategy, PricingStrategy) is True for runtime_checkable, each strategy quotes correctly, a non-conforming object fails the isinstance check.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
