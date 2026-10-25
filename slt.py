"""slt.py — singular learning theory's learning coefficient, on toy models.

Setup: data come from y = 0 * x + noise, so the true slope is 0.
We compare models that differ only in how the slope is built from parameters:

  regular, 1 param    slope = w           loss near truth ~ w^2
  regular, 2 params   y = a*x1 + b*x2     loss near truth ~ a^2 + b^2
  product, 2 params   slope = a*b         loss near truth ~ (a*b)^2
  product, 3 params   slope = a*b*c       loss near truth ~ (a*b*c)^2

All parameters live in the box [-1, 1]. For a small tolerance eps, the
"good set" is the set of parameter settings with loss < eps. Its volume
shrinks like eps^lambda as eps -> 0. The exponent lambda is the
learning coefficient. For a regular model with d parameters, lambda = d/2.
Watanabe: a model's effective parameter count is 2*lambda, not d.

Volumes are computed exactly (closed forms), and checked by random sampling
at a moderate eps.

Pure Python, no libraries.
"""
import math
import random


def vol_regular(d, eps):
    """Volume of {sum of squares < eps} = ball of radius sqrt(eps) in d dims."""
    r = math.sqrt(eps)
    return math.pi ** (d / 2) / math.gamma(d / 2 + 1) * r ** d


def vol_product(m, eps):
    """Volume of {|x1*...*xm| < delta} in [-1,1]^m, delta = sqrt(eps).
    Exact: 2^m * delta * sum_{k<m} ln(1/delta)^k / k!"""
    delta = math.sqrt(eps)
    L = math.log(1 / delta)
    return 2 ** m * delta * sum(L ** k / math.factorial(k) for k in range(m))


MODELS = [
    ("regular, 1 param", lambda e: vol_regular(1, e), lambda p: p[0] ** 2, 1),
    ("regular, 2 params", lambda e: vol_regular(2, e), lambda p: p[0] ** 2 + p[1] ** 2, 2),
    ("product, 2 params", lambda e: vol_product(2, e), lambda p: (p[0] * p[1]) ** 2, 2),
    ("product, 3 params", lambda e: vol_product(3, e), lambda p: (p[0] * p[1] * p[2]) ** 2, 3),
]


if __name__ == "__main__":
    epss = [1e-2, 1e-4, 1e-6, 1e-8, 1e-12, 1e-20]
    print("1. Volume of the good set (loss < eps), as a fraction of the box")
    print(f"   {'model':<19}" + "".join(f"{'eps=' + format(e, '.0e'):>11}" for e in epss))
    for name, vol, _, d in MODELS:
        print(f"   {name:<19}" + "".join(f"{vol(e) / 2 ** d:>11.2e}" for e in epss))

    print("\n2. Learning coefficient: how fast the good set shrinks")
    print("   (slope of log volume against log eps, between successive eps)")
    print(f"   {'model':<19}{'d/2':>5}   slopes ->")
    for name, vol, _, d in MODELS:
        slopes = [math.log(vol(b) / vol(a)) / math.log(b / a) for a, b in zip(epss, epss[1:])]
        print(f"   {name:<19}{d / 2:>5.1f}   " + "  ".join(f"{s:.3f}" for s in slopes))

    print("\n3. Check by random sampling at eps = 1e-2 (1,000,000 samples)")
    rng = random.Random(0)
    for name, vol, loss, d in MODELS:
        hits = sum(loss([rng.uniform(-1, 1) for _ in range(d)]) < 1e-2 for _ in range(1_000_000))
        print(f"   {name:<19} sampled {hits / 1e6:.4f}   exact {vol(1e-2) / 2 ** d:.4f}")

    print("\n4. What it costs in evidence: Watanabe's free energy charge lambda * log(n)")
    for n in [100, 10_000, 1_000_000]:
        print(f"   n = {n:>9,}:  regular 2-param charge {1.0 * math.log(n):5.1f} nats   "
              f"product 2-param charge {0.5 * math.log(n):5.1f} nats (+ a log log n discount)")
