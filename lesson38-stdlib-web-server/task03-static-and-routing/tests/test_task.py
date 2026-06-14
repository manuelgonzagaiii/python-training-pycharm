import unittest

# TODO(author): replace with real checks.
# Test focus: Assert render_products escapes a malicious name like '<script>' so it cannot inject markup; assert parse_form decodes name=Widget&price=9.99 into the right dict; GET the UI page through the server and assert it returns text/html with the product name present.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
