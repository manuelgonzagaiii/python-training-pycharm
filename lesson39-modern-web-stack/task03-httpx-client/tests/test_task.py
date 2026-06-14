import unittest

# TODO(author): replace with real checks.
# Test focus: Wire ERPClient against the FastAPI app via httpx ASGITransport; assert list_products/create_product round-trip, raise_for_status raises on a 404, and an async variant using AsyncClient awaits correctly.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
