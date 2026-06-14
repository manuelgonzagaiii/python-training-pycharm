import unittest

# TODO(author): replace with real checks.
# Test focus: Checks verify setUp creates per-test state (no leakage between tests), that subTest is used for the table, and that at least one assertLogs/assertAlmostEqual/assertRaisesRegex is exercised against the real invoicing code.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
