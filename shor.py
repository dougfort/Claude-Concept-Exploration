"""Shor's nine-qubit code (1995) on the qsim state-vector simulator.

Corrects ANY error on ONE qubit: bit flips (X), phase flips (Z), both (Y),
and continuous small rotations, which syndrome measurement turns into
"no error" or "a flip". Needs qsim.py in the same folder.
Run:  python3 shor.py
"""
import random
from math import cos, sin, sqrt
from qsim import ket, kron, apply, cnot, H, X, Z, show, qubit_of

N = 9

def encode(psi):
    s = psi
    for _ in range(8):
        s = kron(s, ket(1, 0))
    s = cnot(cnot(s, 0, 3, N), 0, 6, N)          # phase-flip layer: 3 blocks
    for q in (0, 3, 6):
        s = apply(s, H, q, N)
    for b in (0, 3, 6):                          # bit-flip layer inside each block
        s = cnot(cnot(s, b, b + 1, N), b, b + 2, N)
    return s

def decode(s):
    for b in (0, 3, 6):
        s = cnot(cnot(s, b, b + 2, N), b, b + 1, N)
    for q in (0, 3, 6):
        s = apply(s, H, q, N)
    return cnot(cnot(s, 0, 6, N), 0, 3, N)

def fix_phase(v):
    """An overall sign or phase is unobservable; normalize so the first amplitude is positive."""
    a = next(x for x in v if abs(x) > 1e-9)
    return [x * abs(a) / a for x in v]

def pauli(s, kind, qubits):
    for q in qubits:
        s = apply(s, X if kind == "X" else Z, q, N)
    return s

def measure(s, kind, qubits):
    """Projectively measure the stabilizer kind^{qubits}; return (+1/-1, new state)."""
    t = pauli(s, kind, qubits)
    plus = [(a + b) / 2 for a, b in zip(s, t)]
    minus = [(a - b) / 2 for a, b in zip(s, t)]
    p_plus = sum(abs(a) ** 2 for a in plus)
    if random.random() < p_plus:
        return +1, [a / sqrt(p_plus) for a in plus]
    return -1, [a / sqrt(1 - p_plus) for a in minus]

Z_CHECKS = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8)]   # catch bit flips
X_CHECKS = [(0, 1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 8)]             # catch phase flips

def correct(s):
    syn = []
    for c in Z_CHECKS:
        v, s = measure(s, "Z", c); syn.append(v)
    for b in range(3):                         # which qubit in block b flipped?
        z1, z2 = syn[2 * b], syn[2 * b + 1]
        q = {(-1, 1): 0, (-1, -1): 1, (1, -1): 2}.get((z1, z2))
        if q is not None:
            s = apply(s, X, 3 * b + q, N)
    xs = []
    for c in X_CHECKS:
        v, s = measure(s, "X", c); xs.append(v)
    blk = {(-1, 1): 0, (-1, -1): 1, (1, -1): 2}.get(tuple(xs))
    if blk is not None:
        s = apply(s, Z, 3 * blk, N)            # Z on any qubit of the block works
    return s, syn, xs

if __name__ == "__main__":
    random.seed(7)
    psi = ket(0.6, 0.8)
    enc = encode(psi)
    rot = lambda th: [[cos(th), -1j * sin(th)], [-1j * sin(th), cos(th)]]  # small X rotation
    cases = [("none", None, None), ("X on 4", X, 4), ("Z on 4", Z, 4),
             ("Y on 7 (X and Z)", "Y", 7), ("rotation 0.3 rad on 2", rot(0.3), 2)]
    for name, U, q in cases:
        s = enc
        if U == "Y":
            s = apply(apply(s, X, q, N), Z, q, N)
        elif U is not None:
            s = apply(s, U, q, N)
        s, zs, xs = correct(s)
        out = fix_phase(qubit_of(decode(s), 0, N))
        print(f"{name:24s} Z-checks {''.join('+' if v > 0 else '-' for v in zs)}  "
              f"X-checks {''.join('+' if v > 0 else '-' for v in xs)}  -> {show(out)}")

    print("\nThe rotation, 2000 times: how often does the syndrome say 'flip on 2'?")
    flips, good = 0, 0
    for _ in range(2000):
        s, zs, _ = correct(apply(enc, rot(0.3), 2, N))
        flips += zs[0] > 0 and zs[1] < 0
        out = fix_phase(qubit_of(decode(s), 0, N))
        good += abs(out[0] - 0.6) < 1e-9 and abs(out[1] - 0.8) < 1e-9
    print(f"  {flips / 2000:.3f}   (sin^2 0.3 = {sin(0.3) ** 2:.3f});  decoded to [0.6, 0.8] in {good}/2000 runs")
