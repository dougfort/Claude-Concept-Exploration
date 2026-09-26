# What Is Randomness?

*Notes from a conversation, September 2026. From the lot to Laplace to Chaitin's Ω to Bell.*

---

## 1. A working definition

**An outcome is random relative to a description when nothing in the description picks it out; a sequence is random when no description shorter than itself generates it.**

The first half is Laplace; the second is Kolmogorov (1965). The intuition had neither. It had *chance* — a claim about causes, not descriptions. The genealogy is the word migrating from events (something happened without a cause) to ratios (Cardano) to frequencies (Bernoulli) to beliefs (Bayes, Laplace) to sequences (von Mises, Kolmogorov, Chaitin) — and at the end, with Bell, back to events.

Distinctions worth keeping:

- **Chance vs. probability vs. randomness.** Chance is a property of an event (no assignable cause). Probability is a number attached to a set of possibilities. Randomness is a property of a process or sequence — a twentieth-century invention.
- **Uncaused vs. unpredictable vs. patternless.** Epicurus asserts the first, Laplace denies it and keeps the second, Kolmogorov defines the third. They come apart cleanly and the intuition ran them together.
- **Fair vs. random.** A fair lot must be unmanipulable — a claim about who controls it, not about pattern. Fairness is the older concept and the one that produced the mathematics.
- **The two faces.** From birth (1660s) probability means both "how often" (aleatory) and "how much to believe" (epistemic). The schism is these two faces fighting after each has a formalism.
- **The string vs. the source.** A pseudorandom generator produces strings no test can distinguish from random, from a short seed. Randomness of outputs and randomness of the process are different questions; only Bell addresses the second.

Unlike entropy (formula first, meaning later) and symmetry (word first, unrelated), randomness is a third pattern: the concept is ancient and fully articulated as a metaphysical dispute, and the mathematics grew up beside it — from contracts and games — without settling it or needing to. (Position.)

---

## 2. The intuition — three that didn't know they were one

**The lot — sacred and fair at once.** Astragali in Mesopotamia; lots in the Hebrew scriptures ("the lot is cast into the lap, but the decision is the Lord's"); the Athenian *kleroterion*, selecting magistrates by lot because election was thought oligarchic. Two incompatible readings held simultaneously: the lot is *fair* because no one controls it, and *oracular* because a god does. The same operation, read as absence of will and as presence of will. Hacking's puzzle: dice were played for four thousand years, for stakes, and no calculus of chances appeared until the 1650s.

**Chance as absence of cause — Aristotle against Epicurus.** Democritus: nothing happens by chance. Aristotle (*Physics* II): chance is not a cause but an *intersection* of independent causal chains — the man at the market meets his debtor. Epicurus: atoms falling in parallel could never collide, so posit the *clinamen*, a swerve at no fixed time or place, with no cause — introduced, Lucretius says, to make room for free will. Cicero ridiculed it. This is the stage-5 question, stated in full in the third century BC with no way to test it. Laplace's demon (1814) is Democritus with the mechanics: probability is "relative in part to our ignorance, in part to our knowledge."

**The fair price — where the mathematics came from.** Roman *fenus nauticum* (loans repaid only if the ship arrived); Ulpian's annuity table; canon law's *periculum sortis*, the peril of chance that made a return on money legitimate. Aleatory contracts posed the question: what is the fair price of an uncertain future? The problem of points (Pacioli 1494; Pascal–Fermat 1654) is this question — how to divide an interrupted stake *equitably* — not a prediction question. Huygens (1657) wrote the first textbook with *expectation*, not probability, as the primitive. In the same decade: Graunt's mortality tables (1662, stable frequencies in a population — the aleatory face) and the Port-Royal *Logic* and Pascal's wager (decision under uncertainty — the epistemic face). *Probabilis* had meant approvable by authority; Hacking's thesis is that the concept required evidence to become internal — the die had to become a witness.

