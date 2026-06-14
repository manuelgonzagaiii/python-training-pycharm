import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm the skip condition is computed (not hard-coded True/False), that an expectedFailure marker exists, and that `python -m unittest discover` collects every test module the lesson has produced so far.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
