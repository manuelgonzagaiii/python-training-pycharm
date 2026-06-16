# Stage 5: bitwise operators and bit flags

A product has several yes/no attributes: is it taxable, can it be discounted, can it be
returned? You could store three separate boolean fields. Or you can pack them into the
**bits of a single integer** — compact, fast to combine, and exactly how permission
systems and file modes have worked for decades. This stage adds that flag system to
`money.py`, and it is the precursor to MiniERP's later Users & Roles permission bitset.

## Integers are made of bits

Every `int` is a row of binary digits. The bitwise operators act on those bits in
parallel:

| Operator | Name | What it does |
|----------|------|--------------|
| `&` | AND | bit is 1 only where **both** inputs are 1 |
| `\|` | OR | bit is 1 where **either** input is 1 |
| `^` | XOR | bit is 1 where the inputs **differ** |
| `~` | NOT | flips every bit |
| `<<` | left shift | moves bits left, i.e. multiply by a power of two |
| `>>` | right shift | moves bits right |

The key idiom for flags is `1 << n`: take the number `1` (binary `...0001`) and shift it
`n` places left to land on bit `n`.

```
1 << 0  ==  0b001  ==  1     # bit 0
1 << 1  ==  0b010  ==  2     # bit 1
1 << 2  ==  0b100  ==  4     # bit 2
```

Each flag owns one bit, so they never collide:

```python
TAXABLE = 1 << 0
DISCOUNTABLE = 1 << 1
RETURNABLE = 1 << 2
```

## The three operations on a flag set

A single integer `flags` holds all the switches. To work with one switch you use its
`mask` (one of the constants above):

- **Turn it on:** `flags | mask`. OR-ing sets that bit and leaves the others as they
  were. A product that is taxable *and* returnable is `TAXABLE | RETURNABLE`.
- **Test it:** `flags & mask == mask`. AND-ing keeps only the bits both have; if the
  result still equals `mask`, every bit of the mask was present.
- **Turn it off:** `flags & ~mask`. `~mask` is all ones except the mask's bits, so
  AND-ing clears exactly those bits and disturbs nothing else.

```
>>> flags = TAXABLE | RETURNABLE      # 0b101 == 5
>>> flags & TAXABLE == TAXABLE        # is it taxable?
True
>>> flags = flags & ~TAXABLE          # make it non-taxable
>>> flags                              # 0b100 == 4, RETURNABLE still set
4
```

(Python also gives you `int.bit_count()`, which returns how many bits are set —
`(TAXABLE | RETURNABLE).bit_count()` is `2`, i.e. two flags on. Handy for counting.)

## Your task

Fill in the three blanks in `money.py`:

1. `has_flag(flags, mask)` — `True` if the mask's bits are set. Use `&`.
2. `set_flag(flags, mask)` — return `flags` with the mask turned on. Use `|`.
3. `clear_flag(flags, mask)` — return `flags` with the mask turned off, leaving other
   bits alone. Use `&` with `~mask`.

## What the check verifies, and what it leaves to you

- Enforced: the flag contract. After `set_flag`, `has_flag` is `True`; after
  `clear_flag`, it is `False`; clearing one flag must not disturb another. Setting an
  already-set flag changes nothing.
- Your free choice: the exact expressions, as long as the bit operations are correct.
  `flags & mask == mask` and `bool(flags & mask)` both pass for single-bit masks, for
  example.

<div class="hint" title="If you are stuck">

`set_flag` is `flags | mask`. `has_flag` is `flags & mask == mask`. `clear_flag` is
`flags & ~mask` — the `~` inverts the mask so the AND clears just those bits.

</div>

Reference: Python documentation, "Numeric Types — Bitwise Operations on Integers" at
docs.python.org.