**What was missing.** *Symmetric ignorance* — the idea that not-knowing can have structure, and that symmetry licenses a number (Leibniz's line applied to belief; astragali are asymmetric, so it couldn't start). *The sequence* — "random" as a predicate of a thing is Victorian; Cardano noted that many throws approximate the ratio "only if the die is honest," with no concept of either the law or the requirement. *Whose ignorance* — the fair-price strand assumed the epistemic reading, the mortality strand the aleatory, and they shared a formula without noticing they had different subjects.

---

## 3. The dispute — what is the p a property of?

### Round 1 — Bernoulli, Bayes, Laplace (1713–1814)

Bernoulli's theorem: given p, the frequency converges. He wanted the inverse — frequency to p, for diseases and weather where cases can't be counted — and died without it; he already worried a worn die's faces weren't equipossible. Bayes (1763) solved the inverse for a ball on a table, with a uniform prior and a scholium arguing ignorance justifies it. Laplace made inverse probability the method of science: the *principle of insufficient reason*, the *rule of succession* (s+1)/(n+2), and the demon. He fused both faces without seeing the seam, because with much data the prior doesn't matter. Applied to the sun rising: 1,826,214 to 1. *Lacking:* any way to say what "no reason to prefer" means when the cases aren't given.

### Round 2 — Ellis, Venn, Bertrand (1843–1889)

Venn's *Logic of Chance* (1866): the principle of insufficient reason manufactures knowledge from ignorance. Probability is a fact about a *series* — a limiting frequency — and applies only to repeatable events; the single case has no probability. Meanwhile Quetelet, Maxwell (1860), Boltzmann use frequency distributions in physics with no philosophy. **Bertrand's paradox (1889):** a chord "at random" in a circle exceeds the inscribed triangle's side with probability ½, ⅓, or ¼ depending on what you take uniform. Von Kries (1886): a uniform density isn't invariant under reparametrization — ignorance in one coordinate is opinion in another. Kant's hands again. Peirce's *tychism*: chance is real and operative in nature. *Lacking:* the invariance group (symmetric under what?); a definition of the random sequence frequentism is defined in terms of; the single case.

### Round 3 — Fisher, Neyman, Ramsey, de Finetti, Jeffreys, Jaynes (1922–1957)

Fisher (1922): inverse probability "must be wholly rejected"; the likelihood, maximum likelihood, significance tests. Neyman–Pearson (1933): tests as decision procedures with long-run error rates; a confidence interval's 95% is a property of the method, not the interval. Fisher and Neyman fought for twenty years while both rejected Bayes. The frequentist's probability is about the data, given a fixed parameter.

Three independent Bayesian reconstructions: **Ramsey** (1926) — degrees of belief measured by betting odds; incoherent odds admit a Dutch book; the axioms are conditions of coherence. **De Finetti** (1931, 1937) — "PROBABILITY DOES NOT EXIST"; the *representation theorem*: exchangeable beliefs (invariant under permuting trials) are mathematically a mixture over an unknown p — the frequentist's chance is the shadow of the believer's symmetry. **Jeffreys** (1939) — objective priors, invariant under reparametrization. The Bayesian's probability is about the parameter, given the data seen.

