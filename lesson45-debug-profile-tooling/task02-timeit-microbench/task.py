"""Micro-benchmarking the hot path with timeit

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import timeit
from erp.reporting import revenue_by_category

setup = 'from erp.testdata import make_sales; sales = make_sales(10_000)'
best = min(timeit.repeat(
    stmt='revenue_by_category(sales)',
    setup=setup, repeat=5, number=10))
print(f'{best=:.4f}s')

"""

# Your code here.
