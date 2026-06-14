import unittest

# TODO(author): replace with real checks.
# Test focus: Blocking calls run off-loop (the loop stays responsive to other tasks during the call), results match the direct sync call, and CPU-bound work runs in a separate process.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
