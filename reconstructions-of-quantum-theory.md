# Reconstructions of Quantum Theory

_Side file, October 2026, written at the close of the information exploration. Why the quantum? Three ways the question has been asked: through the structure of questions (quantum logic, Gleason), through correlations (Bell, Tsirelson, PR boxes, information causality), and through state spaces (generalized probabilistic theories and the axiomatic reconstructions). Runnable companion: gpt.py. The argument and verdict are in what-is-information.md §6; this file carries the lineage and detail._

***

## 1. The question and its three forms

Quantum theory was found, not derived: Hilbert space, complex amplitudes, the Born rule, and the tensor product came as working rules in 1925–32. Relativity, by contrast, follows from two physical principles. The reconstruction program asks whether quantum theory has principles of that kind.

Three ways the question has been posed, roughly in historical order:

| Route                    | Object studied                                    | Typical result                                       | How far it got                                |
| ------------------------ | ------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| Quantum logic (1936–95)  | the lattice of yes/no questions                   | Piron, Solèr: Hilbert space over ℝ, ℂ, or ℍ          | the field left open; probabilities assumed    |
| Correlations (1964–2026) | what two distant boxes can do                     | Tsirelson's 2√2; information causality               | strong bounds, never the exact set in general |
| State spaces (2001–)     | the convex shape of states and how shapes compose | Hardy, Chiribella–D'Ariano–Perinotti, Masanes–Müller | complete finite-dimensional quantum theory    |

_Position:_ only the third route has succeeded, and it succeeded by asking about _composition_ (how systems combine) and _symmetry_ (how pure states transform), not about questions or correlations alone.

***

## 2. Quantum logic: the questions themselves

**Birkhoff and von Neumann (1936).** The yes/no questions about a quantum system correspond to subspaces of Hilbert space ("projections"), ordered by implication. They form a lattice, but not a Boolean one: the distributive law fails.

Worked on one qubit. Let p = "Z = +1" and q = "X = +1", with q⊥ = "X = −1". Then:

* q ∨ q⊥ is the whole space (one of the two X outcomes is certain), so p ∧ (q ∨ q⊥) = p.
* p ∧ q is the zero subspace (no state is certainly Z = +1 and certainly X = +1), and likewise p ∧ q⊥. So (p ∧ q) ∨ (p ∧ q⊥) = 0.

Distributivity would require p = 0. The failure is complementarity written as algebra, and it is the event-structure fact behind _Randomness_ §6.

**Mackey (1957–63)** asked which axioms on questions and probabilities force Hilbert space, and isolated the unexplained one: that the question lattice is a Hilbert-space lattice. **Piron (1964)**: orthomodular lattices with a few extra conditions are lattices of closed subspaces of a "generalized Hilbert space" over a division ring. **Solèr (1995)**: if there is an infinite orthonormal sequence, the ring is the reals, the complex numbers, or the quaternions.

_Position:_ quantum logic proved that the question structure nearly forces Hilbert space and left two choices open: the number field, and the composition rule (the lattice of a pair of systems is not determined by the lattices of each). Both are exactly what the later state-space route settled, by local tomography. Quantum logic stalled because it studied single systems.

***

## 3. Gleason and Kochen–Specker: questions force probabilities

_Covered in what-is-randomness.md §6; recapped._

**Gleason (1957):** in Hilbert space of dimension ≥ 3, every consistent assignment of probabilities to projections is given by a density matrix through the Born rule. **Busch (2003)** extended this to generalized measurements (POVMs), which also covers dimension 2. **Kochen–Specker (1967):** no assignment of definite values to all observables respects their functional relations.

Gleason derives the probabilities from the questions. Reconstructions go one level back and derive the questions.

***

## 4. Correlations: Bell, Tsirelson, and the quantum set

**Bell (1964), CHSH (1969):** local hidden variables bound the CHSH combination at 2. **Tsirelson (1980):** quantum theory bounds it at 2√2 ≈ 2.83 (win probability cos²(π/8) ≈ 0.854 in the CHSH game). **No-signalling** alone allows 4 (the PR box, Popescu–Rohrlich 1994).

**The exact quantum boundary, simplest case.** For two parties with two binary measurements each and unbiased outcomes, a set of correlators E\_xy is quantum exactly when (Tsirelson 1980; Landau 1988; Masanes 2003):

