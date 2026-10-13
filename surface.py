"""A toy rotated surface code, pure Python.

Data qubits sit on a d x d grid. Checks are plaquettes on the faces between
them, coloured like a chessboard (X-checks and Z-checks), plus weight-2 checks
on the edges. This toy simulates bit-flip (X) errors only, which the Z-checks
detect; phase flips are the same story with the roles swapped.

Because every operation here is a Pauli flip, we never need amplitudes: an
error is a set of flipped qubits, and a check's syndrome bit is the parity of
how many flipped qubits it touches. (This is the stabilizer shortcut that lets
real decoders run on classical computers.)
Run:  python3 surface.py
"""
import random
from itertools import combinations

def layout(d):
    q = lambda r, c: r * d + c
    xs, zs = [], []
    for r in range(-1, d):
        for c in range(-1, d):
            cells = [q(rr, cc) for rr in (r, r + 1) for cc in (c, c + 1)
                     if 0 <= rr < d and 0 <= cc < d]
            kind = "X" if (r + c) % 2 == 0 else "Z"
            if len(cells) == 4:
                (xs if kind == "X" else zs).append(cells)
            elif len(cells) == 2:
                top_bottom = r in (-1, d - 1)
                if top_bottom and kind == "X":
                    xs.append(cells)               # X-checks close the top/bottom edges
                if not top_bottom and kind == "Z":
                    zs.append(cells)               # Z-checks close the left/right edges
    return xs, zs

def mask(cells):
    m = 0
    for c in cells:
        m |= 1 << c
    return m

def syndrome(err, checks):                         # err: bitmask of flipped qubits
    return tuple(bin(err & mask(c)).count("1") % 2 for c in checks)

def span_contains(vecs, v):                        # is v a XOR-combination of vecs?
    basis = []
    for b in vecs:
        for x in basis:
            b = min(b, b ^ x)
        if b:
            basis.append(b)
    for x in basis:
        v = min(v, v ^ x)
    return v == 0

def build_decoder(d, zs, max_weight):
    """Lookup table: syndrome -> lowest-weight error producing it."""
    table = {syndrome(0, zs): 0}
    for w in range(1, max_weight + 1):
        for qs in combinations(range(d * d), w):
            e = mask(qs)
            table.setdefault(syndrome(e, zs), e)
    return table

def show_grid(d, err, fix=0):
    rows = []
    for r in range(d):
        row = ""
        for c in range(d):
            b = 1 << (r * d + c)
            row += " X" if err & b and not fix & b else (" *" if fix & b and not err & b
                   else (" ." if not err & b else " o"))
        rows.append(row)
    return "\n".join(rows)

if __name__ == "__main__":
    d = 3
    xs, zs = layout(d)
    assert all(len(set(a) & set(b)) % 2 == 0 for a in xs for b in zs), "checks must commute"
    print(f"d = {d}: {d*d} data qubits, {len(xs)} X-checks, {len(zs)} Z-checks, "
          f"{d*d - len(xs) - len(zs)} logical qubit")
    print("  Z-checks (catch bit flips):", zs)
    table = build_decoder(d, zs, 2)
    X_stabs = [mask(c) for c in xs]

    print("\n1. One bit flip in the middle")
    e = mask([4])
    s = syndrome(e, zs); fix = table[s]
    print("  (o = flipped and corrected, X = flipped and missed, * = wrongly flipped by decoder)")
    print(show_grid(d, e, fix), "\n  syndrome", s, "-> decoder flips", [i for i in range(9) if fix >> i & 1],
          "-> residual", "harmless" if span_contains(X_stabs, e ^ fix) else "LOGICAL ERROR")

    print("\n2. Every single flip, and every pair of flips")
    for w in (1, 2):
        bad = 0
        pats = list(combinations(range(d * d), w))
        for qs in pats:
            e = mask(qs)
            bad += not span_contains(X_stabs, e ^ table[syndrome(e, zs)])
        print(f"  weight {w}: {len(pats)} patterns, {bad} end in a logical error")

    print("\n3. Logical error rate per round, bit flips at rate p on every qubit")
    print("   (d = 5 decoder: lowest-weight lookup up to weight 6, built once)")
    setups = {}
    for dd, mw in ((3, 3), (5, 6)):
        x5, z5 = layout(dd)
        setups[dd] = (z5, [mask(c) for c in x5], build_decoder(dd, z5, mw))
    random.seed(1)
    trials = 50000
    print("     p      d=3       d=5     ratio d3/d5")
    for p in (0.01, 0.03, 0.05, 0.08, 0.12, 0.16):
        rate = {}
        for dd, (z5, X5, tab) in setups.items():
            fails = 0
            for _ in range(trials):
                e = 0
                for i in range(dd * dd):
                    if random.random() < p:
                        e |= 1 << i
                fix = tab.get(syndrome(e, z5), 0)
                fails += not span_contains(X5, e ^ fix)
            rate[dd] = fails / trials
        ratio = rate[3] / rate[5] if rate[5] else float("inf")
        print(f"   {p:.2f}   {rate[3]:.4f}   {rate[5]:.4f}     {ratio:6.1f}")