Each side's foundation is the other's embarrassment: frequentist inference depends on experiments not run (stopping rules; Birnbaum's likelihood principle, 1962), Bayesian inference on priors invented (Bertrand). Ceasefire without resolution: Wald (1950) — admissible rules are Bayes rules; Savage (1954); Cox (1946); Jaynes (1957, 1968) — maximum entropy and *transformation groups*, which answer Bertrand (½) by demanding invariance under what the problem leaves unspecified. Insufficient reason repaired by specifying the group: Lie's move.

*Position:* the schism is not about mathematics or subjectivity but about what the probability is *of* — the repetition class or the proposition — two conditionalizations of one joint distribution, and de Finetti's theorem says the joint is generated by a symmetry. **The frequentist's chance is the Noether charge of the Bayesian's exchangeability.** Held for statistics. It says nothing about whether nature produces the sequence without anyone's symmetry behind it — Peirce's question, stage 5's.

---

## 4. The formalization — Kolmogorov, and the road not taken

**Von Mises (1919).** A *collective*: an infinite sequence with limiting frequencies invariant under every *place selection* (a rule using only prior terms). Randomness as unexploitability — the impossibility of a gambling system. It fell apart on "every": allow all selections and no collectives exist; restrict to countably many (Wald 1937) and Ville (1939) built a sequence passing all of them that violates the law of the iterated logarithm. Frequency invariance was the wrong property. Pronounced dead at Geneva, 1937. Church (1940) restricted selections to computable ones — computation's first appearance in the definition.

**The measure.** Borel (1909): almost every real is normal — the strong law for a fair coin, with the unit interval as the space of toss sequences. Wiener (1923): a measure on paths for Brownian motion, built because physics needed it. Hilbert's sixth problem had asked for it.

**Kolmogorov, *Grundbegriffe* (1933).** A probability space (Ω, 𝓕, P): outcomes; a σ-algebra of *events* — the questions the theory permits; a countably additive measure of mass one. Random variables are measurable functions; expectation is the Lebesgue integral. Three things beyond measure theory: **independence** (what gives probability its own character; every deep theorem runs on it); **conditional expectation given a σ-algebra**, via Radon–Nikodym — projection onto a coarser set of askable questions, the L² projection of the wave notes, and where the entropy notes' *description* enters the calculus; the **extension theorem**, constructing the space von Mises had assumed.

**What it cost.** The single case, officially: P assigns numbers to sets and has no sentence "this outcome is random." The sequence, exiled to a null set: the strong law is about the *set* of bad sequences; every specific sequence is a singleton of measure zero, and the theory cannot point at it. *Random* survives only in "random variable," modifying a measurable function with nothing random about it. Equality: events differing by null sets identified — L²'s silent casualty is now load-bearing. Countable additivity: chosen for convenience, refused by de Finetti for life — the one axiom the schism did fight over has no empirical content. Interpretation: removed. Fourier asked only for integrals; Kolmogorov asked only for a measure. The remainder is randomness itself.

**Reception:** total. "Measure theory with total mass one." Then, 1963, Kolmogorov defected: von Mises's question admits a rigorous answer, and it lies in the theory of algorithms.

*Position:* Kolmogorov formalized probability, not randomness. Probability is a measure, hence a property of sets of possibilities — a description. Randomness is a property of an actual outcome. No measure distinguishes one point from another; the machinery for naming individuals had to come from computation.

---

## 5. The abstraction — algorithmic randomness

**The turn (1960–66).** Solomonoff (universal prior: weight hypotheses by 2^−length of shortest program), Kolmogorov (1965: combinatorial, probabilistic, algorithmic information), Chaitin (1966, aged 18) — three problems, one definition.

**Incompressibility.** K(x) = length of the shortest program making a universal machine print x. **A string is random if K(x) ≈ |x|** — its own shortest description. Von Mises's "no gambling system" becomes "no program." *Invariance theorem:* changing machine changes K by an additive constant — Bertrand's arbitrariness confined, not eliminated. *Counting:* fewer than 2ⁿ programs shorter than n, so most strings are incompressible — Borel's "almost every" by pigeonhole. *Uncomputability:* Berry's paradox as a theorem — "the first string with K > 10⁶" is a short program. Randomness is well-defined, provably abundant, and unrecognizable.

**Typicality — Martin-Löf (1966).** A test is an effectively generated sequence of nested sets of measure ≤ 2⁻ⁿ; a sequence is random if it fails no effective test; a universal test exists. Stage-4's null set is now *effective*, with individual members. Ville's counterexample excluded; von Mises's collectives included.

**Equivalence — Schnorr–Levin.** Incompressible in every prefix (with prefix-free programs; Levin, Chaitin) ⟺ passes every effective test (Martin-Löf) ⟺ no computable gambler grows capital without bound (Schnorr 1971). Patternless, typical, unexploitable — three intuitions, one class. The Riesz–Fischer moment.

**Chaitin's Ω.** Ω = Σ 2^−|p| over halting programs of a universal prefix-free machine — the halting probability. Definable, one specific real. Enumerable from below (run everything, add as programs halt), not computable: its first n bits decide the halting problem for all programs of length ≤ n, hence every Π₁ statement — Goldbach, Riemann. Martin-Löf random. **Any formal system determines at most finitely many bits of Ω** (roughly its own axiom length plus a constant) — otherwise a proof-searching program would compress a random string. Chaitin (1987): an explicit Diophantine equation whose finite/infinite solution counts, parameter by parameter, are the bits of Ω.

**The Gödel connection.** Liar → Gödel 1931 (one sentence). Diagonal → Turing 1936 (the halting problem). Berry → Chaitin 1971–74 (that any specific string is random). Chaitin changes the character of incompleteness: Gödel's sentence looked like a self-referential artefact; "K(x) > L" is true of almost every string of length above L, and provable of none. The system proves "most strings this long are random" and cannot prove it of any one. Incompleteness is the generic case, and the generic case is the random case.

*Position, with correction.* The theorem is right and the gloss overreaches. Raatikainen (1998): the constant L does not measure a system's information content in any stable way — it can be made tiny or huge by choice of machine. "A system can only prove as much randomness as it contains" is a metaphor. What survives is stronger: incompleteness is the normal condition of arithmetic, and the statements it fails on are those with no pattern — a fact about randomness, not about self-reference. Ω is not unpredictable; it is one definite real. It is *unreachable*, and the difference is stage 5's subject.

**Solomonoff closes round 3.** The universal prior is the invariant prior Jeffreys and Jaynes reached for: invariant up to a constant, Occam's razor as a distribution, convergent for any computable source, and uncomputable — the ideal Bayesian. The frequentist program (define randomness) was completed with a Bayesian object (a prior) built from computation. The gambler's strategy *is* the program.

**What it cost, and can't say.** Everything is up to a constant, so short strings are neither random nor not. Randomness can't be verified of any object — exact, abundant, individually unknowable. And the gap between string and source: Yao (1982) — a distribution is *pseudorandom* if no efficient test distinguishes it from uniform; a generator's output is random relative to bounded observers and non-random absolutely, complexity of a few hundred bits (the seed). Randomness indexed by computational power, as entropy was indexed by macrovariables; algorithmic randomness is the limit at infinite computation. A deterministic universe running a generator would pass every test. Telling it from Epicurus's swerve requires a claim about what the source *could not have been* — Bell.

---

## 6. The payoff — quantum randomness

### Born, and the question stated properly

Born (1926), in a footnote added in proof: ψ determines not where the electron goes but the *probability* — and irreducibly so. Einstein to Born: the Old One does not play dice. EPR (1935), properly: if the theory is complete, measuring one particle fixes a distant one's state; refuse action at a distance and the properties were fixed already — hidden variables λ, Democritus as a research programme. Von Neumann (1932) "proved" no hidden variables; Hermann (1935) found the flaw and was ignored for thirty years; Bell (1966) found it again. Bohm (1952): a working hidden-variable theory — definite positions guided by ψ, Born probabilities as Laplacian ignorance of initial conditions — with explicit non-locality as the price. Bell asked whether the non-locality was Bohm's defect or forced on any theory.

### The structural fact — Gleason and Kochen–Specker

Quantum events are projections; for non-commuting projections "A and B" is not an event. The lattice is non-Boolean. **Gleason (1957):** in dimension ≥ 3, every probability measure on the projections is of the Born form — the measure is forced by the event structure. **Kochen–Specker (1967):** no assignment of definite values to all observables respects their algebraic relations — no classical Ω underneath; outcomes are *contextual*. *Position:* Kolmogorov's silence on the individual outcome was structural. Boolean 𝓕 is the assumption that every outcome has a value before you ask. Change 𝓕 and probability survives (Gleason) but the sample space does not (Kochen–Specker). The thing to axiomatize differently was the set of questions, not P.

### Bell (1964)

Two entangled particles, two distant observers, each freely choosing one of two settings, recording ±1. Assume (i) *locality* — my result depends on my setting and a shared λ, not your setting; (ii) *measurement independence* — λ uncorrelated with the settings; (iii) one result per run. Then (CHSH 1969) a combination of four correlations satisfies |S| ≤ 2 for any λ and any physics; quantum mechanics gives 2√2. Freedman–Clauser (1972); Aspect (1982), settings switched in flight; loophole-free 2015 (Delft, NIST, Vienna); cosmic Bell (2018), settings from quasar light; Nobel 2022. **What it rules out:** every theory in which outcomes are a function — deterministic or stochastic — of anything local and prior, including every pseudorandom generator. Stage-5's gap closed from the other side: not by testing outputs but by testing correlations between free inputs and outputs at spacelike separation. Escape routes: drop (i) — Bohm; drop (ii) — superdeterminism, irrefutable and, Bell said, absurd; drop (iii) — Everett.

*Position:* the first and only time the Aristotle–Epicurus question was turned into an inequality and measured. Answer: Epicurus, conditional on locality and free choice — the two assumptions the lot's oracular reading denied (a god arranging the answer; a god arranging the question). Fairness is a theorem with two named escapes, both older than the mathematics.

### Certified randomness

Colbeck (2006), Pironio et al. (2010): Bell violation certifies that the outputs were not a function of anything local, *whoever built the device* — device-independent randomness. 42 bits from trapped ions over a month; Bierhorst et al. (NIST 2018), 1,024 loophole-free bits feeding a public beacon. Two results with no classical analogue: *expansion* (a short seed yields a longer certified string — randomness is not conserved) and *amplification* (Colbeck–Renner 2012: a Santha–Vazirani source, unpurifiable classically, yields perfect bits with entanglement). What cannot be done: randomness from nothing — the protocols need some free choice of settings. The demon paid for bits with erasure; here the price is the assumption that someone chose.

*Position:* the first place randomness is a physical quantity with a price and a certificate. Entropy's inversion in miniature: the individual outcome, which Kolmogorov could not name and Chaitin could not verify, is manufactured, counted, and sold.

### The measurement problem — the schism returns

Von Neumann's two processes: unitary evolution (deterministic, linear, reversible) and measurement (one outcome, Born weight, none of those). Unitarity never yields a single outcome; something must choose. Wigner's friend: the regress. **Decoherence** (Zeh, Zurek): entanglement with the environment kills interference and yields exactly the Laplacian mixture — the coffee cooling into the room — explaining why outcomes look classical and in which basis, not why one happens.

| Interpretation | The probability is of… | Stage-3 ancestor |
|---|---|---|
| Objective collapse (GRW, Penrose) | a real stochastic process; new physics | Peirce's tychism; propensity |
| Bohm | ignorance of initial positions; non-local determinism | Democritus, Laplace |
| Everett (1957) | self-locating uncertainty in a branching world | the demon, with branches |
| Deutsch–Wallace (1999, 2012) | a rational agent's betting rates across branches | Savage |
| QBism (Caves–Fuchs–Schack 2002) | an agent's beliefs about consequences of their actions | de Finetti — literally: the quantum de Finetti theorem is theirs |

The correspondence is exact: Wallace is Savage with branches as states of the world; QBism's founding theorem is de Finetti's 1937 representation with Hilbert space for the coin, and Gleason plays the Dutch book.

*Position:* the measurement problem is the frequentist–Bayesian schism with the Laplacian middle removed. Classically both sides could retreat to "the outcome was fixed; we just didn't know it." Bell and Kochen–Specker take that sentence away, so the surviving positions are purer than their ancestors: chance in the world (collapse), chance nowhere and appearance from position in a deterministic structure (Everett), or chance entirely the agent's and no probabilities in the world (QBism).

### What the intuition could never have said

- **The lot, resolved.** Under locality and free choice, no agent — with any knowledge of the past — arranged the outcome. The oracle survives only as a conspiracy (superdeterminism). Fairness is a theorem.
- **The event structure, not the measure.** Every stage from Cardano to Kolmogorov assumed Boolean questions and fought over the number. Change which questions can be asked together: the measure is forced, the sample space vanishes, and the individual outcome becomes the subject.
- **Randomness as a property of a division.** From inside a branch or an agent's standpoint the result is irreducibly random and certifiably so; from the universal state nothing random occurred — unitarity is Liouville. Which description you occupy is fixed by what you are entangled with. Jaynes's observer-relativity, no longer a choice.
- **A remainder.** Calude–Svozil (2008): given Kochen–Specker, quantum measurement sequences cannot be produced by any computable process — the one physical source of Martin-Löf-random sequences. Ω is unreachable and definite; the quantum outcome is unreachable and, on the Everett reading, not definite until you are in a branch. Whether these are the same unreachability is open.

---

## 7. The single line of thought

One question, asked with steadily less attachment to what is doing the not-knowing: what is left of an outcome once every description has been given?

| Stage | Randomness is a property of… | Missing from the description | What it yields |
|---|---|---|---|
| The lot / Aristotle / Epicurus | events | a cause | fairness, divination, free will |
| Cardano → Laplace (1564–1814) | equipossible cases | a reason to prefer one | the calculus; inverse probability |
| Venn / Bertrand (1866–89) | a series | which coordinates; which sequences are irregular | frequentism, and its debt |
| Fisher / de Finetti (1922–54) | the data, or the parameter | the other one | the schism; chance as the shadow of exchangeability |
| Kolmogorov (1933) | nothing — probability is a measure on sets | the individual outcome, exiled to a null set | all of probability theory |
| Martin-Löf / Chaitin (1965–75) | an individual string | any shorter description | incompleteness as the generic case |
| Bell / certification (1964–2018) | a correlation between free choices and outcomes | any prior variable at all | randomness as a physical, priced, certified quantity |
| Measurement | a division between branch and universe, or agent and world | — | the schism, purified |

Waves kept the space and lost the substrate. Symmetry kept the group and lost the object. Entropy kept the logarithm and lost the engine, the gas, and the ignorance. Randomness kept the *absence* — the thing not in the description — and lost, in turn, the cause, the reason, the sequence, the sample space, and the definite outcome. At the end the absence is certified, sold by the bit, and nobody agrees on whose absence it is.

---

## Suggested next steps

- Build a toy universal machine (a small instruction set or a compact language) and enumerate all programs up to length n; record the shortest program for each output string. Watch the counting argument appear: almost every string of length n has no program shorter than n. Then estimate the lower partial sums of Ω for that machine.
- Run the Berry argument as code: write the program "find the first string of length N with no program shorter than N − 20" and see why it can't work (it needs to decide halting).
- Do the CHSH arithmetic: with A, A′, B, B′ ∈ {±1}, show AB + AB′ + A′B − A′B′ = ±2 always, hence |S| ≤ 2 under any λ; then compute the quantum correlations for the singlet at 0°, 45°, 90°, 135° and get 2√2.
- Verify de Finetti in the smallest case: show that an exchangeable distribution on two coin flips is a mixture of i.i.d. distributions, and find one on three flips that is exchangeable but not a mixture of *independent* flips with the same bias — then see why infinitely many flips fix the problem.
- Compute Bertrand's three answers explicitly and then Jaynes's invariance argument for ½.
- Reading: Hacking, *The Emergence of Probability*; Kolmogorov, *Grundbegriffe* (the first ten pages); Chaitin, "Randomness and Mathematical Proof" (*Scientific American*, 1975); Bell, "Bertlmann's Socks and the Nature of Reality" (1981); Fuchs, "QBism, the Perimeter of Quantum Bayesianism" (2010); Li and Vitányi for the technical algorithmic-randomness material.
- Links forward: *Measurement* (Boolean vs. non-Boolean event structures; Wigner's friend; the division theme); *Computation* (Chaitin's Ω and the halting problem; pseudorandomness); *The continuum* (Kolmogorov's countable additivity vs. de Finetti; Borel normality).
