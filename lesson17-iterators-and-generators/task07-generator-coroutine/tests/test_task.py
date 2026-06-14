import unittest

# TODO(author): replace with real checks.
# Test focus: Coroutine must be primed; each send(amount) returns the correct running total; throw() surfaces an injected error; close() triggers the GeneratorExit/finally path without raising.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
