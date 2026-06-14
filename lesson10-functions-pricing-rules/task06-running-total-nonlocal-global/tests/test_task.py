import unittest

# TODO(author): replace with real checks.
# Test focus: Successive add() calls accumulate via nonlocal; record_pricing_call increments the module global across calls; omitting nonlocal/global would rebind locally (covered by the contrast in tests).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
