import unittest

# TODO(author): replace with real checks.
# Test focus: Tests confirm an @audited function still returns the right value, that the audit record is written, and that *args/**kwargs forwarding preserves behavior; a signature check (inspect.signature / wraps) confirms the wrapper mirrors the original.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
