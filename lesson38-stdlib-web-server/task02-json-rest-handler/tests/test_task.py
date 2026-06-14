import unittest

# TODO(author): replace with real checks.
# Test focus: Start make_server on port 0 in a thread, then use the Lesson-1 urllib client to GET /products (200 + JSON list), GET an unknown id (404), and POST a new product (201 + body echo); assert it actually appears via a follow-up GET.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
