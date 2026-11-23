"""curiosity.py — three motivations for choosing what to look at, and one
active-inference choice, in pure Python.

Companion to 'What Is Intelligence?' stage 4b.

Part 1. An agent can watch one of four streams per step (16-symbol alphabet):
   constant   always the same symbol                    (nothing to learn)
   noise      uniformly random                          (nothing CAN be learned)
   easy       a short repeating pattern (period 6)      (learnable fast)
   hard       a Markov chain, 2 likely successors each  (learnable slowly, to 1 bit)
 Each stream has its own adaptive predictor (orders 0-1, as in prequential.py).
 Three motivations choose the stream (10% of choices random):
   error-seeking     watch where recent surprise is highest
   comfort-seeking   watch where recent surprise is lowest
   progress-seeking  watch where recent surprise is FALLING fastest
                     (Schmidhuber's compression progress), measured as an
                     older moving average of surprise minus a recent one
Part 2. Shadow or puddle (freeenergy.py): drive on, slow down, or look closer?
 Expected free energy G = expected cost of outcomes under preferences
                          - expected information gain about the cause.
"""
import math, random

A, ORDER, BETA, STEPS, W, EPS = 16, 1, 1.0, 3000, 20, 0.10

class Predictor:
    def __init__(self):
        self.c = [dict() for _ in range(ORDER + 1)]
        self.n = [dict() for _ in range(ORDER + 1)]
        self.hist = ()
    def prob(self, s):
        p = 1 / A
        for k in range(ORDER + 1):
            if k > len(self.hist): break
            ctx = self.hist[len(self.hist) - k:]
            tot = self.n[k].get(ctx)
            if tot:
                p = (self.c[k][ctx].get(s, 0) + BETA * p) / (tot + BETA)
        return p
    def observe(self, s):
        bits = -math.log2(self.prob(s))
        for k in range(ORDER + 1):
            if k > len(self.hist): break
            ctx = self.hist[len(self.hist) - k:]
            d = self.c[k].setdefault(ctx, {})
            d[s] = d.get(s, 0) + 1
            self.n[k][ctx] = self.n[k].get(ctx, 0) + 1
        self.hist = (self.hist + (s,))[-ORDER:]
        return bits
    def score(self, s):
        """Code length of s, moving the context along but not learning."""
        bits = -math.log2(self.prob(s))
        self.hist = (self.hist + (s,))[-ORDER:]
        return bits

def make_streams(seed):
    rng = random.Random(seed)
    succ = {s: rng.sample(range(A), 2) for s in range(A)}      # hard chain
    state = {"easy": 0, "hard": 0}
    pattern = [3, 9, 1, 14, 6, 11]
    def constant(): return 5
    def noise(): return rng.randrange(A)
    def easy():
        state["easy"] += 1
        return pattern[state["easy"] % 6]
    def hard():
        state["hard"] = rng.choice(succ[state["hard"]])
        return state["hard"]
    return {"constant": constant, "noise": noise, "easy": easy, "hard": hard}

NAMES = ["constant", "noise", "easy", "hard"]

def run(motive, seed):
    rng = random.Random(seed)
    streams = make_streams(seed + 1000)
    pred = {k: Predictor() for k in NAMES}
    fast = {k: None for k in NAMES}     # moving averages of surprise (bits):
    slow = {k: None for k in NAMES}     # fast tracks recent, slow tracks older
    seen = {k: 0 for k in NAMES}
    chosen = []
    for t in range(STEPS):
        if t < 4 * W:
            k = NAMES[t % 4]                              # look at everything first
        elif rng.random() < EPS:
            k = rng.choice(NAMES)
        else:
            score = {"error":    lambda k: fast[k],
                     "comfort":  lambda k: -fast[k],
                     "progress": lambda k: slow[k] - fast[k]}[motive]   # falling surprise
            k = max(NAMES, key=lambda k: (score(k), rng.random()))
        bits = pred[k].observe(streams[k]())
        if fast[k] is None:
            fast[k] = slow[k] = bits
        fast[k] += 0.10 * (bits - fast[k])
        slow[k] += 0.02 * (bits - slow[k])
        seen[k] += 1
        chosen.append(k)
    # what did it learn? score each predictor on 300 fresh symbols WITHOUT learning
    knowledge = {}
    for k in NAMES:
        knowledge[k] = sum(pred[k].score(streams[k]()) for _ in range(300)) / 300
    return chosen, knowledge

