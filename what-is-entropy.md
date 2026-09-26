# What Is Entropy?

*Notes from a conversation, September 2026. From the steam engine to the demon to the horizon.*

---

## 1. A working definition

**Entropy is the logarithm of the number of microscopic situations compatible with a given description — how much the description leaves unsaid.**

In units: S = k log W is k ln 2 times the number of yes/no questions needed to pin down the microstate once you've been told the macrostate.

Unlike waves and symmetry, entropy has no pre-mathematical intuition. The word was coined in 1865 for a quantity already defined. The genealogy runs backwards: formula first, meaning sought afterwards — which is why the interpretation question is still open. (Position.)

Distinctions worth keeping:

- **Entropy vs. disorder.** Helmholtz's gloss (1882), and misleading. Hard spheres crystallize because the ordered arrangement has more microstates; gravitating gas raises its entropy by clumping. W measures what the description omits, not mess.
- **Fine-grained vs. coarse-grained.** Defined from the exact distribution on phase space, entropy never changes (Liouville). It rises only relative to a choice of which microstates count as the same.
- **Ignorance vs. entanglement.** Classically, entropy reflects not knowing a microstate. Quantum mechanically, a part can have entropy while the whole has none; there is no missing fact.
- **System vs. knowledge.** A false dichotomy (position, §4). Entropy belongs to a system *under a description* — relative like velocity to a frame, not subjective like taste.

---

## 2. The intuition — three near-misses

**One-way-ness.** Coffee cools; eggs don't unbreak. Too obvious to be a problem until there was a mechanics it contradicted. The first fundamental-looking equation with a direction of time is Fourier's heat equation (1822): u_t = κu_xx, first-order in time, blows up when run backwards. The wave equation u_tt = c²u_xx runs equally well both ways. Nobody saw a conflict with Newton for fifty years.

**The engine.** Sadi Carnot (1824, age 28): what is the maximum work obtainable from heat, by any engine, any working substance? His picture was a waterfall — caloric, a conserved fluid, falling from high temperature to low and doing work on the way, as a mill takes work from falling water.

- No temperature difference, no work.
- The best engine is a *reversible* one: if anything beat it, drive the reversible engine backwards as a pump and get work from nothing.
- So maximum efficiency depends only on the two temperatures — the first universal result in the subject, and a result that says nothing about what matter is made of.

The book sold almost nothing; Carnot died of cholera in 1832 at 36; Clapeyron's pressure–volume redrawing (1834) is how it survived.

**The wrong theory.** Joule and Mayer (1840s): heat and work interconvert; heat is not conserved; caloric is dead — and Carnot's theorem rested on it. Thomson was stuck on this through 1848–49. Clausius (1850) kept the theorem and replaced the foundation with a second, independent law: *heat does not pass by itself from cold to hot.* In a reversible cycle the heats in and out differ, but Q/T is the same at both ends. Clausius showed this is a function of state (1854), named it entropy (1865, from *tropē*, transformation, built to sound like "energy"), and stated: the energy of the universe is constant; its entropy tends to a maximum. Thomson had drawn the cosmic conclusion in 1852 (heat death).

*Position:* Carnot's waterfall was not wrong; it was about the wrong quantity. Replace caloric with entropy and the analogy is exact for the reversible engine: S enters at T_hot, the same S leaves at T_cold, work is S × ΔT. What caloric couldn't hold is the irreversible case — a waterfall that gains water as it falls. (Callendar, 1911; a minority reading.) Same pattern as Maxwell's ether: fake scaffolding, right structure.

**What was missing.** By 1865 entropy is computable, appears in a law of nature, and nobody can say what it is a quantity *of*. Missing: atoms as real things (disputed until 1908), and probability as something that could appear in a physical law. The second law is the only fundamental law stated as an inequality; no one yet knows that is a clue.

---

## 3. The dispute — can mechanics have an arrow?

