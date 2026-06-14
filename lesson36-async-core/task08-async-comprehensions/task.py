"""Async comprehensions: streaming reports from an async repository

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: """MiniERP — async reporting over the async customer repository (p13).

Earlier in this phase you built an async repository (`__aiter__`/`__anext__`,
async generators, `async for`). Now turn the reporting layer async using
*async comprehensions*: `[... async for ...]`, `{... async for ...}`,
`{k: v async for ...}`, and `await` expressions *inside* a comprehension.

Key scoping rule: a comprehension that contains `async for` (or `await`) is
only legal inside an `async def`. The same code in a plain `def` is a
SyntaxError. Each report function below is therefore a coroutine.

Implement the four functions marked TODO. Run `tests/test_task.py` to check.
"""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from decimal import Decimal

type CustomerId = int
type Region = str


@dataclass(slots=True, frozen=True)
class Customer:
    id: CustomerId
    name: str
    region: Region
    active: bool = True


# --- The data source: an async repository (recap from earlier in p13) ------
# `stream()` is an async generator. It yields one Customer at a time, awaiting
# between "pages" to simulate paginated / network-backed I/O. You consume it
# with `async for` inside your async comprehensions.
class AsyncCustomerRepo:
    def __init__(self, rows: list[Customer], page_size: int = 2) -> None:
        self._rows = list(rows)
        self._page_size = page_size

    async def stream(self) -> AsyncIterator[Customer]:
        for i, row in enumerate(self._rows):
            if i and i % self._page_size == 0:
                await asyncio.sleep(0)  # yield to the loop at each page boundary
            yield row


# --- An async payments gateway stub: balance(id) is a coroutine ------------
class PaymentGateway:
    def __init__(self, balances: dict[CustomerId, Decimal]) -> None:
        self._balances = balances

    async def balance(self, customer_id: CustomerId) -> Decimal:
        await asyncio.sleep(0)  # simulate an async lookup
        return self._balances.get(customer_id, Decimal("0.00"))


# --------------------------------------------------------------------------- #
# Reports — implement these with ASYNC COMPREHENSIONS.
# --------------------------------------------------------------------------- #

async def active_customer_ids(repo: AsyncCustomerRepo) -> set[CustomerId]:
    """Return the set of ids of active customers.

    Use a SET comprehension driven by `async for`, with an `if` filter:
        {c.id async for c in repo.stream() if c.active}
    """
    # TODO: replace with a `{... async for ... if ...}` comprehension
    raise NotImplementedError


async def customers_by_region(repo: AsyncCustomerRepo) -> dict[Region, list[str]]:
    """Return region -> sorted list of customer names in that region.

    Build it by consuming the repo with `async for` (a dict/loop comprehension
    over the stream, or an async comprehension that collects (region, name)
    pairs). Names within a region must be sorted.
    """
    # TODO: use `async for` to gather rows, then group by region
    raise NotImplementedError


async def outstanding_balances(
    repo: AsyncCustomerRepo, gateway: PaymentGateway
) -> list[tuple[CustomerId, Decimal]]:
    """For each ACTIVE customer, fetch their live balance from the gateway.

    Use an `await` expression INSIDE a list comprehension that is itself
    driven by `async for`:
        [(c.id, await gateway.balance(c.id)) async for c in repo.stream() if c.active]
    Order must follow the stream order.
    """
    # TODO: list comprehension with `await ...` as the element expr + `async for`
    raise NotImplementedError


async def total_outstanding(
    repo: AsyncCustomerRepo, gateway: PaymentGateway
) -> Decimal:
    """Sum every active customer's outstanding balance into a single Decimal."""
    # TODO: reuse outstanding_balances(...) and sum the balances
    raise NotImplementedError


def _demo_data() -> tuple[AsyncCustomerRepo, PaymentGateway]:
    rows = [
        Customer(1, "Acme", "EU", active=True),
        Customer(2, "Globex", "EU", active=False),
        Customer(3, "Initech", "US", active=True),
        Customer(4, "Umbrella", "US", active=True),
        Customer(5, "Soylent", "APAC", active=True),
    ]
    gateway = PaymentGateway({1: Decimal("120.50"), 3: Decimal("0.00"), 4: Decimal("75.00"), 5: Decimal("10.25")})
    return AsyncCustomerRepo(rows), gateway


async def _main() -> None:
    repo, gateway = _demo_data()
    print("active ids :", sorted(await active_customer_ids(repo)))
    print("by region  :", await customers_by_region(repo))
    print("balances   :", await outstanding_balances(repo, gateway))
    print("total      :", await total_outstanding(repo, gateway))


if __name__ == "__main__":
    asyncio.run(_main())

"""

# Your code here.
