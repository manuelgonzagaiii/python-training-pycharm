import unittest

# TODO(author): replace with real checks.
# Test focus: Console handler is INFO-level, file handler DEBUG-level; a DEBUG record reaches the file but not the console; formatted output contains level, logger name, and message; repeat calls don't duplicate handlers.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