**Probability enters physics.** Maxwell (1860) gave up tracking molecules and wrote the *distribution* of their speeds — the first physical law that is a probability distribution, inspired by Quetelet's social statistics. A technique built for populations, where ignorance of individuals is unavoidable, imported into a theory whose individuals are supposedly deterministic. The question of what probability means in a deterministic system starts here.

**The demon (Maxwell, 1867).** A being who sees individual molecules operates a door, sorting fast from slow; one side heats, the other cools, no work done. Maxwell's moral: the second law is *statistical* — true because we deal with matter in bulk and can't handle molecules singly. The law is already tied to what an agent can know and do. Nobody develops this for sixty years.

**Boltzmann's H-theorem (1872).** An equation for how the distribution f(x, v, t) changes under collisions; H = ∫ f log f; proof that dH/dt ≤ 0. Minus H is the entropy. Apparently the second law derived from Newton.

**Loschmidt (1876; Thomson 1874).** Newton's equations are time-symmetric. Reverse every velocity and you have a legitimate state whose H increases. No theorem of mechanics alone can have a time-asymmetric conclusion. The hidden assumption, found twenty years later: molecules are uncorrelated *before* collisions (the *Stosszahlansatz*) — not after. The arrow of time, inserted in a step that looked like bookkeeping.

**Boltzmann's retreat, which is the advance (1877).** Drop the dynamics and count. A macrostate is compatible with W microstates; **S = k log W** (form and constant are Planck's, 1900). Equilibrium is the macrostate with overwhelmingly the most microstates. Entropy increase is not necessity; nearly everywhere you can go from a small region is a bigger one. This concedes Loschmidt entirely, and explains the inequality.

**Zermelo (1896).** Poincaré recurrence (1890): a bounded system with a volume-preserving flow returns arbitrarily close to its start. Volume preservation is Liouville. So entropy must eventually decrease; Zermelo concluded atoms had to go. Boltzmann: correct, and the recurrence time for a cubic centimetre of gas has trillions of digits.

The deeper cut from Liouville: the fine-grained entropy *never changes at all*. Entropy rises only if you blur the distribution. Nobody asked who does the blurring.

**Where the asymmetry lives.** Counting says entropy should rise toward the past too. Boltzmann's answer (the visible universe is a fluctuation) fails — a single observer with false memories is enormously more probable. The modern answer is a boundary condition: the universe began in very low entropy (the Past Hypothesis). Symmetric law, asymmetric state. Unexplained.

**Reception.** Mach and Ostwald: atoms are metaphysics. Einstein's Brownian motion (1905) and Perrin (1908) settled it. Boltzmann died by suicide in 1906; Ostwald conceded in 1909.

*Position:* Boltzmann won on physics and lost the claim he started with. The second law is mechanics plus a count plus a special initial condition. The missing concepts — the analogue of "function," "sum," and "equality" for the string — were what a probability is when nothing is random, and what makes two microstates the *same macrostate*. W depends on a partition mechanics doesn't supply. The waves story ended by quietly changing what equality means; this one turns on it.

---

## 4. The formalization — Gibbs, Shannon, Jaynes

**Gibbs (1902).** Replace the system with a probability distribution ρ on phase space (an "ensemble"): S = −k ∫ ρ log ρ. Uniform ρ gives k log W; ρ ∝ e^(−H/kT) gives all of thermodynamics. Gibbs was silent on what ρ *is*. He knew the Liouville problem (ink stirred into water: volume constant, filaments too fine to see) and left a paradox: mixing different gases raises entropy, mixing identical ones doesn't, discontinuously — so entropy appears to depend on whether you can tell them apart. Von Neumann (1927) carried the formula into Hilbert space as −Tr ρ log ρ.

**Shannon (1948).** An engineering problem: how far can a message be compressed, how much can a noisy channel carry. Demanding a measure of uncertainty that is continuous, grows with the number of equally likely options, and is consistent under staged choices, exactly one function survives: H = −Σ p log p. The formula is forced — nothing physical went in; the logarithm is there for additivity, as in Boltzmann. And it has operational meaning: the minimum average bits per symbol; the expected number of yes/no questions. (Full route in *shannon-and-information.md*.)

