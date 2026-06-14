import unittest

# TODO(author): replace with real checks.
# Test focus: Concrete subclasses auto-register under the right key; the abstract base does NOT register; __prepare__'s namespace preserves declaration order; instances are correct isinstance of base and metaclass type.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