|arcsin E₀₀ + arcsin E₀₁ + arcsin E₁₀ − arcsin E₁₁| ≤ π

Worked:

| Correlators (E₀₀, E₀₁, E₁₀, E₁₁)         | Sum of arcsines | Quantum?        |
| ---------------------------------------- | --------------- | --------------- |
| Tsirelson: (0.707, 0.707, 0.707, −0.707) | 1.000 π         | on the boundary |
| Local deterministic: (1, 1, 1, 1)        | 1.000 π         | on the boundary |
| PR box: (1, 1, 1, −1)                    | 2.000 π         | no              |
| Noisy PR: (0.8, 0.8, 0.8, −0.8)          | 1.181 π         | no              |

The full set, marginals included, was given explicitly only in 2025 (Barizien–Bancal, _Nature Physics_).

**The NPA hierarchy** (Navascués–Pironio–Acín 2007): a sequence of semidefinite programs, each a tighter outer approximation of the quantum set. In programming terms, a convergent sequence of convex relaxations. Level "1+AB" defines the **almost-quantum** set (Navascués et al. 2015), slightly larger than quantum.

__MIP_ = RE_\* (Ji, Natarajan, Vidick, Wright, Yuen 2020). Computing the best quantum winning probability of a nonlocal game to within a fixed accuracy is as hard as the halting problem. Corollaries: Tsirelson's problem has a negative answer (the "tensor product" and "commuting operator" models of quantum correlations differ), and Connes's embedding conjecture is false.

_Position:_ **the quantum set of correlations is uncomputable in general, so no principle that yields an algorithmic membership test can capture it exactly in every scenario.** This is the strongest structural reason why the correlations route keeps reaching "almost": the target is not a decidable object. It ties the reconstruction question to _Computation_'s halting problem.

***

## 5. PR boxes and the principles that exclude them

**Van Dam (2005):** with PR boxes, any distributed function can be computed with one bit of communication. **Brassard et al. (2006):** boxes winning CHSH with probability above (3 + √6)/6 ≈ 0.908 already make communication complexity trivial.

**The random-access game** (gpt.py, section E). Alice holds bits a₀, a₁; Bob wants a\_b; one bit may be sent. Alice inputs a₀ ⊕ a₁ into her box, gets A, sends a₀ ⊕ A; Bob inputs b, gets B; m ⊕ B = a₀ ⊕ (a₀ ⊕ a₁)·b = a\_b. All eight cases succeed.

**Principles proposed, and what each excludes:**

| Principle                                                            | Statement in plain terms                             | Excludes PR?                               | Excludes almost-quantum?               |
| -------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------ | -------------------------------------- |
| Non-trivial communication complexity (van Dam; Brassard et al. 2006) | distributed computation can't be free                | yes                                        | no                                     |
| Information causality (Pawłowski et al. 2009)                        | m bits sent give at most m bits of access            | yes; Tsirelson exactly for isotropic boxes | not known to; 2026 results below       |
| Macroscopic locality (Navascués–Wunderlich 2010)                     | coarse-grained many-copy statistics are classical    | yes                                        | no (equals NPA level 1)                |
| Local orthogonality (Fritz et al. 2013)                              | mutually exclusive events have total probability ≤ 1 | yes                                        | no                                     |
| Specker's principle (exclusivity)                                    | pairwise exclusive events are jointly exclusive      | yes                                        | **yes** (Gonda et al., _Quantum_ 2018) |

**Information causality, worked** (gpt.py, section F). Boxes winning with probability p; one level of the protocol violates the bound only above p ≈ 0.89; nesting many levels gives the sharp test 2E² ≤ 1 (E = 2p − 1), failing exactly above p = 0.854, Tsirelson.

**2025–26 (preprints flagged as unrefereed):**

* Gachechiladze–Miklin (arXiv 2609.10508, Sept 2026): a generalized IC for correlated inputs recovers the Tsirelson–Landau–Masanes criterion in the simplest scenario; generalized IC strictly stronger than macroscopic locality there.
* Pompili–Weilenmann (arXiv 2610.06604, Oct 2026): sets containing post-quantum correlations that satisfy IC for all protocols, already with three inputs per party.
* Yu–Scarani (_PRA_, July 2026): IC via redundant information, closing some gaps; quantum compliance supported numerically.

