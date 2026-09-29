# What Is Computation?

*Notes from a conversation, September 2026. From Leibniz's calculemus to Turing's clerk to the EDVAC report to Shor.*

---

## 1. A working definition

**A computation is a physical process viewed through a description that says which of its features count as symbols. What can be computed is fixed by the constraints on a bounded, local agent; what can be computed feasibly is fixed by the physics that implements the steps.**

The first clause is Deutsch (1985); the second is Turing's analysis (1936) as reconstructed by Sieg; the third is the failure of the extended Church–Turing thesis. The intuition had none of them. It had *reasoning as calculation* (Leibniz) and *calculation without understanding* (Prony's bottom tier).

Working claim broken by the genealogy: **computation is what a clerk does following finite rules with pencil and paper, and what can be computed is a fact of logic, independent of physics.** It fails three times, in three different ways — relocated, overturned, and extended (§6).

Distinctions worth keeping:

- **Computable vs. feasible.** Turing classifies problems as possible or impossible; complexity splits "possible" by cost. The first is robust across all known physics, the second is not.
- **Definition vs. adequacy.** "Recursive" is a precise class; "the recursive functions are exactly the effectively calculable ones" is a separate claim needing its own argument. Church offered evidence; Turing offered an analysis.
- **Total vs. partial.** A class of procedures that only halts can always be escaped by diagonalization. Completeness requires admitting procedures that run forever.
- **Code as data, logical vs. physical.** Programs as input to programs (Turing, 1936) has become the foundation of all software. Instructions and data in one mutable store (EDVAC, 1945) has been split, cached, and guarded against ever since.
- **Superposition vs. interference.** A quantum computer evaluating a function on every input gains nothing by itself; one reading returns one random result. The advantage is arranging amplitudes so wrong answers cancel.
- **Physics as computation vs. computation as physics.** "The universe is a computer" imports a program/hardware layer nature doesn't have. "What can be computed is fixed by physical law" is Deutsch's direction, and the defensible one.

Pattern: unlike entropy (formula first) or measurement (practice first), computation was invented to answer a question about proof — Hilbert's *Entscheidungsproblem* — and the machines came as a byproduct, built mostly by people who had not read the logic. (Position.)

---

## 2. The intuition — three strands that didn't know they were one

**Reasoning as calculation.** Llull's *Ars Magna* (c. 1305): rotating wheels of concepts, combining a finite alphabet exhaustively. Leibniz, *De Arte Combinatoria* (1666): a *characteristica universalis* (concepts as composites of primitives, like primes) and a *calculus ratiocinator* (rules for manipulating it) — disputes settled by "let us calculate." Also the stepped reckoner and binary arithmetic (1703). Missing: logic as algebra. And the inherited assumption: **every well-posed question can be decided by calculation**; limits are practical.

**Logic becomes algebra.** Boole (1847, 1854): classes as quantities, the defining law x² = x, logic as algebra on {0, 1}. Jevons's logic piano (1869). Frege's *Begriffsschrift* (1879): quantifiers, and the **gapless proof** — every step licensed by a rule applied to the shape of formulas, checkable by someone who doesn't know what it means. A formal language precise enough to be checked mechanically, with no mechanism. Russell's letter (1902) and *Principia* (1910–13) lead to stage 2.

**Calculation as divided labour.** Prony (1790s) organized table-making on Adam Smith's pin factory: mathematicians, planners, and a bottom tier (reputedly unemployed hairdressers) who only added and subtracted, via the method of finite differences. Computation as an activity requiring no knowledge of its meaning. Babbage mechanized the bottom tier: Difference Engine (1822; built by the Science Museum in 1991, and it works). Analytical Engine (1834–): store and mill, Jacquard cards, conditional branching. Lovelace's Notes (1843): a Bernoulli-number program; the engine operates on symbols, not only numbers; and it originates nothing (Turing answers "Lady Lovelace's objection" in 1950).

