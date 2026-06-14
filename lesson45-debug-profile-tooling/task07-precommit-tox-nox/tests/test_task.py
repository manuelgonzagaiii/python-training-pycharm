import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm a valid .pre-commit-config.yaml (with ruff + a formatter + a type hook), and a tox.ini and/or noxfile.py defining ordered lint/type/test sessions; the grader runs the test session and confirms the assembled gate passes on the now clean, typed, covered MiniERP codebase.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
