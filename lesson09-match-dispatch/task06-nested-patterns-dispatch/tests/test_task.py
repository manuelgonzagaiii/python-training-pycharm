"""Check for task06-nested-patterns-dispatch.

Grading policy: validity, not wording.
"""

import unittest

import dispatch


class TestDispatch(unittest.TestCase):
    def test_add_token_list(self):
        self.assertEqual(dispatch.dispatch(["add", "A-1", "3"]),
                         dispatch.AddRequest("A-1", 3))

    def test_price_token_list(self):
        self.assertEqual(dispatch.dispatch(["price", "A-1", "2"]),
                         dispatch.PriceRequest("A-1", 2))

    def test_discount_mapping(self):
        self.assertEqual(dispatch.dispatch({"op": "discount", "rules": [1, 2]}),
                         dispatch.DiscountRequest([1, 2]))

    def test_passthrough_request_object(self):
        req = dispatch.PriceRequest("A-1", 1)
        self.assertIs(dispatch.dispatch(req), req)

    def test_unknown_is_help(self):
        self.assertEqual(dispatch.dispatch(["bogus"]), dispatch.Command.HELP)


if __name__ == "__main__":
    unittest.main()
