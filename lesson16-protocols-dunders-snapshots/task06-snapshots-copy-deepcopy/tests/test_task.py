import unittest

# TODO(author): replace with real checks.
# Test focus: deepcopy of an Invoice produces independent line lists (mutating the copy doesn't touch the original), shallow copy shares the lines list (demonstrating the bug), __deepcopy__ uses memo, snapshot is independent of later edits.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