**What was missing.**
1. *A definition of "mechanical."* Only needed to prove something can't be done — as "solvable by radicals" had to be defined before Abel and Galois could prove the quintic impossible.
2. *Universality.* One machine simulating all others is a theorem, and needs the class defined first.
3. *The bridge.* Frege's notation is the program, Babbage's engine the machine; neither saw the other. The bridge was Prony's bottom tier, analysed: Turing's human computer.

*Position:* the working claim is where the intuition ends, and it looked well supported. Babbage failed on tolerances, money, and a quarrel with his engineer, which seemed to confirm that computation is abstract and brass an imperfect copy.

---

## 3. The dispute — what is an effective procedure?

**The question.** Hilbert's program asked consistency, completeness, decidability; Hilbert and Ackermann (1928) posed the *Entscheidungsproblem* for first-order logic. Gödel (1931) settled the first two negatively for a *specific* system; generality required knowing what a formal system is — one whose proofs are mechanically checkable. The open problem and the scope of incompleteness hung on the same undefined word.

**The first candidate fails.** Primitive recursive functions: all computable, all total. Ackermann (1928) exhibited a computable function outside them. Deeper reason: any effectively listable class of total functions can be diagonalized — g(n) = fₙ(n) + 1 is computable and on no list. **No definition of "computable" containing only total functions can be complete.**

**Church.** λ-calculus (1932–33); Kleene's predecessor (the dentist's chair). Church proposed λ-definability as the meaning of "effectively calculable" (c. 1934); Gödel found it thoroughly unsatisfactory. Gödel's own general recursive functions (1934, after Herbrand), with no claim of adequacy. Church–Kleene: the classes coincide. Church's thesis and the unsolvability of the *Entscheidungsproblem* (1936). Arguments: convergence (evidence, not proof — two definitions can share a blind spot) and step-by-step (circular).

**Post (1936).** A worker in a row of boxes, nearly Turing's model; the identification as a *working hypothesis*, a natural law about human mathematizing, to be tested — not a definition.

**Turing (1936).** Newman's question: is there a mechanical process for provability? Turing started from a person computing with pencil and paper and imposed justified constraints: finitely many symbols (else some indistinguishable), finitely many states of mind, bounded observation, local bounded steps. Anything satisfying them is simulable by the machine. Then the universal machine, a diagonal argument (his criterion was "circle-free"; "halting" is Davis's, 1950s), and a negative answer to the *Entscheidungsproblem*. Appendix proving equivalence with λ-definability; Princeton with Church. Church (1937): Turing's formulation made the identification evident immediately. Gödel (1946): the first absolute definition of an interesting epistemological notion; (1964) what makes incompleteness apply to every formal system.

**Why Turing won.** Church offered a definition plus evidence; Turing an analysis — the informal concept broken into explicit constraints, each individually plausible, from which the formal class follows. Galois's move: impossibility after the class of procedures is characterized.

**What resolved the diagonal problem.** Turing machines, like Kleene's partial recursive functions (1938), include procedures that never halt. Diagonalizing over them yields not a new machine but a contradiction — the undecidability of halting.

*Position:* **undecidability is the price of a closed definition.** Every Turing-complete language has infinite loops; total languages (Coq's and Agda's cores) guarantee termination and cannot express every computable function, including their own interpreters.

**Status of the thesis.** Definition (Church); law of nature (Post); analysis (Turing). Sieg (2002 onward) axiomatized Turing's computor and proved a representation theorem — the form of Hölder's theorem for measurement.

*Position:* the third reading is right, with a consequence: **the thesis is a theorem whose premises describe a physical agent** — finite distinguishability, locality. A wave was what locality looks like from outside; a computation is what locality and finite distinguishability look like for a symbol-manipulating agent. Gandy (1980) found the machine version needs bounded signal speed and bounded density of parts: physics.

Gödel's later dissent (1972, minds need not have finitely many states) concerns whether minds are mechanical, not the thesis about mechanical procedures.

