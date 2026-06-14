import unittest

# TODO(author): replace with real checks.
# Test focus: Tests apply_patch leaves MISSING fields untouched while applying None/real values; asserts MISSING is not None and is its own type; tests Money.__eq__ returns NotImplemented (checked via the internal op or comparison fallback) for non-Money and equality works between Money instances.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
