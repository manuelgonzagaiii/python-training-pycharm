import unittest

# TODO(author): replace with real checks.
# Test focus: Concurrent tasks each see their own user/request_id (no leakage), reset restores the prior value after the scope, and the audit log records the correct acting user per request.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
