import unittest

# TODO(author): replace with real checks.
# Test focus: Fragments run concurrently (total time near the slowest, not the sum), a timed-out fragment is reported as partial rather than failing the whole dashboard, and cancellation is handled.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
