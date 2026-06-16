"""MiniERP warehouse geometry: bin coordinates as complex numbers.

A warehouse bin's location is a 2-D point: the aisle along one axis, the shelf
along the other. Python's built-in `complex` is a ready-made, immutable 2-D
point (real part = aisle, imaginary part = shelf), so we use it directly instead
of inventing a coordinate class. These pure helpers do generic 2-D point math --
distance, midpoint, and nearest point -- that a later inventory phase can build on.
"""


def make_location(aisle: float, position: float) -> complex:
    """A bin location: aisle on the real axis, shelf/position on the imaginary axis."""
    return complex(aisle, position)


def coordinates(loc: complex) -> tuple[float, float]:
    """The (aisle, shelf) pair of a location. Both are float, even from int input."""
    return loc.real, loc.imag


def travel_distance(a: complex, b: complex) -> float:
    """Straight-line distance between two bins: the magnitude of the displacement b - a."""
    return abs(b - a)


def midpoint(a: complex, b: complex) -> complex:
    """The point halfway between two bins, e.g. a staging spot."""
    return (a + b) / 2


def nearest_bin(dock: complex, bins: list[complex]) -> complex:
    """The bin closest to the packing dock."""
    return min(bins, key=lambda b: travel_distance(dock, b))
