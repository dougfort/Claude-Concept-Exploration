# What Is a Wave?

*Notes from a conversation, September 2026. From the vibrating string to Maxwell to the wave function.*

---

## 1. A working definition

**A wave is a pattern that travels through something without that something traveling with it.**

The pattern moves. The medium — water, air, string, field — stays put; each piece wiggles locally and hands the disturbance to its neighbor. A wave transports energy, momentum, and information, but not stuff. In a stadium wave, no one changes seats.

Distinctions worth keeping:

- **Oscillation vs. wave.** A pendulum oscillates but nothing propagates. A wave is oscillation with spatial extent that moves.
- **Wave vs. periodic wave.** Sine waves dominate textbooks, but a single pulse down a rope is fully a wave. Sinusoids matter because everything decomposes into them, not because waves are inherently repetitive.
- **Wave vs. medium.** Until 1905 everyone assumed a wave needed a medium. Electromagnetism broke that: the field is its own medium, or there is no medium — the same statement.

The mathematician's fallback definition — "a solution to a wave-type equation" — is precise and circular. The history from 1747 to 1865 is the story of the mathematical definition swallowing the physical one.

---

## 2. Where the concept came from

The mathematical concept of a wave does not come from water or light. It comes from the vibrating string in the 1740s, and the argument it started is the argument that produced modern analysis.

**Precursors, no mathematics:**
- Huygens (1678): light as a disturbance in an ether, each point on a wavefront a new source. Geometric, not analytic.
- Newton (1687): derived the speed of sound from first principles (15% off; Laplace fixed it in 1816). But Newton's corpuscular theory of light buried Huygens for a century.

**The origin — d'Alembert, 1747.** The one-dimensional wave equation for a stretched string, u_tt = c²u_xx, with solution u = f(x − ct) + g(x + ct). Any shape at all, translating rigidly at speed c. The equation, not the medium, defines what a wave is.

**Light joins:** Young (1801) showed interference fringes. Fresnel (1818) gave the full wave theory; Poisson objected it predicted a bright spot at the center of a circular shadow; Arago checked, and the spot was there.

**Maxwell (1865)** found that his equations for electricity and magnetism implied a wave traveling at the speed of light. Hertz confirmed radio waves in 1887.

---

## 3. The vibrating-string dispute and how it built the Hilbert space

Setup: u_tt = c²u_xx on [0, L], fixed ends, initial shape f(x), zero initial velocity.

### The positions

- **D'Alembert (1747):** u = ½[f(x − ct) + f(x + ct)], but f must be a single analytic expression. His reason was sound: the equation has second derivatives.
- **Euler (1748):** A plucked string is a triangle — two expressions glued at a corner. So f must be any curve you can draw. Euler quietly changed the definition of function to fit the physics.
- **D. Bernoulli (1753):** Every motion is a superposition of modes, u = Σ bₙ sin(nπx/L) cos(nπct/L). Argued from overtones; had no formula for bₙ.
- **Euler against Bernoulli:** a sum of sines is analytic, so it can't equal a triangle. Wrong, but the best mathematician alive said it.
- **D'Alembert against Bernoulli:** the triangle has no second derivative at the corner, so it isn't a solution at all. Correct by every standard until the 1930s.
- **Lagrange (1759):** nearly derived the Fourier coefficient formula while trying to defend d'Alembert, and didn't see it.

### Why it couldn't be resolved

Three concepts didn't exist: what a *function* is, what an infinite *sum* means, and what *equality* of functions means. Everyone argued "is f a sum of sines?" without agreeing on "is," "f," or "sum."

### The rigor cascade

- **Fourier (1807/1822):** any function is a sum of sines and cosines, with bₙ = (2/L)∫ f(x) sin(nπx/L) dx. The proof was worthless; the formula was right. Crucially, it only needs f to be *integrable* — Fourier sidestepped the dispute by asking only for integrals against sines.
- **Dirichlet (1829):** first correct convergence proof (piecewise monotone f). Also stated the modern definition of function and gave the indicator of the rationals as one you can't integrate.
- **Riemann (1854):** asked which functions have Fourier coefficients; invented the Riemann integral to answer.
- **Cantor (1870–72):** uniqueness of trigonometric series → derived sets → set theory. Transfinite numbers descend from the string.
- **Du Bois-Reymond (1873):** a *continuous* function whose Fourier series diverges at a point. Pointwise convergence was the wrong notion.

### The resolution

