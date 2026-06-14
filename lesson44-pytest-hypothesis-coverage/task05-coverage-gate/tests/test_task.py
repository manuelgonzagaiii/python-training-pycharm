import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm coverage is configured in pyproject with branch + fail_under, and that the newly added test covers the specific previously-missing branch in the reporting code (i.e. coverage of that module increases) while the suite stays green.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
