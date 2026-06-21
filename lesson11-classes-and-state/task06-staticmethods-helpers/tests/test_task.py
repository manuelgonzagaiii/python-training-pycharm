"""Check for task06-staticmethods-helpers.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestIsValidSku(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(domain.Product.is_valid_sku("A-001"))
        self.assertTrue(domain.Product.is_valid_sku("AB12"))

    def test_invalid(self):
        self.assertFalse(domain.Product.is_valid_sku(""))
        self.assertFalse(domain.Product.is_valid_sku("bad sku"))   # space
        self.assertFalse(domain.Product.is_valid_sku("nope!"))     # punctuation

    def test_callable_without_instance(self):
        # a staticmethod is reachable on the class itself
        self.assertTrue(domain.Product.is_valid_sku("X-1"))


if __name__ == "__main__":
    unittest.main()
