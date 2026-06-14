import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm pyproject configures pytest, that new tests use plain assert (not self.assert*), and that pytest.raises and pytest.approx are each used against real domain behavior, with the whole suite green under `pytest`.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
