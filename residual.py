"""residual.py — predictive coding of one line of an image, in pure Python.

Companion to 'What Is Intelligence?' stage 3a.
  Part 1: the 8-pixel row from stage 1, raw vs. residual (flag code).
  Part 2: a synthetic 4096-pixel line (plateaus, ramps, edges, noise):
          bits per pixel raw, and with residuals from several predictors.
  Part 3: Srinivasan-Laughlin-Dubs (1982): the best "surround" widens
          when the signal is noisy (dim light).
  Part 4: where the bits go: a centre-surround signal on the clean line
          is nonzero only where the slope changes (Mach bands).
Entropies are zeroth-order empirical entropies of the integer values:
the bits per symbol an ideal code would need if it knew the histogram.
"""
import math, random

def entropy(values):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    n = len(values)
    return -sum(c / n * math.log2(c / n) for c in counts.values())

# ---------- Part 1: the stage-1 row ----------
row = [100, 102, 103, 103, 105, 180, 182, 181]
res = [row[i] - row[i - 1] for i in range(1, len(row))]
bits = 8 + sum(4 if -4 <= r <= 3 else 9 for r in res)
print("Part 1: stage-1 row")
print("  residuals:", res)
print("  raw bits: %d   flag-code bits: %d" % (8 * len(row), bits))

# ---------- Part 2: synthetic line ----------
def clean_line(n, seed):
    rng = random.Random(seed)
    out, level = [], rng.uniform(30, 220)
    while len(out) < n:
        length = rng.randint(50, 400)
        target = rng.uniform(30, 220)
        if rng.random() < 0.3:               # ramp from level to target
            for j in range(length):
                out.append(level + (target - level) * j / length)
        else:                                 # edge, then plateau
            out.extend([target] * length)
        level = target
    return out[:n]

def noisy(clean, sigma, seed):
    rng = random.Random(seed)
    return [min(255, max(0, round(v + rng.gauss(0, sigma)))) for v in clean]

def residuals(x, k):
    """Predict each pixel as the mean of the previous k pixels."""
    r = []
    for i in range(k, len(x)):
        pred = round(sum(x[i - k:i]) / k)
        r.append(x[i] - pred)
    return r

N = 4096
clean = clean_line(N, seed=1)
print("\nPart 2: synthetic line, %d pixels" % N)
print("  %-28s %8s %8s" % ("", "bright", "dim"))
print("  %-28s %8s %8s" % ("", "(s=1)", "(s=8)"))
bright, dim = noisy(clean, 1, 2), noisy(clean, 8, 3)
print("  %-28s %8.2f %8.2f" % ("raw pixels", entropy(bright), entropy(dim)))
for k in (1, 2, 4, 8, 16):
    print("  %-28s %8.2f %8.2f" % ("residual, mean of last %d" % k,
          entropy(residuals(bright, k)), entropy(residuals(dim, k))))

# ---------- Part 3: best surround vs. noise ----------
print("\nPart 3: best predictor width k against noise level")
print("  %6s %10s %10s %10s" % ("sigma", "raw bits", "best k", "res bits"))
for sigma in (0.5, 1, 2, 4, 8, 16):
    x = noisy(clean, sigma, 10 + int(sigma * 10))
    best = min((entropy(residuals(x, k)), k) for k in (1, 2, 3, 4, 6, 8, 12, 16, 24))
    print("  %6.1f %10.2f %10d %10.2f" % (sigma, entropy(x), best[1], best[0]))

# ---------- Part 4: centre-surround on the clean line ----------
print("\nPart 4: centre-surround c = x - (left + right)/2 on the clean line")
c = [clean[i] - (clean[i - 1] + clean[i + 1]) / 2 for i in range(1, N - 1)]
nonzero = [i for i, v in enumerate(c) if abs(v) > 1e-9]
print("  pixels: %d   nonzero responses: %d (%.1f%%)" %
      (len(c), len(nonzero), 100 * len(nonzero) / len(c)))
# show the steepest ramp start, and one step edge
def show(i, label):
    seg = range(i - 3, i + 4)
    print("  %s (pixel %d):" % (label, i))
    print("    value: " + " ".join("%6.1f" % clean[j] for j in seg))
    print("    c:     " + " ".join("%+6.2f" % (clean[j] - (clean[j-1] + clean[j+1]) / 2) for j in seg))
ramps = [i for i in range(4, N - 4)
         if abs(clean[i] - clean[i - 1]) < 1e-9 and 1e-9 < abs(clean[i + 1] - clean[i]) < 5]
show(max(ramps, key=lambda i: abs(clean[i + 1] - clean[i])), "start of the steepest ramp")
steps = [i for i in range(4, N - 4)
         if abs(clean[i] - clean[i - 1]) < 1e-9 and abs(clean[i + 1] - clean[i]) > 20
         and abs(clean[i + 2] - clean[i + 1]) < 1e-9]
show(steps[0], "a step edge")
