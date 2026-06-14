import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm parametrize replaces at least one subTest table, that ids and a per-case xfail/skip are used, and that custom markers are registered in pyproject and applied to real tests selectable via -m.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
