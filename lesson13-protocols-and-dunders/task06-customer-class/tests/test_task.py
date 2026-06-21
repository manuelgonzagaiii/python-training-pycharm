"""Check for task06-customer-class.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestCustomer(unittest.TestCase):
    def test_valid(self):
        c = domain.Customer("C-1", "Ann", "ann@x.com")
        self.assertEqual((c.customer_id, c.name, c.email), ("C-1", "Ann", "ann@x.com"))

    def test_invalid_email_rejected(self):
        with self.assertRaises(ValueError):
            domain.Customer("C-1", "Ann", "not-an-email")

    def test_from_dict(self):
        c = domain.Customer.from_dict({"customer_id": "C-2", "name": "Bob", "email": "b@y.com"})
        self.assertEqual(c.name, "Bob")

    def test_equality_and_hash_on_id(self):
        a = domain.Customer("C-1", "Ann", "a@x.com")
        b = domain.Customer("C-1", "Annie", "annie@x.com")
        self.assertEqual(a, b)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual(len({a, b}), 1)

    def test_repr_and_str(self):
        c = domain.Customer("C-1", "Ann", "ann@x.com")
        self.assertIn("C-1", repr(c))
        self.assertIn("Ann", str(c))


if __name__ == "__main__":
    unittest.main()
