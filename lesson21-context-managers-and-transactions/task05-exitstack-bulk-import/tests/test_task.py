import unittest

# TODO(author): replace with real checks.
# Test focus: All files are read and aggregated; if one path is bad, previously opened handles are still closed (no leaked files); cleanup callbacks fire in reverse order.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
