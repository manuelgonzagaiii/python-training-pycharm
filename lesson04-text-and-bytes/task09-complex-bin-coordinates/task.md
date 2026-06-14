# Warehouse Bin Coordinates with Complex Numbers

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 4.9 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use a Python complex value as a lightweight, immutable 2D point (x = aisle along .real, y = shelf along .imag) instead of inventing a custom pair type.
- Read the coordinates back out with the .real and .imag attributes, remembering they are always float even when you passed ints.
- Compute the straight-line travel distance between two bins with abs(b - a): subtraction gives the displacement vector, abs() gives its length (the Pythagorean magnitude).
- Combine points arithmetically: add/subtract to translate, and divide by a scalar to find a midpoint or average position.
- Understand .conjugate() (mirror across the aisle axis) and why abs(z) and abs(z.conjugate()) are equal.
- Pick the nearest bin to the packing dock using min(..., key=lambda bin: abs(bin.coord - dock)), turning a rare numeric type into a real pick-path optimization.
- See how complex participates in the numeric tower: it coerces ints/floats automatically, but unlike int/float it has no ordering, so you must compare via abs().

## Python features introduced
`complex literals (e.g. 3+4j)`, `complex() constructor with real and imaginary args`, `.real attribute (returns float)`, `.imag attribute (returns float)`, `.conjugate() method`, `abs() of a complex as Euclidean magnitude / vector length`, `complex arithmetic: + and - for vector displacement between points`, `scalar multiply/divide of a complex (a + b) / 2 for a midpoint`, `complex equality and the fact .real/.imag are always float`, `mixing complex with int/float in the numeric tower (auto-coercion)`, `round() applied to the float result of abs()`, `min() with a key= function over complex points`, `isinstance(x, complex) type check`, `f-string formatting of a float distance, e.g. f'{d:.2f}'`

## MiniERP increment
Adds a geometry helper to the Inventory module so warehouse bins carry a physical location. New module mini_erp/inventory/geo.py defines warehouse bin coordinates as complex numbers (real part = aisle, imag part = shelf/position) and pure functions over them: make_location(aisle, position) -> complex (wraps complex()), coordinates(loc) -> tuple[float, float] (returns (loc.real, loc.imag)), travel_distance(a, b) -> float (returns abs(b - a), the pick path length between two bins), midpoint(a, b) -> complex ((a + b) / 2, e.g. for a staging point), and nearest_bin(dock, bins) which selects the closest bin to the packing dock using min(bins, key=lambda b: travel_distance(dock, b)). This gives the Products & Inventory module its first spatial query — 'which bin is closest to ship from' — and is consumed later by the Reporting module's pick-efficiency stats. It depends only on numeric features from earlier p02 tasks (the numeric-tower task already introduced complex literals and the complex() constructor) and built-in min()/round().

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Create mini_erp/inventory/geo.py. Implement make_location(aisle, position) returning complex(aisle, position); coordinates(loc) returning (loc.real, loc.imag); travel_distance(a, b) returning abs(b - a); midpoint(a, b) returning (a + b) / 2; and nearest_bin(dock, bins) returning the bin from the non-empty iterable bins with the smallest travel_distance(dock, bin), using min(..., key=...). Add module and function docstrings explaining that a bin location is modeled as a complex point where .real is the aisle and .imag is the shelf position, and that abs() of a displacement is the Pythagorean travel distance. Keep every function pure (no printing, no mutation).
- **Test focus:** Unit-test each function against hand-computed values: make_location(3, 4) == (3+4j) and its .real/.imag are 3.0/4.0 (assert they are float, not int); coordinates((3+4j)) == (3.0, 4.0); travel_distance((1+2j), (4+6j)) == 5.0 (the classic 3-4-5 triangle) and travel_distance is symmetric (a->b equals b->a) via abs() of the conjugate-related displacement; midpoint((1+2j),(3+6j)) == (2+4j); a .conjugate() check asserting abs(z) == abs(z.conjugate()); and nearest_bin returns the correct closest bin given a dock at the origin and several candidate bins (including a tie-break sanity case and a single-element iterable). Also assert that complex coordinates carry float parts even when built from ints, and that round(travel_distance(...), 2) formats as expected for an irrational distance like abs(1+1j).

</div>
