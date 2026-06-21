"""Check for task10-slots-weakref.

Grading policy: validity, not wording.
"""

import unittest

import domain


import gc
import weakref


class TestRegistry(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()

    def test_product_weakly_referenceable(self):
        p = domain.Product("W-1", "X", 1)
        ref = weakref.ref(p)  # works only because "__weakref__" is in __slots__
        self.assertIs(ref(), p)

    def test_registry_returns_canonical(self):
        reg = domain.ProductRegistry()
        p = domain.Product("R-1", "X", 1)
        self.assertIs(reg.canonical(p), p)
        self.assertIs(reg.get("R-1"), p)

    def test_dropped_product_evicted(self):
        reg = domain.ProductRegistry()
        p = domain.Product("E-1", "X", 1)
        reg.canonical(p)
        domain.Product._instances.clear()
        del p
        gc.collect()
        self.assertIsNone(reg.get("E-1"))


if __name__ == "__main__":
    unittest.main()
