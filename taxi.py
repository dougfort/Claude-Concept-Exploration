"""taxi.py — "predicts well, models badly": a toy of Vafa et al. (NeurIPS 2024).

A city is an 8 x 8 grid of intersections. About a quarter of the streets
are closed. A taxi ride is written as tokens: origin, destination, then
moves N, E, S, W along open streets, by a shortest route.

Two learners read the same 80% of all origin-destination rides:

  SURFACE  counts which move followed which context, and predicts the most
           frequent one. Context = everything so far (origin, destination,
           moves); if it has never seen that exact context it backs off to
           shorter ones: origin + moves, then destination + last 3 moves,
           then the last 3, 2, 1 moves. It has no idea of "where" it is.
           (This is compress.py's predictor, applied to rides.)

  MAP      keeps a position (dead reckoning from the origin), records which
           streets it has seen used, and plans a shortest route on that map.
           It has a world model by construction.

Then three tests, following Vafa et al.:
  1. Next-move validity on held-out rides: is each predicted move an open street?
  2. State test (their "compression" metric): two different ride prefixes that
     end at the same intersection should allow the same next moves.
  3. Whole rides with the learner driving, first on rides it was trained on
     and on held-out ones; then with detours: at each step, with probability
     p, force a random open street instead of the learner's choice. Does the
     ride still reach the destination on open streets?

Pure Python, no libraries.
"""
import random
from collections import Counter, defaultdict, deque

SIZE = 8
MOVES = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
rng = random.Random(11)


# ---------------------------------------------------------------- the city
def build_city(closed_fraction=0.25):
    nodes = [(x, y) for x in range(SIZE) for y in range(SIZE)]
    edges = set()
    for x, y in nodes:
        for m in "NE":
            dx, dy = MOVES[m]
            if 0 <= x + dx < SIZE and 0 <= y + dy < SIZE:
                edges.add(frozenset({(x, y), (x + dx, y + dy)}))
    for e in rng.sample(sorted(edges, key=sorted), len(edges)):
        if len(edges) <= (1 - closed_fraction) * 112:
            break
        edges.discard(e)
        if not connected(nodes, edges):
            edges.add(e)
    return nodes, edges


def step(p, m):
    return (p[0] + MOVES[m][0], p[1] + MOVES[m][1])


def open_moves(p, edges):
    return [m for m in "NESW" if frozenset({p, step(p, m)}) in edges]


def connected(nodes, edges):
    seen, todo = {nodes[0]}, [nodes[0]]
    while todo:
        p = todo.pop()
        for m in "NESW":
            q = step(p, m)
            if frozenset({p, q}) in edges and q not in seen:
                seen.add(q)
                todo.append(q)
    return len(seen) == len(nodes)


def shortest_route(o, d, edges):
    """BFS with a fixed move order, so every route is deterministic."""
    prev, todo = {o: None}, deque([o])
    while todo:
        p = todo.popleft()
        if p == d:
            break
        for m in "NESW":
            q = step(p, m)
            if frozenset({p, q}) in edges and q not in prev:
                prev[q] = (p, m)
                todo.append(q)
    route, p = [], d
    while prev[p]:
        p, m = prev[p]
        route.append(m)
    return route[::-1]


# ---------------------------------------------------------------- learners
class Surface:
    def __init__(self):
        self.table = defaultdict(Counter)

    def contexts(self, o, d, moves):
        m = "".join(moves)
        return [("full", o, d, m), ("orig", o, m), ("dest", d, m[-3:]),
                ("last", m[-3:]), ("last", m[-2:]), ("last", m[-1:]), ("none",)]

    def train(self, o, d, route):
        for i, mv in enumerate(route):
            for c in self.contexts(o, d, route[:i]):
                self.table[c][mv] += 1

    def deepest(self, o, d, moves):
        for c in self.contexts(o, d, moves):
            if self.table[c]:
                return self.table[c]

    def predict(self, o, d, moves):
        return self.deepest(o, d, moves).most_common(1)[0][0]

    def allowed(self, o, d, moves):
        return set(self.deepest(o, d, moves))


