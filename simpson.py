"""simpson.py — Simpson's paradox on the kidney-stone data, seen and done.

Charig et al. (BMJ 1986), as tabulated by Julious & Mullee (1994):
  treatment A = open surgery, treatment B = percutaneous nephrolithotomy.
Pure Python, no libraries. Reused in stage 3b (back-door adjustment).

Shows:
  1. the paradox: A wins in each stratum, B wins in the total;
  2. the adjusted comparison (stratify by stone size, re-weight by the
     population's mix of sizes);
  3. a simulation of one causal story consistent with the table
     (size -> treatment, size -> outcome, treatment -> outcome):
     observational data reproduce the paradox; a randomized trial
     (treatment by coin flip) reproduces the ADJUSTED numbers;
  4. the same counts under a different story (the third variable caused
     BY the treatment): now the TOTAL is the right answer.
"""
import random

# successes, patients
DATA = {
    ("A", "small"): (81, 87),
    ("A", "large"): (192, 263),
    ("B", "small"): (234, 270),
    ("B", "large"): (55, 80),
}

def rate(s, n):
    return s / n

def pct(x):
    return f"{100 * x:5.1f}%"

print("1. The table")
for t in "AB":
    row = []
    for z in ("small", "large"):
        s, n = DATA[(t, z)]
        row.append(f"{z}: {s:3d}/{n:3d} = {pct(rate(s, n))}")
    s = sum(DATA[(t, z)][0] for z in ("small", "large"))
    n = sum(DATA[(t, z)][1] for z in ("small", "large"))
    row.append(f"total: {s}/{n} = {pct(rate(s, n))}")
    print(f"  {t}:  " + "   ".join(row))
print("  -> A better for small stones AND for large stones; B better overall.")

print("\n2. Why: who got which treatment")
for z in ("small", "large"):
    nA, nB = DATA[("A", z)][1], DATA[("B", z)][1]
    print(f"  {z:5s} stones: {nA:3d} got A, {nB:3d} got B  ->  A's share {pct(nA / (nA + nB))}")
print("  -> doctors gave the harder cases (large stones) to A.")

N = sum(n for _, n in DATA.values())
p_z = {z: (DATA[("A", z)][1] + DATA[("B", z)][1]) / N for z in ("small", "large")}
print(f"\n3. Adjusted: P(success | do(t)) = sum over size of P(success | t, size) * P(size)")
print(f"   P(small) = {p_z['small']:.3f}, P(large) = {p_z['large']:.3f}")
adj = {}
for t in "AB":
    adj[t] = sum(rate(*DATA[(t, z)]) * p_z[z] for z in ("small", "large"))
    terms = " + ".join(f"{rate(*DATA[(t, z)]):.3f} x {p_z[z]:.3f}" for z in ("small", "large"))
    print(f"   {t}: {terms} = {pct(adj[t])}")

# ---- simulate a world whose causal structure is size -> treatment, size -> outcome, treatment -> outcome
rng = random.Random(1986)
p_A_given = {z: DATA[("A", z)][1] / (DATA[("A", z)][1] + DATA[("B", z)][1]) for z in ("small", "large")}
p_ok = {k: rate(*v) for k, v in DATA.items()}

def patient(randomized):
    z = "small" if rng.random() < p_z["small"] else "large"
    if randomized:
        t = "A" if rng.random() < 0.5 else "B"          # coin flip: ignores size
    else:
        t = "A" if rng.random() < p_A_given[z] else "B"  # doctor's choice: depends on size
    ok = rng.random() < p_ok[(t, z)]
    return t, ok

def trial(randomized, n=200_000):
    s = {"A": 0, "B": 0}; c = {"A": 0, "B": 0}
    for _ in range(n):
        t, ok = patient(randomized)
        c[t] += 1; s[t] += ok
    return {t: s[t] / c[t] for t in "AB"}

obs = trial(False)
rct = trial(True)
print("\n4. Simulated world (200,000 patients each)")
print(f"   observational (doctor chooses):  A {pct(obs['A'])}   B {pct(obs['B'])}   <- the paradox's totals")
print(f"   randomized (coin chooses):       A {pct(rct['A'])}   B {pct(rct['B'])}   <- the adjusted numbers")

print("\n5. Same counts, different story: suppose the third column were caused BY the treatment")
print("   (e.g. 'small' = 'low blood pressure after the operation', as in Pearl's version).")
print("   Then stratifying would compare patients the treatment itself sorted;")
print(f"   the right comparison is the raw total: A {pct(273 / 350)}  vs  B {pct(289 / 350)}.")
print("   The table is identical; the right answer is not. The table does not say which story is true.")
