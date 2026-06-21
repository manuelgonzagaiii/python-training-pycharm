"""Check for task04-order-class-patterns.

Grading policy: validity, not wording.
"""

import unittest

import dispatch


class TestDescribe(unittest.TestCase):
    def test_add_request_positional(self):
        # distinguishable values so a swapped binding -- AddRequest(qty, sku) -- is
        # caught, not merely that both values appear somewhere in the summary
        s = dispatch.describe(dispatch.AddRequest("SKU9", 7))
        self.assertIn("SKU9", s)
        self.assertIn("7", s)
        self.assertLess(s.index("7"), s.index("SKU9"))  # qty precedes sku in "add {qty} x {sku}"

    def test_price_request_keyword(self):
        s = dispatch.describe(dispatch.PriceRequest("A-1", 2))
        self.assertIn("price", s)
        self.assertIn("A-1", s)

    def test_discount_request(self):
        s = dispatch.describe(dispatch.DiscountRequest([1, 2]))
        self.assertIn("discount", s)
        self.assertIn("2", s)

    def test_unknown(self):
        self.assertEqual(dispatch.describe(object()), "unknown request")

    def test_dataclasses_have_fields(self):
        self.assertEqual(dispatch.AddRequest("A-1", 3).qty, 3)
        self.assertEqual(dispatch.PriceRequest("A-1", 2).sku, "A-1")


if __name__ == "__main__":
    unittest.main()
