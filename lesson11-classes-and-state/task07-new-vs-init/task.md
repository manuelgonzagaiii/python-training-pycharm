# Stage 7: __new__ versus __init__ — who builds the object

Every Python object is created in **two** steps, and so far you have only seen the second
one. `__new__` **allocates** the object (decides which object exists); `__init__`
**initializes** it (fills in its fields). Almost always you only write `__init__` and let
Python's default `__new__` quietly make a fresh object. This stage lifts the lid, because
overriding `__new__` lets you do something `__init__` never can: decide to return an
*existing* object instead of a new one.

## The two-step protocol

When you call `Product("A-001", "Widget", 999)`:

1. Python calls `Product.__new__(cls, "A-001", "Widget", 999)`. Its job is to produce an
   instance and return it. The default implementation, `super().__new__(cls)`, allocates a
   fresh blank object.
2. Python then calls `__init__(self, ...)` on whatever `__new__` returned, to set its
   attributes.

The key fact: **`__new__` chooses the object**. If it returns an object that already exists,
`__init__` runs on that existing object instead of a new one.

## Interning: one canonical Product per SKU

MiniERP wants exactly one Product object per SKU, so that a price edit or stock change made
through one reference is seen everywhere. A small cache in `__new__` delivers that:

```
    _instances = {}

    def __new__(cls, sku, name, price_cents):
        if sku in cls._instances:
            return cls._instances[sku]          # hand back the existing object
        instance = super().__new__(cls)         # allocate a new blank object
        cls._instances[sku] = instance
        return instance
```

The first time a SKU is seen, `__new__` allocates and remembers it; later calls with the same
SKU return the **same** object (verified with `is`). This pattern is called **interning** —
the same idea Python uses internally for small integers and short strings. `__init__` still
runs each time and sets the fields, which is why the docstring notes the two methods cooperate
rather than compete.

A caution worth stating: this simple cache holds every Product forever (a strong reference), so
it would slowly leak memory in a long-running program. A later lesson replaces it with a
weak-reference registry that lets unused products be collected. Here the plain dict keeps the
mechanism visible.

## Your task

In `domain.py`, finish `Product.__new__`:

1. when the SKU is already cached, return the existing instance, and
2. otherwise allocate a new bare instance via the base class.

The cache bookkeeping (`cls._instances[sku] = instance`) is written for you.

## Worked example

```
>>> import domain
>>> a = domain.Product("A-001", "Widget", 999)
>>> b = domain.Product("A-001", "Renamed", 100)   # same SKU
>>> a is b                                         # the very same object
True
>>> c = domain.Product("B-010", "Gizmo", 250)      # different SKU
>>> a is c
False
```

## What the check verifies, and what it leaves to you

- Enforced: two constructions with the same SKU return the *same* object (`is`); different
  SKUs return distinct objects; `__init__` still runs so fields are set.
- Your free choice: the cache attribute name and structure are the provided scaffold; what you
  write is the interning decision — return the cached instance, or allocate via
  `super().__new__(cls)`. Any equivalent allocation passes.

<div class="hint" title="If you are stuck">

Return `cls._instances[sku]` on a cache hit. Allocate a new object with
`super().__new__(cls)` — note `object.__new__` takes only the class, none of the other
arguments.

</div>

Reference: Python documentation, "Data model — object.__new__ and object.__init__" at
docs.python.org.
