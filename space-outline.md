# What Is Space? — Outline

*Working plan for the seventh exploration, September 2026. Arc proposed before stage 1; open to steering.*

---

## Working claim to be broken

**Space is the given arena that divides the world into parts: things are separate things, and separate systems, because they occupy different places.**

This is the claim the earlier explorations quietly relied on. Entropy's tracked/untracked split, measurement's system/apparatus/environment, and computation's qubits and local gates all assumed that "subsystem" was well defined, and the unstated guarantee was spatial: a subsystem is what sits in a region.

The genealogy breaks the claim in three moves:
1. **The arena stops being given.** Geometry becomes an empirical question (Gauss), then a structure on a manifold (Riemann), then a dynamical field (Einstein).
2. **Places stop having identity.** The hole argument: points of spacetime are gauge. Only relations among fields are physical.
3. **Parts stop coming from places.** In quantum field theory, a region does not define a tensor factor. In holography the direction reverses: places are read off from how parts are entangled.

The third move leaves the question this arc is organized around.

## The question held in view: the factorization problem

A Hilbert space with a state and a Hamiltonian does not, by itself, say how to split into subsystems. The same vector is entangled in one factorization and a product state in another. Measurement ended with "the cut became a factorization"; entropy ended with space built from entanglement; computation ended with a description saying which physical features count as symbols. All three presuppose a factorization and none supplies one.

If space comes from entanglement, and entanglement is defined relative to a factorization, and the factorization used to come from space, the account is circular. Stage 5 has to say where the circle breaks.

**Opening bet, to be tested, not a result:** the circle breaks by giving up factorization, not by grounding it. Subsystems are subalgebras of observables, not tensor factors, and in gravity they are defined relative to an observer. If that's right, the division that has run through six explorations is neither chosen by us nor imposed by nature. It is what "an observer" means.

---

## 1. The intuition — place, void, container

- Euclid's *Elements* has figures but no word for space; space is what constructions happen in.
- Aristotle's place (*topos*) as the inner boundary of the container, and no void. The atomists' void as the condition for things being many.
- Descartes: extension is matter. Newton: absolute space, the bucket.
- Leibniz–Clarke and Kant's hands: already covered in symmetry and measurement. Cite them, don't repeat them.
- What the intuition contains: separateness comes from place. That is the working claim.

## 2. The dispute — is geometry a fact about the world?

- The parallel postulate: Saccheri, Lambert, then Gauss, Bolyai, Lobachevsky. Consistency later secured by Beltrami's models (1868).
- Gauss's Hohenhagen–Brocken–Inselsberg triangle. Whether he meant it as a test of geometry is disputed; mark it as disputed.
- Helmholtz's free mobility against Kant's synthetic a priori; Poincaré's conventionalism (geometry and physics adjusted together; the disk world).
- Klein's Erlangen program (1872): a geometry is its symmetry group. Links back to symmetry.
- Missing concepts: intrinsic geometry, measurable from inside; and the metric as a physical quantity that could vary.
- Hilbert's *Grundlagen* (1899) mentioned and handed to *Proof*.

## 3. The formalization — Riemann to Einstein

- Gauss's *Theorema egregium* (1827): curvature is intrinsic. Worked example: angle excess of a triangle on a sphere equals area over R².
- Riemann's Habilitation lecture (1854, published 1868): manifold, metric, curvature, and the suggestion that the ground of metric relations must be sought in physical forces.
- Christoffel, Ricci and Levi-Civita; Levi-Civita's parallel transport (1917) as the geometric form of Weyl's rod and the gauge connection.
- Einstein 1907–1915: the equivalence principle, geometry as a field, the field equations.
- What it cost: the hole argument (1913; revived by Stachel and by Earman–Norton). General covariance makes points gauge. Consequences: no local gravitational energy; no local observables in quantum gravity.

## 4. The abstraction — space as an algebra

- Stripping in stages: metric → topology → the algebra of functions. Gelfand–Naimark (1943): a (compact Hausdorff) space *is* its commutative algebra of continuous functions.
- Connes: drop commutativity, get noncommutative geometry. Kac's drum question (1966), answered no by Gordon–Webb–Wolpert (1992): the spectrum alone doesn't fix the shape.
- Haag–Kastler (1964): quantum field theory as a net, region → algebra of observables. The algebras are type III (Araki): a region does not give a tensor factor, and the entanglement across its boundary is infinite. Gauge fields break factorization again (edge modes).
- **The factorization problem stated precisely.** Worked example: one state in a 4-dimensional space, entangled under one split into two qubits, a product under another.
- Carroll–Singh on quantum mereology (2021); Cotler–Penington–Ranard, locality from the spectrum (2019): a generic Hamiltonian admits at most one factorization in which it is local, if any.

## 5. The payoff — space from entanglement, and who it is for

- Ryu–Takayanagi and Van Raamsdonk are recapped only; entropy reached them already.
- ER = EPR (Maldacena–Susskind 2013).
- Holography as quantum error correction (Almheiri–Dong–Harlow 2015; HaPPY 2015; Harlow 2017). Worked example: the three-qutrit code, in which any two qutrits recover the logical one. Bulk locality as redundancy, the same concept as quantum Darwinism's records.
- Complexity = volume (Susskind); the computational hardness of the dictionary (Bouland–Fefferman–Vazirani 2019). Computation's hand-off.
- Cao–Carroll–Michalakis (2017): space from Hilbert space alone, and what it presupposes.
- Gravity forbids local subsystems: gravitational dressing (Donnelly–Giddings). Algebras in gravity become well defined, with finite entropy, only relative to an observer with a clock (Witten 2022; Chandrasekaran–Longo–Penington–Witten 2022). Measurement's observer returns as a structural ingredient.
- The endpoint question: do places define parts, or parts define places, or does an observer define both?

---

## Threads to carry in

- **The division** (six instances): here it either gets a ground or is shown to have none.
- **Locality** (waves, Bell, Gandy): local Hamiltonians as the proposed source of the factorization.
- **Transport and comparison** (symmetry, measurement): Weyl's rod, Levi-Civita's connection, parallel transport.
- **Equality and sameness:** points identified under diffeomorphism; the hole argument as the gauge redundancy of spacetime.
- **Redundancy as objectivity** (measurement): bulk operators redundantly encoded on the boundary.
- **Observation bounded by computation** (computation): complexity = volume; the dictionary's hardness.
- **Liouville / unitarity:** black-hole information as the constraint that forces the entanglement picture.

## Threads to hand off

- **Time:** the problem of time and Wheeler–DeWitt; whether the observer's clock in stage 5 is a first answer.
- **The continuum:** whether space is a manifold at all; discreteness proposals.
- **Proof:** Euclid's axioms and Hilbert's *Grundlagen*.

## Guardrails

- Shape first, few derivations; worked examples in plain terms with small numbers.
- No second pass on Leibniz–Clarke, Kant's hands, or Ryu–Takayanagi: link and build.
- Relativity is the largest risk of sprawl. General relativity appears in stage 3 as a conceptual turn, not a course. If it needs more, it becomes a side file.
