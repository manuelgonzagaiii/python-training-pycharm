import unittest

# TODO(author): replace with real checks.
# Test focus: Point fetch_json at a local ThreadingHTTPServer fixture returning JSON and assert the dict parses; start a server that returns 404/500 and assert PriceFeedError is raised; assert a custom Accept header reaches the server.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
