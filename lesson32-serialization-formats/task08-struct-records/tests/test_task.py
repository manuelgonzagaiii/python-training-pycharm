import unittest

# TODO(author): replace with real checks.
# Test focus: pack_row produces calcsize(REC.format)-length records; iter_unpack restores rows; sku padding is stripped on read; a memoryview slice exposes one record without copying; array.array round-trips numeric data.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
