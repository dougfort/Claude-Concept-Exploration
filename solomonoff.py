"""solomonoff.py — a toy Solomonoff predictor.

Solomonoff (1964): to predict the next symbol, consider every program that
would print the data seen so far, weight each by 2^-(its length in bits),
and let them vote on what comes next.

The real thing uses every program for a universal Turing machine, which is
uncomputable. This toy uses a tiny language with two kinds of program, so we
can list them all:

  R(p)        print the pattern p over and over          ("repeat")
  S(p, n, q)  print R(p) for n symbols, then R(q) forever ("switch": grue)

Each program is written in bits with a self-delimiting code (so no program is
a prefix of another), and its prior weight is 2^-(length). Short programs
dominate; long ones never vanish.

Pure Python, no libraries.
"""
import math
from itertools import product

MAX_PAT = 5      # longest pattern
MAX_SWITCH = 24  # latest switch point


def num_bits(n):
    """Elias-gamma-style length for a positive integer: 2*floor(log2 n) + 1."""
    return 2 * int(math.log2(n)) + 1


def pattern_bits(p):
    return num_bits(len(p)) + len(p)


def all_patterns():
    for k in range(1, MAX_PAT + 1):
        for bits in product("01", repeat=k):
            yield "".join(bits)


def is_primitive(p):
    """Skip patterns that are themselves repeats ('0101' = '01' twice),
    so each sequence is counted once per program shape."""
    return not any(len(p) % d == 0 and p[:d] * (len(p) // d) == p
                   for d in range(1, len(p)))


def programs():
    """Yield (name, length_in_bits, generator function)."""
    pats = [p for p in all_patterns() if is_primitive(p)]
    for p in pats:
        yield (f"R({p})", 1 + pattern_bits(p),
               lambda i, p=p: p[i % len(p)])
    for p in pats:
        for q in pats:
            if p == q:
                continue
            for n in range(1, MAX_SWITCH + 1):
                yield (f"S({p},{n},{q})", 1 + pattern_bits(p) + num_bits(n) + pattern_bits(q),
                       lambda i, p=p, n=n, q=q: p[i % len(p)] if i < n else q[(i - n) % len(q)])


PROGRAMS = list(programs())


def consistent(data):
    return [(name, L, g) for name, L, g in PROGRAMS
            if all(g(i) == data[i] for i in range(len(data)))]


def predict(data):
    """Return P(next = '1'), the top surviving programs, and the
    share of weight held by 'switch' programs (the grue hypotheses)."""
    alive = consistent(data)
    w = {name: 2.0 ** -L for name, L, _ in alive}
    total = sum(w.values())
    p1 = sum(w[name] for name, _, g in alive if g(len(data)) == "1") / total
    switch_share = sum(w[n] for n, _, _ in alive if n.startswith("S")) / total
    top = sorted(alive, key=lambda t: t[1])[:3]
    return p1, [(n, L) for n, L, _ in top], switch_share


def total_surprise(sequence):
    """Bits of surprise the mixture suffers predicting the whole sequence,
    one symbol at a time: sum of -log2 P(actual next symbol)."""
    bits = 0.0
    for t in range(len(sequence)):
        alive = consistent(sequence[:t])
        total = sum(2.0 ** -L for _, L, _ in alive)
        right = sum(2.0 ** -L for _, L, g in alive if g(t) == sequence[t])
        bits += -math.log2(right / total)
    return bits


if __name__ == "__main__":
    print(f"{len(PROGRAMS)} programs in the toy language\n")

    print("1. Predicting the next symbol")
    for data in ["0101", "010101", "011011", "0000", "00000000",
                 "0000000000000000", "01101"]:
        p1, top, sw = predict(data)
        print(f"   after {data:<18} P(next=1) = {p1:.3f}   "
              f"weight on switch (grue) programs = {sw:.4f}   best: {top[0][0]} ({top[0][1]} bits)")

    print("\n2. Solomonoff's bound: total surprise <= length of the true program")
    for name, L, g in PROGRAMS:
        if name in ("R(0)", "R(011)", "R(01101)", "S(0,12,1)"):
            seq = "".join(g(i) for i in range(40))
            print(f"   source {name:<12} program length {L:2d} bits   "
                  f"total surprise over 40 symbols = {total_surprise(seq):5.2f} bits")
