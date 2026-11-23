"""aixi_toy.py — Legg-Hutter universal intelligence on three tiny environments.

Companion to universal-intelligence-and-aixi.md ('What Is Intelligence?').
Each environment hides a repeating pattern of correct actions (0 or 1). Each step
the agent acts; reward is 1 if the action matches the pattern, else 0. Because
actions are binary, the reward also tells the agent what the right action was.
   A  "always 0"           pattern 0            complexity K = 3 bits
   B  "alternate"          pattern 0 1          K = 5 bits
   C  "two ones, a zero"   pattern 1 1 0        K = 8 bits
Universal intelligence:  U(agent) = sum over environments of 2^-K * (average reward)
Agents:
   always-0    a specialist for the simplest world
   random      coin flips
   occam       a miniature Solomonoff/AIXI learner: it weights every repeating
               pattern of period 1-4 by 2^-(2 + 2*period) bits, drops those the
               rewards contradict, and acts on the weighted vote
Part 2 changes the reference machine (which world counts as simple) and reranks.
"""
import itertools, random

T = 12
ENVS = {"A": ((0,), 3), "B": ((0, 1), 5), "C": ((1, 1, 0), 8)}

def run(agent, pattern, rng):
    total, history = 0, []
    for t in range(T):
        a = agent(history, rng)
        correct = pattern[t % len(pattern)]
        r = 1 if a == correct else 0
        total += r
        history.append(correct)          # binary actions: reward reveals the right one
    return total / T

def always0(history, rng): return 0
def randomly(history, rng): return rng.randrange(2)

HYPS = [(p, 2.0 ** -(2 + 2 * len(p)))
        for n in range(1, 5) for p in itertools.product((0, 1), repeat=n)]
def occam(history, rng):
    votes = [0.0, 0.0]
    for p, w in HYPS:
        if all(history[t] == p[t % len(p)] for t in range(len(history))):
            votes[p[len(history) % len(p)]] += w
    return 0 if votes[0] >= votes[1] else 1

AGENTS = {"always-0": always0, "random": randomly, "occam": occam}

def table(envs, label):
    print("\n" + label)
    print("  %-10s" % "agent" + "".join("%8s" % ("%s(%d)" % (e, k)) for e, (_, k) in envs.items())
          + "%10s" % "U")
    for name, agent in AGENTS.items():
        rng = random.Random(0)
        vals = {e: sum(run(agent, p, rng) for _ in range(200)) / 200 for e, (p, _) in envs.items()}
        U = sum(2.0 ** -k * vals[e] for e, (_, k) in envs.items())
        print("  %-10s" % name + "".join("%8.3f" % vals[e] for e in envs) + "%10.4f" % U)

print("environment weights 2^-K:  " + ", ".join("%s %.4f" % (e, 2.0 ** -k) for e, (_, k) in ENVS.items()))
table(ENVS, "Part 1: average reward over %d steps, and universal intelligence U" % T)

SWAPPED = {"A": ((0,), 8), "B": ((0, 1), 5), "C": ((1, 1, 0), 3)}
table(SWAPPED, "Part 2: another reference machine, in which pattern C is short (3 bits) and A long (8)")
