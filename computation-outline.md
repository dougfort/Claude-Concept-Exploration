# What Is Computation? — Outline

*Working plan for the sixth exploration, September 2026. Arc confirmed before stage 1.*

---

## Working claim to be broken

**Computation is what a clerk does following finite rules with pencil and paper, and what can be computed is a fact of logic, independent of physics.**

The genealogy is that claim failing:
1. Turing's analysis (1936) makes the clerk the *definition*, so the Church–Turing thesis is a claim about agents, not a theorem.
2. Deutsch (1985) recasts it as a physical principle.
3. Complexity becomes a physical limit: quantum computation changes what is *feasible* without changing what is *computable*, and horizons are protected by computational hardness (Harlow–Hayden).

---

## 1. The intuition — full prehistory

- Llull's *Ars Magna*; Leibniz's *characteristica universalis* and *calculus ratiocinator*, the stepped reckoner, binary arithmetic.
- Logic becomes algebra: Boole (1847, 1854), Jevons's logic piano, Frege's *Begriffsschrift* (1879), gapless proof.
- Calculation as divided labour: Prony's tables, Babbage's Difference and Analytical Engines, Lovelace's Notes.
- Missing concepts to identify: what "mechanical" means; universality; the bridge between formal proof and machine.

## 2. The dispute — what is an effective procedure?

- Hilbert's program and the *Entscheidungsproblem*; Brouwer's objection; Gödel (1931).
- 1936: Church (λ-definability), Gödel–Herbrand (recursive functions), Post, Turing.
- Crux: why Gödel rejected Church's definition and accepted Turing's.
- Is the Church–Turing thesis a definition, a theorem, or a law?

## 3. The formalization — the universal machine

- Equivalence of the models; universality; the halting problem.
- Code as data: the universal machine as the conceptual origin of the stored program — Shannon's relays (1937), von Neumann's EDVAC report (1945).
- What it cost: no account of time or resources.

## 4. The abstraction — computation as a bounded resource

- Cobham–Edmonds (feasible = polynomial time); Cook–Levin; P vs NP.
- Yao's pseudorandomness: random relative to bounded observers.
- Landauer–Bennett: the thermodynamic cost; reversible computation.
- Curry–Howard deliberately excluded (side file).

## 5. The payoff — is computation physical?

- Deutsch (1985) and the physical Church–Turing thesis; the extended (complexity) thesis.
- Shor, BQP, quantum advantage.
- Harlow–Hayden; pseudorandom Hawking radiation; complexity as a physical limit.
- Stance on "is physics computation?": the extended thesis is the defensible version; digital physics (Zuse, Wolfram) is a different, weaker claim.

---

## Threads to carry in

- **Observation bounded by computation** (randomness, measurement): Yao, Chaitin's Ω, Harlow–Hayden. The claim this arc tests.
- **Liouville / unitarity**: reversible computation; Landauer's erasure bound.
- **Shannon**: the relay thesis (*shannon-and-information.md*).
- **Randomness §5**: Kolmogorov complexity, Ω, and Chaitin's incompleteness, which presuppose the universal machine.
- **Symmetry §3**: an impossibility proof requires defining the class of permitted procedures (radicals then, effective procedures now).

## Side files planned

- **Curry–Howard**: programs as proofs, types as propositions. Points toward *Proof*.

## Working conventions for this exploration

- Fog's background: broad programming experience, imperative and functional.
- Runnable artefacts (Turing machine, λ-interpreter, busy beaver, SAT) can be built in the sandbox during the relevant stage.