- **Lebesgue (1902)** replaced the integral.
- **Riesz–Fischer (1907):** L²[0, L] is complete, and f ↦ (bₙ) is an isometry onto ℓ². Every square-integrable function has a Fourier series converging to f *in L² norm*; Parseval holds.

Read against 1753:
- Bernoulli was right: every configuration is a superposition of modes.
- Euler was right that the shape is arbitrary — arbitrary now meaning any element of L².
- Euler was wrong that sines can't make a triangle; the corner survives because L² convergence ignores single points.
- D'Alembert's objection about the corner was right, resolved only by **weak solutions** (Sobolev, Schwartz, 1930s–40s): "solves the equation" redefined as solving it against test functions. Fourier's move again.
- The silent casualty: **equality**. Functions differing on a set of measure zero are the same element of L².

### The structural picture

Take A = −d²/dx² with Dirichlet boundary conditions. It is self-adjoint on the right domain in L². Eigenfunctions sin(nπx/L), eigenvalues (nπ/L)², forming an orthonormal basis. The Fourier coefficient bₙ is the inner product ⟨f, eₙ⟩. Bernoulli's mode expansion *is* the spectral theorem for A; the wave equation decouples into independent harmonic oscillators, one per eigenvalue.

This is the exact template for quantum mechanics: state as vector, observable as self-adjoint operator, dynamics as diagonalization. It was all present in a stretched string in 1753. Nobody could see it because "vector" meant an arrow.

---

## 4. The abstract nature of a wave

Two examples strip away what makes the string look special.

**The traffic jam.** Cars all move forward. The jam moves *backward*, at about 20 km/h against the flow, regardless of car speed. The jam persists for an hour; no car is in it for more than a minute. What propagates is a relation among stuff, with its own velocity, lifetime, and identity that belong to none of the parts.

**The stadium (Mexican) wave.** No force, no tension, no inertia. Each person follows a rule: stand when your neighbor stands, then sit. The result has a speed (~12 m/s), a width, a direction, and a threshold. A wave is a consequence of a local rule plus a spatial arrangement.

### Three families of wave

The string's mechanism (restoring force + inertia) is one way to get a wave, not what a wave is.

1. **Oscillatory** — restoring force + inertia. Strings, sound, light.
2. **Kinematic** — conservation + a flow rate depending on density. Traffic, floods.
3. **Excitable** — rest → triggered by neighbor → fire → refractory. Stadium waves, nerve impulses, forest fires, dominoes, cardiac rhythm.

No shared equation.

### What they share

- A quantity spread over space.
- Each location changes only in response to immediate neighbors.
- That locality forces disturbances to spread at a finite speed set by the rules, not the parts.

**A wave is what locality looks like from the outside.** Any world where influence passes only neighbor to neighbor will have waves, whatever the neighbors are made of.

Ontologically, a rock is a persistence of matter; a wave is a persistence of pattern with total turnover of matter. It exists at a level above its substrate, like a melody or a word. This is what made the electromagnetic case swallowable: once the traffic jam is real, has a velocity, and is made of nothing in particular, the field is only one step further.

---

## 5. From locality to Maxwell (and Heaviside)

**Faraday's move (1830s):** replace action at a distance with a *field* — a quantity at every point in space, obeying local rules. He treated lines of force as physically real. Nobody took the ontology seriously except Faraday; Maxwell did.

**Vocabulary for local rules:**
- **Divergence** — is the field spreading out from here (source) or converging (drain)?
- **Curl** — is the field swirling around here (a paddle wheel would spin)?

Both are computed from an arbitrarily small neighborhood. Any law stated with them is a neighbor-to-neighbor rule.

