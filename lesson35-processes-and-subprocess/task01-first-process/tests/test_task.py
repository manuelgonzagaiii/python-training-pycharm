import unittest

# TODO(author): replace with real checks.
# Test focus: The computed result matches the in-thread version, runs in a distinct PID, and a deliberately failing job yields a non-zero exitcode.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
