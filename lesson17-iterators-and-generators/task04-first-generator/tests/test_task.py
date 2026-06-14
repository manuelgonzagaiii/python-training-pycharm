import unittest

# TODO(author): replace with real checks.
# Test focus: iter_lines is a generator function (returns a generator); yields lines lazily in order; calling it does not execute the body until next() is called; integrates so SalesLedger stays multi-pass.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