Missing, now present: a class defined by constraints on the agent; partiality; the distinction between a definition and its adequacy. Silent casualty: sameness — two procedures are the same computation when they compute the same partial function.

---

## 4. The formalization — from universal machine to stored program

**What 1936 contained.** A machine's table is a string of symbols, so the universal machine reads other machines as data. The entire logical content of the stored-program idea. The cost: no clock, unbounded tape — nothing about time or memory, the only things engineers cared about.

**Three lineages without stored programs.**
- *Analog:* Bush's differential analyzer (1931); Shannon characterized what it generates (1941). Lost because continuous quantities accumulate error; digital restores each signal to one of finitely many states — Turing's distinguishability premise as engineering. Von Neumann (1956): reliable logic from unreliable components.
- *Relays:* Shannon's thesis (1937), Boolean algebra designs switching circuits. Stibitz's remote computation (1940). Zuse's Z3 (1941), program on film, no conditional branch. Aiken's Harvard Mark I (1944), instructions physically separate — the original "Harvard architecture"; Hopper.
- *Tubes:* Atanasoff–Berry (1937–42), electronic, not programmable. Colossus (1943–44), Flowers: valves are reliable if never switched off; secret until the 1970s.

**ENIAC** (Eckert and Mauchly, 1943–45; public 1946): ~17,500 tubes, decimal, fast, able to branch — and programmed by rewiring, days of setup for seconds of run. Programmed by Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Wescoff, Fran Bilas, Ruth Lichterman: Prony's middle tier, long unnamed. The setup problem is where the stored program came from on the engineering side.

**The EDVAC report** (dated 30 June 1945). Eckert's mercury delay line from radar made a real memory possible; an Eckert memo of January 1944 is disputed evidence of earlier thinking. Von Neumann, consultant from 1944 (Goldstine on the Aberdeen platform), wrote the *First Draft*: central arithmetic, central control, memory, I/O; binary; **instructions and numbers in one memory**; drawn in McCulloch–Pitts neurons, not circuits. Circulation counted as publication; stored program in the public domain; Eckert and Mauchly left (UNIVAC). Moore School Lectures (1946) seeded the first generation.

**Turing.** Frankel (1972): von Neumann urged him to read Turing (1936) and credited Turing with the fundamental conception; the report cites no one. Turing's ACE report (1946): more engineering detail, subroutines, programs that manipulate programs, and the prediction that programming would be where the intellectual interest lay. NPL was slow; Pilot ACE ran in 1950.

*Position on priority:* "stored program" is three things — the **logical concept** (Turing), the **engineering realization** (Eckert), the **architectural abstraction** (von Neumann). The name is unfair to the first two, but the third was real: an instruction set and organization standing between physics and programmer, which is what made the design copyable and what every ISA descends from.

**Memory made it real.** Delay lines (serial), Williams tubes (random access, temperamental), drums, then core (Whirlwind, 1953). Manchester Baby, 21 June 1948: highest proper factor of 2¹⁸, 52 minutes, 32 words. EDSAC, 6 May 1949: first regular service. ENIAC converted to run instructions from read-only function tables in spring 1948 (Haigh, Priestley, Rope); whether that counts decides "first" — the question has no answer until the concept is defined.

**To the architecture of today.** Self-modification was the first use of code-as-data: array loops by arithmetic on instruction addresses. Index registers (Manchester B-lines, 1949) made it unnecessary. Code-as-data moved into software: Wheeler's initial orders (first assembler and loader, 1949), the Wheeler jump, subroutine libraries, Hopper's A-0 (1952), FORTRAN (1957), interpreters, JITs. Hardware fenced it off: split L1 I/D caches (Harvard returning inside von Neumann), W^X, non-executable stacks. Backus (1977): the von Neumann bottleneck; the memory wall and speculative execution as workarounds.

*Position:* Turing's contribution grew with time, Eckert's shrank, and von Neumann's layer is what persists.

Missing at the end of the stage: a machine-independent measure of cost, and a notion of *feasible* distinct from computable.

