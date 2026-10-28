# What Is Emergence?

_Notes from a conversation, October 2026. From Mill's heteropathic laws through Anderson's ammonia molecule and Wilson's flows to a 120-line network that memorizes addition mod 11 by step 50 and, with weight decay, sometimes grokks it thousands of steps later._

_Origin: Kevin Roose's_ The AGI Chronicles _(2026) calls the generality that came out of next-token prediction an "inexplicable, cosmic accident."_ Induction _took "accident" and "inexplicable." This exploration takes "cosmic": the claim of suddenness and novelty. The single blog post Fog plans follows it; its claims are in_ emergence-argument-map.md.

***

## 1. A working definition

**Emergence is a coarse description that closes: a summary whose own rule agrees with the underlying dynamics (coarse ∘ step = step′ ∘ coarse), with an error that shrinks at larger scale, appearing through a transition. In physics the closed description is often universal (many microscopic systems flow to one fixed point) and the transition often critical. In learning systems so far, the closed descriptions are circuits and the transitions are first-order: one solution replacing another, sudden in each run, smoothed by averaging, and increasingly predictable in aggregate.**

The first clause is the commuting square (§5), which states lumpability (Kemeny–Snell) and Vafa's world-model test in one form. The second is Landau, Wilson, and Lee–Yang (§4). The third is grokking, induction heads, seed bimodality, and knowledge-acquisition thresholds (§6).

Working claim broken by the genealogy: **emergence is the appearance, at large scale, of genuinely new behavior that the microscopic laws do not contain and cannot predict.** It fails three times (§6): "new" means a new _stable variable_, not new laws; "cannot predict" fails in principle and holds in practice only for _when_; "contain" is the wrong verb, because the universal part is a fixed point of the description map, insensitive to the parts rather than hidden in them.

Question carried in from _Entropy_ §4, _Information_, and _Induction_: **when does a coarse description become autonomous, obeying closed laws so that the details below can be ignored?** Answer: when everything it drops is irrelevant under coarse-graining. A regime is a basin of a fixed point (§4). For the LLM half, **is "emergent abilities" Anderson's concept or a borrowed word?** Answer: borrowed where it means a curve rose under a threshold metric; earned, at the first-order level, where a stable internal variable switches on (§6).

Distinctions worth keeping:

