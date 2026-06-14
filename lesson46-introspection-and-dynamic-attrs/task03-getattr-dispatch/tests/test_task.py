import unittest

# TODO(author): replace with real checks.
# Test focus: Tests public_callables excludes _private/__dunder and non-callable attributes; tests dispatch invokes the right method, passes kwargs through, raises LookupError for unknown/private/non-callable verbs.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