---

## 5. The abstraction — computation as a bounded resource

**Gödel's letter** (1956, to the dying von Neumann; found 1988): for a formula of length n, how fast can one decide whether it has a proof of length ≤ n? If linearly or quadratically, mathematicians' yes-or-no work could be replaced by machines. P vs NP, fifteen years early. Bounded provability is trivially decidable; the question is only how long.

**Cost.** Rabin (1960); Hartmanis–Stearns (1965): time classes, and the time hierarchy theorem by diagonalization. Exact cost depends on the machine, so a coarser notion was needed.

**Cobham–Edmonds (1964–65).** Cobham: a machine-free characterization of polynomial-time functions, the same class on every reasonable model — Church's convergence applied to cost. Edmonds (*Paths, Trees, and Flowers*): blossom algorithm; polynomial = "good"; good characterizations (short certificates both ways, ≈ NP ∩ coNP); TSP conjectured hard (1967). Thesis: feasible = P.

**Why polynomial.** Contains linear time; closed under composition (subroutines); invariant across reasonable models (invariance thesis, Slot–van Emde Boas 1984); empirically, exponents shrink.

*Position:* misnamed. P is the class fixed by what computation must be closed under — composition and change of hardware — as partiality was forced by closure under diagonalization. "Feasible" is a label added afterwards, looser than "effective."

**The extended thesis.** "Reasonable" excludes unit-cost arithmetic on unbounded integers (factoring in polynomial steps, Shamir 1979) and infinite-precision analog machines — excluded because no physical register holds unboundedly many distinguishable values. Extended Church–Turing thesis: every physically reasonable model is simulable with polynomial overhead by a probabilistic Turing machine. Unlike the original, it has a credible counterexample.

**NP-completeness.** NP: checkable in polynomial time. Cook (1971; newly at Toronto): SAT is NP-complete, by encoding a machine's run as a Boolean formula. Levin (1973), from the Soviet *perebor* tradition. Karp (1972): 21 problems; Garey–Johnson (1979): hundreds. Sameness made explicit: **problems are the same if mutually reducible in polynomial time**; all NP-complete problems are one problem.

**The barriers.** Relativization (Baker–Gill–Solovay 1975); natural proofs (Razborov–Rudich 1994): if strong pseudorandom generators exist, no natural proof separates the classes, because it would be an efficient test telling pseudorandom functions from random; algebrization (Aaronson–Wigderson 2008).

*Position:* **the hardness of proving hardness is a consequence of hardness.** The shape of Chaitin's result: most functions need large circuits (counting), none provably so; the target is indistinguishable from what surrounds it.

**Randomness and secrecy.** Probabilistic primality (1976–77); BPP; BPP = P expected (Impagliazzo–Wigderson 1997); AKS (2002). Public-key cryptography (Diffie–Hellman 1976; RSA 1977); PRGs from one-way functions (Blum–Micali, Yao 1982); **PRGs exist iff one-way functions exist** (HILL 1999). Hardness spent two ways: to remove randomness, or to manufacture it for bounded observers. Impagliazzo's five worlds (1995); TLS bets on Cryptomania. Cryptography is "what can be compared is bounded by what can be computed," engineered.

**SAT solvers.** CDCL (GRASP 1996, Chaff 2001) solve industrial instances with millions of variables. *Position:* not a counterexample; worst-case theory classifies what problems can encode, and real instances are structured — low-entropy descriptions of the search space.

**Landauer–Bennett, briefly.** Only erasure costs kT ln 2; any computation can be made reversible (Bennett 1973; time–space trade-off 1989). Fredkin–Toffoli (1980–82): the Toffoli gate is universal for reversible classical logic — the classical part of quantum circuits.

Left open: what "reasonable" means (a physics question), why hardness can't be proved, and whose bound it is (an observer's).

---

## 6. The payoff — is computation physical?