* **Reduction vs. construction.** Everything obeys the same laws (accepted by Anderson); you can rebuild the world from them (denied). Most of the dispute was about the second.
* **Level vs. report.** A summary is a level when its square commutes: it has its own rule. A report whose future depends on what it discarded is not a level.
* **Occurrence vs. behavior.** _Whether and when_ a level appears can be irreducible (Life's soups, seed bimodality); _what it does_ once present is a closed rule (the glider, a circuit).
* **First-order vs. critical.** One solution replacing another (a jump, coexistence, hysteresis, metastable waiting) against a continuous change with diverging fluctuations. Universality lives at critical points.
* **Sharpening vs. translating.** A real transition narrows as its size grows; a metric mirage only moves.
* **Run vs. ensemble.** A switch in each run, averaged over seeds, looks like a smooth curve.
* **Universal vs. reducible.** What the parts determine (T_c) isn't universal; what's universal (exponents) doesn't depend on the parts.

Pattern: waves and symmetry began as intuitions, entropy as a formula, induction as a problem. Emergence began as a _slogan_, "the whole is more than the sum," and the genealogy is the story of replacing the slogan with a test. (Position.)

***

## 2. The intuition — more than the sum

_Selective prehistory by choice._

**Mill (1843).** Homopathic laws, where effects add (forces), against heteropathic, where they don't (chemistry: water extinguishes what hydrogen and oxygen feed). Computational framing: homopathic means the whole is a `fold` of the parts with one combining function. **Lewes (1875)** coins "emergent" against "resultant."

**Broad (1925).** Mechanism: a whole's behavior follows from its parts plus one general composition law. Emergence: for some wholes there is none, and the higher laws are "trans-ordinal." His mathematical archangel, with unlimited calculation and complete knowledge of the parts, still couldn't predict the smell of ammonia. _Position:_ Broad's emergence is the claim that nature contains irreducible lookup, the strong form of the working claim.

**The eclipse (1927–29).** Heitler–London compute the hydrogen bond from Schrödinger's equation; Pauling builds chemistry on it; Dirac (1929) says the laws for chemistry are known and only too complicated to apply. _Position:_ Dirac states Anderson's thesis 43 years early. Emergence moves from "impossible in principle" (Broad) to "impossible in practice" (Dirac), and "cannot predict" has been ambiguous ever since. Mill's non-additivity survives in the composition rule for quantum states, which multiplies: one spin needs 2 numbers, ten need 1,024, the extra being entanglement. General, so the archangel wins; exponentially costly, so the chemist loses.

**The magnet, in small numbers.** Four independent spins: average |m| = 6/16 = 0.375; with 10²³ spins about 10⁻¹². Strongly coupled spins: only all-up and all-down survive, average m still 0 by symmetry. A real magnet exists because it picks one and stays: the flip time grows exponentially with the boundary that must be crossed. _Correction to the outline:_ "nothing in one atom says 770" is true, but a pair nearly does (T_c is set by the neighbour coupling and the lattice). What the parts don't supply is the _existence_ of a sharp transition, which needs a limit.

**As machine learning restated it.** Wei et al. (2022) define an ability as emergent if absent in smaller models, present in larger, and not predictable by extrapolation. _Position:_ that is Lewes's definition with model size as the size, a test of non-additivity on a curve, closer to Mill than to Anderson. Their "quantitative changes … qualitative changes" is the Marx–Engels line Anderson quotes as a joke before Fitzgerald and Hemingway ("Yes, they have more money").

***

## 3. The dispute — reduction against construction

_Anderson at full weight by choice; Weinberg in one paragraph; philosophy of mind capped at two._

**Anderson, "More Is Different" (_Science_, 1972; project file).** Reductionism accepted "without question"; the target is constructionism and Weisskopf's intensive/extensive ranking. The worked chain: ammonia inverts about 3 × 10¹⁰ times a second and has no dipole in a stationary state; PH₃ ten times slower; PF₃ not measurably; sugar never, so parity is "not repealed, but broken"; ferroelectric crystals keep a direction for longer than the age of the universe. Three inferences: symmetry is central; internal structure needn't share the state's symmetry (no one predicts ammonia's inversion without passing through the pyramid no stationary state has); big systems have less symmetry than their laws. The limit made explicit: three or ten particles define no shape; synthesis from the laws needs two impossible things, solving an infinite-body problem and applying it to a finite one. Rigidity as the image of an emergent variable. "Information-bearing crystallinity" as the record in 1972 vocabulary. And the caution: there may be no useful parallel between many-body physics and truly complex systems; the relation is "a one-way street," analysis possible, synthesis all but impossible.

_Positions:_ Anderson's unpredictability is construction _without the higher-level concept_; with it, prediction works; the fix is a change of variables. Schaeffer's paraphrase ("cannot be predicted even from a precise quantitative understanding") isn't wild but moves the emphasis, and neither Wei nor Schaeffer uses his mechanism (broken symmetry, the limit, rigidity). Citing Anderson for trained networks cites the half he labelled speculation. The irony: the mirage critique is an Anderson move (pick the right variable and the mystery becomes analysis), run in the opposite direction.

**Weinberg and the Super Collider.** Reductionism as the convergence of explanatory arrows; the SSC cancelled in October 1993 after about $2 billion and some 14 miles of tunnel. _Position:_ a dispute about status dressed as one about nature; Weinberg's 1979 phenomenological Lagrangians helped found effective field theory, the formal version of Anderson's point.

**Laughlin–Pines (2000): protectorates.** The quantum Hall resistance quantized to parts in a billion in dirty samples; Josephson's h/2e likewise. _Position:_ the signature of emergence is not surprise but robustness, criterion (c) as experiment.

**Weak against strong.** Bedau (1997): derivable only by simulation. Chalmers (2006): not derivable at all, consciousness the only candidate. _Position:_ every LLM output is a finite computation over known weights, so strong emergence is ruled out by construction and weak emergence is met trivially; the live question is which weak emergence is structural.

**Missing:** a notion of level; why a coarse description closes; what "cannot predict" means; a criterion separating structural novelty from surprise.

***

## 4. The formalization — phases, limits, flows

### 3a: Landau to Lee–Yang

**Landau (1937).** A phase is a minimum of a free energy written as a short polynomial in an order parameter, with symmetry choosing the terms. _landau.py_:

