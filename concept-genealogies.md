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

## Side files

- **The Lagrangian and the Hamiltonian** — *lagrangian-and-hamiltonian.md*. The action principle, the Legendre transform, phase space, Liouville, Poisson brackets, and the road to quantum mechanics. Written during the symmetry exploration; Liouville's theorem then carried the entropy exploration.
- **Shannon and the measure of information** — *shannon-and-information.md*. Nyquist and Hartley, Shannon's route through cryptography, the 1948 theorems, what he knew of the physics, and the Szilard–von Neumann link. Written during the entropy exploration.

## Cross-references

Threads that have now surfaced in more than one exploration, and belong to whichever topic takes them up next:

- **Liouville's theorem** — phase-space incompressibility: Zermelo's recurrence objection, Jaynes's proof of the second law, Landauer's erasure bound. Unitarity is its quantum form, and in the randomness exploration it is why, from the universal state, no random event ever occurs.
- **Locality** — the through-line of waves; the gauge field as what locality forces on internal freedom; the area law as the sign that locality is an approximation; Bell's assumption (i), the one whose failure would rescue Democritus.
- **Law vs. state** — the pencil on its tip; Lagrangian vs. Hamiltonian; the symmetric dynamics and asymmetric initial condition behind the arrow of time; unitary evolution vs. the measurement outcome.
- **Equality and sameness** — L² identifying functions that differ on measure zero; W depending on which microstates count as the same macrostate; the Gibbs mixing paradox; Kolmogorov identifying events that differ by null sets, which is why the theory cannot name a sequence.
- **Symmetry as the source of a number** — Noether's conserved quantities; Jaynes's transformation groups answering Bertrand; de Finetti's exchangeability generating the frequentist's chance; the invariance theorem confining the arbitrariness of description language to a constant.
- **The division** — entropy as a property of tracked vs. untracked; randomness as a property of branch vs. universe, or agent vs. world; Yao's pseudorandomness as randomness relative to an observer's computational bound. Three instances; the theme now has a shape.
- **Boolean vs. non-Boolean event structure** — new. Kolmogorov's 𝓕 assumes every outcome has a value before you ask; Gleason and Kochen–Specker show that dropping it forces the Born measure and removes the sample space. Feeds *Measurement* directly.
- **What probability is when nothing is random** — the open question from entropy, now answered in two halves: in statistics, chance is the shadow of a symmetry of belief (de Finetti); in physics, Bell says the outcome was not a function of anything prior, conditional on locality and free choice. What remains open is whether those two answers are about the same thing.

## Proposed

### Measurement — *recommended next*
Kant's hands and Leibniz's indistinguishables → the quantum measurement problem → the demon as a measuring device → horizons as measurement boundaries. Emerged as a theme across all four explorations and now has a technical entry point from randomness: the non-Boolean event lattice, Wigner's friend, and the division theme. Would also be the place to take the Everett/QBism split further than the randomness exploration did.

### Space
Euclid → Gauss's surveying → Riemann's 1854 lecture (which also introduced the Riemann integral) → Einstein → the current view that spacetime may be emergent from entanglement. The entropy exploration reached the Ryu–Takayanagi and Van Raamsdonk endpoint from the other side; this arc would arrive at it from geometry.

### The continuum
Zeno → Newton's fluxions and Berkeley's "ghosts of departed quantities" → Cauchy, Weierstrass, Dedekind → Cantor → Brouwer's intuitionist revolt → Robinson's nonstandard analysis rehabilitating infinitesimals. Runs directly through real analysis. Live question: is the real line a discovery or a construction? Now touched from randomness: countable additivity vs. de Finetti's finite additivity; Borel normality; the reals as the space of coin-toss sequences.

### Computation
Leibniz's dream → Hilbert's program → Gödel, Church, Turing → Shannon's circuits → quantum computation → whether physics is itself computation. Three entry points from completed work: Shannon's relay thesis, Landauer–Bennett reversible computing, and Chaitin's Ω with the halting problem and Yao's pseudorandomness.

### The function
The story of mathematics deciding what an object is. Touched from the side in the waves exploration (Euler vs. d'Alembert, Dirichlet's definition); deserves its own treatment. Could extend to the general question of what counts as a mathematical object.

## Possible later additions

- **Force** — Aristotle → Newton → fields → curvature → gauge connections. Largely absorbed by symmetry and space; may not need its own treatment.
- **Number** — counting → zero and negatives → irrationals → complex → quaternions and beyond → what a number is.
- **Proof** — Euclid → the 19th-century rigor crisis → Hilbert's formalism → Gödel → computer-checked proofs. Chaitin's version of incompleteness is now an entry point.
- **Time** — Newton's absolute time → thermodynamic arrow → relativity → the problem of time in quantum gravity. The arrow is now covered in entropy; what remains is relativity and the quantum-gravity problem.
