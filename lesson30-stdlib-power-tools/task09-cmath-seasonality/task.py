"""Seasonality with cmath: a DFT for monthly sales

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: Create reporting/seasonality.py importing cmath and the type alias for a monthly series (e.g. `type MonthSeries = Sequence[float]`, reusing PEP 695 aliases from p09). Implement dft_bin(series, k) using cmath.exp / cmath.pi over enumerate(series); implement seasonal_strength(series) by unpacking cmath.polar(dft_bin(series, 1)) into (modulus, angle), returning (2*modulus/len(series), peak_month) where peak_month maps the angle through (-angle % cmath.tau) / cmath.tau * len(series); implement is_flat(series, tol=1e-9) with cmath.isclose(...0j, abs_tol=tol). Seed the module docstring with a note contrasting math.sqrt(-1) (raises) vs cmath.sqrt(-1) (==1j). Provide a tiny demo under `if __name__ == '__main__':` that prints the polar form of a hand-built 12-month series with a Q4 bump.
"""

# Your code here.
