# Concept Genealogies

*A research program: tracing a concept from intuition, through the fight over formalizing it, to the point where the formalization turns out to be more real than the intuition.*

## Method

Each exploration follows the same arc:

1. **The intuition** — where the idea first shows up, before anyone has mathematics for it.
2. **The dispute** — the argument that breaks out when people try to make it precise, and what concepts were missing that made it unresolvable.
3. **The formalization** — who resolved it, with what machinery, and what the resolution cost.
4. **The abstraction** — what the concept looks like once the original physical picture is stripped away.
5. **The payoff** — where the abstract version turns out to describe something the intuition never could.

Working conventions:
- Genealogy and abstract shape first; derivations only when they clarify a concept.
- Take stances on disputed questions; mark them as positions, not results.
- One stage per message, with steering between stages.
- Settle the arc before stage 1 and save it as a short outline file; open the outline with a working claim for the genealogy to break. (Adopted in the measurement exploration.)
- End each exploration with a markdown summary saved to the project, in the format of the existing ones.
- Detours that outgrow a stage become side files rather than sections.
- Worked mathematical examples in plain terms, with small numbers. (Adopted in the computation exploration.)
- One conversation per topic.

## Completed

### Waves — *what-is-a-wave.md*
Vibrating string (d'Alembert, Euler, Bernoulli) → Fourier and the century of rigor that built L² → the abstract wave as locality → Faraday, Maxwell, Heaviside → the wave function → quantum fields. Endpoint: a wave is a persisting pattern under local rules, with progressively less insistence that anything be underneath it.

### Symmetry — *what-is-symmetry.md*
Euclid's five solids and the crystallographers → Galois's unsolvable quintic and the group as "operation as object" → Lie's generators → the action principle and Noether's theorem → gauge theory, where demanding a local symmetry forces a field with Maxwell's dynamics → spontaneous breaking and the Higgs mechanism. Endpoint: symmetry begins as a property of things and ends as a property of descriptions, at which point it becomes geometry and tells the object what to be. Position taken: gauge symmetry is a redundancy, and the physical content is the connection.

### Entropy — *what-is-entropy.md*
Carnot's waterfall and Clausius's δQ/T → the Boltzmann–Loschmidt–Zermelo dispute and the Past Hypothesis → Gibbs, Shannon, and Jaynes's statistical mechanics as inference → Szilard, Landauer, Bennett: the demon pays when it forgets → entanglement entropy, black holes, the area law, and gravity as an equation of state. Endpoint: entropy is a property of a division between tracked and untracked variables; where we choose the division it is relative to us, where nature imposes it (a horizon) it is as objective as mass. Position taken: "system or knowledge" is a false dichotomy, like asking whether velocity belongs to the object.

### Randomness — *what-is-randomness.md*
The lot, Aristotle against Epicurus, and the aleatory contract → the three-round dispute over what a probability is a property of (Bernoulli/Bayes/Laplace; Venn and Bertrand; Fisher/Neyman against Ramsey/de Finetti/Jeffreys/Jaynes) → Kolmogorov's measure, which formalized probability by exiling randomness to a null set, with von Mises as the road not taken → algorithmic randomness: Kolmogorov complexity, Martin-Löf tests, the Schnorr–Levin equivalence, Chaitin's Ω and incompleteness as the generic case → Gleason and Kochen–Specker, Bell, certified randomness, and the measurement problem as the schism purified. Endpoint: randomness is what is absent from a description, and the genealogy strips away in turn the cause, the reason, the sequence, the sample space, and the definite outcome. Positions taken: the frequentist's chance is the Noether charge of the Bayesian's exchangeability; Kolmogorov formalized probability, not randomness; Chaitin's theorem is right and his gloss overreaches; Bell settles Epicurus against Democritus conditional on locality and free choice; the interpretations of quantum mechanics are the round-3 positions with the Laplacian middle removed.

### Measurement — *what-is-measurement.md*
The cubit and the metre bar, Eudoxus to Helmholtz and Hölder, Leibniz's compresence and Kant's hands, Weyl's rod and Einstein's atoms, the 2019 SI → von Neumann's chain and the movable cut, proper vs. improper mixtures, Schrödinger's cat, Wigner's friend, Deutsch's reversible friend, DLP irreversibility and Bell's FAPP → POVMs and Naimark dilation; decoherence (Zeh, Joos–Zeh), einselection, and quantum Darwinism, with redundancy as the definition of a record → Everett (measurement as correlation, outcomes as indexical) against QBism (measurement as an agent's act, the urgleichung) → Local Friendliness, black-hole complementarity, AMPS, and Harlow–Hayden. Working claim broken: measurement is comparison under a transported convention — transport repaired (atoms, the SI), non-disturbing comparison reconstructed as a regime (redundant records), universal comparability not repaired (friends, horizons). Endpoint: a measurement result is a record, and physics is increasingly a theory of which records can be brought together, by whom, and at what cost. Positions taken: the 2019 SI vindicates Duff — fixing dimensionful constants is a gauge choice; Bohr identified the missing concept (the record) and wrongly made it a primitive; von Neumann's consistency theorem did more harm than good; Boolean event structure is what survives copying; quantum Darwinism solves objectivity, not outcomes, and the cut has become a factorization; Everett is the stronger abstraction of measurement, QBism of probability, and QBism repeats Bohr's move; observed events are absolute to the degree their records are redundant; what can be compared is bounded by what can be computed. Tentative: Everett and QBism are complementary views of one structure.