**Feynman (1982):** simulating n quantum particles classically needs exponentially many amplitudes; simulate quantum with quantum. **Deutsch (1985):** the Church–Turing thesis as a physical principle; classical machines fail it for quantum systems; a universal quantum computer; the theory of computation as a branch of physics. Bernstein–Vazirani (1993), BQP; Simon (1994); Shor (1994).

**What it doesn't do.** "Tries every answer at once" is wrong: evaluating on a superposition then reading gives one random result. Amplitudes are arrows; probabilities only add, arrows can cancel. Algorithms arrange wrong answers to cancel. Unstructured search gets only Grover's square-root speedup, optimal (BBBV 1997); NP-complete problems believed outside BQP.

**Worked example: factoring 15.**
- *Classical reduction.* Powers of 7 mod 15: 1, 7, 4, 13, 1, … period r = 4. Then 7⁴ − 1 = (7² − 1)(7² + 1) = 48 · 50, remainders 3 and 5; 15 = 3 × 5. Period-finding for 2048-bit numbers has no known classical shortcut.
- *The comb.* Superpose x = 0…15, compute 7ˣ mod 15; reading remainder 4 leaves x = 2, 6, 10, 14 — spacing = period, starting point random. Reading x directly is useless.
- *The Fourier transform.* Output y collects an arrow from each tooth at y·x/16 of a turn. y = 1: ⅛, ⅜, ⅝, ⅞ — cancel. y = 2: ¼, ¾, ¼, ¾ — cancel. y = 4: ½, ½, ½, ½ — reinforce. Survivors 0, 4, 8, 12, each ¼. The random start rotates all arrows of an output equally (Fourier shift property): phases change, alignment doesn't.
- *Readout.* y/16 = ¼ or ¾ → r = 4; ½ → try 2, fails, rerun; 0 → rerun. For large N, a bigger register and continued fractions.

