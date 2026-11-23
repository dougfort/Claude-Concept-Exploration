# What Is Intelligence? — Outline

_Working plan for the thirteenth exploration, November 2026. Prompted by 3Blue1Brown, "This algorithm changed how I think about compression" (Information theory, part 3, 17 November 2026), chapter 6, "Reflections on 'Compression is Intelligence'" (transcript supplied by Fog). Drafted 2026-11-19; arc settled before stage 1. Completed 2026-11-23; superseded by the summary_ what-is-intelligence.md, _kept as a record of the plan as it ran._

**Steering (2026-11-19, before drafting):** a full genealogy, not an extension of _compression-is-prediction.md_; the brain as predictive compressor at **equal weight** with machines throughout, not one stage.

**Steering (2026-11-19, before stage 1):** selective prehistory in stage 1; **all three side files** (predictive coding and the free-energy principle; universal intelligence and AIXI; measuring intelligence: _g_ and factor analysis); psychometrics limited to what _g_ is as a construct, group-difference debates out of scope entirely; the free-energy principle stated **in operational terms only**, no philosophical debate.

**Steering (2026-11-20, after stage 1):** stage 2 as two strands of equal length (machines and tests; brains and perception); Searle kept at one paragraph.

**Steering (2026-11-20, after stage 2):** stage 3 split 3a (brains) / 3b (machines); _residual.py_ run on a **synthetic line** with edges, ramps and noise (no real image); the Hinton–van Camp bits-back argument **stated** in 3a, with the working left to _predictive-coding-and-free-energy.md_.

**Steering (2026-11-21, after 3a):** Fog asked for a fuller explanation of free energy before 3b; given as a stage-3a addendum (shadow-or-puddle example, _freeenergy.py_) and, at Fog's request ("this form has been very helpful"), saved as a **fourth side file**, _free-energy-in-plain-terms.md_. For 3b: build a small **C-test** in pure Python (_ctest.py_); give **Chollet a full section**.

**Steering (2026-11-21, after 3b):** stage 4 split 4a (cost) / 4b (action) as proposed. For _prequential.py_, Fog supplied a chapter of fiction, _benefit-street-chapter-07.md_ (preferred over the Portsmouth novel), as the text to adapt to.

**Steering (2026-11-21, after 4a):** build _curiosity.py_ (three motivations on constant, noise, easy and hard streams; the step-closer choice as expected free energy).

**Steering (2026-11-22, after 4b):** stage 5 split 5a (machines) / 5b (brains); nothing added to the search list.

**Steering (2026-11-22, after 5a):** no adjustments.

**Steering (2026-11-23, after 5b):** endpoint accepted unchanged; **no argument map** (no post planned). Close: summary, three remaining side files with _factor.py_ and _aixi_toy.py_, updated _concept-genealogies.md_.

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

Expected breaks (all four occurred; _what-is-intelligence.md_ §6):

1. **"Short" has no owner-free meaning.**
2. **Compression scores passive observation; intelligence acts.**
3. **Compression ignores cost.**
4. **"One measure for all" may fail.**

## Opening bet, to be tested, not a result

**Intelligence is not compression but the efficiency of compressing new data: how quickly a system's prequential code length drops on experience it hasn't seen, per sample and per unit of resource, in service of acting.**

Predictions and results:

* Grant's claims 2 and 3 collapse into one. _(Confirmed; amended: a prior weighted by reliability, not smallness (4a); the accountings agree when the prior is small and matched (5a).)_
* Periphery firm, cortex weak. _(Confirmed, sharper: error cells exist, predictive suppression doesn't (5b).)_
* Repairs for action smuggle in a goal. _(Confirmed for all three (4b).)_
* Chollet and on-the-fly adaptation are one proposal; TTT its experiment. _(Confirmed: TTT won ARC 2023–25; the ARC-AGI-3 harness effect is its within-episode form (5a).)_

**Endpoint (accepted 2026-11-23):** compression is the currency of intelligence, not its definition. Intelligence is the rate at which a system turns experience, some of it chosen, into compression that serves goals compression doesn't supply, per unit of resource. It belongs to the whole learning system (prior, memory and learning rule), and its distinctively human form is a rate that increases: learning to learn.

***

## 1. The intuition _(written 2026-11-19)_

Aristotle's _anchinoia_; Hobbes and Leibniz in a line; Mach (bands 1865; economy of thought 1882–83; refraction table against Snell's law; atoms); Helmholtz's unconscious inference (1867); Spearman against Binet; Turing (1950). Working example: one row of pixels, 64 bits raw against 41 residual.

## 2. The dispute _(written 2026-11-20)_

Machines and tests: Thomson's bonds, Thurstone, mutualism, Boring; Turing, Dartmouth, symbols against networks, Moravec; Searle at a paragraph; Blockhead. Brains and perception: Watson, Tolman, Prägnanz and Hochberg–McAlister, Craik, Gibson against Helmholtz, Marr.

## 3. The formalization

**3a** _(written 2026-11-20; free-energy addendum 2026-11-21)_: Attneave, Barlow, Srinivasan–Laughlin–Dubs with _residual.py_, Olshausen–Field, Rao–Ballard, free energy as code length (stated); _freeenergy.py_; _free-energy-in-plain-terms.md_.

**3b** _(written 2026-11-21)_: the C-test with _ctest.py_, Sanghi–Dowe, Mahoney and the Hutter Prize, AIXI and Legg–Hutter, Chollet at full weight.

## 4. The abstraction

**4a** _(written 2026-11-21)_: Kt, depth and memoization, ATP per bit, the genomic bottleneck, _prequential.py_ on _Benefit Street_ chapter 7.

**4b** _(written 2026-11-21)_: AIXI's reward, expected free energy (_curiosity.py_ Part 2), compression progress against the noisy TV and the dark room (_curiosity.py_ Part 1), epistemic against pragmatic action.

## 5. The payoff

**5a** _(written 2026-11-22)_: ARC 2024 figures checked; ARC-AGI-2 (2025) and CompressARC; ARC-AGI-3 from under 1% to about 80% and the harness effect (62.7% → 98.6%); Epoch's "Flawed"; the Hutter Prize's 2026 record (a 3 MB prior saving about 8 MB); compression–capability correlation; "Sampling Is Not Curiosity."

**5b** _(written 2026-11-22)_: prediction-error neurons and limited predictive suppression; brain–LLM alignment saturating at human competence and the confound critique; Frank's accelerating returns (κ ≈ 11–13 against 1.16); active inference against RL; Grant's test answered (a currency, as energy was).

***

## Side files (all written)

* _free-energy-in-plain-terms.md_ (2026-11-21, mid-exploration)
* _predictive-coding-and-free-energy.md_ (2026-11-23)
* _universal-intelligence-and-aixi.md_ (2026-11-23)
* _measuring-intelligence.md_ (2026-11-23)

## Scripts (pure Python, no libraries; kept in GitHub)

_residual.py_, _freeenergy.py_, _ctest.py_, _prequential.py_, _curiosity.py_, _factor.py_, _aixi_toy.py_; reused _compress.py_, _shannon_game.py_, _solomonoff.py_, _taxi.py_.

## Guardrails (as kept)

* Shape first; worked examples with small numbers; runnable scripts where they help.
* No second pass on Solomonoff, arithmetic coding, MDL, grokking, or the identity.
* Consciousness capped at a paragraph; psychometrics limited to _g_ as a construct; no group differences.
* The free-energy principle in operational terms only.
* Claude is an instance of the systems studied; its sense of how it works was not used as evidence.