**Jaynes (1957).** Statistical mechanics *is* inference. You know a few things (say mean energy U); any distribution with less than maximum Shannon entropy consistent with them claims information you don't have. Maximize −Σ p log p subject to Σ pE = U: one Lagrange multiplier β, answer p ∝ e^(−βE), with β = 1/kT. Temperature is the multiplier enforcing the energy constraint. No imaginary copies, no ergodic hypothesis.

- *Why ignorance predicts:* macroscopic experiments are reproducible, so nearly all microstates compatible with the controlled variables behave alike. When max-ent fails, the failure reveals an unknown constraint.
- *The second law from Liouville (1965):* start with the max-ent distribution for the initial macrovariables; evolve; fine-grained entropy is constant. The thermodynamic entropy of the final macrostate is a maximum over all distributions consistent with the new macrovariables, of which the evolved one is a member. So S_final ≥ S_initial. The increase is the information about initial conditions that the final macrovariables no longer carry. The blurring is located: in the experimenter's choice of variables.
- *The mixing paradox dissolves:* entropy is relative to the variables you track. If you can't distinguish the gases, no mixing entropy and no error. Find a separating membrane and both your capabilities and your entropy assignment change. Entropy is "anthropomorphic" (Jaynes, after Wigner).

**What it cost, and a position.** The objection: coffee cools whether or not anyone knows anything. This defeats "entropy is knowledge" but not Jaynes. *Position:* entropy is a property of a system *under a description* — a microstate space plus a choice of macrovariables. Fix the description and it is entirely objective; change it and you get a different, equally objective number.

Against the strong claim that it was *never* physics, three residues:
- Max-ent needs a prior measure, and it is Liouville's phase-space volume. That is dynamics.
- It is a physical fact that some coarse descriptions (pressure, temperature) obey closed laws of their own and most don't.
- The 1965 argument retrodicts as well as predicts; the arrow still needs the low-entropy past.

The probabilities are epistemic; the measure, the macrovariables, and the boundary condition are physical.

The debt: if entropy is relative to what an agent tracks, an agent tracking individual molecules should beat the second law. The demon becomes a real test.

---

## 5. The abstraction — the demon pays

**Szilard (1929).** One molecule in a box at temperature T. Insert a partition; find which side the molecule is on; let it push a piston (work kT ln 2 drawn from the bath); remove the partition. One bit becomes kT ln 2 of work, in a cycle. Szilard replaced the intelligent being with a two-state memory and concluded something must generate k ln 2 of entropy. He assigned it to the measurement. Right total, wrong place.

**Brillouin (1951).** A demon at uniform temperature is blind; seeing a molecule needs a photon above kT, whose dissipation exceeds k ln 2. The textbook answer for thirty years. It shows one method of measurement is dissipative, not that all must be.

**Landauer (1961).** A different question: the minimum dissipation of computation. Logically reversible operations (NOT) vs. irreversible ones (ERASE). A bit lives in a physical system with reversible dynamics. Erasure halves the memory's occupied phase-space volume; total volume can't shrink (Liouville); so the environment's must double: at least kT ln 2 of heat per bit erased (~3 × 10⁻²¹ J at room temperature).

Liouville has now appeared three times: Zermelo's weapon, the engine of Jaynes's proof, and the reason forgetting costs energy.

**Bennett (1973, 1982).** Any computation can be made logically reversible, so computation as such has no minimum cost; only erasure does. And measurement is a *copy* — correlating a blank memory with the thing measured — which can be done with arbitrarily little dissipation. The demon pays when it resets its memory, and the reset costs exactly what it gained. If it never resets, its memory fills with random bits: a blank tape has fuel value, and a finite-memory demon is an engine that runs by randomizing its tape.

