# Seasonality with cmath: a DFT for monthly sales

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.9 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that complex numbers are a first-class numeric type and that cmath is the standard module for math functions over them (sqrt, exp, log, polar/rect, phase) where the real-only math module would raise or be undefined.
- Know the key difference between math and cmath: cmath always returns a complex result and never raises ValueError on negative/complex inputs (e.g. cmath.sqrt(-1) == 1j while math.sqrt(-1) raises).
- Compute a single Discrete Fourier Transform (DFT) bin by summing samples weighted by complex exponentials exp(-2j*pi*k*n/N), using cmath.exp, cmath.pi/cmath.tau.
- Convert a complex DFT coefficient to interpretable business quantities: amplitude via abs()/cmath.polar, and phase (peak timing) via cmath.phase, then round/unpack the polar form.
- Compare complex results robustly with cmath.isclose (rel_tol/abs_tol) instead of ==, and recognise the special constants cmath.inf/cmath.nan/cmath.infj.
- Read complex attributes (.real, .imag, .conjugate()) and reason about why the conjugate appears in DFT magnitude/energy calculations.

## Python features introduced
`cmath module (import cmath)`, `complex number type and literals (3+4j), the j suffix`, `cmath.exp (complex exponential)`, `cmath.pi and cmath.tau constants`, `cmath.polar (returns (modulus, phase) tuple)`, `cmath.rect (inverse of polar)`, `cmath.phase (argument of a complex number, in radians)`, `abs() on a complex value (modulus / magnitude)`, `cmath.sqrt (square root that handles negative reals, returns complex)`, `cmath.isclose with rel_tol/abs_tol for complex comparisons`, `complex.real / complex.conjugate() attributes and methods`, `cmath.inf / cmath.nan / cmath.infj / cmath.nanj special-value constants`, `contrast with the math module (math.sqrt(-1) raises ValueError; cmath.sqrt(-1) does not)`, `math.atan2-style angle handling via cmath.phase`, `round() and tuple unpacking of polar form`, `list/generator comprehensions over enumerate() to build the DFT sum`, `sum() over complex numbers`

## MiniERP increment
Adds a seasonality analyzer to the Reporting/Analytics module. Building on the existing reporting helpers (which already aggregate sales into a list of monthly totals across a year), this stage adds reporting.seasonality with three pure functions over a sequence of 12 monthly revenue figures: (1) dft_bin(series, k) -> complex computes the k-th DFT coefficient as sum(x_n * cmath.exp(-2j * cmath.pi * k * n / N) for n, x_n in enumerate(series)); (2) seasonal_strength(series) -> tuple[float, float] returns the amplitude and phase (in months, 0..12) of the dominant yearly cycle (k=1) by taking cmath.polar of dft_bin(series, 1), scaling the modulus by 2/N to get the revenue swing around the mean and converting the phase angle to the month index of the seasonal peak via cmath.phase; (3) is_flat(series, tol) -> bool reports whether sales are essentially aseasonal by checking cmath.isclose(dft_bin(series, 1), 0j, abs_tol=tol). The CLI/report layer can then label a product as 'Strong Q4 peak', 'Summer-skewed', or 'No clear season' from amplitude and peak month — real analytics, computed from first principles with the standard library, no numpy. This makes MiniERP's reporting able to detect seasonal demand patterns that drive inventory and purchasing decisions.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Create reporting/seasonality.py importing cmath and the type alias for a monthly series (e.g. `type MonthSeries = Sequence[float]`, reusing PEP 695 aliases from p09). Implement dft_bin(series, k) using cmath.exp / cmath.pi over enumerate(series); implement seasonal_strength(series) by unpacking cmath.polar(dft_bin(series, 1)) into (modulus, angle), returning (2*modulus/len(series), peak_month) where peak_month maps the angle through (-angle % cmath.tau) / cmath.tau * len(series); implement is_flat(series, tol=1e-9) with cmath.isclose(...0j, abs_tol=tol). Seed the module docstring with a note contrasting math.sqrt(-1) (raises) vs cmath.sqrt(-1) (==1j). Provide a tiny demo under `if __name__ == '__main__':` that prints the polar form of a hand-built 12-month series with a Q4 bump.
- **Test focus:** edu unit tests (unittest) that: (a) assert dft_bin of a constant series at k=1 is cmath.isclose to 0j and at k=0 equals N*mean; (b) feed a pure cosine season x_n = base + amp*cos(2*pi*n/12) and assert seasonal_strength recovers amp within tolerance and peak_month near 0/12; (c) shift the cosine by a quarter and assert the recovered peak_month shifts by ~3; (d) assert is_flat is True for a flat series and False for the seasonal one; (e) assert that math.sqrt(-1) raises ValueError while cmath.sqrt(-1) is cmath.isclose to 1j, and check abs()/.real/.conjugate() relationships (abs(z)**2 isclose (z*z.conjugate()).real). Use cmath.isclose with explicit abs_tol for all complex/float comparisons; avoid == on floats.

</div>
