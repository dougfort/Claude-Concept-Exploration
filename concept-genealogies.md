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

## Side files

- **The Lagrangian and the Hamiltonian** — *lagrangian-and-hamiltonian.md*. The action principle, the Legendre transform, phase space, Liouville, Poisson brackets, and the road to quantum mechanics. Written during the symmetry exploration; Liouville's theorem then carried the entropy exploration.
- **Shannon and the measure of information** — *shannon-and-information.md*. Nyquist and Hartley, Shannon's route through cryptography, the 1948 theorems, what he knew of the physics, and the Szilard–von Neumann link. Written during the entropy exploration.
- **Measurement outline** — *measurement-outline.md*. The arc settled before the measurement exploration began; superseded by the summary, kept as a record of the plan.
- *Candidate, not yet written:* the representational theory of measurement (Stevens's scale types, Krantz–Luce–Suppes–Tversky), noted in measurement §2 as the complete classical formalization that never meets quantum mechanics.

## Cross-references

Threads that have now surfaced in more than one exploration, and belong to whichever topic takes them up next:

- **Liouville's theorem / unitarity** — Zermelo's recurrence objection, Jaynes's proof of the second law, Landauer's erasure bound; in randomness, why from the universal state no random event occurs; in measurement, why von Neumann's chain never produces an outcome, and why the measurement problem and the second law's direction share one structure (reversible dynamics, one-way appearance in a partial description).
- **Locality** — the through-line of waves; the gauge field as what locality forces on internal freedom; the area law as the sign that locality is an approximation; Bell's assumption (i); Local Friendliness's assumption (3), whose failure is Bohm's price.
- **Law vs. state** — the pencil on its tip; Lagrangian vs. Hamiltonian; the arrow of time; unitary evolution vs. the measurement outcome; in measurement, law-based vs. artefact standards (the 2019 SI).
- **Equality and sameness** — L² identifying functions that differ on measure zero; W depending on which microstates count as the same macrostate; the Gibbs mixing paradox; Kolmogorov identifying events differing by null sets; proper and improper mixtures identified by one density matrix, which is how von Neumann's cut becomes movable; "measuring h" becoming "defining the kilogram."
- **Symmetry as the source of a number** — Noether's conserved quantities; Jaynes's transformation groups answering Bertrand; de Finetti's exchangeability; the invariance theorem; Gleason and envariance as the Born rule forced by symmetry; Stevens's scale types classified by admissible transformations.
- **The division** — entropy (tracked vs. untracked); randomness (branch vs. universe, agent vs. world); Yao's pseudorandomness; in measurement, the movable cut, the tensor factorization quantum Darwinism presupposes, and the Everett–QBism split as outside vs. inside. Five instances. Measurement's closing position recasts it as *the structure of comparability*.
- **Boolean vs. non-Boolean event structure** — Kolmogorov's 𝓕; Gleason and Kochen–Specker; in measurement, answered from the other side: Boolean structure is what survives redundant copying.
- **What probability is when nothing is random** — de Finetti in statistics; Bell in physics; in measurement, Everett's self-location (probability as uncertainty about an indexical fact) and QBism's urgleichung (quantum probability as a normative deformation of total probability). Whether the statistical and physical answers are about the same thing remains open.
- **Transport and comparison** — new. Kant's hands and the Ozma problem; Weyl's rod and the gauge connection; Wu's parity violation and Einstein's atoms as nature supplying a standard; the SI as reproducibility replacing transport; complementarity as the case where comparison is impossible. The symmetry notes' "the convention must be transported, and the transport is the force" and measurement's "standards stopped being transported when a law made transport unnecessary" are two halves of one thread.
- **Redundancy as objectivity** — new. Quantum Darwinism's plateau; absoluteness of observed events holding to the degree records are redundant; Everett's intersubjectivity argument as its early form. Candidate link to entropy: redundant records are why the second law's direction is shared by all observers.
- **Observation bounded by computation** — new. Yao's pseudorandomness; Chaitin's unreachable Ω; Harlow–Hayden's decoding bound; Hawking radiation as computationally pseudorandom. Pattern across four explorations: entropy relative to macrovariables, randomness to computational power, objectivity to redundancy, measurability to complexity. Feeds *Computation* directly.

## Proposed

### Computation — *recommended next*
Leibniz's dream → Hilbert's program → Gödel, Church, Turing → Shannon's circuits → quantum computation → whether physics is itself computation. Now has four entry points from completed work: Shannon's relay thesis; Landauer–Bennett reversible computing; Chaitin's Ω, the halting problem, and Yao's pseudorandomness; and from measurement, Harlow–Hayden and Deutsch's reversible friend. The newest cross-reference thread (observation bounded by computation) runs through all of them, and this arc is where the claim that complexity is a physical limit gets tested.

### Space
Euclid → Gauss's surveying → Riemann's 1854 lecture (which also introduced the Riemann integral) → Einstein → the current view that spacetime may be emergent from entanglement. Entropy reached the Ryu–Takayanagi and Van Raamsdonk endpoint from one side; measurement reached horizons and complementarity from another, and left the factorization problem (what counts as a subsystem) as a question this arc could take up.

### The continuum
Zeno → Newton's fluxions and Berkeley's "ghosts of departed quantities" → Cauchy, Weierstrass, Dedekind → Cantor → Brouwer's intuitionist revolt → Robinson's nonstandard analysis rehabilitating infinitesimals. Live question: is the real line a discovery or a construction? Touched from randomness (countable vs. finite additivity, Borel normality) and from measurement (Eudoxus's ratios, the Archimedean axiom, Hölder's representation theorem).

### The function
The story of mathematics deciding what an object is. Touched from the side in the waves exploration (Euler vs. d'Alembert, Dirichlet's definition); deserves its own treatment. Could extend to the general question of what counts as a mathematical object.

## Possible later additions

- **Time** — Newton's absolute time → thermodynamic arrow → relativity → the problem of time in quantum gravity. The arrow is covered in entropy; measurement added the irreversibility of records and the shared-direction question. What remains is relativity and quantum gravity. Now a stronger candidate than before.
- **Force** — Aristotle → Newton → fields → curvature → gauge connections. Largely absorbed by symmetry and space; may not need its own treatment.
- **Number** — counting → zero and negatives → irrationals → complex → quaternions and beyond → what a number is. Measurement's counting-vs-measuring strand is an entry point.
- **Proof** — Euclid → the 19th-century rigor crisis → Hilbert's formalism → Gödel → computer-checked proofs. Chaitin's version of incompleteness is an entry point.
