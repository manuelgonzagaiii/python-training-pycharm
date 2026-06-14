import unittest

# TODO(author): replace with real checks.
# Test focus: Tests pass a mix of Invoice/Payment-like objects (structurally matching) to grand_total and assert the summed Decimal; an isinstance(obj, SupportsTotal) check confirms @runtime_checkable behavior, and a shape-mismatch object is rejected.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
