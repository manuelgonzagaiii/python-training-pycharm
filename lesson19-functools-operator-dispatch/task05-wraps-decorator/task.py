"""Writing a well-behaved decorator with wraps

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from functools import wraps

def audited(func):
    @wraps(func)                     # preserves name, doc, __wrapped__
    def wrapper(*args, **kwargs):
        # TODO: append a record of (func.__name__, args, kwargs) to the audit log
        result = func(*args, **kwargs)
        return result
    return wrapper

"""

# Your code here.
