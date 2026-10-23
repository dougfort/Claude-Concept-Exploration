"""nfl.py — Wolpert's no-free-lunch theorem, checked by enumeration.

The world: 8 possible inputs (all 3-bit strings). A "target" is any rule
that labels each input 0 or 1. There are 2^8 = 256 possible targets.

The learner sees the labels on 4 training inputs and must guess the labels
on the other 4. We score only those 4 unseen inputs ("off-training-set").

Claim: averaged over all 256 targets, EVERY learner scores exactly 50%,
however clever or stupid. A learner only beats chance in a world that
matches its bias. This is Hume's argument as a counting result.

Pure Python, no libraries.
"""
from itertools import product

INPUTS = ["".join(b) for b in product("01", repeat=3)]  # 000 .. 111
TRAIN = ["000", "001", "010", "100"]
TEST = [x for x in INPUTS if x not in TRAIN]             # 011 101 110 111


def hamming(a, b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))


# ---------- learners: each maps (training labels) -> predicted label for x ----------

def always_zero(train, x):
    return 0


def majority(train, x):
    ones = sum(train.values())
    return 1 if ones > len(train) / 2 else 0


def anti_majority(train, x):
    return 1 - majority(train, x)


def nearest_neighbour(train, x):
    """Copy the label of the closest training input(s); vote on ties, ties -> 0."""
    d = min(hamming(x, t) for t in train)
    votes = [train[t] for t in train if hamming(x, t) == d]
    return 1 if sum(votes) > len(votes) / 2 else 0


def parity_fitter(train, x):
    """Assume the target is c XOR (some subset of bits): a 'parity' rule.
    The 4 training inputs determine c and the subset exactly."""
    c = train["000"]
    a = [train["100"] ^ c, train["010"] ^ c, train["001"] ^ c]
    return c ^ (sum(int(b) & ai for b, ai in zip(x, a)) % 2)


LEARNERS = {
    "always 0": always_zero,
    "majority": majority,
    "anti-majority": anti_majority,
    "nearest neighbour": nearest_neighbour,
    "parity fitter": parity_fitter,
}


# ---------- worlds: sets of targets ----------

def all_targets():
    for labels in product((0, 1), repeat=8):
        yield dict(zip(INPUTS, labels))


def threshold_targets():
    """'Smooth' world: label = 1 when a weighted vote of the bits clears a bar
    (the linearly separable rules, which a single artificial neuron can draw).
    Neighbouring inputs tend to share a label."""
    seen = set()
    for w in product(range(-3, 4), repeat=3):
        for bar in [b + 0.5 for b in range(-10, 10)]:
            labels = tuple(int(sum(wi * int(b) for wi, b in zip(w, x)) > bar) for x in INPUTS)
            seen.add(labels)
    return [dict(zip(INPUTS, labels)) for labels in sorted(seen)]


def parity_targets():
    """'Parity' world: the label is c XOR (sum of some subset of bits) mod 2."""
    out = []
    for c in (0, 1):
        for a in product((0, 1), repeat=3):
            out.append({x: c ^ (sum(int(b) & ai for b, ai in zip(x, a)) % 2) for x in INPUTS})
    return out


def score(learner, targets):
    right = total = 0
    for f in targets:
        train = {t: f[t] for t in TRAIN}
        for x in TEST:
            right += learner(train, x) == f[x]
            total += 1
    return right / total


if __name__ == "__main__":
    worlds = {
        "all 256 targets": list(all_targets()),
        f"threshold ({len(threshold_targets())})": threshold_targets(),
        "parity (16)": parity_targets(),
    }
    print(f"train on {TRAIN}, score on unseen {TEST}\n")
    print(f"{'learner':<20}" + "".join(f"{w:>20}" for w in worlds))
    for name, learner in LEARNERS.items():
        print(f"{name:<20}" + "".join(f"{score(learner, ts):>20.1%}" for ts in worlds.values()))
