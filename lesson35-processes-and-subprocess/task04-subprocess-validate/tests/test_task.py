import unittest

# TODO(author): replace with real checks.
# Test focus: A clean CSV passes (return code 0, parsed report), a malformed CSV raises/returns a structured failure, a hanging command hits the timeout, and arguments are passed as a list (no shell).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