* Second order, F = (T − 1)m² + m⁴/2: m\* = 0, 0, 0.316, 0.500, 0.707, 1.000 at T = 1.2, 1.0, 0.9, 0.75, 0.5, 0. Continuous; Landau's β = ½.
* First order, F = Tm² − m⁴ + m⁶: a second valley appears below T = ⅓, levels at ¼, wins below; m\* jumps 0 → 0.714.
* Hysteresis, rolling downhill only: cooling stays at 0 until T ≈ 0 (supercooling); heating stays ordered up to T ≈ 0.32 (0.632; superheating).

Fingerprints: second order has continuous onset, diverging fluctuations, critical slowing down, no history dependence; first order has a jump, modest fluctuations, hysteresis and metastable waiting. _Criterion (a) amended:_ the average spin is definable on four spins; what's new is a variable the system **holds stably**.

**Ising, Peierls, Onsager.** 1D, by counting: one wall costs 2, has about N placements, so ΔF = 2 − T ln N goes negative for long chains at any T > 0 (N = 1,000 at T = 0.5: −1.5). 2D, Peierls (1936): a wall of length P costs 2P and has about 3^P shapes, so ΔF = P(2 − T ln 3) > 0 for T < 1.82; order survives. _Position:_ whether order survives is a race between two exponentials. Onsager (1944): T_c = 2/ln(1 + √2) ≈ 2.269, β = 1/8.

_ising.py_ (Metropolis; about two minutes): |m| below T_c ≈ 0.91 at every size; above, halving per doubling (0.350, 0.172, 0.085 at T = 3.0); χ peaks 1.75, 6.26, 16.5 moving toward 2.27.

**Lee–Yang (1952).** For finite N, Z is a finite sum of smooth positive terms, so F is smooth: no finite system has a phase transition. Zeros of Z pinch the real axis only as N → ∞. Programmer's framing: two phases with per-spin preference x give f_N(x) = (1/N) ln(1 + e^(Nx)); the order parameter is sigmoid(Nx): 0.269, 0.5, 0.731 at N = 10; 0.00005, 0.5, 0.99995 at N = 100. _Position:_ criterion (b) is a theorem; "sharp" means "sharpening as a named size grows."

### 3b: universality and the renormalization group

_Technical home:_ the-renormalization-group.md.

**Universality.** β ≈ 0.33 for CO₂, xenon, uniaxial magnets, and binary mixtures; Landau ½; 2D Ising ⅛. Landau fails by ignoring fluctuations (correct only in d ≥ 4).

**Kadanoff (1966), Wilson (1971).** Coarse-grain, ask what coupling reproduces the physics, repeat, follow the flow. Phases are basins, transitions unstable fixed points, exponents the speed of escape (ν = ln b / ln λ), universality classes basins of one fixed point, irrelevant couplings the reason detail can be ignored. 1D exact: tanh K′ = tanh² K; K = 1 flows 1.000 → 0.663 → 0.350 → 0.114 → 0.013 → 0. 2D Migdal–Kadanoff (_blockspin.py_): the two orderings give K\* = 0.3047 and 0.6094 (T_c = 3.28 and 1.64) and the same ν = 1.34 (exact 1). _Correction:_ the "2.26–2.3" I quoted beforehand is only the geometric mean (2.32). _Position:_ where the transition is depends on details, even of the approximation; the exponent doesn't. What the parts determine is exactly what isn't universal.

