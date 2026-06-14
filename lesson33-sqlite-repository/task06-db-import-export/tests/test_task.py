import unittest

# TODO(author): replace with real checks.
# Test focus: Importing the same CSV twice upserts (no duplicate rows, second values win); export streams all rows via a generator; the whole import is atomic (failure midway rolls back).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
