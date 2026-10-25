"""implicit_bias.py — which exact fit does gradient descent pick?

When a model has more parameters than equations, infinitely many settings
fit the data exactly. Gradient descent doesn't choose at random among them.
Started from zero on squared error, it finds the one with the smallest
weights: the minimum-norm fit. Nobody asked for that; it is a property of
the procedure. That is "implicit bias."

Part 1: one equation, two unknowns, by hand-sized numbers.
Part 2: 3 equations, 6 unknowns, gradient descent against the closed-form
        minimum-norm answer.
Part 3: the starting point matters. Start elsewhere, get a different fit
        that is equally exact.

Pure Python, no libraries.
"""
import random


def gd(X, y, w0, lr=0.02, steps=20000):
    w = w0[:]
    for _ in range(steps):
        r = [sum(a * b for a, b in zip(row, w)) - t for row, t in zip(X, y)]
        g = [sum(r[i] * X[i][k] for i in range(len(X))) for k in range(len(w))]
        w = [wk - lr * gk for wk, gk in zip(w, g)]
    return w


def solve(A, b):
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


def min_norm(X, y):
    n, p = len(X), len(X[0])
    A = [[sum(X[i][k] * X[j][k] for k in range(p)) for j in range(n)] for i in range(n)]
    c = solve(A, y)
    return [sum(X[i][k] * c[i] for i in range(n)) for k in range(p)]


def fmt(w):
    return "(" + ", ".join(f"{v:6.3f}" for v in w) + ")"


def norm(w):
    return sum(v * v for v in w) ** 0.5


def residual(X, y, w):
    return max(abs(sum(a * b for a, b in zip(row, w)) - t) for row, t in zip(X, y))


if __name__ == "__main__":
    print("1. One equation, two unknowns:  w1 + 2*w2 = 5")
    X, y = [[1.0, 2.0]], [5.0]
    for name, w in [("(5, 0)", [5, 0]), ("(1, 2)", [1, 2]), ("(-1, 3)", [-1, 3])]:
        print(f"   exact fit {name:<8} size (norm) = {norm(w):.3f}")
    w = gd(X, y, [0.0, 0.0])
    print(f"   gradient descent from (0, 0) -> {fmt(w)}  norm {norm(w):.3f}")

    print("\n2. Three equations, six unknowns")
    rng = random.Random(4)
    X = [[rng.gauss(0, 1) for _ in range(6)] for _ in range(3)]
    y = [rng.gauss(0, 1) for _ in range(3)]
    w_gd = gd(X, y, [0.0] * 6, lr=0.02, steps=50000)
    w_mn = min_norm(X, y)
    print(f"   gradient descent from 0: {fmt(w_gd)}  fit error {residual(X, y, w_gd):.1e}")
    print(f"   minimum-norm formula:    {fmt(w_mn)}  fit error {residual(X, y, w_mn):.1e}")

    print("\n3. Same data, different starting points")
    for start in ([0.0] * 6, [1.0] * 6, [rng.gauss(0, 2) for _ in range(6)]):
        w = gd(X, y, start, lr=0.02, steps=50000)
        print(f"   start {fmt(start)} -> norm {norm(w):.3f}, fit error {residual(X, y, w):.1e}")
