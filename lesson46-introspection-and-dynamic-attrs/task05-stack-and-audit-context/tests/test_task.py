import unittest

# TODO(author): replace with real checks.
# Test focus: Tests caller_site(1) reports the function that called the helper (not the helper itself) with correct function name and a plausible lineno; tests that increasing depth walks further up; ensures no frame objects leak (via gc check).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