**The four rules (Maxwell, 1861–65):**
1. Electric field lines start and end on charges. (div E = charge density — Gauss.)
2. Magnetic field lines never start or end. (div B = 0.)
3. A changing magnetic field makes the electric field curl around it. (Faraday's induction.)
4. A current makes the magnetic field curl around it (Ampère) — **and so does a changing electric field** (Maxwell's addition, the displacement current).

Rule 4's second clause is the whole story. Maxwell added it for consistency (charge conservation in a charging capacitor) and dressed it in a mechanical ether he later discarded. The scaffolding was fake; the term was right.

**Why it makes a wave:** in empty space, a changing B makes a curling E; a changing E makes a curling B. Neither can change without creating the other next door. It's the stadium-wave rule with two quantities taking turns. Combining the curl equations, each field satisfies d'Alembert's equation with speed 1/√(μ₀ε₀) — computed from benchtop constants as ~310,000 km/s, matching the measured speed of light. The field is its own medium.

**Heaviside (1884–85):** Maxwell published twenty component equations in twenty unknowns, organized around potentials. Heaviside — self-taught, ex-telegraph operator — invented the vector notation (div, curl), dropped the potentials, and reduced it to the four "duplex" equations everyone learns. He chose the name "Maxwell's equations" out of deference. Hertz did similar work independently. Heaviside also derived the telegrapher's equations and distortionless transmission. A radio engineer of the 1920s works in Heaviside's world.

**One sentence:** Maxwell wrote local rules for two fields, found the rules force each to keep generating the other, and the speed of that chain reaction was the speed of light.

---

## 6. The quantum wave function

### The descent is genealogical

- Einstein (1905): Maxwell's wave exchanges energy in lumps — photons.
- De Broglie (1924): ran it backwards — particles have wavelength h/p.
- Schrödinger (1926): used Hamilton's 1830s optical–mechanical analogy. Geometric optics is the short-wavelength limit of wave optics; if classical mechanics is the "ray" version, what is the wave version? His equation.
- Von Neumann (1932): a state is a vector in a Hilbert space.

The mathematics is the same: linear, superposition, decomposition into eigenmodes of a self-adjoint operator (the Hamiltonian), each evolving independently. Bernoulli's mode expansion, on the Riesz–Fischer machinery.

### Where it stops being a wave in our sense

In increasing order of seriousness:

1. **Dispersive.** First-order in time; different wavelengths travel at different speeds; packets spread.
2. **Complex-valued.** The phase is unobservable directly but physically decisive — it interferes.
3. **Unobservable.** Only |ψ|² appears, as a probability density; measurement changes ψ discontinuously.
4. **Not in space.** Two particles have one wave function on 6-dimensional configuration space; N particles, 3N dimensions. Every classical wave, including light, is a pattern *somewhere*. The wave function is not somewhere.

### What it is, relative to our definition

The traffic jam dropped the requirement of a permanent substrate. Light dropped the substrate but kept the space. The wave function drops the space too. What remains is the abstract structure — a vector in Hilbert space, a self-adjoint operator generating motion, a mode decomposition. Bernoulli's picture with the string removed. The wave function is what remains of the wave concept once everything physical is subtracted except the mathematics that made superposition work.

What's waving? Nothing. "A wave of probability" treats probability as a stuff; it isn't. The formalism assigns amplitudes to configurations and the amplitudes interfere. Whether ψ is a physical object in configuration space, a description of knowledge, a branching of worlds, or bookkeeping is the interpretation question, unresolved because every interpretation reproduces the same predictions. (One view, held here: ψ is at least as real as the traffic jam — it does causal work and can't be eliminated. A philosophical position, not a result.)

### The reunion

Decompose the electromagnetic field into modes as Bernoulli would — each mode is an oscillator. Quantize each oscillator; it holds 0, 1, 2, … quanta. Those quanta are photons (Dirac, 1927). The photon is an excitation of one Bernoulli mode of the Maxwell field. Then the electron also needed a field, of which the electron is an excitation, and the first-quantized wave function turned out to be a halfway station. In quantum field theory, light and matter are the same kind of thing: fields in space obeying local rules, with Hilbert-space structure on top. Locality comes back; the waves are back in space; what's in space is now an operator-valued field.

---

## 7. The single line of thought

The string, the traffic jam, Maxwell, Schrödinger, and the photon are one line of thought about what it means for a pattern to persist and propagate under local rules — with progressively less insistence that anything be underneath it.

| Stage | Substrate | Space | What persists |
|---|---|---|---|
| String (1747) | Matter | Yes | Shape, translating |
| Traffic jam | Matter, with total turnover | Yes | A relation with its own velocity |
| Maxwell field (1865) | None — the field is its own medium | Yes | E and B mutually regenerating |
| Wave function (1926) | None | No — configuration space | A vector in Hilbert space |
| Quantum field | None | Yes, again | Excitations of a field of operators |

---

## Suggested next steps

- Compute the Fourier sine coefficients of a plucked triangle (peak h at x = a) and check that Σ|bₙ|² is finite and bₙ ~ 1/n². Compare with a square wave (bₙ ~ 1/n). Decay rate is smoothness; this makes the Sobolev picture nearly obvious.
- Derive the wave equation from Maxwell's curl equations in vacuum — one page of vector calculus.
- Read on the spectral theorem for unbounded self-adjoint operators (projection-valued measures), which is what continuous spectrum in quantum mechanics requires.
