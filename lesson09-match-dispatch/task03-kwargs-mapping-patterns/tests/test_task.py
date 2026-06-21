"""Check for task03-kwargs-mapping-patterns.

Grading policy: validity, not wording.
"""

import unittest

import dispatch


class TestClassifyRequest(unittest.TestCase):
    def test_price_extracts_sku(self):
        op, fields = dispatch.classify_request({"op": "price", "sku": "A-1", "qty": 2})
        self.assertEqual(op, "price")
        self.assertEqual(fields["sku"], "A-1")

    def test_discount(self):
        op, fields = dispatch.classify_request({"op": "discount", "rules": [1, 2]})
        self.assertEqual(op, "discount")

    def test_other_op_passes_through(self):
        op, _ = dispatch.classify_request({"op": "report"})
        self.assertEqual(op, "report")

    def test_no_op_is_help(self):
        op, _ = dispatch.classify_request({})
        self.assertEqual(op, "help")


if __name__ == "__main__":
    unittest.main()
