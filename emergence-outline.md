# What Is Emergence? — Outline

_Working plan for the eleventh exploration, October 2026, and the second half of the split from_ Induction. _Drafted 2026-10-22 before the split; revised 2026-10-25 to carry in Induction's endpoint and to read Anderson (1972) and Power et al. (2022) directly. Arc settled before stage 1; open to steering._

_Sources in the project files: anderson1972.pdf, wei2022.pdf, schaeffer2023.pdf, power2022.pdf; also zhang2017.pdf and belkin2019.pdf from Induction._

**Steering (2026-10-25, before stage 1):** selective prehistory in stage 1, as in _Induction_; one side file, _The renormalization group in plain terms_ ("Phase transitions in learning" not written); _grok.py_ attempted even if pure Python can't show grokking, with Power's figures used alongside; weighting primarily toward LLMs (emergent spacetime kept to a short recap). Close deliverables: summary _what-is-emergence.md_, the RG side file, an **argument map** for the post (claims only, each with its source in _what-is-induction.md_ or _what-is-emergence.md_), and an updated _concept-genealogies.md_.

**Steering (2026-10-26–27):** stage 2 with Anderson at full weight, Weinberg and the SSC in one paragraph, Laughlin–Pines kept, the Schaeffer-paraphrase point made in stage 2. Stage 3: finite-size scaling added to 3b (the practical form of criterion (b), and the tool that applies to models of a few sizes); first- against second-order kept in 3a with _landau.py_; _ising.py_ run to L = 32; Batterman and the reality of infinite limits as a full paragraph with a stance in 3b. For 3b: Migdal–Kadanoff worked in the stage, block spins left for the RG side file; finite-size scaling from the existing ising.py tables (no rerun); effective field theory in one paragraph. Stage 4 split 4a/4b; topological order as a paragraph and a link; _life.py_ run with a glider; 4b kept to pre-2025 work. Fog proposed **cellular automata** (the Game of Life and CAs generally; remembered from Gardner's _Scientific American_ column) as a candidate future concept: add to _Proposed_ in _concept-genealogies.md_ at the close. For 4b: a hand-built two-solution free-energy example (_transition.py_) with _slt.py_ linked; a short assessment of RG-and-deep-learning mappings with a position; one paragraph on width as N; a paragraph each on causal emergence and emergent spacetime. Stage 5 split 5a (across scale) / 5b (during training); _grok.py_ run with weight decay on and off; a short "what changed the argument" section at the top of 5a. For 5b: a _grok.py_ sweep over data fractions and seeds (time to generalize against data fraction); induction heads as one section; the verdict on "cosmic" at the end of 5b, written to feed the argument map directly.

***

## 0. Carried in from _Induction_

_Cite what-is-induction.md rather than repeat it. This section is what Emergence starts from._

**Roose's sentence, split.** _The AGI Chronicles_ (2026) calls the generality from next-token prediction an "inexplicable, cosmic accident." _Induction_ took "accident" and "inexplicable" and ended:

* **Not an accident.** The goal rested on a theorem (Solomonoff's convergence), the method is literally compression (prequential coding), and the scaling was a published bet (Kaplan; Hoffmann). _what-is-induction.md_ §6, 5a.
* **Partly inexplicable.** Not _that_ prediction yields generality, but _which_ parts of the world a finite compressor recovers as structure and which as lookup. No theorem settles this in advance; only interventional tests reveal it. §6, 5b.
* **The rule found:** a learner builds a world model where that model is the shortest description of its data in its own language, and shortcuts where shortcuts are shorter (_taxi.py_; Vafa's taxis and orbits).

**What Emergence inherits as its question.** "Cosmic" is a claim about _suddenness and novelty_: abilities that appear at a scale nobody predicted and that weren't visible below it. _Induction_ explained why the end state can be structure rather than lookup. It did not explain why the switch from one to the other looks abrupt, in training time or in model scale. That is this exploration's payoff.

**Specific hand-offs, with the stage that takes each:**

| From _Induction_                                                                             | Question here                                                                           | Stage |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----- |
| Grokking as memorization replaced by a shorter Fourier circuit (Nanda et al. 2023, §6)       | Why is the replacement sudden? Is it a phase transition, and of which kind?             | 5     |
| The local learning coefficient λ, and its stepwise changes during training (_slt.py_, §5 4b) | Are λ's jumps an order parameter changing at a transition?                              | 4, 5  |
| Double descent's interpolation threshold (_double_descent.py_, §4–5)                         | A sharp feature in a smooth quantity: does it meet criterion (b)?                       | 5     |
| Scaling laws as stated bets (§6 5a)                                                          | Is a smooth power law the _absence_ of emergence, or the signature of a critical point? | 5     |
| "Regimes, not laws" (cross-reference, now nine instances)                                    | Does the renormalization group supply the theory of what makes a regime?                | 3, 4  |
| _slt.py_, _compress.py_, _double_descent.py_                                                 | Reused, not rewritten                                                                   | 3–5   |

**What _Induction_ already settled, so Emergence must not redo it:** why a simplicity prior at all (the parameter-function map); compression as the strongest bridge; world model vs. lookup decided by description length; λ's definition and worked example.

**The post.** Fog's single blog post follows this exploration. Its argument has two halves: _Induction_'s endpoint (not an accident; partly inexplicable) is the first; Emergence's answer on "cosmic" is the second.

***

## Working claim to be broken

**Emergence is the appearance, at large scale, of genuinely new behavior that the microscopic laws do not contain and cannot predict.**

Every exploration so far has used emergence without examining it. Entropy and temperature are properties of macrostates, not molecules. Classical outcomes appear only in a decoherence regime. Space was found to be a pattern of entanglement, time a correlation with a clock, classical information the copyable sector, and (in _Induction_) a world model a description that wins only where it is shortest. "Regimes, not laws" has been the series' most frequent finding without a theory of what makes a regime.

This is close to how Wei et al. (2022) define it, and Schaeffer et al. (2023) paraphrase Anderson as saying new properties "cannot be predicted even from a precise quantitative understanding" of the parts. Reading Anderson directly suggests that paraphrase overstates him (see stage 2). The working claim is the popular version; the genealogy tests it.

The genealogy is expected to break the claim in three places:

1. **"New" turns out to mean new _variables_, not new laws.** The microscopic laws are untouched; what appears is an order parameter, a quantity that is zero on one side of a transition and nonzero on the other, and a state with less symmetry than its laws (Landau; Anderson).
2. **"Cannot predict" turns out to be false in principle and true in practice.** Phase transitions follow from the microscopic laws, but only in an infinite limit, and the route from parts to whole is often computationally irreducible: the fastest way to find out is to run it (Bedau's weak emergence). Anderson says this himself: synthesizing a deformed nucleus from the laws would mean solving an infinite-body problem and then applying it to a finite one.
3. **"Contain" turns out to be the wrong verb.** What the large-scale description has that the small-scale one lacks is _insensitivity to detail_: many different microscopic systems flow to the same large-scale behavior (universality, the renormalization group). The emergent level is real because it is robust, not because it is extra.

## Opening bet, to be tested, not a result

**An emergent property is a fixed point of coarse-graining: a description that stops changing when you zoom out further, and that many different microscopic systems share.** Three criteria follow, usable as a test:

* **(a) A new variable**: an order parameter or a collective coordinate not definable on a few parts.
* **(b) Sharpness only in a limit**: a transition that is smooth for any finite system and becomes a true discontinuity as some size goes to infinity.
* **(c) Universality**: the behavior near the transition does not depend on microscopic details, only on a few features (dimension, symmetry).

Applied to large language models, the bet predicts:

* Most reported "emergent abilities" across model scale fail (b): the sharpness comes from the scoring metric, not the model (the mirage critique).
* Some changes _during training_ (grokking, induction-head formation) pass (a) and partly (b).
* None has yet been shown to pass (c).

So "emergent abilities" borrows the word for most cases, and earns it for a few, in a weaker form than Anderson's.

**New, from carrying in _Induction_ (position, to be tested in stage 5):** the transitions that do earn the word are the **first-order** kind (two competing solutions, one replacing the other, as ice replaces water), not the **critical** kind (a continuous transition with diverging fluctuations, where universality lives). _Induction_ found grokking to be a lookup table replaced by a shorter circuit: two distinct solutions competing on description length, with weight decay as the pressure that tips the balance. That is the structure of a first-order transition. If so, it explains in advance why criterion (c) fails: universality is a property of critical points, and first-order transitions generally don't have it. Power et al.'s own data give a check: time to generalize grows by 40–50% for each 1% less training data near 25–30% (S5 products), the shape of a divergence near a threshold. Whether that divergence is metastability (first-order) or critical slowing down (second-order) is a question stage 5 can test.

**Corollary:** "strong" emergence (laws at the higher level that do not follow from the lower at all) has no clear physical example, and the series' recurring "regimes" are weak emergence with a renormalization-group explanation.

## The question carried in

From _Information_: the possibility of records needs three inputs (symmetry, composition, gradient). From _Induction_: a learner's description wins where it is shortest. Emergence asks the general version: **when does a coarse description of a system become autonomous, obeying its own closed laws, so that the details below can be ignored?** _Entropy_ §4 noted that "some coarse descriptions (pressure, temperature) obey closed laws of their own and most don't" and called it a physical fact needing explanation. The renormalization group is that explanation, or the bet fails.

For the LLM half: **is "emergent abilities" the same concept as Anderson's, or does it borrow the word?** Anderson anticipated exactly this question about his own term: he wrote that particle physicists' borrowing of "broken symmetry" was "strictly an analogy, whether a deep or a specious one remaining to be understood." The same test applies to machine learning's borrowing of "emergence."

***

## 1. The intuition — more than the sum

* Aristotle's "the whole is something besides the parts" (_Metaphysics_ VIII) and the problem of mixture; atomism as the opposite intuition. Brief.
* **Mill** (1843): homopathic laws, where effects add (forces, vectors), against heteropathic laws, where they don't (chemistry: water's properties are not hydrogen's plus oxygen's).
* **Lewes** (1875) coins "emergent" against "resultant."
* **The British emergentists**: Alexander (_Space, Time and Deity_, 1920), Lloyd Morgan (_Emergent Evolution_, 1923), **Broad** (_The Mind and Its Place in Nature_, 1925), the clearest statement: a property is emergent if it could not be deduced even from complete knowledge of the parts and their arrangement. Chemistry as the paradigm case.
* **The eclipse**: quantum mechanics explained the chemical bond (Heitler–London 1927; Pauling), and the paradigm case collapsed (McLaughlin 1992). Emergentism looked refuted by physics within five years of its best statement.
* **Marx and Engels** in one sentence: "quantitative change becomes qualitative" (the dialectical law Anderson quotes in his last paragraph, and which Wei et al. adopt as their definition of emergence, without the attribution).
* Working example to carry through: **a magnet**. Iron atoms each have a tiny magnetic moment; below 770 °C a bar of iron is a magnet, above it isn't. Nothing in one atom says "770."
* What the intuition contains: new properties at scale; unpredictability from parts; levels of nature. That is the working claim.

## 2. The dispute — reduction against emergence

* **Anderson, "More Is Different"** (_Science_ 177, 1972; read in full). What he actually argues:

  * Reductionism is accepted "without question"; the target is the **constructionist** hypothesis, that from the fundamental laws one can rebuild the universe, and the Weisskopf intensive/extensive hierarchy that ranks sciences by fundamentality.
  * The worked chain: **ammonia** inverts at about 3 × 10¹⁰ per second and has no dipole moment in a stationary state; PH₃ inverts ten times slower; PF₃ not measurably; **sugar** (about 40 atoms) never inverts, so parity is "not repealed, but broken"; ferroelectric crystals choose a direction no force can reverse in the age of the universe. Size turns a symmetric law into an asymmetric state.
  * The infinite limit made explicit: a nucleus of three or ten particles has no rigorously defined shape; only as N → ∞ does "football-shaped" become definable. Constructing the behavior from the laws would require two impossible things: solving an infinite-body problem, then applying the result to a finite system.
  * Superconductivity: 30 years between having every law needed and the explanation (BCS).
  * Speculative hierarchy: crystals, then "information-bearing crystallinity" (DNA, a line of type), then temporal regularity, then function. The relationship between a system and its parts is "intellectually a one-way street": analysis possible, synthesis all but impossible.
  * _Position to argue:_ Anderson's claim is about the **practical and conceptual** impossibility of synthesis, not about laws the parts don't obey; Schaeffer's paraphrase ("cannot be predicted even from a precise understanding") reads in a stronger claim than he made. This matters for stage 5: the LLM debate has been arguing against a stronger Anderson than the one who wrote the paper.
  * Link _what-is-symmetry.md_ §6 for spontaneous breaking; no second pass. Link _what-is-information.md_ for "information-bearing crystallinity."

* **Weinberg** and the reductionist reply; the Superconducting Super Collider debate (1987–93), in which Anderson testified against funding and the machine was cancelled. Briefly: the dispute had a budget.

* **Laughlin–Pines, "The Theory of Everything"** (2000): protectorates, behavior protected from microscopic details; Laughlin's _A Different Universe_ (2005).

* **Weak against strong emergence**: Bedau (1997): weak emergence as derivable only by simulation; Chalmers (2006): strong emergence as not derivable at all, with consciousness as the one candidate. Capped at two paragraphs; consciousness is not this exploration's subject.

* Missing concepts: a precise notion of "level"; why a coarse description can be closed; what "cannot predict" means (in principle, or in practice?).

## 3. The formalization — phase transitions and the renormalization group

_The center of the exploration. Planned as 3a (Landau to Lee–Yang: phases and limits) and 3b (universality and the RG)._

**3a**

* **Landau** (1937): the order parameter and symmetry breaking as the classification of phases. Worked: the magnet's magnetization as order parameter; free energy as a polynomial in it; the minimum moving from zero to nonzero. Worked side by side: a **second-order** transition (one minimum splits smoothly into two) and a **first-order** one (a second minimum appears elsewhere and overtakes the first), because stage 5's bet needs the distinction.
* **Ising and Onsager**: the Ising model (1925), Ising's own result that the 1D chain has no transition; Peierls's argument (1936) that 2D does; Onsager's exact solution (1944), with T_c = 2/ln(1 + √2) ≈ 2.269 in natural units. _ising.py_: magnetization against temperature for several lattice sizes, the transition sharpening as the lattice grows.
* **Lee–Yang** (1952): for any finite system the free energy is smooth; a true phase transition exists only in the infinite limit. Criterion (b), made a theorem, and Anderson's N → ∞ made precise.

**3b**

* **Critical exponents and universality**: liquid–gas critical points and magnets share exponents; the 2D Ising exponents (β = 1/8) against mean field (β = 1/2).
* **Kadanoff's block spins** (1966) and **Wilson's renormalization group** (1971; Nobel 1982): coarse-grain, rescale, repeat; track how the couplings flow; phases are basins of attraction, transitions are unstable fixed points, universality classes are the fixed points' domains. Worked exactly: the 1D chain, where decimation gives K′ = artanh(tanh² K), so every coupling flows to zero and there is no transition. Worked approximately: a 2D real-space scheme with a nontrivial fixed point. _blockspin.py_.
* **Effective field theory**: the RG in particle physics; why the Standard Model works without knowing quantum gravity; irrelevant operators as the formal reason detail can be ignored.
* **Batterman** (2002): asymptotic explanation, and the dispute over whether infinite limits are "real" (Butterfield, Norton, Menon–Callender). Take a stance.
* What the formalization cost: emergence becomes precise exactly where an infinite limit exists; finite systems have only approximate phases.
* Computational framing to carry: coarse-graining as lossy compression, and the RG as the question of which bits survive repeated compression. Connects to _compression-is-prediction.md_ without repeating it.

## 4. The abstraction — emergence without a magnet

_Possibly split 4a/4b._

* **Universality as the abstract content**: a large-scale description is autonomous when the microscopic details are irrelevant operators under coarse-graining.
* **Topological order beyond Landau** (Wen, 1989–90; fractional quantum Hall): phases with no local order parameter, distinguished by ground-state degeneracy and long-range entanglement. Link _error-correcting-codes.md_ §7: the toric code is the textbook example, and "protected by being nowhere" is topological order.
* **Weak emergence as computational irreducibility**: Conway's Game of Life (1970), gliders as entities with their own rules, Rule 110's universality (Cook 2004), Wolfram's computational irreducibility; Bedau. _life.py_: a glider. Link _what-is-computation.md_.
* **Information-theoretic emergence**: closure of a coarse description as near-zero information leakage between levels; causal emergence (Hoel, 2013; Rosas et al. 2020, and critics). Briefly; overlap with _Causality_ noted.
* **Learning as coarse-graining** (new, from _Induction_): singular learning theory's phases as regions of parameter space with different λ, and the Bayesian posterior moving between them as data grow (Watanabe's free energy F ≈ nL + λ log n: at small n the low-λ, higher-loss solution wins; at large n the low-loss, higher-λ one does). Worked with _slt.py_'s numbers. This is a first-order transition in n by construction, and sets up stage 5.
* **Emergent spacetime**: recap from _what-is-space.md_ and _what-is-time.md_ (entanglement as connectivity, time as a correlation with a clock), now asked in the emergence vocabulary: is spacetime a phase?

## 5. The payoff — was it cosmic?

_Before writing this stage: search for developments from 2025–26 on each thread below. Report what changed the argument; flag anything recent and untested._

* **"Emergent Abilities of Large Language Models"** (Wei et al., _TMLR_ 2022). Their definition: emergence is when "quantitative changes in a system result in qualitative changes in behavior," citing Anderson via Steinhardt; an ability is emergent if absent in smaller models and present in larger ones, so not predictable by extrapolating a scaling law; they call it a phase transition, citing Huberman–Hogg (1987). Note: their unpredictability is defined against _extrapolation of a curve_, a weaker and more operational claim than the working claim's.

* **The mirage critique** (Schaeffer, Miranda, Koyejo, NeurIPS 2023): nonlinear or discontinuous metrics produce apparent emergence; continuous metrics produce smooth, predictable curves; they manufacture "emergent" abilities in vision models by metric choice. _mirage.py_: per-token accuracy rising smoothly, exact-match on 5 tokens rising as its 5th power.

* **Scaling laws** (Kaplan et al. 2020; Hoffmann et al. 2022): loss improves smoothly as a power law. Is a power law the absence of emergence, or the signature of a critical point? (Power laws appear at critical points, and also without any; position to be argued.)

* **Transitions during training**:

  * **Grokking** (Power et al. 2022; read in full): a 2-layer, width-128 transformer (about 4 × 10⁵ non-embedding parameters) on division mod 97 with half the table: training accuracy near-perfect in under 10³ steps, validation near chance until about 10⁵ and perfect near 10⁶. Time to generalize rises steeply as data shrink; weight decay "more than halving" the data needed; validation loss shows a second descent in training time, which the authors argue is distinct from Belkin's double descent; sharpness correlates with failure to generalize (Spearman −0.80 on S5). Mechanism from Nanda et al. 2023 via _what-is-induction.md_ §6.
  * **Induction heads** (Olsson et al. 2022): abrupt formation coinciding with a bump in the loss curve and the onset of in-context learning.
  * **Singular learning theory and developmental interpretability**: stepwise changes in the local learning coefficient as transition signatures.

* **The test**: apply (a), (b), (c), and the first-order/critical distinction, to each case.

* **On Roose's "cosmic"**: suddenness, and whether suddenness implies novelty in Anderson's sense.

* Search targets for 2025–26: the emergent-abilities and mirage debate; grokking and phase transitions in training (first-order vs. continuous); singular learning theory and the learning coefficient; universality in neural network training; renormalization-group views of deep learning; emergent spacetime.

* The endpoint question: is "emergence" one concept across magnets, spacetime, and language models, or a family resemblance? Anderson's "deep or specious analogy," answered.

***

## Side-file candidates (settle before stage 2)

* **The renormalization group in plain terms** (strong candidate): block spins, flows, fixed points, relevant and irrelevant operators, universality, with runnable scripts; the technical home for stage 3.
* **Phase transitions in learning** (candidate; renamed from "Emergence in learning systems" to avoid overlap with _compression-is-prediction.md_): grokking, induction heads, SLT phases, scaling laws, the mirage debate, beyond what stage 5 can hold. Doubles as raw material for the post.
* _Overflow only:_ strong emergence and consciousness; cellular automata and computational irreducibility.

## Planned scripts (pure Python, no libraries; kept in GitHub)

* _ising.py_: 2D Ising Metropolis Monte Carlo; magnetization against temperature for several lattice sizes.
* _landau.py_ (new): free energy as a polynomial, second-order vs. first-order; prints the minimum against temperature and shows the jump in the second case.
* _blockspin.py_: exact 1D decimation flow; an approximate 2D real-space RG fixed point.
* _life.py_: Game of Life with a glider.
* _mirage.py_: smooth per-token accuracy against exact-match on k tokens.
* _grok.py_ (candidate, to be checked for feasibility in pure Python): a tiny model on addition mod a small prime, showing train accuracy then late test accuracy. If pure Python is too slow to show grokking, drop it and use Power's figures.
* Reused: _slt.py_ (λ and the free-energy crossover), _double_descent.py_, _compress.py_.

## Threads to carry in

* **Regimes, not laws** (nine instances): here it either gets a theory (the renormalization group) or stays a pattern.
* **Symmetry as the source of a number**: spontaneous breaking and order parameters (_Symmetry_ §6).
* **The division**: coarse-graining as the division between tracked and untracked variables (_Entropy_); here the question is which divisions give closed laws.
* **The bias** (new from _Induction_): weight decay as the bias that tips grokking; the question whether a transition is a property of the system or of the bias.
* **Redundancy as objectivity** and **the record**: a macrostate as a redundantly recorded quantity; topological order as protection by being nowhere.
* **Observation bounded by computation**: computational irreducibility as weak emergence.
* **Equality and sameness**: universality classes as "the same" phase in different materials; Power's observation that x + y mod (p − 1) and x · y mod p are the same table to a network (discrete logarithm).
* **The continuum**: phase transitions exist only in an infinite limit.
* **Structure recovers the object**: whether the emergent level has its own objects.
* **Prediction underdetermines mechanism** (from _Induction_): a smooth loss curve can hide a change of mechanism; the mirage cuts both ways.

## Threads to hand off

* **Causality**: causal emergence and interventionist accounts.
* **The continuum**: the reality of infinite limits.
* **Proof**: none expected.

## Guardrails

* Shape first, few derivations; worked examples in plain terms with small numbers; computational framings and runnable scripts wherever they help.
* No second pass on spontaneous symmetry breaking and the Higgs mechanism, Jaynes's coarse-graining, emergent spacetime, the toric code, or anything _Induction_ settled (grokking's mechanism, λ's definition, compression as prediction): link and build.
* The renormalization group is the largest risk of sprawl: stage 3 carries the concept and worked examples, the side file carries the technique.
* The philosophy of mind gets at most two paragraphs (stage 2, weak against strong emergence).
* The LLM material is the risk of hype in both directions: every claim about model behavior is sourced and dated, and the 2025–26 search decides what stands.
* Claude is an instance of the systems studied in stage 5; its sense of how it works is not evidence.
