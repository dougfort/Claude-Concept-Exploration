"""shatter.py — shattering, growth, and the counting bound with real numbers.

A model class "shatters" a set of points if, for EVERY way of labelling the
points 0/1, some model in the class produces exactly that labelling.
The VC dimension is the size of the largest set the class can shatter.

Part 1: thresholds on a line ("label 1 if x >= t") and intervals
        ("label 1 if a <= x <= b"), checked by brute force.
Part 2: how many labellings each class can actually produce on n points,
        against all 2^n. Finite VC dimension means polynomial, not
        exponential, growth (Sauer's lemma). That gap is the whole guarantee.
Part 3: the VC bound with numbers, including a network the size of the
        one Zhang et al. (2017) trained on CIFAR-10.

Pure Python, no libraries.
"""
import math
from itertools import product


def threshold_labellings(xs):
    """All labellings produced by 'x >= t', for every choice of t."""
    cuts = [-math.inf] + sorted(xs) + [math.inf]
    out = set()
    for i in range(len(cuts) - 1):
        t = cuts[i + 1]
        lab = tuple(int(x >= t) for x in xs)
        out.add(lab)
    return out


def interval_labellings(xs):
    """All labellings produced by 'a <= x <= b' (empty interval included)."""
    s = sorted(xs)
    out = {tuple(0 for _ in xs)}
    for i in range(len(s)):
        for j in range(i, len(s)):
            a, b = s[i], s[j]
            out.add(tuple(int(a <= x <= b) for x in xs))
    return out


def shatters(labeller, xs):
    return len(labeller(xs)) == 2 ** len(xs)


def vc_bound(d, n, delta=0.05):
    """Vapnik's bound on (test error - training error), with probability 1 - delta.
    Meaningful only when n is comfortably larger than d."""
    if n <= d:
        return math.inf
    return math.sqrt((d * (math.log(2 * n / d) + 1) + math.log(4 / delta)) / n)


def examples_needed(d, gap=0.05):
    n = max(d + 1, 2)
    while vc_bound(d, n) > gap:
        n = int(n * 1.05) + 1
    return n


if __name__ == "__main__":
    print("1. Which point sets can each class shatter?")
    for name, f in [("thresholds", threshold_labellings), ("intervals", interval_labellings)]:
        for xs in [[1.0], [1.0, 2.0], [1.0, 2.0, 3.0]]:
            got = f(xs)
            missing = sorted(set(product((0, 1), repeat=len(xs))) - got)
            print(f"   {name:<10} on {len(xs)} point(s): {len(got)} of {2**len(xs)} labellings"
                  f"{'  -> shattered' if not missing else '  missing ' + str(missing)}")

    print("\n2. Labellings each class can produce on n points, against all 2^n")
    print(f"   {'n':>3} {'thresholds':>11} {'intervals':>10} {'2^n':>10}")
    for n in [2, 4, 8, 16, 20]:
        xs = [float(i) for i in range(n)]
        print(f"   {n:>3} {len(threshold_labellings(xs)):>11} {len(interval_labellings(xs)):>10} {2**n:>10}")

    print("\n3. The VC bound: guaranteed gap between test and training error (95% confidence)")
    for d, n, label in [(2, 1_000, "intervals, 1,000 examples"),
                        (100, 50_000, "100-parameter model, CIFAR-10-sized data"),
                        (1_649_402, 50_000, "Inception (Zhang 2017), CIFAR-10")]:
        b = vc_bound(d, n)
        print(f"   d = {d:>9,}  n = {n:>7,}  {label:<42} gap <= "
              + ("no bound (d >= n)" if b == math.inf else f"{b:.3f}"))

    print("\n   Examples needed to guarantee a gap of at most 5 percentage points:")
    for d in [2, 100, 10_000, 1_649_402]:
        print(f"   d = {d:>9,}  ->  n ~ {examples_needed(d):>14,}")
