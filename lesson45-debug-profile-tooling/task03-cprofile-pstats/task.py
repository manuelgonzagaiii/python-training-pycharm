"""Finding the bottleneck: cProfile, pstats & a measured fix

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import cProfile, pstats
from erp.reporting import generate_report
from erp.testdata import make_sales

cProfile.run('generate_report(make_sales(20_000))', 'report.prof')
stats = pstats.Stats('report.prof').strip_dirs().sort_stats('cumulative')
stats.print_stats(10)
# TODO: optimize revenue_by_category, keep results identical, re-profile

"""

# Your code here.
