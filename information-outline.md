# What Is Intelligence? — Outline

_Working plan for the thirteenth exploration, November 2026. Prompted by 3Blue1Brown, "This algorithm changed how I think about compression" (Information theory, part 3, 17 November 2026), chapter 6, "Reflections on 'Compression is Intelligence'" (transcript supplied by Fog). Drafted 2026-11-19; arc settled before stage 1._

**Steering (2026-11-19, before drafting):** a full genealogy, not an extension of _compression-is-prediction.md_; the brain as predictive compressor at **equal weight** with machines throughout, not one stage.

**Steering (2026-11-19, before stage 1):** selective prehistory in stage 1; **all three side files** (predictive coding and the free-energy principle; universal intelligence and AIXI; measuring intelligence: _g_ and factor analysis); psychometrics limited to what _g_ is as a construct, group-difference debates out of scope entirely; the free-energy principle stated **in operational terms only**, no philosophical debate.

**Steering (2026-11-20, after stage 1):** stage 2 as two strands of equal length (machines and tests; brains and perception); Searle kept at one paragraph.

**Steering (2026-11-20, after stage 2):** stage 3 split 3a (brains) / 3b (machines); _residual.py_ run on a **synthetic line** with edges, ramps and noise (no real image); the Hinton–van Camp bits-back argument **stated** in 3a, with the working left to _predictive-coding-and-free-energy.md_.

**Steering (2026-11-21, after 3a):** Fog asked for a fuller explanation of free energy before 3b; given as a stage-3a addendum (shadow-or-puddle example, _freeenergy.py_) and, at Fog's request ("this form has been very helpful"), saved as a **fourth side file**, _free-energy-in-plain-terms.md_. For 3b: build a small **C-test** in pure Python (_ctest.py_); give **Chollet a full section**.

**Steering (2026-11-21, after 3b):** stage 4 split 4a (cost) / 4b (action) as proposed. For _prequential.py_, Fog supplied a chapter of fiction, _benefit-street-chapter-07.md_ (preferred over the Portsmouth novel), as the text to adapt to.

***

## 0. Carried in

_Cite, don't repeat._

* **The identity** (_compression-is-prediction.md_ §1–3): log loss = code length; arithmetic coding turns any predictor into a compressor; Grant's chapters 1–5 match §2–5.
* **Prequential coding** (_compression-is-prediction.md_ §5; Blier–Ollivier 2018): send no model; the decoder refits as it decodes; the training curve is the code length.
* **Where the identity stops** (_compression-is-prediction.md_ §7): compressible ≠ efficiently predictable; compression ≠ mechanism; prediction ≠ intervention.
* **The bias** (_what-is-induction.md_; _solomonoff-and-the-universal-prior.md_): "short" is relative to a reference machine, up to a translation constant; every learner brings an assumption the data don't supply.
* **World model vs. lookup** (_what-is-induction.md_ §6): a learner builds a map where the map is the shortest description of its data.
* **Emergence** (_what-is-emergence.md_): capabilities appear through first-order transitions in training, sudden per run, smooth on average.

### Grant's three claims, as stated

1. Compression and prediction are equivalent (arithmetic coding one way; 2^−δ from a compressor the other), and good prediction seems to need a coherent model; predictive processing says the brain does this.
2. Understanding is a thing getting smaller: equal prediction from a smaller model is better, and the Hutter Prize's count of the decoder makes that measurable.
3. Learning quickly is intelligence too, and it enters the score when the model adapts on the fly (prequential coding from a shared pseudo-random start).

