# Async comprehensions: streaming reports from an async repository

> **Phase:** Concurrency, Parallelism & Async  •  **Stage:** 36.8 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write list, set, and dict comprehensions driven by `async for` over an async iterator instead of a plain `for`
- Use an `await` expression as the element expression of a comprehension to call a per-item coroutine (e.g. an async pricing/enrichment service)
- Add an `if` filter clause to an async comprehension and understand it runs once per yielded item
- Recognize that `[... async for ...]` is only valid inside an `async def` (or, since 3.11, an async REPL) — and explain why a plain `def` raises `SyntaxError`
- Distinguish an async *list* comprehension (eagerly materializes) from an async *generator expression* (lazy, itself an async iterator)
- Reuse the async repository / async generator built earlier in this phase as the data source
- Choose the comprehension form (list vs set vs dict) that matches the report shape

## Python features introduced
`async comprehensions: list comprehension with async for ([row async for row in repo])`, `set comprehension with async for ({c.id async for c in repo})`, `dict comprehension with async for ({k: v async for k, v in repo})`, `await expression inside a comprehension ([await enrich(r) async for r in repo])`, `filtering an async comprehension with an if clause evaluated per item`, `combining async for and a nested sync for in one comprehension`, `async generator expressions ((x async for x in repo)) passed to async consumers`, `asynchronous generator functions with yield (__aiter__/__anext__ recap)`, `async def coroutine functions and await`, `asyncio.run as the event-loop entry point`, `scoping rule: a comprehension's async for makes the *enclosing* function a coroutine context (only legal inside async def)`, `collections.abc.AsyncIterator / AsyncIterable typing`, `PEP 695 type alias + PEP 604 unions in async signatures`

## MiniERP increment
Adds an async reporting layer to MiniERP that reads from the async repository introduced earlier in p13. In `reports/async_reports.py` the learner implements report builders that consume `AsyncCustomerRepo.stream()` (an async generator yielding Customer rows page-by-page, simulating paginated/network-backed I/O). They write: (1) `active_customer_ids(repo)` returning a *set* via `{c.id async for c in repo if c.active}`; (2) `customers_by_region(repo)` returning a *dict* `region -> [names]` built from a dict/loop comprehension over `async for`; (3) `outstanding_balances(repo, gateway)` which uses an `await` expression inside a list comprehension — `[(c.id, await gateway.balance(c.id)) async for c in repo if c.active]` — to fetch each active customer's live balance from an async PaymentGateway stub concurrently with iteration; and (4) `total_outstanding(repo, gateway)` reducing that report to a single `Decimal`. This turns the previously-blocking export/report code into an async pipeline that streams over the repository, the foundation the Web (FastAPI) and Reporting modules build on in later phases.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** """MiniERP — async reporting over the async customer repository (p13).

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

- **Test focus:** Drive each coroutine with `asyncio.run`. Verify: (1) `active_customer_ids` returns exactly the active-customer id set `{1, 3, 4, 5}` and is a `set` (excludes inactive id 2). (2) `customers_by_region` returns `{'EU': ['Acme'], 'US': ['Initech', 'Umbrella'], 'APAC': ['Soylent']}` with names sorted within each region. (3) `outstanding_balances` returns active customers in stream order with balances awaited from the gateway: `[(1, Decimal('120.50')), (3, Decimal('0.00')), (4, Decimal('75.00')), (5, Decimal('10.25'))]`, and skips inactive id 2. (4) `total_outstanding` equals `Decimal('205.75')` and is a `Decimal`. Add a white-box check that the implementations actually use async comprehensions: `inspect.getsource` of `outstanding_balances` contains both `async for` and `await`, and `active_customer_ids` contains `async for` inside `{...}`. Add a guard test proving the scoping rule: `compile('[x async for x in xs]', '<t>', 'exec')` succeeds while wrapping the same in a plain `def` body raises `SyntaxError` (so learners see `async for` in a comprehension forces a coroutine context). Use a fresh repo instance per assertion since the async generator is single-pass.

</div>