print("Part 1: where each motivation looks (share of steps), and what it learns")
PHASES = 6
for motive in ("error", "comfort", "progress"):
    alloc = [{k: 0 for k in NAMES} for _ in range(PHASES)]
    know = {k: 0.0 for k in NAMES}
    SEEDS = 5
    for seed in range(SEEDS):
        chosen, knowledge = run(motive, seed)
        for t, k in enumerate(chosen):
            alloc[t * PHASES // STEPS][k] += 1
        for k in NAMES: know[k] += knowledge[k] / SEEDS
    print("\n  %s-seeking   (steps per phase = %d, averaged over %d runs)" %
          (motive, STEPS // PHASES, SEEDS))
    print("    %-10s" % "phase" + "".join("%9d" % (p + 1) for p in range(PHASES)) +
          "   bits/symbol after")
    per = STEPS // PHASES * SEEDS
    for k in NAMES:
        print("    %-10s" % k + "".join("%9.2f" % (alloc[p][k] / per) for p in range(PHASES)) +
              "   %8.2f" % know[k])
    excess = know["constant"] + know["easy"] + (know["hard"] - 1.0)
    print("    excess over the floor on the learnable streams (constant, easy, hard): %.2f bits"
          % excess)

print("\n  floors: constant 0, noise 4.00, easy 0, hard 1.00 bits/symbol")

# ---------------- Part 2 ----------------
def H(ps): return -sum(p * math.log2(p) for p in ps if p > 0)

def efe(p_puddle, cost, p_shine_if_puddle=0.9, p_shine_if_shadow=0.1, verbose=True):
    """Expected cost (bits) under preferences, info gain (bits), and G per policy."""
    def act_cost(pp):   # best of driving on or slowing down, given P(puddle)
        drive = (1 - pp) * cost["fine"] + pp * cost["skid"]
        slow = cost["delay"]
        return min((drive, "drive on"), (slow, "slow down"))
    rows = []
    d = (1 - p_puddle) * cost["fine"] + p_puddle * cost["skid"]
    rows.append(("drive on", d, 0.0))
    rows.append(("slow down", cost["delay"], 0.0))
    ps = p_puddle * p_shine_if_puddle + (1 - p_puddle) * p_shine_if_shadow
    pp_shine = p_puddle * p_shine_if_puddle / ps
    pp_dull = p_puddle * (1 - p_shine_if_puddle) / (1 - ps)
    c_shine, a_shine = act_cost(pp_shine)
    c_dull, a_dull = act_cost(pp_dull)
    risk = ps * c_shine + (1 - ps) * c_dull
    gain = H([p_puddle, 1 - p_puddle]) - (ps * H([pp_shine, 1 - pp_shine]) +
                                         (1 - ps) * H([pp_dull, 1 - pp_dull]))
    rows.append(("look closer, then act", risk, gain))
    if verbose:
        print("    P(shine) = %.2f; if shine P(puddle) = %.3f -> %s; "
              "if not P(puddle) = %.3f -> %s" % (ps, pp_shine, a_shine, pp_dull, a_dull))
        print("    %-24s %10s %10s %8s" % ("policy", "cost", "info gain", "G"))
        for name, r, g in rows:
            print("    %-24s %10.3f %10.3f %8.3f" % (name, r, g, r - g))
    return rows

def bits(p): return -math.log2(p)
print("\nPart 2: shadow or puddle, P(puddle) = 0.4 after the first glance")
print("  preferences as probabilities: fine 0.90, delay 0.09, skid 0.01")
pref = {"fine": bits(0.90), "delay": bits(0.09), "skid": bits(0.01)}
print("  costs in bits (-log2 preference): fine %.3f, delay %.3f, skid %.3f"
      % (pref["fine"], pref["delay"], pref["skid"]))
efe(0.4, pref)
print("\n  the same scene with nothing at stake (all outcomes equally preferred):")
flat = {"fine": bits(1 / 3), "delay": bits(1 / 3), "skid": bits(1 / 3)}
efe(0.4, flat)