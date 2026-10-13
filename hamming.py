from functools import reduce
from operator import xor
import random

DATA_POS = [3, 5, 6, 7]          # positions 1..7; parity bits at 1, 2, 4

def encode(d):                   # d: list of 4 bits
    c = [0] * 8                  # index 0 unused, so positions are 1..7
    for pos, bit in zip(DATA_POS, d):
        c[pos] = bit
    for p in (1, 2, 4):          # parity p covers every position whose index has bit p set
        c[p] = reduce(xor, (c[i] for i in range(1, 8) if i & p and i != p))
    return c[1:]

def syndrome(word):              # XOR of the positions holding a 1
    return reduce(xor, (i for i, b in enumerate(word, start=1) if b), 0)

def decode(word):
    w = list(word)
    s = syndrome(w)
    if s:                        # s is the address of the flipped bit
        w[s - 1] ^= 1
    return [w[p - 1] for p in DATA_POS], s

if __name__ == "__main__":
    d = [1, 0, 1, 1]
    c = encode(d)
    print("data    ", d)
    print("codeword", "".join(map(str, c)), " syndrome", syndrome(c))
    bad = c.copy(); bad[5] ^= 1  # flip position 6
    print("received", "".join(map(str, bad)), " syndrome", syndrome(bad))
    print("decoded ", decode(bad))
    # exhaustive check: every data word, every single-bit error
    ok = all(decode([b ^ (i == j) for i, b in enumerate(encode(
        [(n >> k) & 1 for k in range(4)]))])[0] == [(n >> k) & 1 for k in range(4)]
        for n in range(16) for j in range(7))
    print("all 16 x 7 single errors corrected:", ok)
