"""Check for task02-argv-sequence-patterns.

Grading policy: validity, not wording.
"""

import unittest

import dispatch


class TestParseTokens(unittest.TestCase):
    def test_empty_is_help(self):
        self.assertEqual(dispatch.parse_tokens([]), (dispatch.Command.HELP, []))

    def test_bare_verb(self):
        self.assertEqual(dispatch.parse_tokens(["report"]), (dispatch.Command.REPORT, []))

    def test_verb_with_args(self):
        cmd, args = dispatch.parse_tokens(["price", "A-1", "3"])
        self.assertEqual(cmd, dispatch.Command.PRICE)
        self.assertEqual(args, ["A-1", "3"])

    def test_single_arg_captured_as_list(self):
        cmd, args = dispatch.parse_tokens(["add", "A-1"])
        self.assertEqual(cmd, dispatch.Command.ADD)
        self.assertEqual(args, ["A-1"])


if __name__ == "__main__":
    unittest.main()
