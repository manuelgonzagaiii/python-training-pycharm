import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm a strict-ish mypy config and a py.typed marker exist, and that `mypy erp` reports zero errors after the learner's annotations/fixes (the suite verifies the previously-failing type defect is now correctly typed).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
