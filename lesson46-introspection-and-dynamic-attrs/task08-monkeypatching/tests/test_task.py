import unittest

# TODO(author): replace with real checks.
# Test focus: Tests patched swaps a module-level function and a class method, that calls inside the block see the new behavior, and the original is restored after the block even on exception; tests the not-previously-set attribute case is removed on exit.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
