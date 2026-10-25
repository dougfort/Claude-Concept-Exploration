"""compress.py — prediction is compression, measured.

A predictor reads a text one byte at a time. Before each byte it gives a
probability to every possible next byte. If the byte that actually comes
has probability p, an arithmetic coder can encode it in -log2(p) bits
(the whole file comes within 2 bits of the sum). So:

    compressed size = total surprise of the predictor, in bits.

Better prediction is exactly smaller files. We measure this for:
  - order-k predictors (k = 0..5): counts of what followed the last k bytes.
    A context seen rarely leans on the next-shorter context (back-off, the
    idea behind the PPM compressors); with no context, every byte gets the
    add-1/2 rule (Laplace's rule of succession, softened);
  - a MIXTURE of all six, each weighted by how well it has predicted so far
    (a tiny Bayesian / Solomonoff-style mixture over models);
  - Python's built-in compressors (zlib = gzip's method, bz2, lzma), for scale.

Nothing is transmitted about the model: the decoder rebuilds the same counts
as it decodes, so these sizes are complete. (A pretrained language model is
different: unless its weights count toward the size, it isn't a fair
comparison. See Deletang et al. 2024.)

Usage:  python3 compress.py [file.txt]
With no file, uses English documentation text collected from Python's own
standard library (numbers vary slightly between Python versions).

Pure Python, standard library only.
"""
import bz2
import importlib
import inspect
import lzma
import math
import sys
import zlib
from collections import defaultdict

ALPHA = 0.5     # smoothing: add 1/2 to every count (Krichevsky-Trofimov)
BETA = 1.0      # how much an unfamiliar context trusts the shorter one
ORDERS = range(6)


def default_corpus():
    mods = ["string", "textwrap", "collections", "itertools", "functools", "random",
            "statistics", "fractions", "decimal", "json", "csv", "pathlib", "argparse",
            "logging", "unittest", "threading", "subprocess", "email", "http.client",
            "urllib.request", "datetime", "calendar", "heapq", "bisect", "difflib"]
    seen, parts = set(), []
    for name in mods:
        try:
            m = importlib.import_module(name)
        except Exception:
            continue
        objs = [m] + [o for _, o in sorted(inspect.getmembers(m), key=lambda t: t[0])]
        for o in objs:
            d = inspect.getdoc(o) if (inspect.ismodule(o) or inspect.isclass(o)
                                     or inspect.isfunction(o)) else None
            if d and d not in seen:
                seen.add(d)
                parts.append(d)
    return "\n\n".join(parts).encode("utf-8", "ignore")


class Counts:
    """Shared counts for every context length 0..5."""
    def __init__(self):
        self.counts = defaultdict(lambda: defaultdict(int))
        self.totals = defaultdict(int)

    def update(self, ctx, b):
        for k in ORDERS:
            if k <= len(ctx):
                c = ctx[len(ctx) - k:]
                self.counts[c][b] += 1
                self.totals[c] += 1


class OrderK:
    """Predicts from the last k bytes. An unfamiliar context borrows its
    prediction from the next-shorter context (back-off), so a long context
    costs little until it has evidence; with no context at all, every byte
    gets the add-1/2 rule (Laplace's rule of succession, softened)."""
    def __init__(self, k, shared):
        self.k, self.c = k, shared

    def prob(self, ctx, b):
        p = (self.c.counts[b""][b] + ALPHA) / (self.c.totals[b""] + 256 * ALPHA)
        for j in range(1, min(self.k, len(ctx)) + 1):
            c = ctx[len(ctx) - j:]
            u = len(self.c.counts[c]) or 1     # distinct bytes seen here (Witten-Bell)
            p = (self.c.counts[c][b] + BETA * u * p) / (self.c.totals[c] + BETA * u)
        return p

    def update(self, ctx, b):
        pass  # counts are shared and updated once per byte


def run(data):
    shared = Counts()
    models = [OrderK(k, shared) for k in ORDERS]
    bits = [0.0] * len(models)
    mix_bits = 0.0
    logw = [0.0] * len(models)          # log2 weights, equal prior
    checkpoints = {len(data) // 10: None, len(data): None}
    snap = {}
    for i in range(len(data)):
        ctx, b = data[max(0, i - 5):i], data[i]
        ps = [m.prob(ctx, b) for m in models]
        # mixture probability: weighted average of the models' predictions
        top = max(logw)
        ws = [2 ** (lw - top) for lw in logw]
        p_mix = sum(w * p for w, p in zip(ws, ps)) / sum(ws)
        mix_bits -= math.log2(p_mix)
        for j, p in enumerate(ps):
            bits[j] -= math.log2(p)
            logw[j] += math.log2(p)       # Bayes: weight *= probability it gave
        shared.update(ctx, b)
        if i + 1 in checkpoints:
            snap[i + 1] = (bits[:], mix_bits)
    return snap


if __name__ == "__main__":
    data = open(sys.argv[1], "rb").read() if len(sys.argv) > 1 else default_corpus()
    n = len(data)
    print(f"text: {n:,} bytes  (8 bits per byte uncompressed)\n")
    snap = run(data)
    first, whole = n // 10, n
    print(f"{'predictor':<22}{'bits/byte, first 10%':>22}{'bits/byte, whole':>18}")
    for k in ORDERS:
        print(f"{'order-' + str(k) + ' context':<22}"
              f"{snap[first][0][k] / first:>22.3f}{snap[whole][0][k] / whole:>18.3f}")
    print(f"{'mixture of all six':<22}{snap[first][1] / first:>22.3f}{snap[whole][1] / whole:>18.3f}")
    print()
    for name, f in [("zlib (gzip's method)", lambda d: zlib.compress(d, 9)),
                    ("bz2", lambda d: bz2.compress(d, 9)),
                    ("lzma (xz)", lambda d: lzma.compress(d, preset=9))]:
        print(f"{name:<22}{8 * len(f(data[:first])) / first:>22.3f}{8 * len(f(data)) / whole:>18.3f}")
