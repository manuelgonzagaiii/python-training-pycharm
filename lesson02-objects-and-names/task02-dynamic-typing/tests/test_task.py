"""Check for stage 2: dynamic typing via describe().

Grading policy: describe() is a debugging helper, so its exact
wording is the learner's choice. The rule we enforce is that the result reports two
true facts about the value: its repr and its type name. Any phrasing that contains
both passes.
"""

import unittest

import main


class TestDescribe(unittest.TestCase):
    def _check(self, value):
        result = main.describe(value)
        self.assertIsInstance(result, str, "describe() must return a string.")
        self.assertIn(repr(value), result, "describe() should include the value's repr (use !r).")
        self.assertIn(
            type(value).__name__,
            result,
            "describe() should include the type name from type(value).__name__.",
        )

    def test_describes_an_int(self):
        self._check(42)

    def test_describes_a_str(self):
        self._check("x")

    def test_describes_none(self):
        # None's type name is 'NoneType'; this proves one name handled many types.
        self._check(None)

    def test_describes_a_float_and_list(self):
        self._check(3.5)
        self._check(["a", "b"])


if __name__ == "__main__":
    unittest.main()
