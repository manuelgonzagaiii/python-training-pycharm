import unittest

# TODO(author): replace with real checks.
# Test focus: @audit('x') records exactly one AuditEntry per call with the correct action and bound argument names; the wrapped function's return value is unchanged; metadata preserved via wraps.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
