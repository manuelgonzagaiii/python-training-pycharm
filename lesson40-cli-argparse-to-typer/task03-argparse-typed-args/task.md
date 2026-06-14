# argparse: typed, validated arguments

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 40.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Add positional and optional arguments with type converters (int, Decimal, a custom SKU validator)
- Constrain values with choices= and validate with a callable that raises ArgumentTypeError
- Use store_true / count / append actions for flags, verbosity, and repeated values
- Pass cleanly-typed data into core service calls (e.g. add a product with name, price as Decimal, qty as int)

## Python features introduced
`add_argument(type=, choices=, default=, nargs=, metavar=)`, `custom type=callable converters`, `argparse.FileType`, `required keyword`, `action='store_true'/'append'/'count'`, `ArgumentTypeError`

## MiniERP increment
Add `products add --name --price --qty [--tag ...]` and `customers add`, with a custom Decimal/price converter and a SKU validator, so new records can be created from the terminal via the core service. `-v/-vv` controls log verbosity.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Give a price_arg(s)->Decimal converter raising ArgumentTypeError on bad input and a partially-built `add` subparser; learner finishes the arguments and the handler that calls create_product/create_customer.
- **Test focus:** Assert valid argv produces correctly-typed Namespace and the service is called with a Decimal price and int qty; assert invalid price/SKU raises SystemExit(2) from argparse; assert --tag appends and -vv sets count=2.

</div>
