"""How @property Works Underneath

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: # Theory page. Shows the equivalence:
#
#   class Invoice:
#       @property
#       def total(self): return sum(l.amount for l in self.lines)
#
# is roughly:
#   def _total(self): ...
#   total = property(_total)   # a data descriptor instance on the class
#
# plus a cached_property contrast (non-data: instance dict shadows it).
"""

# Your code here.
