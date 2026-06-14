"""Memory with tracemalloc & bytecode with dis

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import tracemalloc
import dis
from erp.reporting import revenue_by_category, revenue_by_category_streaming
from erp.testdata import make_sales

tracemalloc.start()
revenue_by_category(list(make_sales(50_000)))
print('list peak', tracemalloc.get_traced_memory()[1])
# TODO: snapshot.compare_to for streaming version; dis.dis(both)

"""

# Your code here.
