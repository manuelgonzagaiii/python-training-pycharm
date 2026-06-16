"""Check for stage 9: warehouse bin coordinates as complex numbers.

Grading policy: validity, not wording. We check the geometry against
hand-computed values.
"""

import unittest

import geo


class TestGeo(unittest.TestCase):
    def test_make_location(self):
        loc = geo.make_location(3, 4)
        self.assertEqual(loc, 3 + 4j)
        self.assertIsInstance(loc.real, float, ".real is always float")
        self.assertIsInstance(loc.imag, float, ".imag is always float")

    def test_coordinates(self):
        self.assertEqual(geo.coordinates(3 + 4j), (3.0, 4.0))

    def test_travel_distance_is_345(self):
        self.assertEqual(geo.travel_distance(1 + 2j, 4 + 6j), 5.0)  # classic 3-4-5

    def test_midpoint(self):
        self.assertEqual(geo.midpoint(0 + 0j, 4 + 6j), 2 + 3j)

    def test_nearest_bin(self):
        dock = 0 + 0j
        bins = [10 + 0j, 1 + 1j, 5 + 5j]
        self.assertEqual(geo.nearest_bin(dock, bins), 1 + 1j)


if __name__ == "__main__":
    unittest.main()
