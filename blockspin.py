"""blockspin.py -- renormalization-group flows you can run.

Pure Python, no libraries. Companion to what-is-emergence.md, stage 3b.

K is the coupling: how strongly neighbours want to agree, K = J/T
(large K = cold and ordered, small K = hot and disordered).
A renormalization step coarse-grains by a factor b = 2 and asks:
what coupling K' between the surviving spins reproduces the same physics?
Then repeat, and watch where K goes.

1. One dimension, exact.  Sum out every second spin of a chain.
   Two bonds K in series become one bond:   tanh K' = tanh(K)^2
   Since tanh K < 1, K' < K always: every coupling flows to 0.
   Only K = infinity (T = 0) stays put. No transition at any T > 0.

2. Two dimensions, Migdal-Kadanoff (approximate).  On a square lattice,
   removing every second spin also removes bonds a 1D step can't handle.
   Migdal and Kadanoff's trick: first move every second row of bonds onto
   its neighbour (doubling those bonds: K -> 2K), leaving 1D chains, then
   decimate along the chains:
                 tanh K' = tanh(2K)^2
   Now there is an unstable fixed point K* between the flows to 0 and to
   infinity. T_c = 1/K*. Exact (Onsager): K_c = 0.4407, T_c = 2.269.
   The order of the two moves is a choice; the other order gives
                 K' = 2 artanh(tanh(K)^2)
   and a different K*. That a free choice moves the answer is what
   "approximate" means here.

The slope of the flow at K* gives the critical exponent nu:
   lambda = dK'/dK at K*,   nu = ln b / ln lambda   (exact 2D Ising: nu = 1)
"""
import math

def step_1d(K):
    return math.atanh(math.tanh(K) ** 2)

def mk_a(K):                      # move bonds, then decimate
    return math.atanh(math.tanh(2 * K) ** 2)

def mk_b(K):                      # decimate, then move bonds
    return 2 * math.atanh(math.tanh(K) ** 2)

def flow(f, K, steps):
    out = [K]
    for _ in range(steps):
        K = f(K)
        out.append(K)
        if K > 50 or K < 1e-12:
            break
    return out

def fixed_point(f, lo=0.05, hi=2.0):
    g = lambda K: f(K) - K
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(lo) * g(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

def fmt(seq):
    return " -> ".join("inf" if k > 50 else f"{k:.4f}" for k in seq)

if __name__ == "__main__":
    print("1D CHAIN (exact): tanh K' = tanh(K)^2")
    for K in (0.5, 1.0, 2.0, 3.0):
        print(f"  K = {K}:  {fmt(flow(step_1d, K, 6))}")
    print()

    for name, f in (("tanh K' = tanh(2K)^2", mk_a),
                    ("K' = 2 artanh(tanh(K)^2)", mk_b)):
        Ks = fixed_point(f)
        h = 1e-6
        lam = (f(Ks + h) - f(Ks - h)) / (2 * h)
        nu = math.log(2) / math.log(lam)
        print(f"2D MIGDAL-KADANOFF: {name}")
        print(f"  fixed point K* = {Ks:.4f}  ->  T_c = {1/Ks:.3f}"
              f"   (exact K_c = 0.4407, T_c = 2.269)")
        print(f"  slope at K* = {lam:.3f}  ->  nu = {nu:.3f}   (exact nu = 1)")
        for K in (Ks * 0.9, Ks * 1.1):
            print(f"  start K = {K:.4f}:  {fmt(flow(f, K, 8))}")
        print()

    # Geometric mean of the two orders (a common symmetrization)
    Ka, Kb = fixed_point(mk_a), fixed_point(mk_b)
    print(f"Geometric mean of the two K*: {math.sqrt(Ka*Kb):.4f}"
          f"  ->  T_c = {1/math.sqrt(Ka*Kb):.3f}")


# ---------------------------------------------------------------------------
# 3. Kadanoff's block spins, done on real samples (for the RG side file).
#
# Sample an 81 x 81 Ising lattice at temperature T (Metropolis, as in
# ising.py). Replace each 3 x 3 block by its majority spin: 81 -> 27 -> 9.
# (A further step to 3 x 3 leaves 9 spins: too few to measure anything.)
# At each level measure the nearest-neighbour correlation <s_i s_j> of the
# block spins. That number is a stand-in for the effective coupling K':
#   below T_c  it rises toward 1 as you zoom out   (flows to order, K -> inf)
#   above T_c  it falls toward 0                   (flows to disorder, K -> 0)
#   at T_c     it stays roughly put                 (the fixed point)
# On a finite lattice the flat row sits a little off Onsager's 2.269, between
# the rows that rise and the rows that fall.
# Usage: python3 blockspin.py blocks      (about a minute)
# ---------------------------------------------------------------------------
import random, sys

def sample_ising(L, T, sweeps, every, rng):
    N = L * L
    s = [rng.choice((-1, 1)) for _ in range(N)] if T > 2.2 else [1] * N
    nbr = [((i // L) * L + (i + 1) % L, (i // L) * L + (i - 1) % L,
            (i + L) % N, (i - L) % N) for i in range(N)]
    acc = {4: math.exp(-4 / T), 8: math.exp(-8 / T)}
    rand, randrange = rng.random, rng.randrange
    out = []
    for sweep in range(sweeps):
        for _ in range(N):
            i = randrange(N)
            a, b, c, d = nbr[i]
            dE = 2 * s[i] * (s[a] + s[b] + s[c] + s[d])
            if dE <= 0 or rand() < acc[dE]:
                s[i] = -s[i]
        if sweep >= sweeps // 3 and sweep % every == 0:
            out.append(s[:])
    return out

def block(s, L):
    M = L // 3
    return [1 if sum(s[(3 * by + dy) * L + 3 * bx + dx]
                     for dy in range(3) for dx in range(3)) > 0 else -1
            for by in range(M) for bx in range(M)], M

def nn_corr(s, L):
    tot = 0
    for y in range(L):
        for x in range(L):
            v = s[y * L + x]
            tot += v * s[y * L + (x + 1) % L] + v * s[((y + 1) % L) * L + x]
    return tot / (2 * L * L)

def block_flow():
    rng = random.Random(1966)
    print("BLOCK SPINS: nearest-neighbour correlation at each level of 3x3 majority blocking")
    print("    T      81x81   27x27    9x9")
    for T in (2.0, 2.2, 2.269, 2.3, 2.4, 2.6):
        samples = sample_ising(81, T, 3000, 10, rng)
        levels = [[], [], []]
        for s in samples:
            L = 81
            for k in range(3):
                levels[k].append(nn_corr(s, L))
                if k < 2:
                    s, L = block(s, L)
        row = "   ".join(f"{sum(v) / len(v):.3f}" for v in levels)
        print(f"  {T:5.3f}    {row}")

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "blocks":
    block_flow()
