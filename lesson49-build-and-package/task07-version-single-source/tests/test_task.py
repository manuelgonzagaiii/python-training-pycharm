import unittest

# TODO(author): replace with real checks.
# Test focus: get_version() returns a PEP 440/SemVer string matching pyproject; parse_version splits MAJOR.MINOR.PATCH correctly and rejects malformed input; PackageNotFoundError path returns a sane fallback; __version__ is exported.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