**Multipartite principles needed.** Gallego, Würflinger, Acín, and Navascués (2011) showed that principles stated for two parties cannot single out quantum correlations among three: some tripartite supra-quantum correlations satisfy every bipartite principle. _Position:_ this, with the uncomputability above, explains why the correlations route stops short. How three or more systems compose is information the two-box picture lacks; it is exactly what local tomography supplies in the state-space route.

***

## 6. State spaces: generalized probabilistic theories

**The framework** (Ludwig, Mackey, Davies–Lewis lineage; Hardy 2001; Barrett 2007). A state is a vector of outcome probabilities for reference measurements; mixing is averaging, so states form a convex set; measurements are linear functionals; transformations are linear maps preserving the set. Classical theory has a simplex as its state space; quantum theory has the set of density matrices; box world (Barrett 2007) has the square (gbit) and composes to give PR boxes.

**Worked: three shapes** (gpt.py, _gpt\_shapes.svg_):

```
classical bit (segment): every mixed state has ONE decomposition -> a copier exists
qubit slice (disk): ... <X1 Y2> = +0.00 and +0.50 at once -> NO copier
gbit (square):      ... <X1 Y2> = +1.00 and -1.00 at once -> NO copier
```

**General facts established in the framework:**

* **No-broadcasting** holds in every non-classical GPT (Barnum–Barrett–Leifer–Wilce 2007): copying all states is possible exactly for simplexes.
* **Box world has trivial reversible dynamics** (Gross–Müller–Colbeck–Dahlsten 2010): only local operations and permutations; no reversible interaction correlates two gbits.
* **Entanglement and steering** exist in many GPTs; teleportation exists in some without being quantum.
* **Self-dual homogeneous cones** are exactly the state spaces of Euclidean Jordan algebras (Koecher–Vinberg). Barnum–Müller–Ududec (2014): a few single-system postulates (including no third-order interference) give Jordan algebraic theories; composition then picks the complex case.

***

## 7. The reconstructions

| Reconstruction                       | Key axioms (abridged)                                                                                                           | Distinctive move                                                   |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Hardy (2001)                         | probabilities; simplicity; subspaces; composite K\_AB = K\_A·K\_B, N\_AB = N\_A·N\_B; **continuity**                            | K = N^r; r = 1 classical, r = 2 quantum; continuity excludes r = 1 |
| Clifton–Bub–Halvorson (2003)         | within C\*-algebras: no signalling, no broadcasting, no bit commitment                                                          | informational, but C\*-structure assumed                           |
| Dakić–Brukner (2009)                 | information capacity per system; local tomography; continuous reversibility                                                     | the ball must be 3-dimensional                                     |
| Chiribella–D'Ariano–Perinotti (2011) | causality; perfect distinguishability; ideal compression; local distinguishability; pure conditioning; **purification**         | purification as the single non-classical axiom                     |
| Masanes–Müller (2011)                | finiteness; local tomography; subspace equivalence; **symmetry** (continuous reversible transitivity); all measurements allowed | derivation from "physical requirements"                            |
| Höhn (2017)                          | rules on an observer's questions and their information content                                                                  | quantum theory as rules for what can be asked                      |
| Selby–Scandolo–Coecke (2021)         | diagrammatic postulates (process theories)                                                                                      | composition as the primitive                                       |
| QBism (Fuchs–Schack; Weiss 2026)     | coherence with one reference measurement (SIC or 3-design)                                                                      | the Born rule as a deformed law of total probability               |

**Worked: what continuity and local tomography do** (gpt.py, sections B and C):

```
continuity:   segment no, disk yes (rotations), square no
local tomography:
  classical bit    K = 2, pair needs  4: OK
  qubit (complex)  K = 4, pair needs 16: OK
  rebit (real)     K = 3, pair needs 10: FAILS (10 != 3x3=9)
  gbit             K = 3, pair needs  9: OK
```

Continuity rules out the segment and square; local tomography rules out the real disk (and quaternions); the qubit's ball survives, and composition with continuity forces it to be three-dimensional.

_Position:_ in every successful reconstruction the decisive non-classical axiom is either **symmetry** (Hardy's continuity, Masanes–Müller's transitivity) or **purification** (CDP), and the decisive choice of complex numbers is **composition** (local tomography). The informational axioms do real work but never finish the job alone.

***

