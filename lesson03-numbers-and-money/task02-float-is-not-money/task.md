# Why 0.1 + 0.2 != 0.3

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.2 of 7  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Internalize that binary float cannot represent most decimal fractions exactly
- Know that == on floats is unreliable and money must never be a float
- Recognize math.isclose as the tolerant comparison and why it is still wrong for currency

## Python features introduced
`float binary representation pitfalls`, `0.1 + 0.2 == 0.3 is False`, `math.isclose() for tolerant float comparison`, `float.is_integer()`, `float special values (float('inf'), float('nan'))`, `repr vs str of floats`

## MiniERP increment
Knowledge check that justifies the phase's central ERP decision (money uses Decimal). No code change; the correct mental model gates the Decimal refactor in later tasks.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice task. Learner evaluates statements such as:
#   - What does (0.1 + 0.2 == 0.3) evaluate to?
#   - Which is the right way to store a $19.99 price for an invoice?
#   - Is math.isclose() acceptable for deciding if an invoice is fully paid?
# Answers are encoded in the EduTools task config, not in task.py.
- **Test focus:** Choice task: a single correct option (float == is False; money must use Decimal; isclose is unsuitable for exact currency).

</div>