**The accounting** (in mutual information): before measurement, molecule 1 bit, memory 0. After: each 1 bit alone, perfectly correlated, joint entropy still 1 bit — nothing dissipated. Work extraction *spends the correlation*: joint entropy 2 bits, bath down k ln 2. Erasure moves the memory's bit to the bath. The books balance at every step. General form (Sagawa–Ueda, 2008–10): extractable work ≤ kT × mutual information acquired. Tested: Toyabe et al. (2010), Bérut et al. (2012, the erasure bound directly), Koski et al. (2014).

*Position on why it took 53 years:* the missing concept was the distinction between logical and thermodynamic reversibility, and the obstacle was quantum mechanics, which had made measurement the paradigm of the irreversible act. The cost is in forgetting, not learning — invisible until memory was a physical object one could point to.

*Position on the circularity objection* (Earman and Norton, 1998–99): right about the logic — Landauer–Bennett assumes statistical mechanics and is not an independent proof of the second law. Wrong about what's at stake. What it provides is a *localization*: where the entropy goes, and that the informational description is exact accounting, not metaphor.

The debt is settled: an agent who knows more *can* extract more work. Observer-relativity is real and harmless, because the observer's knowledge is a physical state of a physical memory inside the ledger. Jaynes's entropy survives by placing the observer inside the physics.

> **Reversible dynamics never destroys information; it only moves it into correlations you aren't tracking. Entropy is the amount that has moved out of your description, and the second law says it is easier to lose track than to regain it.**

Jaynes's inequality and Landauer's bound are the same statement read in opposite directions. A wave was what locality looks like from outside; entropy is what *reversibility* looks like from inside a partial description.

---

## 6. The payoff

### Entropy without ignorance

An entangled pair is in one definite state: entropy zero. Each particle alone is maximally mixed: entropy ln 2. Classically impossible; quantum mechanically typical (Schrödinger, 1935: best knowledge of a whole does not include best knowledge of its parts). There is no missing fact; the entropy comes entirely from describing *part* of something. Almost every pure state of a large system looks exactly thermal on a small piece (Popescu–Short–Winter, 2006). No ensembles; no ignorance. The coffee cools because it becomes entangled with the room.

### Black holes

Wheeler's puzzle: pour hot tea into a black hole and its entropy vanishes from the universe. Bekenstein (1972–73): the black hole itself has entropy proportional to horizon area. Bardeen–Carter–Hawking (1973): four laws matching thermodynamics term for term — taken as analogy, since a classical black hole has temperature zero. Hawking (1974), partly aiming to refute Bekenstein, found thermal radiation at exactly the required temperature, fixing **S = kA/4ℓ²** (ℓ the Planck length). The analogy was an identity.

A solar-mass black hole: ~10⁷⁷ k; the Sun: ~10⁵⁸. Black holes dominate the universe's entropy. This explains the Past Hypothesis: the smooth early universe was *low* entropy because, with gravity, clumping is the high-entropy direction.

### What the intuition could never have said: area

