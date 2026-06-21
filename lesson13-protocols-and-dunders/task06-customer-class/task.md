# Stage 6: the Customer domain class

This stage is a consolidation. Instead of one new concept, you build a whole domain class —
`Customer` — that brings together everything the phase has covered: a constructor, a property
with validation, value equality and hashing, an alternate constructor, and clean repr/str. It
replaces the loose customer dicts from earlier phases with a real object, completing the
Customers module's core.

## Pulling the pieces together

`Customer` holds an id, a name, and an email, with the email **validated** through a property
setter (a malformed address must never be stored):

```
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email          # validated by the setter

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError(f"invalid email: {value!r}")
        self._email = value
```

The rest is the toolkit you already have:

- A `from_dict` **classmethod** to build a Customer from a mapping (the import shape).
- **Value equality and hashing on `customer_id`** — two records for the same customer id are
  the same customer, and hashing on the id lets customers live in sets and dict keys. (Remember
  the pairing rule: define `__eq__` and `__hash__` together.)
- A `__repr__` (developer, eval-able-ish) and `__str__` (`"Ann <ann@x.com>"` for people).

Identity here is the **customer id**, not the name or email — those can change, the id cannot.
Choosing the right identifying field for equality and hashing is a modelling decision, and
getting it wrong (hashing on a mutable field like email) is a real bug, which is why the check
keys on the id.

## Your task

In `domain.py`, finish two pieces of `Customer`:

1. the `email` setter — reject an address with no `@` (raise `ValueError`), otherwise store it
   in `self._email`.
2. `__eq__` — two customers are equal when their `customer_id`s match.

The `from_dict` factory, `__hash__`, `__repr__`, and `__str__` are provided.

## Worked example

```
>>> import domain
>>> c = domain.Customer("C-1", "Ann", "ann@x.com")
>>> c.email
'ann@x.com'
>>> domain.Customer("C-1", "Ann", "not-an-email")
Traceback (most recent call last):
ValueError: invalid email: 'not-an-email'
>>> a = domain.Customer("C-1", "Ann", "a@x.com")
>>> b = domain.Customer("C-1", "Annie", "annie@x.com")   # same id, different details
>>> a == b, len({a, b})
(True, 1)
```

## What the check verifies, and what it leaves to you

- Enforced: a missing-`@` email raises `ValueError`; a valid customer round-trips; `from_dict`
  builds one; equality and hashing key on `customer_id` (so same-id customers are equal and
  collapse in a set); repr/str surface the fields.
- Your free choice: the email rule beyond "must contain `@`", the exception message, and the
  repr/str layout are yours. The identity field (the id) is fixed because the rest of the
  system relies on it.

<div class="hint" title="If you are stuck">

Email setter: `if "@" not in value: raise ValueError(...)`, then `self._email = value` (store
in the backing attribute). `__eq__`: `self.customer_id == other.customer_id`.

</div>

Reference: Python documentation, "Classes", "@property", and "Data model — object.__eq__ /
__hash__" at docs.python.org.
