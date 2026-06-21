"""Check for task07-slots-optimization.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestSlots(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()

    def test_classes_define_slots(self):
        for cls in (domain.Money, domain.Product, domain.LineItem, domain.Customer):
            self.assertTrue(hasattr(cls, "__slots__"))

    def test_no_instance_dict(self):
        self.assertFalse(hasattr(domain.Money(100), "__dict__"))
        # Product is the class the learner slots, so check it directly: a slot list
        # that smuggles in "__dict__" would defeat the whole optimization
        self.assertFalse(hasattr(domain.Product("A-1", "W", 1), "__dict__"))

    def test_stray_attribute_rejected(self):
        with self.assertRaises(AttributeError):
            domain.Money(100).not_a_field = 1
        with self.assertRaises(AttributeError):
            domain.Product("A-1", "W", 1).not_a_field = 1

    def test_features_survive_slots(self):
        from decimal import Decimal
        p = domain.Product("A-1", "Widget", 1500)
        self.assertEqual(p.price_dollars, Decimal("15.00"))
        self.assertEqual(p.label(), "A-1 - Widget")
        p.discount_cents = 100
        self.assertEqual(p.discount_cents, 100)


if __name__ == "__main__":
    unittest.main()
