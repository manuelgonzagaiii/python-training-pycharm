import unittest

# TODO(author): replace with real checks.
# Test focus: Unit-test each function against hand-computed values: make_location(3, 4) == (3+4j) and its .real/.imag are 3.0/4.0 (assert they are float, not int); coordinates((3+4j)) == (3.0, 4.0); travel_distance((1+2j), (4+6j)) == 5.0 (the classic 3-4-5 triangle) and travel_distance is symmetric (a->b equals b->a) via abs() of the conjugate-related displacement; midpoint((1+2j),(3+6j)) == (2+4j); a .conjugate() check asserting abs(z) == abs(z.conjugate()); and nearest_bin returns the correct closest bin given a dock at the origin and several candidate bins (including a tie-break sanity case and a single-element iterable). Also assert that complex coordinates carry float parts even when built from ints, and that round(travel_distance(...), 2) formats as expected for an irrational distance like abs(1+1j).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
