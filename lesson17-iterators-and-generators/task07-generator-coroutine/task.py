"""Generators as coroutines: send, throw, close

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: def running_total():
    """Coroutine: send() an amount, receive the running total back."""
    total = 0.0
    try:
        while True:
            amount = yield total      # value arrives via .send(amount)
            # TODO: add amount to total so the NEXT yield returns the new running total
            ...
    except GeneratorExit:
        # TODO: final cleanup/flush when .close() is called
        ...

"""

# Your code here.
