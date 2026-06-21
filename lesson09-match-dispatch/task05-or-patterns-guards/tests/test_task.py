"""Check for task05-or-patterns-guards.

Grading policy: validity, not wording.
"""

import unittest

import dispatch


class TestRouteCommand(unittest.TestCase):
    def test_or_pattern_shares_handler(self):
        a = dispatch.route_command(dispatch.Command.HELP, [])
        b = dispatch.route_command(dispatch.Command.REPORT, [])
        self.assertEqual(a, b)

    def test_price_with_args(self):
        s = dispatch.route_command(dispatch.Command.PRICE, ["A-1", "2"])
        self.assertIn("2", s)

    def test_price_without_args_is_usage(self):
        s = dispatch.route_command(dispatch.Command.PRICE, [])
        self.assertNotEqual(s, dispatch.route_command(dispatch.Command.PRICE, ["A-1"]))
        self.assertIn("price", s.lower())

    def test_add_routes(self):
        s = dispatch.route_command(dispatch.Command.ADD, [])
        self.assertIn("add", s.lower())


if __name__ == "__main__":
    unittest.main()
