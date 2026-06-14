"""Custom JSON: JSONEncoder & object_hook

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import json
from decimal import Decimal
from datetime import datetime

class ERPEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return {'_type': 'Decimal', 'value': str(o)}
        ...  # datetime, dataclasses
        return super().default(o)

def erp_object_hook(d: dict):
    ...  # rebuild based on d.get('_type')

"""

# Your code here.