## 8. Experiments that test the axioms

**Complex vs. real** (local tomography). Real quantum theory (Stueckelberg 1960) reproduces every single-system and standard Bell prediction; it fails only in networks with independent sources. Hardy–Wootters (2012) showed real QT violates local tomography. Renou et al. (_Nature_ 2021) proposed a network test; photonic and superconducting experiments (2022) violated the real-QT bound under source independence; Weilenmann–Gisin–Sekatski (2025) showed partial independence suffices. _Position:_ local tomography is the reconstruction axiom with the best experimental support.

**Born rule exponent: higher-order interference** (Sorkin 1994). With three slits A, B, C, quantum probabilities are squared magnitudes of summed amplitudes, so the third-order term vanishes identically:

I₃ = P(ABC) − P(AB) − P(BC) − P(AC) + P(A) + P(B) + P(C)

Worked, amplitudes 1, 0.5 + 0.5i, −0.5 + 0.3i:

```
P: A 1.00  B 0.50  C 0.34  AB 2.50  AC 0.34  BC 0.64  ABC 1.64
ordinary (second-order) interference I2(AB) = 1.0
third-order I3 = 0 (exactly)
with a 5% cubic term added to the rule: I3 = -0.051
```

Triple-slit experiments (Sinha et al. 2010 onward) bound I₃ at the percent level and below; many-particle tests (Pleinert et al. 2021) extend them. No violation has been seen. Barnum–Müller–Ududec make "no third-order interference" an axiom that, with others, gives Jordan-algebraic theories.

**Quaternionic QT** (Adler; Peres 1979): tests of commuting phase shifts; no deviation found; tightly constrained.

**PR boxes and the gravity witness.** No supra-quantum correlation has ever been observed; every CHSH violation stays at or below 2√2. Gravitational entanglement tests (_what-is-information.md_ §6) would test interoperability, not quantum theory's form.

***

## 9. Verdict

1. **Quantum logic** showed the question lattice nearly forces Hilbert space and stalled on single systems.
2. **Gleason** showed questions force probabilities.
3. **Correlation principles** come close and cannot finish: bipartite principles can't fix multipartite correlations (Gallego et al.), and the quantum set is uncomputable (MIP\* = RE). Information causality reaches Tsirelson for isotropic boxes and may (2026, unrefereed) characterize the simplest scenario; it fails beyond it (2026, unrefereed).
4. **State-space reconstructions** succeed for finite dimensions, with symmetry and composition as the decisive axioms.
5. **Experiments** support local tomography (complex over real) and the quadratic Born rule (no third-order interference); none has found a supra-quantum correlation.

_Position, carried from what-is-information.md §6:_ **quantum theory is information plus symmetry plus composition.** Information principles are consequences once symmetry and composition are fixed; the informational statement is the clearest language for the theory, not its source.

***

## Suggested next steps

* In _gpt.py_, add a hexagon state space and find two decompositions of its centre; then a triangle (a classical trit) and confirm uniqueness.
* Compute the arcsine sum for the correlators of a quantum strategy at measurement angles of your choice and confirm it never exceeds π.
* Run the PR-box random-access protocol with a box that wins with probability 0.908 and estimate Bob's success over many trials; compare with Brassard et al.'s threshold.
* Verify I₃ = 0 symbolically: expand |a + b + c|² and check the cancellation term by term.
* Reading: Hardy, "Quantum Theory From Five Reasonable Axioms" (2001); Müller, "Probabilistic theories and reconstructions of quantum theory" (SciPost Lecture Notes 28, 2021); Barrett, "Information processing in generalized probabilistic theories" (2007); Chiribella–D'Ariano–Perinotti, "Informational derivation of quantum theory" (2011); Masanes–Müller (2011); Pawłowski et al., "Information causality as a physical principle" (2009); Popescu, "Nonlocality beyond quantum mechanics" (_Nature Physics_ 2014); Renou et al. (2021).
* Links: _what-is-information.md_ (§6 the argument and verdict); _what-is-randomness.md_ (§6 Gleason, Kochen–Specker, Bell); _what-is-symmetry.md_ (continuous groups; the symmetry axiom); _what-is-space.md_ (composition, factorization); _what-is-computation.md_ (MIP\* = RE and the halting problem); _what-is-measurement.md_ (§5 QBism's urgleichung).
