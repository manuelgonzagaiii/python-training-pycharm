import unittest

# TODO(author): replace with real checks.
# Test focus: Tests chunk returns memoryview slices that are views (mutating the bytearray is visible through them) of the right lengths; tests totals_buffer produces an array whose memoryview reports the expected nbytes/format for handing to ctypes.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
