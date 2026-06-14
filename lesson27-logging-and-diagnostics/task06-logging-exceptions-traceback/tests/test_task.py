import unittest

# TODO(author): replace with real checks.
# Test focus: report_failure logs at ERROR with the exception's traceback; the returned string contains the chained cause and the ERPError code; non-ERP exceptions log as 'unhandled' without crashing the reporter.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
