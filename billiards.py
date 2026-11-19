"""billiards.py — Hume's billiard balls as a reversible program.

Two equal balls on a line, integer positions and velocities, one tick at a time.
Equal-mass elastic collision = the balls exchange velocities.
Pure Python, no libraries.

Shows:
  1. the forward film: A moves, hits B, A stops, B moves;
  2. the same law run on the reversed final state reproduces the start exactly;
  3. Hume's counterfactual definition, computed: remove a ball and see what
     the other does — in the forward film and in the reversed film.
"""

def step(balls):
    # balls: list of [name, pos, vel]
    (n1, x1, v1), (n2, x2, v2) = balls
    # would they meet or cross during this tick?
    if (x1 + v1 >= x2 + v2 and x1 < x2) or (x2 + v2 >= x1 + v1 and x2 < x1):
        v1, v2 = v2, v1                       # elastic, equal masses
    return [[n1, x1 + v1, v1], [n2, x2 + v2, v2]]

def step_one(ball):
    n, x, v = ball
    return [n, x + v, v]

def film(balls, ticks):
    frames = [balls]
    for _ in range(ticks):
        balls = step(balls) if len(balls) == 2 else [step_one(balls[0])]
        frames.append(balls)
    return frames

def show(frames, width=12):
    for t, balls in enumerate(frames):
        row = ["."] * width
        for n, x, v in balls:
            if 0 <= x < width:
                row[x] = n
        print(f"  t={t:2d}  {''.join(row)}   " +
              "  ".join(f"{n}: v={v:+d}" for n, x, v in balls))

def reverse(balls):
    return [[n, x, -v] for n, x, v in balls]

T = 8
start = [["A", 1, +1], ["B", 6, 0]]

print("1. Forward film (A struck toward B at rest)")
fwd = film(start, T)
show(fwd)

print("\n2. Reverse every velocity at the end and run the SAME law")
back = film(reverse(fwd[-1]), T)
show(back)
recovered = reverse(back[-1])
print("  reversed end, reversed again == start:", recovered == start)

print("\n3. Hume's second definition: 'if the first had not been, the second never had existed'")
noA = film([["B", 6, 0]], T)
print("  forward film without A: B ends at", noA[-1][0][1], "with v =", noA[-1][0][2],
      "(in the real film B ends at", fwd[-1][1][1], "with v =", fwd[-1][1][2], ")")
noB = film([["A", fwd[-1][0][1], 0]], T)  # reversed film's starting A, B removed
print("  reversed film without B: A ends at", noB[-1][0][1], "with v =", noB[-1][0][2],
      "(in the reversed film A ends at", back[-1][0][1], "with v =", back[-1][0][2], ")")
print("  -> forward: A's motion makes the difference to B; reversed: B's makes the difference to A.")
