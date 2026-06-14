import unittest

# TODO(author): replace with real checks.
# Test focus: Drive each coroutine with `asyncio.run`. Verify: (1) `active_customer_ids` returns exactly the active-customer id set `{1, 3, 4, 5}` and is a `set` (excludes inactive id 2). (2) `customers_by_region` returns `{'EU': ['Acme'], 'US': ['Initech', 'Umbrella'], 'APAC': ['Soylent']}` with names sorted within each region. (3) `outstanding_balances` returns active customers in stream order with balances awaited from the gateway: `[(1, Decimal('120.50')), (3, Decimal('0.00')), (4, Decimal('75.00')), (5, Decimal('10.25'))]`, and skips inactive id 2. (4) `total_outstanding` equals `Decimal('205.75')` and is a `Decimal`. Add a white-box check that the implementations actually use async comprehensions: `inspect.getsource` of `outstanding_balances` contains both `async for` and `await`, and `active_customer_ids` contains `async for` inside `{...}`. Add a guard test proving the scoping rule: `compile('[x async for x in xs]', '<t>', 'exec')` succeeds while wrapping the same in a plain `def` body raises `SyntaxError` (so learners see `async for` in a comprehension forces a coroutine context). Use a fresh repo instance per assertion since the async generator is single-pass.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
