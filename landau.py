"""landau.py -- Landau free energies, second-order vs first-order.

Pure Python, no libraries. Companion to what-is-emergence.md, stage 3a.

A phase is the value of the order parameter m that minimizes a free
energy F(m, T). Landau's idea: near a transition, write F as a short
polynomial in m that respects the symmetry m -> -m (only even powers).

  Second order:  F(m) = (T - 1) m^2 + m^4 / 2
                 The single minimum at m = 0 splits smoothly into two.
                 m* = sqrt(1 - T) below T = 1. No jump.

  First order:   F(m) = T m^2 - m^4 + m^6
                 A second pair of minima appears away from zero and
                 overtakes m = 0 at T = 1/4, where m* jumps from 0 to
                 sqrt(1/2) = 0.707. Between T = 0 and T = 1/3 both kinds
                 of minimum exist: one is the phase, the other is
                 metastable (supercooling / superheating).
"""

def second(m, T):
    return (T - 1) * m * m + m ** 4 / 2

def first(m, T):
    return T * m * m - m ** 4 + m ** 6

GRID = [i / 1000 for i in range(0, 1501)]   # m from 0 to 1.5 (F is even)

def minima(F, T):
    """Global minimum and all local minima of F on the grid."""
    vals = [F(m, T) for m in GRID]
    best = min(range(len(GRID)), key=lambda i: vals[i])
    local = []
    for i in range(len(GRID)):
        left = vals[i - 1] if i > 0 else vals[i + 1]   # mirror at m = 0
        right = vals[i + 1] if i + 1 < len(GRID) else float("inf")
        if vals[i] <= left and vals[i] < right:
            local.append(GRID[i])
    return GRID[best], local

def table(name, F, temps):
    print(name)
    print("   T     phase m*    all minima (m >= 0)")
    for T in temps:
        g, loc = minima(F, T)
        locs = ", ".join(f"{m:.3f}" for m in loc)
        print(f"  {T:5.3f}   {g:6.3f}      {locs}")
    print()

def hysteresis(F, temps_down):
    """Follow the nearest local minimum while cooling, then while heating."""
    def follow(temps, start):
        m, out = start, []
        for T in temps:
            # a small thermal nudge, then gradient descent from the current
            # m: the system can only slide downhill, it can't tunnel over a
            # barrier to a distant better minimum
            m = max(m, 0.01)
            for _ in range(20000):
                h = 1e-5
                g = (F(m + h, T) - F(m - h, T)) / (2 * h)
                m_new = max(0.0, m - 0.01 * g)
                if abs(m_new - m) < 1e-9:
                    break
                m = m_new
            out.append((T, m))
        return out
    down = follow(temps_down, 0.0)
    up = follow(list(reversed(temps_down)), down[-1][1])
    return down, up

if __name__ == "__main__":
    temps = [1.2, 1.0, 0.9, 0.75, 0.5, 0.25, 0.0]
    table("SECOND ORDER  F = (T-1) m^2 + m^4/2   (transition at T = 1)",
          second, temps)

    temps1 = [0.40, 0.34, 0.30, 0.26, 0.25, 0.24, 0.20, 0.10, 0.02]
    table("FIRST ORDER   F = T m^2 - m^4 + m^6   (transition at T = 0.25)",
          first, temps1)

    print("FIRST ORDER, following the system downhill (no jumps over barriers)")
    temps_h = [0.40, 0.34, 0.32, 0.30, 0.25, 0.20, 0.10, 0.05, 0.01, -0.01]
    down, up = hysteresis(first, temps_h)
    print("   T     cooling m    heating m")
    up_map = dict(up)
    for T, m in down:
        print(f"  {T:5.2f}    {m:6.3f}       {up_map[T]:6.3f}")
