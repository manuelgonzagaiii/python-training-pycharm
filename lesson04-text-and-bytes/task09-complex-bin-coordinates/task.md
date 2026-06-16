# Stage 9: warehouse bin coordinates with complex numbers

Back in stage 1 you were told `complex` has no place in business arithmetic. That is true
for *money* — but a `complex` number is also just a **2-D point**, and that is genuinely
useful. A warehouse bin has a location (which aisle, which shelf), and Python's built-in
`complex` is a ready-made, immutable point with distance and midpoint built in. This stage
is a small standalone module, `geo.py`, of generic 2-D point math — distance, midpoint, and
nearest point — using a warehouse bin (which one is closest to the packing dock) as the
motivating example. A later inventory phase builds on it.

(This is a separate file from `text.py` on purpose — it is geometry, not text. It lives as
a flat module for now; it will move under the inventory package much later, in the
packaging phase.)

## A complex number is a point

`complex(x, y)` (or the literal `x + yj`) is a pair of floats you can do vector maths on:

- `.real` and `.imag` read the two components back — **always as `float`**, even if you
  passed ints.
- `b - a` is the **displacement vector** from `a` to `b`; `abs(...)` of a complex is its
  **magnitude**, so `abs(b - a)` is the straight-line distance between two points.
- `(a + b) / 2` is the **midpoint**.

```
>>> p = complex(3, 4)          # aisle 3, shelf 4
>>> p.real, p.imag
(3.0, 4.0)
>>> abs((4 + 6j) - (1 + 2j))   # distance: a 3-4-5 triangle
5.0
```

Using `complex` here means you get equality, distance, and arithmetic for free, with no
custom class to write or test.

## min() with a key function

`nearest_bin` picks the closest bin. `min(iterable, key=...)` returns the smallest item
*by the key you give it* — here, the bin whose distance from the dock is smallest:

```
>>> min(bins, key=lambda b: travel_distance(dock, b))
```

The `key` is a function applied to each element to decide the ordering; `min`/`max`/`sorted`
all take one. You will use this pattern constantly.

## Your task

Fill in the five blanks in `geo.py`:

1. `make_location(aisle, position)` — build the `complex` point.
2. `coordinates(loc)` — return `(loc.real, loc.imag)`.
3. `travel_distance(a, b)` — the magnitude of the displacement, `abs(b - a)`.
4. `midpoint(a, b)` — the average of the two points.
5. `nearest_bin(dock, bins)` — the bin with the smallest `travel_distance` from the dock,
   via `min(..., key=...)`.

## Worked example

```
>>> import geo
>>> geo.travel_distance(1 + 2j, 4 + 6j)
5.0
>>> geo.nearest_bin(0j, [10 + 0j, 1 + 1j, 5 + 5j])
(1+1j)
```

## What the check verifies, and what it leaves to you

- Enforced: `make_location(3, 4)` is `3+4j` with float `.real`/`.imag`; distance follows
  the 3-4-5 triangle; midpoint and nearest-bin are correct.
- Your free choice: the exact expressions, as long as the geometry is right.

<div class="hint" title="If you are stuck">

`complex(aisle, position)`; `loc.real, loc.imag`; `abs(b - a)`; `(a + b) / 2`; and
`min(bins, key=lambda b: travel_distance(dock, b))`.

</div>

Reference: Python documentation, "Built-in Types — Numeric Types (complex)" and "Built-in
Functions — min()" at docs.python.org.
