"""life.py -- Conway's Game of Life: a glider, and how long soups take to settle.

Pure Python, no libraries. Companion to what-is-emergence.md, stage 4a.

The rule (Conway 1970; Gardner's "Mathematical Games," Scientific American,
October 1970): on a grid of live and dead cells, count each cell's eight
neighbours.
  - a live cell with 2 or 3 live neighbours stays alive; otherwise it dies
  - a dead cell with exactly 3 live neighbours becomes alive
That's all.

Part 1: a glider. Five cells that rebuild themselves one cell down and one
right every 4 generations. Nothing in the rule mentions motion.

Part 2: random "soups". Fill a 24x24 torus at random and run until the
pattern repeats. How long that takes varies wildly from seed to seed, and
there is no known shortcut to finding out other than running it.
"""
import random

def step(live, W, H):
    counts = {}
    for (x, y) in live:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx or dy:
                    c = ((x + dx) % W, (y + dy) % H)
                    counts[c] = counts.get(c, 0) + 1
    return {c for c, n in counts.items()
            if n == 3 or (n == 2 and c in live)}

def show(frames, W, H):
    for y in range(H):
        print("   ".join("".join("#" if (x, y) in f else "." for x in range(W))
                         for f in frames))

def glider():
    W = H = 6
    g = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
    frames = [g]
    for _ in range(4):
        frames.append(step(frames[-1], W, H))
    print("GLIDER, generations 0-4 (6x6 torus)")
    print("   ".join(f"gen {i}".ljust(W) for i in range(5)))
    show(frames, W, H)
    shift = {((x + 1) % W, (y + 1) % H) for (x, y) in frames[0]}
    print("gen 4 == gen 0 moved one cell down-right:", frames[4] == shift)
    print("speed: 1 cell per 4 generations (c/4)\n")

def soup(seed, W=24, H=24, density=0.35, limit=5000):
    rng = random.Random(seed)
    live = {(x, y) for x in range(W) for y in range(H) if rng.random() < density}
    seen = {}
    for t in range(limit):
        key = frozenset(live)
        if key in seen:
            return seen[key], t - seen[key], len(live)
        seen[key] = t
        live = step(live, W, H)
    return None, None, len(live)

if __name__ == "__main__":
    glider()
    print("SOUPS (24x24 torus, 35% alive): generations until the pattern repeats")
    print("  seed   settles at   period   cells left")
    for seed in range(1, 9):
        t, p, n = soup(seed)
        if t is None:
            print(f"  {seed:4d}   > 5000")
        else:
            print(f"  {seed:4d}   {t:10d}   {p:6d}   {n:10d}")