**Where the speedup lives.** The arithmetic is reversible Toffoli logic — the bulk of the cost (a few billion Toffolis for RSA-2048 in Gidney's 2025 design). The QFT on 2ⁿ amplitudes takes ~n² gates, factoring like the FFT (Cooley–Tukey 1965), but yields one sample, not the spectrum. *Position:* the computer never knows the function's values; interference extracts one global property and sacrifices the rest. Lovelace's store of readable symbols becomes a store of amplitudes that can be used but not looked at.

**Symmetry again.** A periodic function is shift-invariant: the period is a hidden symmetry; Shor solves the abelian hidden subgroup problem; non-abelian (graph isomorphism, some lattice problems) largely open. Bernoulli's mode decomposition finds a Galois-style symmetry. *Position:* **quantum speedup, where it exists, is the detection of hidden symmetry by interference.**

**What has been built** (as of September 2026). Sampling advantage (Sycamore 2019; boson sampling from 2020) real on contrived tasks, magnitude contested. Error correction the real milestone: Willow (2024), logical error falling ~2.14× per surface-code size step; 2026 — QuEra up to 96 verified logical qubits, Microsoft–Quantinuum logical computation beyond memory (Nature). Factoring: no cryptographic-size Shor run; estimates falling — Gidney 2025, RSA-2048 with under a million noisy qubits in under a week (20 million in 2019); 2026 preprints lower on unbuilt, non-comparable architectures. The reason post-quantum cryptography is being deployed now.

**Positions on the physical thesis.**
1. *The original thesis survives:* classical machines simulate quantum ones with exponential slowdown; nothing new is computable.
2. *The extended thesis is probably false* — conditional on factoring not being in BPP (BQP ≠ BPP unproven). The first thesis about computation overturned, conditionally, by a physical theory.
3. *The quantum extended thesis is the live candidate:* holds for QFT (Jordan–Lee–Preskill 2012); gravity open — Bouland–Fefferman–Vazirani (2019) on the AdS/CFT dictionary; Susskind's complexity–volume conjecture. Conjectural throughout.
4. *"Is physics computation?"* (a) Efficient quantum simulability — defensible. (b) The universe as a classical computer (Zuse 1969, Fredkin, Wolfram) — refuted in local form by Bell unless superdeterminism ('t Hooft pays that price). (b) confuses description with substrate: it imports §4's program/hardware layer where there is no interpreter. **Physics is not computation; computation is a physical category.**

**The working claim, broken three times.**
1. *The clerk became the definition* — computability rests on physical premises. **Relocated.**
2. *Feasibility depends on physics* — the extended thesis falls to quantum mechanics. **Overturned**, conditionally.
3. *Hardness became a physical boundary* — cryptography, natural proofs, horizons (Harlow–Hayden). **New.**

**What the intuition could never have said.** Leibniz expected calculation to end disputes. Turing: some questions can't be calculated. Complexity: most that can, can't in practice. Quantum computation: which are practical depends on physical law, and the most powerful computers hold states no one can read.

*Closing position:* **a computation is a physical process viewed through a description that says which of its features count as symbols.** The division thread again: the logical description is a coarse-graining of a physical process, objective once fixed, like entropy — and the physics beneath the description decides what it can achieve.

---

## 7. The single line of thought

One question, asked with steadily less confidence that logic alone answers it: what can be done by following rules, and what decides it?

| Stage | Computation is… | Performed by | What it yields |
|---|---|---|---|
| Llull / Leibniz / Boole / Frege | reasoning reduced to symbol manipulation | an idealized reasoner | the dream that calculation ends disputes; gapless proof |
| Prony / Babbage / Lovelace (1790s–1843) | divided labour needing no understanding | clerks, then brass | the engine; symbols beyond number |
| Church / Post / Turing (1936) | what a bounded, local agent can do | the analysed clerk | undecidability; universality; partiality as the price |
| Eckert / von Neumann / Turing (1944–49) | an instruction stream in a shared memory | the stored-program machine | the architecture layer; code as data made physical |
| Cobham / Edmonds / Cook / Karp (1964–72) | a process with a cost | any reasonable machine | P, NP, completeness; sameness as reduction |
| Yao / Razborov–Rudich (1982–94) | what bounded observers can and can't distinguish | an observer with limited computation | pseudorandomness, cryptography, the barriers |
| Feynman / Deutsch / Shor (1982–94) | a physical process described as symbolic | whatever the laws permit | the extended thesis overturned; speedup as hidden symmetry |

Waves kept the space and lost the substrate. Symmetry kept the group and lost the object. Entropy kept the logarithm and lost the engine, the gas, and the ignorance. Randomness kept the absence. Measurement kept the record. Computation kept the *step* and lost the clerk, the readable store, and the guarantee that logic alone decides what a step can do.

---

## Suggested next steps

- Run the diagonal argument against the primitive recursive functions by hand: list a few (f₀(n) = 0, f₁(n) = n + 1, f₂(n) = 2n, …), define g(n) = fₙ(n) + 1, and see why no total list escapes it — then see why the same move against Turing machines produces the halting problem instead of a new machine.
- Do Shor's classical reduction for N = 21 with a = 2: powers of 2 mod 21 are 1, 2, 4, 8, 16, 11, 1, … (period 6); then 2³ = 8 gives 7 and 9, sharing factors 7 and 3 with 21. Then draw the comb for a 32-value register and check which outputs cancel.
- Read Turing (1936) §9 alongside Sieg's axiomatization, and compare with Hölder's theorem in the measurement notes.
- Reading: Turing, "On Computable Numbers" (1936); Gödel's 1956 letter (in Sipser's 1992 survey or online); von Neumann, *First Draft of a Report on the EDVAC* (1945); Haigh, Priestley, and Rope, *ENIAC in Action* (2016); Cook (1971); Aaronson, *Quantum Computing Since Democritus* (2013); Deutsch (1985).
- Links forward: *Proof* (Curry–Howard, Gödel, natural proofs; see *curry-howard.md*); *Space* (complexity–volume, the holographic dictionary, factorization); *Time* (reversible computation and the arrow).