Every entropy in §§2–5 scales with volume. The maximum entropy of a region scales with its *boundary*. Holographic principle ('t Hooft, Susskind, 1993–95): about one degree of freedom per four Planck areas of boundary. A local field theory vastly overcounts. The wave notes ended with locality as the through-line; entropy is the quantity indicating locality is an approximation.

### What is W counting?

- *Boltzmann's reading:* there are microstates; count them. Strominger–Vafa (1996) did so for special supersymmetric black holes and got A/4 exactly. For real black holes, no count exists.
- *The entanglement reading:* the vacuum is entangled across any surface, and the entanglement entropy of a region scales with boundary area (Bombelli et al., 1986; Srednicki, 1993). A horizon is a surface you can't see past.

System or knowledge, turned into a research problem — with a new feature: the division into tracked and untracked is imposed by causal structure, not chosen. Unruh (1976): an accelerating observer in vacuum has a horizon and detects a thermal bath. "Relative like velocity to a frame" can be read almost literally.

### The information paradox

Hawking (1976): a black hole formed from a pure state evaporates into thermal radiation — information *destroyed*, not exported, violating the §5 principle (unitarity is the quantum Liouville). Page (1993): unitarity requires the radiation's entropy to rise, turn over near the halfway point, and fall to zero. In 2019, Penington and Almheiri–Engelhardt–Marolf–Maxfield derived the Page curve from semiclassical gravity. The curve comes out right; the mechanism is not understood. *Position:* the principle holds, and the apparent destruction is again a description tracking too little.

### Space from entropy

Both within frameworks whose application to our universe is conjectural:

- Ryu–Takayanagi (2006): in holographic duality, the entanglement entropy of a boundary region *equals* the area of a minimal interior surface over 4G. Van Raamsdonk (2010): reduce the entanglement between two halves and the space connecting them pinches off. Connectivity of space is a pattern of entanglement.
- Jacobson (1995): assume every local horizon has entropy proportional to area, impose Clausius's δQ = T dS on the energy crossing it, and Einstein's equations follow as an equation of state. The relation invented to rate steam engines yields gravity.

### The inversion

Entropy began as the least fundamental quantity in physics — an accounting of what engineers couldn't recover, which Jaynes argued was not physical at all. It is now the only quantitative handle anyone has on quantum gravity, and the best indication of what space is made of.

*Closing position.* Entropy is a property of a *division*: tracked from untracked, system from environment, inside from outside a horizon. Where we choose the division, entropy is relative to us, harmlessly. Where nature imposes it, entropy is as objective as mass. The two readings of W will probably turn out to be one fact, as Boltzmann's count and Gibbs's functional did. (Held with less confidence than the rest.)

---

## 7. The single line of thought

One question, asked with steadily less attachment to who is asking: how much does this description leave out, and where did it go?

| Stage | Entropy is a property of… | What is counted | What it yields |
|---|---|---|---|
| Carnot / Clausius (1824–65) | a body in equilibrium | nothing — δQ/T | the limit on engines; an arrow of time |
| Boltzmann (1877) | a macrostate | compatible microstates | the second law as overwhelming probability |
| Gibbs (1902) | a distribution on phase space | weighted microstates | all of equilibrium thermodynamics |
| Shannon (1948) | a message source | yes/no questions | the limits of compression and communication |
| Jaynes (1957–65) | a description | what the description omits | statistical mechanics as inference; the second law from Liouville |
| Landauer / Bennett (1961–82) | a correlation between memory and world | bits | the price of forgetting; the observer inside the ledger |
| Horizons (1973– ) | a division imposed by causal structure | unknown | the area law, holography, gravity as an equation of state |

The wave concept kept the space and lost the substrate. The symmetry concept kept the group and lost the object. The entropy concept kept the logarithm and lost the engine, then the gas, then the ignorance — and at the end it is counting something, exactly, and nobody knows what.

---

## Suggested next steps

- Do the max-ent calculation: maximize −Σ p ln p subject to normalization and fixed mean energy; obtain p ∝ e^(−βE); then show S = k(ln Z + βU) and match dS = δQ/T to identify β = 1/kT.
- Run the Szilard engine ledger by hand: track H(molecule), H(memory), and their mutual information through measure → extract → erase, and check the totals against the bath.
- Compute the entropy of mixing for two ideal gases, then let the gases become identical, and locate exactly where the discontinuity enters (the N! in the count).
- Write the reduced density matrix for one half of a Bell pair and verify S = ln 2 for the part, 0 for the whole.
- Reading: Jaynes, "Gibbs vs Boltzmann Entropies" (1965); Bennett, "The Thermodynamics of Computation — a Review" (1982); Jacobson, "Thermodynamics of Spacetime" (1995).
- Links forward: *Randomness* (what probability is when nothing is random — left open in §3, reframed in §6); *Space* (the Ryu–Takayanagi endpoint, from the other side); *Computation* (Landauer and reversible computing).
