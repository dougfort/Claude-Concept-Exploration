"""Three toy state spaces, and what each one allows. Pure Python.

  classical bit : a line segment  (2 pure states)
  rebit / qubit : a disk          (a slice of the Bloch ball; a circle of pure states)
  gbit          : a square        (4 pure states, the PR-box world)

A state is a point (x, y): x is the expected value (+1/-1) of measurement X,
y of measurement Y. Mixing two states = taking a point between them.
Run:  python3 gpt.py      (also writes gpt_shapes.svg)
"""
from math import cos, sin, pi, sqrt, log2, isclose
from itertools import combinations

SHAPES = {
    "classical bit (segment)": [(1, 0), (-1, 0)],
    "qubit slice (disk)":      [(cos(2*pi*k/8), sin(2*pi*k/8)) for k in range(8)],
    "gbit (square)":           [(1, 1), (1, -1), (-1, -1), (-1, 1)],
}
# reversible transformations that are continuous: rotations of the disk only.
CONTINUOUS = {"classical bit (segment)": False, "qubit slice (disk)": True, "gbit (square)": False}

def mid(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)

def same(p, q):
    return isclose(p[0], q[0], abs_tol=1e-9) and isclose(p[1], q[1], abs_tol=1e-9)

def two_decompositions(pure):
    """Find one mixed state that is a 50/50 mix of two *different* pairs of pure states."""
    pairs = list(combinations(pure, 2))
    for (a, b), (c, d) in combinations(pairs, 2):
        if same(mid(a, b), mid(c, d)):
            return (a, b), (c, d)
    return None

def copy_correlation(pair, i, j):
    """If a linear copier sends each pure state s to s (x) s, a 50/50 mix of the pair
    goes to the 50/50 mix of the copies. Correlation of coordinate i of copy 1 with
    coordinate j of copy 2 in that mixture:"""
    return sum(s[i] * s[j] for s in pair) / 2

def H(p):
    return 0 if p in (0, 1) else -p*log2(p) - (1-p)*log2(1-p)

if __name__ == "__main__":
    print("A. CAN THE PURE STATES BE COPIED?  (linearity test)")
    for name, pure in SHAPES.items():
        found = two_decompositions(pure)
        if not found:
            print(f"  {name}: every mixed state has ONE decomposition -> a copier exists")
            continue
        (a, b), (c, d) = found
        m = mid(a, b)
        x1 = copy_correlation((a, b), 0, 1)
        x2 = copy_correlation((c, d), 0, 1)
        r = lambda s: tuple(round(v, 2) + 0.0 for v in s)
        print(f"  {name}: state ({m[0]:+.2f},{m[1]:+.2f}) = mix of {r(a)},{r(b)} AND of {r(c)},{r(d)}")
        print(f"      copier must give <X1 Y2> = {round(x1, 9) + 0.0:+.2f} and {x2:+.2f} at once -> NO copier")

    print("\nB. CONTINUOUS REVERSIBLE PATH BETWEEN PURE STATES? (Hardy's continuity axiom)")
    for name in SHAPES:
        print(f"  {name}: {'yes (rotations)' if CONTINUOUS[name] else 'no: only finitely many symmetries'}")

    print("\nC. LOCAL TOMOGRAPHY: parameters to describe one system (K) and a pair")
    rows = [("classical bit", 2, 4), ("qubit (complex)", 4, 16),
            ("rebit (real)", 3, 10), ("gbit", 3, 9)]
    for name, k, pair in rows:
        ok = "OK" if pair == k * k else f"FAILS ({pair} != {k}x{k}={k*k})"
        print(f"  {name:16s} K = {k}, pair needs {pair:2d}: {ok}")

    print("\nD. BOXES: Alice inputs x, Bob y, outputs a, b; win if a XOR b == x AND y")
    for name, p in [("classical best", 0.75), ("quantum best (Tsirelson)", (1 + 1/sqrt(2)) / 2),
                    ("PR box", 1.0)]:
        print(f"  {name:26s} win prob {p:.3f}   CHSH = {8*p - 4:.3f}")

    print("\nE. PR BOX AS A RANDOM-ACCESS MEMORY: Alice has bits a0,a1; sends ONE bit")
    for a0 in (0, 1):
        for a1 in (0, 1):
            for b in (0, 1):                      # which bit Bob wants
                x, y = a0 ^ a1, b                 # box inputs
                A = 0                             # PR box: any A, then B = A ^ (x & y)
                B = A ^ (x & y)
                m = a0 ^ A                        # the one bit Alice sends
                guess = m ^ B
                assert guess == (a0, a1)[b]
    print("  all 8 cases: Bob recovers whichever bit he wants -> 2 bits from 1 sent")

    print("\nF. INFORMATION CAUSALITY for a box that wins with probability p")
    print("     p      one-level sum I   many-level test 2E^2 (E=2p-1)   IC?")
    for p in (0.75, 0.80, (1 + 1/sqrt(2)) / 2, 0.86, 0.90, 1.0):
        E = 2 * p - 1
        one = 2 * (1 - H(p))
        print(f"   {p:.3f}       {one:.3f}              {2*E*E:.3f}             "
              f"{'violated' if 2*E*E > 1 + 1e-9 else ('boundary' if 2*E*E > 1 - 1e-9 else 'ok')}")

    # --- picture ---
    W, S = 660, 90
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="260" '
           f'font-family="sans-serif" font-size="13">',
           '<rect width="100%" height="100%" fill="white"/>']
    for k, (name, pure) in enumerate(SHAPES.items()):
        cx, cy = 110 + 220 * k, 120
        if "disk" in name:
            out.append(f'<circle cx="{cx}" cy="{cy}" r="{S}" fill="#dde8f5" stroke="#246"/>')
        else:
            pts = " ".join(f"{cx + S*x},{cy - S*y}" for x, y in pure)
            out.append(f'<polygon points="{pts}" fill="#dde8f5" stroke="#246" stroke-width="2"/>')
        for x, y in pure:
            out.append(f'<circle cx="{cx + S*x}" cy="{cy - S*y}" r="5" fill="#246"/>')
        out.append(f'<text x="{cx}" y="245" text-anchor="middle">{name}</text>')
    out.append("</svg>")
    with open("gpt_shapes.svg", "w") as f:
        f.write("\n".join(out))
    print("\n(wrote gpt_shapes.svg)")
