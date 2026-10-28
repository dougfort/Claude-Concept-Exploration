"""transition.py -- a first-order transition in sample size, by hand.

Pure Python, no libraries. Companion to what-is-emergence.md, stage 4b.
The theory is singular learning theory's (Watanabe); slt.py, from the
induction exploration, computes the learning coefficient lambda itself.

Two candidate solutions compete for the Bayesian posterior.

  SIMPLE   slightly wrong: excess loss 0.01 nats per example, lambda = 1
  ACCURATE exactly right:  excess loss 0,                    lambda = 10

Watanabe's free energy (lower is better, in nats):
        F(n) = n * loss + lambda * ln(n)
The first term is what being wrong costs on n examples; the second is the
price of complexity, which grows only logarithmically. The posterior
probability of each solution is proportional to exp(-F).

Small n: complexity dominates, SIMPLE wins. Large n: error dominates,
ACCURATE wins. The switch is a crossing of two lines -- a first-order
transition, with n playing the role of system size.
"""
import math

SIMPLE = (0.01, 1.0)
ACCURATE = (0.0, 10.0)

def F(sol, n):
    loss, lam = sol
    return n * loss + lam * math.log(n)

def p_accurate(n):
    d = F(ACCURATE, n) - F(SIMPLE, n)
    return 1 / (1 + math.exp(d)) if d < 700 else 0.0

def crossover(lo=10, hi=10**7):
    for _ in range(200):
        mid = (lo + hi) / 2
        if F(ACCURATE, mid) < F(SIMPLE, mid):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def width(scale):
    """Where P(accurate) goes from 10% to 90%, with SIMPLE's error divided
    by `scale` (a subtler error needs more data to detect)."""
    s = (SIMPLE[0] / scale, SIMPLE[1])
    def p(n):
        d = F(ACCURATE, n) - F(s, n)
        return 1 / (1 + math.exp(d)) if d < 700 else 0.0
    def find(target, lo=10, hi=10**9):
        for _ in range(200):
            mid = (lo + hi) / 2
            if p(mid) < target:
                lo = mid
            else:
                hi = mid
        return mid
    a, b = find(0.1), find(0.9)
    return a, b

if __name__ == "__main__":
    print("     n     F_simple   F_accurate   P(accurate)")
    for n in (100, 1000, 3000, 6000, 7500, 8100, 8700, 10000, 20000):
        print(f"  {n:6d}   {F(SIMPLE, n):8.1f}    {F(ACCURATE, n):8.1f}"
              f"      {p_accurate(n):.4f}")
    print(f"\ncrossover at n = {crossover():.0f}\n")
    print("Make SIMPLE's error subtler: the switch moves later and gets")
    print("relatively sharper (width as a fraction of where it happens).")
    print("  error     10%->90% of P(accurate)     relative width")
    for scale in (1, 10, 100):
        a, b = width(scale)
        print(f"  {0.01/scale:.4f}   n = {a:9.0f} -> {b:9.0f}        "
              f"{(b - a) / ((a + b) / 2):.3f}")
