# Executable documentation with doctest

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 43.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Turn usage examples in docstrings into tests that fail when the docs go stale
- Control fragile output with ELLIPSIS and NORMALIZE_WHITESPACE
- Document and test exception-raising behavior in a docstring
- Integrate doctests into the unittest run with the load_tests protocol so one command runs both

## Python features introduced
`doctest module`, `writing >>> examples in docstrings`, `doctest directives: # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE, +SKIP`, `doctest.testmod / running python -m doctest -v`, `load_tests protocol to fold doctests into the unittest suite via doctest.DocTestSuite`, `exception examples (Traceback ... lines) in doctests`

## MiniERP increment
Add worked >>> examples to the public docstrings of the money/pricing helpers and the Invoice summary method in the domain layer, making each example self-verifying. Wire a load_tests hook in tests/test_doctests.py so `python -m unittest discover` also runs every domain doctest, giving MiniERP living, checked documentation.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # In erp/money.py:
def money(value):
    '''Return a 2dp Decimal amount.

    >>> money('10') + money('2.5')
    Decimal('12.50')
    >>> money('x')
    Traceback (most recent call last):
        ...
    ValueError: not a valid amount: 'x'
    '''
    ...
# In tests/test_doctests.py: use doctest.DocTestSuite + load_tests

- **Test focus:** Checks confirm at least one domain module gained passing >>> examples (including an exception example and one directive), and that the load_tests protocol successfully surfaces the doctests to the unittest runner.

</div>
