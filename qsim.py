"""A tiny state-vector simulator, pure Python, no libraries.

A state of n qubits is a list of 2**n amplitudes. Qubit 0 is the leftmost
bit of the index, so for two qubits the list is [a00, a01, a10, a11].
Run:  python3 qsim.py
"""
from math import sqrt, log2

R = 1 / sqrt(2)
X = [[0, 1], [1, 0]]                 # bit flip
Z = [[1, 0], [0, -1]]                # phase flip
H = [[R, R], [R, -R]]                # Hadamard: |0> -> |+>, |1> -> |->
I2 = [[1, 0], [0, 1]]

def ket(*amps):                      # build a state from amplitudes
    return [complex(a) for a in amps]

def kron(a, b):                      # tensor product of two states
    return [x * y for x in a for y in b]

def bit(i, q, n):                    # value of qubit q in basis index i
    return (i >> (n - 1 - q)) & 1

def apply(s, U, q, n):               # one-qubit gate U on qubit q
    s, m = list(s), 1 << (n - 1 - q)
    for i in range(len(s)):
        if not i & m:
            a, b = s[i], s[i | m]
            s[i], s[i | m] = U[0][0]*a + U[0][1]*b, U[1][0]*a + U[1][1]*b
    return s

def cnot(s, c, t, n):                # flip qubit t where qubit c is 1
    s, mc, mt = list(s), 1 << (n - 1 - c), 1 << (n - 1 - t)
    for i in range(len(s)):
        if i & mc and not i & mt:
            s[i], s[i | mt] = s[i | mt], s[i]
    return s

def probs(s, qs, n):                 # outcome distribution for measuring qubits qs
    d = {}
    for i, a in enumerate(s):
        k = "".join(str(bit(i, q, n)) for q in qs)
        d[k] = d.get(k, 0) + abs(a) ** 2
    return {k: round(v, 6) for k, v in sorted(d.items()) if v > 1e-12}

def collapse(s, q, v, n):            # keep the branch where qubit q reads v
    t = [a if bit(i, q, n) == v else 0 for i, a in enumerate(s)]
    norm = sqrt(sum(abs(a) ** 2 for a in t))
    return [a / norm for a in t]

def rho1(s, q, n):                   # reduced 2x2 density matrix of qubit q
    r = [[0j, 0j], [0j, 0j]]
    m = 1 << (n - 1 - q)
    for i, a in enumerate(s):
        for j, b in enumerate(s):
            if (i | m) == (j | m):   # same values on every other qubit
                r[bit(i, q, n)][bit(j, q, n)] += a * b.conjugate()
    return r

def entropy(r):                      # von Neumann entropy of a 2x2 density matrix
    a, d, b = r[0][0].real, r[1][1].real, abs(r[0][1])
    gap = sqrt((a - d) ** 2 / 4 + b ** 2)
    return -sum(p * log2(p) for p in ((a + d) / 2 + gap, (a + d) / 2 - gap) if p > 1e-12)

def show(s):
    return "[" + ", ".join(f"{a.real:+.3f}" if abs(a.imag) < 1e-9 else f"{a:.3f}" for a in s) + "]"

def qubit_of(s, keep, n):            # read off one qubit's state when the others are fixed
    out = [0j, 0j]
    for i, a in enumerate(s):
        if abs(a) > 1e-12:
            out[bit(i, keep, n)] = a
    return out

if __name__ == "__main__":
    print("1. NO-CLONING: CNOT onto a blank target")
    for name, psi in [("|0>", ket(1, 0)), ("|1>", ket(0, 1)), ("|+>", ket(R, R))]:
        out = cnot(kron(psi, ket(1, 0)), 0, 1, 2)
        print(f"   {name}: got {show(out)}   a true copy would be {show(kron(psi, psi))}")

    print("\n2. HOLEVO: two bits written into one qubit, read with one measurement")
    states = {"00": ket(1, 0), "01": ket(0, 1), "10": ket(R, R), "11": ket(R, -R)}
    for basis, U in [("Z", I2), ("X", H)]:
        rows = {m: probs(apply(v, U, 0, 1), [0], 1) for m, v in states.items()}
        print(f"   measure {basis}: {rows}")

    print("\n3. SUPERDENSE CODING: share a Bell pair, send 1 qubit, deliver 2 bits")
    bell = cnot(apply(kron(ket(1, 0), ket(1, 0)), H, 0, 2), 0, 1, 2)
    print(f"   shared Bell pair {show(bell)}")
    for msg, ops in [("00", []), ("01", [X]), ("10", [Z]), ("11", [X, Z])]:
        s = bell
        for U in ops:
            s = apply(s, U, 0, 2)              # Alice acts on her half only
        s = apply(cnot(s, 0, 1, 2), H, 0, 2)   # Bob's Bell measurement
        print(f"   Alice sends {msg}: Bob reads {probs(s, [0, 1], 2)}")

    print("\n   TELEPORTATION: share a Bell pair, send 2 bits, deliver 1 qubit")
    psi = ket(0.6, 0.8)
    s = kron(psi, bell)                       # qubit 0 = psi, qubits 1,2 = Bell pair
    print(f"   Bob's qubit before any message: rho = "
          f"{[[round(x.real, 3) for x in row] for row in rho1(s, 2, 3)]}")
    s = apply(cnot(s, 0, 1, 3), H, 0, 3)      # Alice's Bell measurement
    for m0 in (0, 1):
        for m1 in (0, 1):
            b = collapse(collapse(s, 0, m0, 3), 1, m1, 3)
            if m1: b = apply(b, X, 2, 3)      # Bob's fix-up from the two bits
            if m0: b = apply(b, Z, 2, 3)
            print(f"   Alice gets {m0}{m1}: Bob's qubit {show(qubit_of(b, 2, 3))}")
    print(f"   original psi                    {show(psi)}")

    print("\n4. NEGATIVE CONDITIONAL ENTROPY: S(A|B) = S(AB) - S(B)")
    for name, s in [("product |00>", kron(ket(1, 0), ket(1, 0))), ("Bell pair", bell)]:
        sb = abs(entropy(rho1(s, 1, 2)))
        print(f"   {name}: S(AB) = 0 (pure), S(B) = {sb:.3f}, S(A|B) = {0 - sb:+.3f}")

    print("\n5. THREE-QUBIT BIT-FLIP CODE (2 extra qubits hold the syndrome)")
    n = 5
    s = kron(kron(ket(0.6, 0.8), ket(1, 0)), kron(ket(1, 0), kron(ket(1, 0), ket(1, 0))))
    s = cnot(cnot(s, 0, 1, n), 0, 2, n)       # 0.6|000> + 0.8|111>  (entangled, not copied)
    for err in (None, 0, 1, 2):
        t = apply(s, X, err, n) if err is not None else s
        t = cnot(cnot(t, 0, 3, n), 1, 3, n)   # ancilla 3 <- parity of qubits 0,1
        t = cnot(cnot(t, 1, 4, n), 2, 4, n)   # ancilla 4 <- parity of qubits 1,2
        syn = probs(t, [3, 4], n)
        flip = {"10": 0, "11": 1, "01": 2}.get(next(iter(syn)))
        if flip is not None:
            t = apply(t, X, flip, n)
        t = cnot(cnot(t, 0, 2, n), 0, 1, n)   # decode back onto qubit 0
        print(f"   error on {err}: syndrome {syn} -> fix {flip}; "
              f"data qubit {show(qubit_of(t, 0, n))}")