### Computation — *what-is-computation.md*
Llull and Leibniz's calculemus, Boole's x² = x, Frege's gapless proof, Prony's divided labour, Babbage and Lovelace → Hilbert's *Entscheidungsproblem*, the diagonal escape from every class of total functions, and the 1936 contest of definitions (Church, Gödel–Herbrand, Post, Turing), won by Turing's analysis of the clerk → the stored-program computer: analog, relay, and tube lineages, ENIAC's setup problem, the EDVAC report and the priority dispute, Turing's ACE, memory technology, the first runs, and code-as-data from self-modification to W^X → complexity: Gödel's 1956 letter, Hartmanis–Stearns, Cobham–Edmonds, the extended Church–Turing thesis, Cook–Levin–Karp, the relativization and natural-proofs barriers, pseudorandomness and cryptography, Landauer–Bennett and the Toffoli gate → Feynman and Deutsch, interference as the source of quantum speedup, Shor worked for N = 15, the state of hardware in 2026, and the physical Church–Turing thesis. Working claim broken: computation is what a clerk does by finite rules, a fact of logic independent of physics — relocated (the thesis is a theorem with physical premises), overturned (feasibility depends on physics), extended (hardness as a physical boundary). Endpoint: a computation is a physical process viewed through a description that says which of its features count as symbols. Positions taken: undecidability is the price of a closed definition; the Church–Turing thesis is a theorem whose premises describe a physical agent; "von Neumann architecture" names the least inventive and most consequential contribution, the abstraction layer; code-as-data grew in software and was fenced off in hardware; polynomial time is the class fixed by closure under composition and change of machine, and "feasible" is a loose label; the hardness of proving hardness is a consequence of hardness; SAT solvers show what worst-case theory is about, not its failure; quantum speedup is hidden-symmetry detection by interference; the extended thesis is false (conditionally); physics is not computation, computation is a physical category.

## Side files

