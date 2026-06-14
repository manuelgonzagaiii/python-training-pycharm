import unittest

# TODO(author): replace with real checks.
# Test focus: Round-trip arbitrary bytes through to_b64/from_b64; urlsafe output contains no + or /; decoding malformed input raises binascii.Error; a struct blob survives embedding in and extraction from a dict.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
