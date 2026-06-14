import unittest

# TODO(author): replace with real checks.
# Test focus: Repeated calls with the same args hit the cache (cache_info hits increment, body runs once); cache_clear resets stats; distinct args miss then cache; verifies pure/hashable usage.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
