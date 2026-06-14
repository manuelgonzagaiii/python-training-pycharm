import unittest

# TODO(author): replace with real checks.
# Test focus: mro_names returns the C3 order for a diamond (e.g. ['Invoice','Timestamped','Identified','Entity','object']), and cooperative __init__ runs each class exactly once in MRO order.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
