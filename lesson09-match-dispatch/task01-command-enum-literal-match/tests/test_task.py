"""Check for task01-command-enum-literal-match.

Grading policy: validity, not wording.
"""

import unittest

import dispatch


class TestNormalizeVerb(unittest.TestCase):
    def test_known_verbs(self):
        self.assertEqual(dispatch.normalize_verb("add"), dispatch.Command.ADD)
        self.assertEqual(dispatch.normalize_verb("price"), dispatch.Command.PRICE)
        self.assertEqual(dispatch.normalize_verb("discount"), dispatch.Command.DISCOUNT)
        self.assertEqual(dispatch.normalize_verb("report"), dispatch.Command.REPORT)

    def test_unknown_defaults_to_help(self):
        self.assertEqual(dispatch.normalize_verb("frobnicate"), dispatch.Command.HELP)
        self.assertEqual(dispatch.normalize_verb(""), dispatch.Command.HELP)

    def test_strenum_is_a_string(self):
        self.assertEqual(dispatch.Command.ADD, "add")


if __name__ == "__main__":
    unittest.main()
