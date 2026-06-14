import unittest

# TODO(author): replace with real checks.
# Test focus: edu unit tests (unittest) that: (a) assert dft_bin of a constant series at k=1 is cmath.isclose to 0j and at k=0 equals N*mean; (b) feed a pure cosine season x_n = base + amp*cos(2*pi*n/12) and assert seasonal_strength recovers amp within tolerance and peak_month near 0/12; (c) shift the cosine by a quarter and assert the recovered peak_month shifts by ~3; (d) assert is_flat is True for a flat series and False for the seasonal one; (e) assert that math.sqrt(-1) raises ValueError while cmath.sqrt(-1) is cmath.isclose to 1j, and check abs()/.real/.conjugate() relationships (abs(z)**2 isclose (z*z.conjugate()).real). Use cmath.isclose with explicit abs_tol for all complex/float comparisons; avoid == on floats.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
