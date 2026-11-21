"""prequential.py — Grant's claims 2 and 3 as one number, in pure Python.

Companion to 'What Is Intelligence?' stage 4a.
A byte-level context model (orders 0-4, each smoothed toward the next-shorter
context) is the predictor; -log2 p of each byte is its code length, so the
totals below are real compressed sizes (arithmetic coding gets within 2 bits).

Target text: a chapter of fiction (path given as the first argument).
Base text:   English docstrings from Python's standard library -- a different
             genre, like Grant's model trained on Wikipedia then given Shakespeare.

Conditions:
  scratch, adapting      start empty (the "shared pseudo-random start"); learn as you go
  pretrained, static     trained on the base text; never updates
  pretrained, adapting   trained on the base text; keeps learning on the chapter
  pretrained, fast       same, but new evidence counts 4x (a higher learning rate)
  light prior, adapting  base text counted at 1/20 weight: a weak prior, easily overruled
Two-part ("Hutter") accounting adds the cost of sending the model, taken as the
prequential code length of the base text the model was trained on.
"""
import math, sys, zlib, lzma, importlib

K, BETA = 4, 2.0

class Model:
    def __init__(self):
        self.c = [dict() for _ in range(K + 1)]   # context -> {byte: count}
        self.n = [dict() for _ in range(K + 1)]   # context -> total
    def prob(self, hist, b):
        p = 1 / 256
        for k in range(K + 1):
            if k > len(hist): break
            ctx = hist[len(hist) - k:]
            tot = self.n[k].get(ctx)
            if tot:
                p = (self.c[k][ctx].get(b, 0) + BETA * p) / (tot + BETA)
        return p
    def update(self, hist, b, w=1):
        for k in range(K + 1):
            if k > len(hist): break
            ctx = hist[len(hist) - k:]
            d = self.c[k].setdefault(ctx, {})
            d[b] = d.get(b, 0) + w
            self.n[k][ctx] = self.n[k].get(ctx, 0) + w
    def contexts(self):
        return sum(len(d) for d in self.c)

def code(model, data, learn=True, w=1, block=None):
    """Prequential code length of data in bits; optionally per-block bits/byte."""
    total, curve, acc = 0.0, [], 0.0
    for i, b in enumerate(data):
        hist = data[max(0, i - K):i]
        bits = -math.log2(model.prob(hist, b))
        total += bits; acc += bits
        if learn: model.update(hist, b, w)
        if block and (i + 1) % block == 0:
            curve.append(acc / block); acc = 0.0
    return total, curve

def train(model, data, w=1):
    for i, b in enumerate(data):
        model.update(data[max(0, i - K):i], b, w)

def base_text(limit=200_000):
    names = ["os", "re", "json", "collections", "itertools", "functools", "math",
             "random", "string", "textwrap", "datetime", "calendar", "pathlib",
             "shutil", "subprocess", "threading", "queue", "socket", "email",
             "http.client", "urllib.request", "argparse", "logging", "unittest",
             "decimal", "fractions", "statistics", "csv", "sqlite3", "zipfile",
             "tarfile", "pickle", "copy", "inspect", "dataclasses", "enum",
             "typing", "asyncio", "contextlib", "heapq", "bisect", "difflib"]
    parts = []
    for name in names:
        try:
            mod = importlib.import_module(name)
        except Exception:
            continue
        for obj in [mod] + [getattr(mod, a, None) for a in sorted(dir(mod))]:
            doc = getattr(obj, "__doc__", None)
            if isinstance(doc, str) and len(doc) > 200:
                parts.append(doc.strip())
    seen, out = set(), []
    for p in parts:
        if p not in seen:
            seen.add(p); out.append(p)
    return "\n\n".join(out).encode("utf-8")[:limit]

chapter = open(sys.argv[1], "rb").read()
base = base_text()
n = len(chapter)
BLOCK = 2000
print("chapter: %d bytes   base text (stdlib docstrings): %d bytes" % (n, len(base)))
print("reference: zlib %.3f, lzma %.3f bits/byte on the chapter" %
      (8 * len(zlib.compress(chapter, 9)) / n, 8 * len(lzma.compress(chapter, preset=9)) / n))

model_cost, _ = code(Model(), base)                     # bits to send the base text
print("cost of sending the pretrained model (prequential size of base text): %.0f bytes"
      % (model_cost / 8))

results = {}
m = Model(); results["scratch, adapting"] = code(m, chapter, True, 1, BLOCK)
for label, learn, w, prior in [("pretrained, static", False, 1, 1),
                               ("pretrained, adapting", True, 1, 1),
                               ("pretrained, fast", True, 4, 1),
                               ("light prior, adapting", True, 1, 0.05)]:
    m = Model(); train(m, base, prior)
    results[label] = code(m, chapter, learn, w, BLOCK)

print("\n  %-22s %10s %10s %16s" % ("", "bits/byte", "bytes", "+ model (Hutter)"))
for label, (bits, _) in results.items():
    extra = 0 if label.startswith("scratch") else model_cost
    print("  %-22s %10.3f %10.0f %16.0f" % (label, bits / n, bits / 8, (bits + extra) / 8))

print("\nlearning curves: bits/byte in successive %d-byte blocks of the chapter" % BLOCK)
labels = list(results)
short = {"scratch, adapting": "scratch", "pretrained, static": "static",
         "pretrained, adapting": "adapting", "pretrained, fast": "fast",
         "light prior, adapting": "light"}
print("  block " + "".join("%11s" % short[l] for l in labels))
for j in range(n // BLOCK):
    print("  %5d " % (j + 1) + "".join("%11.3f" % results[l][1][j] for l in labels))