import unittest

# TODO(author): replace with real checks.
# Test focus: Decimal and datetime survive dumps(cls=ERPEncoder) -> loads(object_hook=erp_object_hook) unchanged; unknown types still raise TypeError; a full Product round-trips losslessly.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
