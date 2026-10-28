"""mirage.py -- how a smooth model looks "emergent" through an all-or-nothing metric.

Pure Python, no libraries. Companion to what-is-emergence.md, stage 5a.
After Schaeffer, Miranda & Koyejo (2023), "Are Emergent Abilities of Large
Language Models a Mirage?"

A toy family of models. Per-token loss on some task falls as a power law in
parameter count N (as scaling laws say it does):

        loss(N) = 0.35 * (N / 1e7) ** -0.4         (nats per token)
        per-token accuracy p(N) = exp(-loss)

Nothing sudden happens anywhere in the model. Then score it three ways on
answers k tokens long:

  exact match      all k tokens right:        p ** k     (all-or-nothing)
  edit distance    expected wrong tokens:     k * (1 - p)    (graded)
  log-likelihood   of the whole answer:       -k * loss   (graded, smooth)

Finite-size test (stage 3b): a real transition gets SHARPER as its size
parameter grows. Here, make the answer longer (k up) and see whether the
exact-match switch from 10% to 90% narrows. It doesn't: it only moves.
"""
import math

def loss(N):
    return 0.35 * (N / 1e7) ** -0.4

def p_tok(N):
    return math.exp(-loss(N))

def exact(N, k):
    return p_tok(N) ** k

def switch(k, lo_q=0.1, hi_q=0.9):
    """log10 N where exact match reaches lo_q and hi_q (solved exactly)."""
    def at(q):
        target = -math.log(q) / k             # loss at which p**k == q
        return 7 + math.log10(0.35 / target) / 0.4
    return at(lo_q), at(hi_q)

if __name__ == "__main__":
    sizes = [10 ** e for e in (7, 8, 9, 10, 11, 12)]
    print("SAME MODELS, THREE METRICS (answers k = 20 tokens long)")
    print("  params    per-token  exact-match  wrong tokens  log-lik")
    for N in sizes:
        print(f"  1e{int(math.log10(N)):<2d}      {p_tok(N):.3f}      "
              f"{exact(N, 20):.3f}        {20*(1-p_tok(N)):5.2f}     "
              f"{-20*loss(N):6.2f}")
    print()
    print("EXACT MATCH vs ANSWER LENGTH k")
    print("  params " + "".join(f"   k={k:<4d}" for k in (1, 5, 20, 100)))
    for N in sizes:
        print(f"  1e{int(math.log10(N)):<2d}  " +
              "".join(f"   {exact(N, k):.3f} " for k in (1, 5, 20, 100)))
    print()
    print("FINITE-SIZE TEST: does the switch sharpen as k grows?")
    print("    k    10% at log10 N   90% at log10 N   width (decades)")
    for k in (1, 5, 20, 100, 1000):
        a, b = switch(k)
        print(f"  {k:4d}       {a:6.2f}           {b:6.2f}          {b - a:.2f}")
