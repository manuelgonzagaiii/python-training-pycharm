# Stage 4: a reservation loop with while

A `for` loop is the right tool when you know the collection you are walking. A `while`
loop is for when you **do not** know how many passes you need ahead of time — you keep
going *while* some condition holds and stop when it stops. Stock reservation is exactly
that shape: keep drawing stock until either the request is filled or the shelf is empty,
whichever comes first.

```
while reserved < requested and available > 0:
    ...
```

The whole correctness of a `while` loop rests on one question: **why does it end?** A loop
whose condition never becomes false runs forever. Here it ends because every pass either
moves `reserved` closer to `requested` or lowers `available` (usually both), so one of the
two tests is guaranteed to fail eventually. When you write a `while`, always be able to
point at the line that makes progress toward the exit.

This stage introduces a second module, `inventory.py`. Your `pricing.py` from the earlier
stages is unchanged and carried alongside it.

## Reserving in batches

Real warehouses move stock in batches, not one unit at a time. This loop reserves up to a
batch (10 units) per pass, but never more than the remaining request and never more than
what is on hand — `min(batch, requested - reserved, available)` picks the largest safe
amount. When stock is short, the request is only **partially** filled, and the function
returns how many units were actually reserved.

## Your task

In `inventory.py`, finish `reserve_units(available, requested)`. The batch logic inside the
loop is written; you supply the **loop condition** that keeps it running while there is
still demand to fill and stock to fill it with.

## Worked example

```
>>> import inventory
>>> inventory.reserve_units(100, 35)     # plenty of stock
35
>>> inventory.reserve_units(25, 100)     # only 25 on hand -> partial fill
25
>>> inventory.reserve_units(0, 10)       # nothing on hand
0
```

## What the check verifies, and what it leaves to you

- Enforced: a fully-stocked request reserves exactly what was asked; a short request
  reserves all that is available and no more; zero stock or a zero request reserves 0; the
  result never exceeds either bound.
- Your free choice: the condition can be written either order (`available > 0 and
  reserved < requested` is the same), and a different but terminating loop structure that
  produces the right counts also passes.

<div class="hint" title="If you are stuck">

The loop should run `while reserved < requested and available > 0`. Both parts matter:
drop the first and you over-reserve; drop the second and you loop forever when stock runs
out.

</div>

Reference: Python documentation, "while statements" at docs.python.org.
