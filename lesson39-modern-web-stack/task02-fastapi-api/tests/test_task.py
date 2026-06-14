import unittest

# TODO(author): replace with real checks.
# Test focus: Use FastAPI's TestClient (httpx-backed) to GET /products (200 list), POST a valid product (201, matches response_model), POST an invalid one (422 from validation), and GET an unknown product id (404).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