class Map:
    def __init__(self):
        self.seen = set()

    def train(self, o, d, route):
        p = o
        for m in route:
            q = step(p, m)
            self.seen.add(frozenset({p, q}))
            p = q

    def where(self, o, moves):
        p = o
        for m in moves:
            p = step(p, m)
        return p

    def predict(self, o, d, moves):
        p = self.where(o, moves)
        r = shortest_route(p, d, self.seen) if p != d else []
        return r[0] if r else rng.choice(open_moves(p, self.seen) or list("NESW"))

    def allowed(self, o, d, moves):
        return set(open_moves(self.where(o, moves), self.seen))


# ---------------------------------------------------------------- tests
def validity(model, rides, edges):
    ok = total = 0
    for o, d, route in rides:
        p = o
        for i in range(len(route)):
            ok += model.predict(o, d, route[:i]) in open_moves(p, edges)
            total += 1
            p = step(p, route[i])
    return ok / total


def state_test(model, rides, edges, pairs=3000):
    """Pairs of held-out prefixes ending at the same intersection, from
    different origins: do they get the same allowed-move set?"""
    at = defaultdict(list)
    for o, d, route in rides:
        p = o
        for i in range(len(route) + 1):
            at[p].append((o, d, route[:i]))
            if i < len(route):
                p = step(p, route[i])
    keys = [k for k in at if len(at[k]) > 1]
    same = n = 0
    while n < pairs:
        a, b = rng.sample(at[rng.choice(keys)], 2)
        if a[0] == b[0]:
            continue
        same += model.allowed(*a) == model.allowed(*b)
        n += 1
    return same / n


def detour_test(model, rides, edges, p_detour, trials=600):
    ok = 0
    for o, d, route in rng.sample(rides, trials):
        p, moves = o, []
        for _ in range(4 * SIZE * SIZE):
            if p == d:
                ok += 1
                break
            legal = open_moves(p, edges)
            m = rng.choice(legal) if rng.random() < p_detour else model.predict(o, d, moves)
            if m not in legal:
                break
            moves.append(m)
            p = step(p, m)
    return ok / trials


if __name__ == "__main__":
    nodes, edges = build_city()
    rides = [(o, d, shortest_route(o, d, edges)) for o in nodes for d in nodes if o != d]
    rng.shuffle(rides)
    cut = int(0.8 * len(rides))
    train, test = rides[:cut], rides[cut:]
    print(f"city: {len(nodes)} intersections, {len(edges)} open streets of 112; "
          f"{len(train)} training rides, {len(test)} held-out rides\n")

    learners = {"SURFACE": Surface(), "MAP": Map()}
    for L in learners.values():
        for r in train:
            L.train(*r)

    print("1. Next-move validity on held-out rides (is the predicted move an open street?)")
    for name, L in learners.items():
        print(f"   {name:<8} {validity(L, test, edges):.1%}")

    print("\n2. State test: same intersection, different history -> same allowed moves?")
    for name, L in learners.items():
        print(f"   {name:<8} {state_test(L, test, edges):.1%} of pairs agree")

    print("\n3. Whole rides, learner driving: fraction that arrive on open streets")
    print("   no detours:            training rides   held-out rides")
    for name, L in learners.items():
        print(f"   {name:<23}{detour_test(L, train, edges, 0.0):>14.0%}"
              f"{detour_test(L, test, edges, 0.0):>17.0%}")
    ps = [0.0, 0.01, 0.1, 0.5, 0.75]
    print("\n   with detours, on training rides (the routes it has seen):")
    print(f"   {'detour probability':<20}" + "".join(f"{p:>8.0%}" for p in ps))
    for name, L in learners.items():
        print(f"   {name:<20}" + "".join(f"{detour_test(L, train, edges, p):>8.0%}" for p in ps))