- **The Lagrangian and the Hamiltonian** — *lagrangian-and-hamiltonian.md*. The action principle, the Legendre transform, phase space, Liouville, Poisson brackets, and the road to quantum mechanics. Written during the symmetry exploration; Liouville's theorem then carried the entropy exploration.
- **Shannon and the measure of information** — *shannon-and-information.md*. Nyquist and Hartley, Shannon's route through cryptography, the 1948 theorems, what he knew of the physics, and the Szilard–von Neumann link. Written during the entropy exploration.
- **Measurement outline** — *measurement-outline.md*. The arc settled before the measurement exploration began; superseded by the summary, kept as a record of the plan.
- **Computation outline** — *computation-outline.md*. The arc settled before the computation exploration; superseded by the summary.
- **Curry–Howard** — *curry-howard.md*. Propositions as types, proofs as programs; BHK, Curry, Gentzen, Howard, Martin-Löf, System F; general recursion as inconsistency; classical logic as `call/cc`. Written at the close of the computation exploration; entry point for *Proof*.
- *Candidate, not yet written:* the representational theory of measurement (Stevens's scale types, Krantz–Luce–Suppes–Tversky), noted in measurement §2 as the complete classical formalization that never meets quantum mechanics.

## Cross-references

Threads that have now surfaced in more than one exploration, and belong to whichever topic takes them up next:

- **Liouville's theorem / unitarity** — Zermelo's recurrence objection, Jaynes's proof of the second law, Landauer's erasure bound; in randomness, why from the universal state no random event occurs; in measurement, why von Neumann's chain never produces an outcome, and why the measurement problem and the second law's direction share one structure; in computation, reversible logic (Bennett, Toffoli) as the bulk of Shor's algorithm.
- **Locality** — the through-line of waves; the gauge field as what locality forces on internal freedom; the area law as the sign that locality is an approximation; Bell's assumption (i); Local Friendliness's assumption (3); in computation, Turing's bounded, local steps and Gandy's bounded signal speed as the physical premises of the Church–Turing thesis, and Bell as the refutation of local classical digital physics.
- **Law vs. state** — the pencil on its tip; Lagrangian vs. Hamiltonian; the arrow of time; unitary evolution vs. the measurement outcome; law-based vs. artefact standards (the 2019 SI).
- **Equality and sameness** — L² identifying functions that differ on measure zero; W depending on which microstates count as the same macrostate; the Gibbs mixing paradox; Kolmogorov identifying events differing by null sets; proper and improper mixtures identified by one density matrix; "measuring h" becoming "defining the kilogram"; in computation, two procedures the same when they compute the same partial function, and two problems the same when mutually reducible in polynomial time — all NP-complete problems are one problem.
- **Symmetry as the source of a number** — Noether's conserved quantities; Jaynes's transformation groups answering Bertrand; de Finetti's exchangeability; the invariance theorem; Gleason and envariance; Stevens's scale types; in computation, Shor's period as a hidden symmetry found by the Fourier transform (the hidden subgroup problem).
- **The division** — entropy (tracked vs. untracked); randomness (branch vs. universe, agent vs. world); Yao's pseudorandomness; in measurement, the movable cut, the factorization, the Everett–QBism split; in computation, the logical description as a coarse-graining of a physical process. Six instances.
- **Boolean vs. non-Boolean event structure** — Kolmogorov's 𝓕; Gleason and Kochen–Specker; Boolean structure as what survives redundant copying.
- **What probability is when nothing is random** — de Finetti in statistics; Bell in physics; Everett's self-location and QBism's urgleichung. Open whether the statistical and physical answers are about the same thing.
- **Transport and comparison** — Kant's hands and the Ozma problem; Weyl's rod and the gauge connection; Wu's parity violation; the SI; complementarity as impossible comparison.
- **Redundancy as objectivity** — quantum Darwinism's plateau; absoluteness to the degree records are redundant; Everett's intersubjectivity argument. Candidate link to entropy: redundant records as why the second law's direction is shared. In computation, von Neumann's reliable logic from unreliable parts, and quantum error correction, as redundancy protecting a record.
- **Observation bounded by computation** — Yao; Chaitin's Ω; Harlow–Hayden; pseudorandom Hawking radiation. Tested in computation: confirmed and grounded (PRGs iff one-way functions; cryptography as engineered comparability limits; natural proofs as hardness shielding itself). Pattern across five explorations: entropy relative to macrovariables, randomness to computational power, objectivity to redundancy, measurability to complexity, feasibility to physical law.
- **Closure forces the price** — new. Partial functions forced by closure under diagonalization (undecidability as the price); polynomial time forced by closure under composition and change of machine; general recursion making a logic inconsistent (Curry–Howard). Candidate link to symmetry: a class is fixed by the operations it must be invariant under, Klein's program applied to definitions.
- **Unprovable of the individual, true of almost all** — new. Chaitin: most strings random, none provably so; complexity: most functions need large circuits, no explicit one provably so (natural proofs); Kolmogorov: the individual outcome exiled to a null set. Feeds *Proof*.
- **The Fourier transform as the recurring instrument** — new. Bernoulli's modes and L²; the spectral theorem as quantum mechanics' template; Shor's quantum Fourier transform; the FFT. A candidate side file.

## Proposed

### Space — *recommended next*
Euclid → Gauss's surveying → Riemann's 1854 lecture → Einstein → spacetime as emergent from entanglement. Now approached from three completed explorations: entropy (Ryu–Takayanagi, Van Raamsdonk), measurement (horizons, complementarity, the factorization problem), and computation (complexity–volume, the computational hardness of the holographic dictionary). The factorization problem — what counts as a subsystem — is the open question all three left, and this arc is where it belongs.

### Proof
Euclid → the 19th-century rigor crisis → Frege and Russell → Hilbert's formalism → Gödel and Gentzen → Curry–Howard and proof assistants → computer-checked mathematics and the natural-proofs barrier. Promoted from possible to proposed: computation supplied Gödel's letter (checking vs. finding), the "unprovable of the individual" thread, and the Curry–Howard side file as an entry point.

### The continuum
Zeno → Newton's fluxions and Berkeley's "ghosts of departed quantities" → Cauchy, Weierstrass, Dedekind → Cantor → Brouwer's intuitionist revolt → Robinson's nonstandard analysis. Live question: is the real line a discovery or a construction? Touched from randomness (countable vs. finite additivity, Borel normality), measurement (Eudoxus, Hölder), and computation (analog computing and infinite precision as the excluded "unreasonable" model; Brouwer again via BHK).

### The function
The story of mathematics deciding what an object is. Touched in waves (Euler vs. d'Alembert, Dirichlet), and in computation (a function as a rule — λ-calculus — vs. a graph; sameness of computations as sameness of partial functions).

## Possible later additions

- **Time** — Newton's absolute time → thermodynamic arrow → relativity → the problem of time in quantum gravity. Entropy covered the arrow; measurement added the irreversibility of records; computation added reversible computation. What remains is relativity and quantum gravity.
- **Force** — Aristotle → Newton → fields → curvature → gauge connections. Largely absorbed by symmetry and space.
- **Number** — counting → zero and negatives → irrationals → complex → quaternions → what a number is. Entry points in measurement (counting vs. measuring) and computation (binary, Boole's two-valued algebra).
