import unittest

# TODO(author): replace with real checks.
# Test focus: A successful with-block commits both updates; raising inside the block rolls back so neither update persists; a UNIQUE/PRIMARY KEY violation raises IntegrityError and leaves the table unchanged.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
