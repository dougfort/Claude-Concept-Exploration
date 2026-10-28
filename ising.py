"""ising.py -- 2D Ising model by Metropolis Monte Carlo.

Pure Python, no libraries. Companion to what-is-emergence.md, stage 3a
(and 3b, finite-size scaling).

An L x L grid of spins, each +1 or -1, wrapping around at the edges.
Energy = -(number of agreeing neighbour pairs) + (number of disagreeing).
At temperature T (coupling J = 1, Boltzmann's constant = 1):

  repeat: pick a spin; compute dE, the energy change if it flipped;
          flip it if dE <= 0, otherwise flip with probability exp(-dE/T).

That's the whole physics. Onsager (1944): the infinite lattice has a
sharp transition at T_c = 2 / ln(1 + sqrt 2) = 2.2692.

Printed for each L and T:
  |m|   average absolute magnetization (the order parameter)
  chi   susceptibility N(<m^2> - <|m|>^2)/T: how strongly m fluctuates;
        its peak grows with L at a true transition
  U     Binder cumulant 1 - <m^4>/(3<m^2>^2): ~2/3 when ordered, ~0 when
        disordered; curves for different L cross near T_c (used in 3b)
"""
import math, random, sys, time

TC = 2 / math.log(1 + math.sqrt(2))

def simulate(L, T, equil, sweeps, rng):
    N = L * L
    s = [1] * N                       # start ordered (fast at low T)
    nbr = [((i // L) * L + (i + 1) % L, (i // L) * L + (i - 1) % L,
            (i + L) % N, (i - L) % N) for i in range(N)]
    acc = {4: math.exp(-4 / T), 8: math.exp(-8 / T)}
    M = N
    sm = sm2 = sm4 = 0.0
    rand, randrange = rng.random, rng.randrange
    for sweep in range(equil + sweeps):
        for _ in range(N):
            i = randrange(N)
            a, b, c, d = nbr[i]
            dE = 2 * s[i] * (s[a] + s[b] + s[c] + s[d])
            if dE <= 0 or rand() < acc[dE]:
                s[i] = -s[i]
                M += 2 * s[i]
        if sweep >= equil:
            m = abs(M) / N
            sm += m; sm2 += m * m; sm4 += m ** 4
    sm /= sweeps; sm2 /= sweeps; sm4 /= sweeps
    chi = N * (sm2 - sm * sm) / T
    U = 1 - sm4 / (3 * sm2 * sm2)
    return sm, chi, U

if __name__ == "__main__":
    rng = random.Random(1944)
    sizes = [int(a) for a in sys.argv[1:]] or [8, 16, 32]
    temps = [1.50, 2.00, 2.15, 2.20, 2.25, 2.27, 2.30, 2.35, 2.45, 2.60, 3.00, 3.50]
    print(f"Onsager T_c = {TC:.4f}\n")
    for L in sizes:
        t0 = time.time()
        sweeps = {8: 20000, 16: 15000, 32: 10000}.get(L, 2000)
        print(f"L = {L}  ({L*L} spins, {sweeps} sweeps per T)")
        print("    T      |m|      chi       U")
        for T in temps:
            m, chi, U = simulate(L, T, sweeps // 5, sweeps, rng)
            mark = "  <- T_c" if abs(T - TC) < 0.01 else ""
            print(f"  {T:5.2f}   {m:6.3f}  {chi:7.2f}   {U:6.3f}{mark}")
        print(f"  ({time.time() - t0:.0f} s)\n")