Grant's frame: treat "compression is intelligence" as a proposed _definition_, judged like Newton's "energy" — reductive, but is it productive, does it unify? (Correction: the quantity he gives, kg·m/s², is force; energy was not Newton's. Its real history — Leibniz's _vis viva_, Young's naming in 1807, the conservation law of the 1840s — is itself a successful concept genealogy, and the better model for his test.)

***

## Working claim to be broken

**Intelligence is compression: a system is intelligent to the degree that it finds short descriptions of its experience, and one measure ranks brains and machines alike.**

Expected breaks:

1. **"Short" has no owner-free meaning.** Short in whose language? (Carried in from _Induction_: the reference machine, grue, the invariance constant.) A brain's language is fixed by evolution and a metabolic budget; a transformer's by architecture and gradient descent.
2. **Compression scores passive observation; intelligence acts.** A compressor can't choose what to look at next. AIXI must add reward; the free-energy principle must add expected free energy. Whether action can be folded into prediction is the central test for the brain half.
3. **Compression ignores cost.** Kolmogorov complexity is free to compute forever; brains and machines are not. Levin's Kt, the speed prior, logical depth, and the energy cost of a spike all reintroduce time and energy, and the measure changes when they do.
4. **"One measure for all" may fail.** Spearman's _g_ is a statistical construct across humans; Moravec's paradox says the ranking of tasks inverts between humans and machines.

## Opening bet, to be tested, not a result

**Intelligence is not compression but the efficiency of compressing new data: how quickly a system's prequential code length drops on experience it hasn't seen, per sample and per unit of resource, in service of acting.**

Predictions:

* Grant's claims 2 and 3 collapse into one: in a prequential code a big model is not penalized for its size but for how slowly it learns, so "smaller" is a proxy for "learns faster" (Blier–Ollivier's finding, applied to his framing; not new).
* The brain half confirms efficient and predictive coding at the sensory periphery (retina, early vision) and is much weaker as a total theory of cortex; the 2025–26 search decides how weak.
* Action breaks pure compression in both halves, and the repairs (AIXI's reward, active inference's expected free energy, Schmidhuber's compression progress) each smuggle in a goal or a prior.
* Chollet's "skill-acquisition efficiency" and Grant's on-the-fly fine-tuning are the same proposal; test-time training on ARC is its experiment.

***

## 1. The intuition — quick wit and economy of thought _(written 2026-11-19)_

_Selective prehistory._

* **Aristotle**: _anchinoia_, "quick wit," hitting on the middle term in an imperceptible time (_Posterior Analytics_ I.34), with his own example of the moon's bright side: intelligence as speed of finding the explanation.
* **Hobbes** and **Leibniz** in a line; link _what-is-computation.md_ §1.
* **Mach**: Mach bands (1865) and the economy of thought (1882 lecture; _Die Mechanik_, 1883), with his refraction example (a table of angles against Snell's law); his use of economy against atoms.
* **Helmholtz's unconscious inference** (_Physiological Optics_, vol. 3, 1867): perception as inference from signs to causes; the pressed-eyeball phosphene.
* **Spearman's _g_** (1904) against **Binet's** refusal of a single quantity (1905): in a paragraph; the side file carries the rest.
* **Turing** (1950): replace the definition with a test; the "child machine" as learning.
* Working example to carry: one line of a photograph, raw (64 bits) against residual coding (41 bits).

## 2. The dispute — what is being measured, and is it inside? _(written 2026-11-20)_

_Two strands at equal length._

**Machines and tests.**

* _g_ real or artefact: Spearman against Thomson's bonds (1916), worked on six bonds; Thurstone's primary abilities (1938); van der Maas's mutualism (2006) as a third mechanism for the same table. Boring (1923): "intelligence is what the tests test." Construct only; side file _measuring-intelligence.md_ carries the factor analysis.
* Turing's behaviourism and Lady Lovelace's objection; Dartmouth (1955–56); symbol systems (Newell–Simon) against connectionism (McCulloch–Pitts, Rosenblatt, Minsky–Papert, PDP 1986, Fodor–Pylyshyn 1988); Moravec's paradox (1988) as where the strands cross.
* Searle (1980) at one paragraph; Block's Blockhead (1981) as the case compression decides.
* What the dispute lacked: a measure of how much structure is in data, independent of a test.

**Brains and perception.**

* Behaviourism's refusal of inner models (Watson 1913); Tolman's cognitive maps (1948) as the detour test, with the replication caveat.
* Gestalt _Prägnanz_ (Wertheimer 1923) and Hochberg–McAlister's minimum principle (1953): economy on the brain side.
* Craik's _The Nature of Explanation_ (1943): small-scale models for trying out actions.
* Helmholtz's inference against **Gibson's direct perception** (1966, 1979): invariants and affordances.
* Marr (1982) in a line: compression as a computational-level claim.
* What the dispute lacked: a way to quantify "redundancy in the input" and "a model's fit."

## 3. The formalization — two lines that meet at description length

_Split 3a (brains) / 3b (machines)._

**3a. The brain as compressor.** _(written 2026-11-20; addendum on free energy 2026-11-21)_

* **Attneave** (1954): Shannon's guessing game run on pictures; information concentrated at contours and corners; the 38-point cat.
* **Barlow** (1961): redundancy reduction; his 2001 revision ("redundancy exploitation").
* **Srinivasan, Laughlin and Dubs** (1982): predictive coding in the fly retina; surround widens as noise grows. _residual.py_ on a synthetic 4,096-pixel line: bright 5.98 → 2.48 bits/pixel, dim 7.41 → 5.24; best predictor width 2 → 8 pixels as σ goes 0.5 → 16; centre-surround nonzero at 0.7% of pixels; Mach-band caveat (bands absent at step edges).
* **Olshausen–Field** (1996): sparse coding's objective as a two-part code length; V1-like filters.
* **Rao–Ballard** (1999): hierarchical predictive coding; end-stopping explained.
* **Variational free energy as code length**, stated (Hinton–van Camp 1993; Hinton–Zemel 1994; Helmholtz machine 1995): F = −log p(data) + KL(q‖posterior); **Friston** (2005, 2010), perception half only, operationally. Addendum: shadow-or-puddle, _freeenergy.py_; now _free-energy-in-plain-terms.md_. Bits-back working to _predictive-coding-and-free-energy.md_.

**3b. The machine as compressor.** _(written 2026-11-21)_

* Solomonoff linked, not redone.
* **Hernández-Orallo** (1998): C-tests; _ctest.py_ (items graded by Kt in a four-constructor language; unquestionable items 18.8% at 3 letters shown, 99.2% at 4; three outside solvers fall to zero above Kt ≈ 22–28 while the test-maker's language scores 100% by construction). **Sanghi–Dowe** (2003): a small program at human-average on IQ sequence items.
* **Mahoney** (1999) and the **Hutter Prize** (2006; 2020 rules: < 10 GB RAM, < 50 h, one core); Gwern's 2026 critique (wrong side of the scaling laws).
* **AIXI** (Hutter 2000, 2005), Leike–Hutter's bad priors (2015), and **Legg–Hutter universal intelligence** (2007) worked on three environments in small numbers; full toy in _universal-intelligence-and-aixi.md_.
* **Chollet** (2019), full section: skill vs. intelligence; the definition (efficiency against priors, experience, generalization difficulty) in plain terms; Core Knowledge priors; ARC; the 2024 ARC Prize and test-time training (details checked in stage 5); Chollet's measure as Hutter's accounting plus prequential accounting.

## 4. The abstraction — compression plus what?

_Split 4a (cost) / 4b (action)._

**4a. Compression plus cost.** _(written 2026-11-21)_

* **Time**: Levin's Kt (1973) worked on two programs; Levin search; Schmidhuber's speed prior (2002).
* **Depth**: Bennett's logical depth (1988); short-and-deep vs. long-and-shallow; chess chunks (Simon–Gilmartin 1973); expertise as caching. Position: Grant's "smaller is smarter" holds when time is free and inverts under time pressure.
* **Energy**: Laughlin et al. (1998): \~10⁴ ATP per bit at a synapse, 10⁶–10⁷ for graded or spike signals; brain \~20% of resting energy; cost per bit rising with rate (Niven et al. 2007); sparse coding as energy efficiency.
* **Evolution as the prior**: the genome (\~6 × 10⁹ bits) vs. 10¹⁴–10¹⁵ synapses (Zador 2019, genomic bottleneck); the data gap (Frank 2023; 2026 preprint on children's accelerating returns, flagged).
* _**prequential.py**_ on _benefit-street-chapter-07.md_ (21,377 bytes), base text 200 KB of stdlib docstrings: scratch 2.986 bits/byte; pretrained static 4.973; pretrained adapting 3.106; pretrained fast (4×) 3.038; light prior (1/20 weight) 2.507; lzma 2.985. Hutter accounting adds 64,292 bytes for the model. Positions: wrong priors held strongly hurt; priors help when held lightly; learning rate shows in the code length; the two accountings disagree on which learner is best.

**4b. Compression plus action.**

* AIXI's reward; active inference (expected free energy, operationally); Schmidhuber's compression progress (1991, 2009) and the noisy-TV problem.
* Candidate endpoint form: intelligence as a rate, not a level.

## 5. The payoff — does the definition unify?

_Before writing: search 2025–26 on each thread; report what changed the argument; flag anything recent and untested._

* Compression and capability in LLMs (Huang 2024, Xuyang 2025, cited); newer results.
* Test-time training and ARC-AGI-2/3 (2025–26); check the 2024 figures quoted in 3b.
* Hutter Prize records since fx2-cmix.
* Brains and LLMs: Schrimpf et al. (2021), Caucheteux–Gramfort–King (2023); newer work.
* Children's learning curves vs. LMs (Frank 2026 preprint; Feng–Tan–Frank 2026 "Baby Scale").
* Empirical tests of predictive coding in cortex (2024–26); where the free-energy principle stands, operationally.
* Grant's test answered: is compression to intelligence what energy was to _vis viva_?

***

## Side files (settled 2026-11-19: three; fourth added 2026-11-21)

* **Free energy in plain terms** — _free-energy-in-plain-terms.md_. **Written 2026-11-21.**
* **Predictive coding and the free-energy principle in plain terms** — _predictive-coding-and-free-energy.md_. Residual coding → Rao–Ballard → bits-back working; cites the free-energy side file rather than repeating it; operational only.
* **Universal intelligence and AIXI** — _universal-intelligence-and-aixi.md_. Legg–Hutter worked on toy environments; links the Solomonoff side file.
* **Measuring intelligence: g and factor analysis** — _measuring-intelligence.md_. Spearman's two-factor model on a 3 × 3 correlation matrix, Thomson's bonds, mutualism, what _g_ is and isn't. No group differences.

## Scripts (pure Python, no libraries; kept in GitHub)

* _residual.py_ (written, stage 3a).
* _freeenergy.py_ (written, 3a addendum).
* _ctest.py_ (written, stage 3b).
* _prequential.py_ (written, stage 4a): order-0–4 context model; five conditions on a supplied text; Hutter accounting; learning curves by 2,000-byte block.
* _factor.py_: Spearman's _g_ from a small correlation matrix; Thomson's bonds and mutualism simulated.
* _aixi_toy.py_: universal intelligence over three tiny environments.
* Candidate for 4b: _curiosity.py_ (compression progress vs. prediction error on three streams; an active-inference choice to look closer).
* Reused: _compress.py_, _shannon_game.py_, _solomonoff.py_, _taxi.py_.

## Threads to carry in

* **The bias** — evolution as the supplier of a brain's prior; the C-test's reference language; Chollet's Core Knowledge as a declared prior; _prequential.py_'s strong vs. light prior.
* **Prediction underdetermines mechanism** — Moravec; Thomson's bonds; equal compression from different mechanisms.
* **Observation bounded by computation** — Kt, logical depth; the Hutter Prize's resource limits.
* **The record** and **the copy** — memorization vs. compression; Blockhead as pure copy; expertise as caching.
* **The division** — Markov blankets as the free-energy principle's cut between agent and world.
* **Causality** — action and intervention (stage 4b), handed back; Tolman's detour.

## Guardrails

* Shape first; worked examples with small numbers; runnable scripts where they help.
* No second pass on Solomonoff, arithmetic coding, MDL, grokking, or the identity: link and build.
* Consciousness capped at a paragraph; psychometrics limited to _g_ as a construct; no group differences.
* The free-energy principle in operational terms only.
* Claude is an instance of the systems studied; its sense of how it works is not evidence.
