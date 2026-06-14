import unittest

# TODO(author): replace with real checks.
# Test focus: Each subclass is catchable as ERPError, exposes its own code, and carries its category-specific fields; narrow excepts select the right subclass without catching siblings.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
