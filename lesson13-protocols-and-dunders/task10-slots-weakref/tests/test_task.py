import unittest

# TODO(author): replace with real checks.
# Test focus: Verify (1) the fixed slotted Product can be weakly referenced: weakref.ref(product) succeeds and `'__weakref__'` is in Product.__slots__ (the class still uses slots, so setting an undeclared attribute still raises AttributeError); (2) ProductRegistry.canonical returns the *same* object (assertIs) for two equal Products sharing a SKU, and a later get(sku) returns that identical instance; (3) the registry does not keep Products alive — after dropping all strong refs and calling gc.collect(), get(sku) returns None and len shrinks (entry auto-evicted via the WeakValueDictionary); (4) a regression guard reproducing the gotcha: a sibling slotted class WITHOUT '__weakref__' raises TypeError when inserted into a WeakValueDictionary, with the message containing 'cannot create weak reference'; (5) a subclass of Product that adds its own slots but omits '__weakref__' is still weakrefable (inherited).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
