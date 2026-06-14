import unittest

# TODO(author): replace with real checks.
# Test focus: Verify bytes(Money(amount=12345, currency="USD")) returns a bytes object of length exactly 12 (struct.calcsize("!B3sq")), that its first byte is the version tag 1, and that bytes 1..4 decode to b"USD". Assert the round-trip invariant Money.from_bytes(bytes(m)) == m across several amounts including negative (e.g. -500 for a refund) and zero. Confirm from_bytes raises ValueError on a record whose version byte is not 1, and that supplying a wrong-length buffer raises struct.error. Include a check that bytes(m) is an instance of bytes (not bytearray) so a __bytes__ returning the wrong type would fail. Optionally assert the encoding is deterministic (two equal Money objects produce identical bytes).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
