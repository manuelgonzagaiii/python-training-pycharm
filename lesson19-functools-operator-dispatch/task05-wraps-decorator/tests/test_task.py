import unittest

# TODO(author): replace with real checks.
# Test focus: Decorated function keeps __name__/__doc__ (thanks to wraps) and exposes __wrapped__; the call is recorded to the audit log once; arguments and return value pass through unchanged.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