**Finite-size scaling** (from ising.py's tables as they stood, by choice): |m| at T_c 0.769, 0.705, 0.663, ratios 0.917 and 0.940 against L^(−1/8)'s 0.917; χ peak exponent ≈ 1.62 against 7/4; Binder cumulant 0.610, 0.608, 0.611 at T = 2.27. _Position:_ the checklist for criterion (b): name N; several sizes; width narrowing as a power of N; a crossing. The only form in which (b) can apply to language models.

**Effective field theory (one paragraph by choice).** Fermi's four-fermion theory; Weinberg 1979; gravity suppressed at colliders by about 10⁻³⁰. _Position:_ "irrelevant operator" is the precise version of "details below can be ignored."

**Coarse-graining as lossy compression.** Irrelevant couplings are bits every round discards; relevant ones survive. _Position:_ universality says repeated lossy compression of physical systems has few fixed points. _Induction_ found descriptions that win by being shortest; the RG finds those that survive being made shorter.

**Batterman and infinite limits (a paragraph with a stance, by choice).** Batterman (2002): universality is explained only asymptotically, so the limit is indispensable. Butterfield (2011), Norton (2012), Menon–Callender (2013): the infinite system is an idealization; finite systems approximate it. _Position:_ the infinite system is a fiction; the fixed point isn't. It's a property of the coarse-graining map, and finite systems are trajectories passing near it (the Binder crossing is the fixed point seen through 8, 16, and 32 spins). Asymptotic explanations are statements about the map, like "this loop converges to 0.4407."

**Stage 3's answer to _Entropy_ §4.** A coarse description is closed when everything it drops is irrelevant under the flow. _Position:_ **a regime is a basin of a fixed point**; "regimes, not laws" gets its theory. Cost: the RG needs a scale and a coarse-graining map, which networks don't obviously supply.

***

## 5. The abstraction — emergence without a magnet

### 4a: levels, topology, irreducibility

**A level is a commuting square.** coarse(step(x)) = step′(coarse(x)). Worked: X = {A}, Y = {B, C}; if B and C both move to A with probability 0.3, Y has its own rule (lumpable); if 0.1 and 0.5, the forecast depends on the hidden microstate by 0.4 and Y is a report. _Position:_ emergence is a coarse-graining whose square commutes better the coarser it gets. **A world model in Vafa's sense (Myhill–Nerode) is a commuting coarse-graining**, so "does a network build a world model?" and "does it find an emergent level?" are one question.

**Topological order (a paragraph and a link, by choice).** Fractional quantum Hall; Wen 1989–90; ground-state count by topology; long-range entanglement; the toric code in _error-correcting-codes.md_ §7. _Position:_ breaks Landau's local order parameter, keeps the amended (a): stable, not necessarily local; the purest protectorate. An emergent variable may be invisible to any single probe.

**Life and irreducibility.** Conway's rules (Gardner, October 1970). _life.py_: the glider rebuilds itself one cell diagonally every four generations (c/4), "gen 4 == gen 0 moved one cell down-right: True." Gosper's gun (November 1970); Turing-completeness (Berlekamp–Conway–Guy 1982; Rendell 2000); Wolfram's four classes (1984); Rule 110 universal (Cook 2004). Eight 24 × 24 soups at 35% settle at generations 1116, 95, 216, 110, 278, 135, 537, 205: same rule, a factor of 12, nothing at generation 0 tells them apart. _Positions:_ the glider's square commutes exactly inside a regime (isolation) with no limit at all, so (b) generalizes to "a regime where a summary's square commutes"; Bedau's weak emergence splits into **irreducible occurrence** and **reducible behavior**. **Emergence is a reducible level whose occurrence may be irreducible.**

### 4b: learning as coarse-graining (pre-2025 by choice)

**A transition in the posterior.** Watanabe's F(n) = n·loss + λ·ln n. _transition.py_: SIMPLE (loss 0.01, λ = 1) against ACCURATE (0, λ = 10); F equal at n ≈ 8,100; P(accurate) 0.005, 0.50, 0.995 at n = 7,500, 8,100, 8,700. Subtler errors move the switch later and sharpen it only logarithmically (10–90% width 6.1%, 4.6%, 3.7% of the crossover for errors 0.01, 0.001, 0.0001). The posterior has no hysteresis; gradient descent does. _Position (prediction):_ grokking is the dynamical shadow of a Bayesian first-order transition: SGD reaches the memorizing solution first and stays until weight decay erodes the barrier. Chen et al. (2023) and Hoogland et al. (2024) point the same way. _slt.py_ (from _Induction_) computes λ itself.

**RG and deep learning (short assessment).** Mehta–Schwab (2014) "exact mapping" to RBMs; Lin–Tegmark–Rolnick (2017) objection; Koch-Janusz–Ringel (2018) learn the RG by maximizing mutual information with the distant environment. _Position:_ the optimal coarse-graining keeps what predicts the far away, the same act as compression-as-prediction across space; the analogy is deep for self-supervised prediction and specious for a classifier with arbitrary labels.

**Width as N (one paragraph).** In the lazy NTK limit (Jacot et al. 2018; Chizat et al. 2019) features don't move and nothing emerges, by construction; mean-field and maximal-update limits (Mei et al. 2018; Yang–Hu 2021) allow it. Saxe–McClelland–Ganguli (2014): deep linear networks learn modes one at a time, sigmoids sharpening as initialization shrinks; there, N is named.

**Causal emergence (a paragraph).** Hoel et al. (2013): four states, 1–3 mixing randomly and 4 fixed; micro EI ≈ 0.81 bits, macro {1,2,3}/{4} EI = 1 bit. _Position:_ lumpability scored under a uniform intervention prior; the bias thread and Bertrand again; a measure of a summary's quality, not evidence that macro causes are extra. Handed to _Causality_.

**Emergent spacetime (a paragraph).** Swingle (2012): the extra dimension of a holographic tensor network is RG scale. _Position:_ spacetime in holography is the RG made into a dimension.

***

## 6. The payoff — was it cosmic?

### 5a: across model scale

_Search findings, October 2026:_ grokking as first-order was already argued by **Rubin, Seroussi, Ringel (2023)**, so the outline's "new" position wasn't new; **Ersoy–Wiesner** (ICML 2026 workshop poster; abstract only, untested): first-order transitions in weight decay with metastable states and Arrhenius-type escape, grokking consistent with hysteresis in deep linear networks; **Zhao, Qin, Alvarez-Melis, Kakade, Saphra** (preprint, v5 February 2026): performance bimodal across seeds, appearing abruptly at a capacity threshold, persisting under continuous loss; **Gu, Lyu, Li, Zhang** (2025; venue unconfirmed): knowledge acquisition switching at critical model size and data-mix ratio (410M: near 0 at r = 0.3, about 80% at 0.4), steps growing exponentially as r falls, a capacity-allocation mechanism, critical ratio a power law in size; **Snell, Wallace, Klein, Levine** (2024): fine-tuning shifts emergence to smaller models, forecasts up to 4× compute ahead in some cases; **Du et al.** (2024) loss thresholds, challenged by **Elhady et al.** (2025); **Krakauer, Krakauer, Mitchell** (2025): emergence requires a compressed effective theory of internal behavior, world models the strongest candidate; **Brill** (2024 preprint): power-law scaling from data at a percolation threshold; **Peraza Coppola, Helias, Ringel** (2025–26 preprint): RG and universality of learning curves. Read and not used: Hong and Hong, Havlík, Nakagi et al.

**Wei, tested.** No internal variable, no named N, no universality: a borrowed word, defined against curve extrapolation, the weakest sense of "cannot predict."

**The mirage, run.** _mirage.py_: per-token loss a smooth power law; on 20-token answers exact match 0.001, 0.062, 0.330, 0.643, 0.839, 0.932 at 10⁷…10¹² parameters while wrong tokens fall 5.91 → 0.07 and log-likelihood −7.00 → −0.07. Finite-size test with answer length k as N: the 10–90% switch sits at log₁₀ N 4.95–8.30 (k = 1), 8.21–11.56 (k = 20), 12.45–15.80 (k = 1000): **width fixed at 3.35 decades**, about 1.34/α. _Position:_ **a metric mirage translates; a phase transition sharpens.**

**Seeds.** _Position:_ bimodality across seeds is phase coexistence; the mirage is right about the averaged curve and wrong to conclude nothing happens in each run.

**Gu's thresholds.** _Position:_ the strongest scale-axis case: stable variable, first-order switch in two control parameters, threshold law, mechanism; (c) untested. "Deep, at the level of first-order transitions; silent on universality."

**Scaling laws.** Three readings: critical data (Brill), an RG fixed point in learning (Peraza Coppola et al.), many small transitions summed (Michaud et al. 2023 "quanta"; skill k needed with frequency ∝ 1/k², a model knowing N skills has residual loss ≈ 0.095 at N = 10, 0.00995 at N = 100). _Position:_ aggregate smoothness and component sharpness don't conflict; a smooth power law is what many first-order switches look like added up.

_Position on Anderson's caveat:_ specious where "emergence" means a fast-rising curve under a threshold metric, deep where an optimum switches between discrete solutions. LLMs show **ice forming, not a magnet at its Curie point.**

### 5b: during training

**grok.py** (two-layer network, squaring activation, addition mod 11, symbols not numbers, AdamW, full batch; every one of 39 runs fits training data by step 50):

|                               | 0.50 | 0.55 | 0.60  | 0.65  | 0.70                | 0.80                   |
| ----------------------------- | ---- | ---- | ----- | ----- | ------------------- | ---------------------- |
| weight decay off: generalized | —    | —    | 0/3   | —     | 0/3                 | 0/3                    |
| weight decay on: generalized  | 0/5  | 0/5  | 1/5   | 1/5   | 3/5                 | 5/5                    |
| steps to 95% test (successes) | —    | —    | 7,575 | 1,875 | 1,800, 2,175, 3,300 | 575–1,075 (median 675) |

Weight decay is the switch (Power's central ablation, reproduced). Delay after fitting 12–150× (Power: about 1,000×, division mod 97, training near-perfect before 10³ steps, validation near 10⁶). Waiting time grows as data shrink (Power: 40–50% per 1% near 25–30% on S5). Seed bimodality at 60–70% data, Zhao's phenomenon in a toy. Caveats: "never" means not within 8,000 steps (an earlier 30,000-step run at 50% stayed at 0.20); five seeds can't tell exponential from power-law divergence; weight decay three times stronger prevented fitting. _Position:_ grokking is a first-order transition with metastability (coexistence, delay, divergent waiting), seen late by gradient descent; Power's sharpness correlation (Spearman −0.80 on S5) places generalizing runs in the flatter, lower-λ valley. (a) passes; (b) in first-order form; (c) untested.

**Induction heads.** Olsson et al. (2022): 34 models, 1–40 layers, 13M–13B; every model with two or more layers shows a phase change (about 2.5–5 billion tokens in the main runs) in which induction heads form, ICL score (loss at token 500 minus token 50) jumps from under 0.15 to about 0.4 nats, and the loss curve has its only non-convex bump; one-layer models don't, unless a smeared key lets them. Singh, Moskovitz, Hill, Chan, Saxe (2024): three subcircuits (previous-token, query–key match, copy), **each smooth alone, sharp together**. _Position:_ mirage.py's exponent moved inside the model: real, because the mechanism (not the scorer) needs all parts, but the same algebra and not a limit. Hoogland et al. (TMLR 2025): λ marks five stages in a 3M-parameter LM, its one decrease (−1.57) as the induction circuit begins. _Position:_ λ is the nearest thing learning theory has to an order parameter, a stage marker whose drops are a solution being replaced by a more compressed one. Aoyama, Wilcox, Schneider (preprint February 2026; untested): onset tokens ∝ B^0.63 · C^0.38, r = 0.98 in log space, **model size not significant** from 50M to 7B; formation needs bigram repetition above a frontier. _Position:_ the best case of emergence in Anderson's sense in real language models, the most predictable in onset, and a weak candidate for (c).

### The bet, tested

| Prediction                                     | Result                                                                           |
| ---------------------------------------------- | -------------------------------------------------------------------------------- |
| Most reported abilities across scale fail (b)  | **Confirmed**, sharpened: mirages translate                                      |
| Training-time transitions pass (a), partly (b) | **Confirmed**: grokking (first-order), induction heads (composition)             |
| None pass (c)                                  | **Mostly holds**; Aoyama's size-independence a weak candidate                    |
| Real transitions are first-order               | **Confirmed** in training and across scale; **not original** (Rubin et al. 2023) |

**Amendments.** A third source of sharpness besides limits and metrics: **composition**. Seed bimodality is the first-order fingerprint in aggregate. Criterion (b) needs a named N whose increase narrows the width; no learning-system case has measured one, the most important missing experiment.

**Working claim, broken three times.** "New": a stable variable (order parameter, glider, circuit), not new laws. "Cannot predict": false in principle, true in practice only for _when_ (Lee–Yang, Bedau, seeds; against Aoyama, Snell, Gu). "Contain": the universal part is a fixed point of the description map.

### On Roose's sentence

**Not cosmic.** Much reported suddenness is in the scoring (C1). Real sudden changes are first-order transitions physics has understood since van der Waals and Landau (C2), or composition of smoothly learned parts (C3). What is sudden is _when_, not _what_: the onset in a single run can be hard to forecast, the thing that appears is a circuit with its own rule, and onsets are increasingly predictable in aggregate (C4). Smooth scaling laws are many such steps added up (C5). "Emergence" is borrowed for curves and earned for circuits, at the first-order level, with universality untested (C6). Combined with _Induction_: **not an accident, partly inexplicable, not cosmic** (C7). Claims, sources, and expected objections in _emergence-argument-map.md_.

Caveat kept throughout: Claude is an instance of the systems studied in §6, and its sense of how it works was not used as evidence.

***

## 7. The single line of thought

One question, asked with steadily less confidence that "new" means anything beyond "newly closed": when does a summary of a system get a life of its own?

| Stage                                    | Emergence is…                              | What makes it closed            | What it yields                              |
| ---------------------------------------- | ------------------------------------------ | ------------------------------- | ------------------------------------------- |
| Mill to Broad (1843–1925)                | effects that don't add; trans-ordinal laws | nothing: brute fact             | the slogan; the archangel                   |
| Heitler–London, Dirac (1927–29)          | construction too costly                    | the laws, in principle          | "in principle" vs. "in practice"            |
| Anderson (1972)                          | broken symmetry at large N                 | the order parameter, the limit  | rigidity; the one-way street                |
| Landau to Lee–Yang (1937–52)             | a minimum that moves; a kink at infinity   | the free energy's symmetry      | first vs. second order; (b) as a theorem    |
| Kadanoff, Wilson (1966–71)               | a fixed point of coarse-graining           | irrelevant couplings            | universality; regimes as basins             |
| Conway to Cook (1970–2004)               | a pattern with its own rule                | an exact regime (isolation)     | irreducible occurrence, reducible behavior  |
| SLT, grokking, induction heads (2014–26) | one solution replacing another             | weight decay, data, composition | first-order transitions; circuits as levels |

Waves kept the space and lost the substrate. Symmetry kept the group. Entropy kept the logarithm. Randomness kept the absence. Measurement kept the record. Computation kept the step. Space kept the relation. Time kept the correlation with a clock. Information kept the copy. Induction kept the bias. Emergence kept the _closure_, the commuting square, and lost new laws, unpredictability in principle, and the idea that the whole contains something its parts lack.

***

## Runnable companions

Pure Python, no libraries; kept in GitHub.

* _landau.py_: second- and first-order free energies; hysteresis.
* _ising.py_: 2D Metropolis for L = 8, 16, 32 (about two minutes); |m|, χ, Binder cumulant.
* _blockspin.py_: exact 1D decimation; Migdal–Kadanoff both orders; `blocks` mode for 3 × 3 majority blocking (about a minute).
* _life.py_: the glider; eight soups.
* _transition.py_: a first-order transition in sample size.
* _mirage.py_: one smooth model family under three metrics; the translation test.
* _grok.py_: addition mod 11; single runs and `sweep` mode (recorded sweep: §6, 5b; about 15 minutes on two cores).
* Reused from _Induction_: _slt.py_.

## Suggested next steps

* In _grok.py_, run 20 seeds at 0.6, 0.65, 0.7, and 0.75 with 20,000 steps, and plot log(waiting time) against data fraction: a straight line favours barrier crossing (first order), a straight line on log–log favours critical slowing down. That is the test this exploration couldn't afford.
* In _grok.py_, vary the width H (20, 40, 80) at 0.7 and see whether the fraction of seeds that succeed changes more sharply with data at larger H: criterion (b) with width as N.
* In _mirage.py_, replace the power law with Michaud-style quanta (each skill a sigmoid, frequencies ∝ 1/k²) and check that the summed loss is still a power law.
* In _ising.py_, add T = 2.28 and 2.29 and rerun L = 32 with 30,000 sweeps to tighten the χ exponent.
* In _life.py_, count gliders escaping from soups as a function of density, and look for a threshold.
* In _blockspin.py_, run `blocks` at T = 2.269 from both starts with 20,000 sweeps and see whether the two rows converge.
* Reading: Anderson (1972) (project file); Goldenfeld, _Lectures on Phase Transitions and the Renormalization Group_, ch. 1–3 and 9; Batterman, _The Devil in the Details_ (2002), ch. 1–4; Butterfield, "Less is Different" (2011); Gardner, "Mathematical Games," _Scientific American_, October 1970; Schaeffer et al. (2023) and Power et al. (2022) (project files); Olsson et al. (2022); Krakauer, Krakauer, Mitchell (2025).
* Links forward: _the-renormalization-group.md_ (side file); _emergence-argument-map.md_ (the post); _Causality_ (causal emergence; interventions); _The continuum_ (the reality of infinite limits); _Cellular automata_ (proposed at this close).
