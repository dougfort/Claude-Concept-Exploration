"""double_descent.py — bias-variance, the interpolation threshold, and beyond.

The world: each case has D = 400 measurements (random numbers), and the
true answer is a weighted sum of all of them plus a little noise. Early
measurements matter most; later ones matter less but never stop mattering.

The learner: sees n = 20 cases and fits a straight-line (linear) model that
uses only the first p measurements. We vary p, the number of parameters.

Fitting is least squares. When p > n there are infinitely many models that
fit the 20 cases exactly; we take the one with the smallest weights (the
"minimum-norm" fit, which is what gradient descent from zero finds).

  p < n : the classical regime. Few parameters underfit (bias); more help,
          up to a point, then start fitting noise (variance).
  p = n : the interpolation threshold. Just enough parameters to pass through
          every training case; the fit is as unstable as it can be.
  p > n : the modern regime. Every model fits the training data exactly,
          yet error on new cases falls again: the second descent.

Run with --classical to stop at the threshold (stage 3b);
run with no flag for the full curve (stage 4).

We report the MEDIAN over trials: right at p = n a few unlucky draws give
astronomically bad fits, and a mean would be dominated by them.
Pure Python, no libraries.
"""
import math
import random
import sys

D = 400          # measurements the world actually uses
N_TRAIN = 20     # training cases
NOISE = 0.5      # noise on each answer
TRIALS = 101

BETA = [1 / math.sqrt(j) for j in range(1, D + 1)]          # true weights
scale = math.sqrt(sum(b * b for b in BETA))
BETA = [b / scale for b in BETA]                             # total signal = 1


def solve(A, b):
    """Gaussian elimination with partial pivoting."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (M[r][n] - sum(M[r][k] * x[k] for k in range(r + 1, n))) / M[r][r]
    return x


def fit(X, y):
    """Least squares if p <= n; minimum-norm exact fit if p > n."""
    n, p = len(X), len(X[0])
    if p <= n:   # solve (X^T X) w = X^T y
        A = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(p)] for a in range(p)]
        rhs = [sum(X[i][a] * y[i] for i in range(n)) for a in range(p)]
        return solve(A, rhs)
    # solve (X X^T) c = y, then w = X^T c
    A = [[sum(X[i][k] * X[j][k] for k in range(p)) for j in range(n)] for i in range(n)]
    c = solve(A, y)
    return [sum(X[i][k] * c[i] for i in range(n)) for k in range(p)]


def trial(p, rng):
    X_full = [[rng.gauss(0, 1) for _ in range(D)] for _ in range(N_TRAIN)]
    y = [sum(a * b for a, b in zip(row, BETA)) + rng.gauss(0, NOISE) for row in X_full]
    X = [row[:p] for row in X_full]
    w = fit(X, y)
    train = sum((sum(a * b for a, b in zip(r, w)) - t) ** 2 for r, t in zip(X, y)) / N_TRAIN
    # error on a fresh case, averaged exactly: |w - beta|^2 (measurements are independent)
    w_full = w + [0.0] * (D - p)
    test = sum((a - b) ** 2 for a, b in zip(w_full, BETA))
    return train, test


def median(v):
    v = sorted(v)
    return v[len(v) // 2]


if __name__ == "__main__":
    classical = "--classical" in sys.argv
    rng = random.Random(7)
    sizes = [1, 2, 4, 6, 8, 10, 12, 15, 18, 20]
    if not classical:
        sizes += [22, 25, 30, 40, 60, 100, 200, 400]
    print(f"{N_TRAIN} training cases; the world uses {D} measurements; noise sd {NOISE}")
    print("test error = error on new cases, not counting the unavoidable noise")
    print("(guessing 0 every time scores 1.000)\n")
    print(f"{'parameters p':>12} {'train error':>12} {'test error':>12}")
    for p in sizes:
        results = [trial(p, rng) for _ in range(TRIALS)]
        tr = median([r[0] for r in results])
        te = median([r[1] for r in results])
        mark = "  <- interpolation threshold" if p == N_TRAIN else ""
        print(f"{p:>12} {tr:>12.3f} {te:>12.3f}{mark}")
