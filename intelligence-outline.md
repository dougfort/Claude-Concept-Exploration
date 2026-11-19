# What Is Intelligence? — Outline

_Working plan for the thirteenth exploration, November 2026. Prompted by 3Blue1Brown, "This algorithm changed how I think about compression" (Information theory, part 3, 17 November 2026), chapter 6, "Reflections on 'Compression is Intelligence'" (transcript supplied by Fog). Drafted 2026-11-19; open to steering before stage 1._

**Steering (2026-11-19, before drafting):** a full genealogy, not an extension of _compression-is-prediction.md_; the brain as predictive compressor at **equal weight** with machines throughout, not one stage.

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

Grant's frame: treat "compression is intelligence" as a proposed _definition_, judged like Newton's "energy" — reductive, but is it productive, does it unify? (Correction for stage 1: the quantity he gives, kg·m/s², is force; energy was not Newton's. Its real history — Leibniz's _vis viva_, Young's naming in 1807, the conservation law of the 1840s — is itself a successful concept genealogy, and the better model for his test.)

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

## 1. The intuition — quick wit and economy of thought

* **Aristotle**: _nous_; _anchinoia_, "quickness of wit," defined as hitting on the middle term in an imperceptible time (_Posterior Analytics_ I.34): intelligence as speed of finding the explanation.
* **Hobbes** (reasoning is reckoning) and **Leibniz** in a line each; link _what-is-computation.md_ §1.
* **Mach's economy of thought** (_Die Mechanik_, 1883): science as the most economical description of experience. Grant's "understanding is something becoming smaller in my mind" is Mach's position.
* **Helmholtz's unconscious inference** (_Physiological Optics_, 1867): perception as inference from sensations to their causes — the ancestor of predictive processing.
* **Galton** (1869), **Binet–Simon** (1905), **Spearman's _g_** (1904): intelligence as a measurable, ranked trait.
* **Turing** (1950): replace the definition with a test.
* Working example to carry: one line of a photograph (pixel values) — compressible because neighbours predict each other; a retina and a PNG both exploit it.

## 2. The dispute — what is being measured, and is it inside?

_Two strands at equal weight._

**Machines and tests.**

* _g_ real or artefact: Spearman against Thomson's bonds (1916) and Thurstone's primary abilities; Boring (1923): "intelligence is what the tests test."
* Turing's behaviourism; Dartmouth (1956); symbol systems (Newell–Simon) against connectionism; Searle (1980) capped at a paragraph.
* What the dispute lacked: a measure of how much structure is in data, independent of a test.

**Brains and perception.**

* Helmholtz's inference against **Gibson's direct perception** (1966, 1979): is perception a reconstruction or a pickup?
* Behaviourism's refusal of inner models; Craik's _The Nature of Explanation_ (1943): the brain as building "small-scale models" of the world.
* What the dispute lacked: a way to quantify "redundancy in the input" and "a model's fit."

## 3. The formalization — two lines that meet at description length

_Probably split 3a (brains) / 3b (machines)._

**3a. The brain as compressor.**

* **Attneave** (1954) and **Barlow** (1961): redundancy reduction as the purpose of sensory coding.
* **Srinivasan, Laughlin and Dubs** (1982): predictive coding in the fly retina — centre-surround as subtracting a prediction from the neighbours and sending the residual. Worked with small numbers; _residual.py_ (new): code a row of pixels raw and as residuals, count the bits.
* **Olshausen–Field** (1996): sparse coding reproduces V1 receptive fields from natural images.
* **Rao–Ballard** (1999): hierarchical predictive coding; errors up, predictions down.
* **Hinton–van Camp** (1993), **Dayan–Hinton's Helmholtz machine** (1995): variational free energy as a code length (bits-back). **Friston** (2005, 2010): the free-energy principle. _Position to argue:_ Friston's free energy is a two-part description length, so "the brain minimizes free energy" is "the brain compresses its sensory stream" said with a physicist's vocabulary.

**3b. The machine as compressor.**

* Solomonoff linked, not redone.
* **Hernández-Orallo** (1998): C-tests, intelligence tests built from Kolmogorov complexity.
* **Mahoney** (1999) and the **Hutter Prize** (2006): compression as an AI benchmark, decoder counted.
* **Hutter's AIXI** (2000, 2005) and **Legg–Hutter universal intelligence** (2007): expected reward across all computable environments weighted by 2^−K. Worked on a toy of two or three environments.
* **Chollet**, "On the Measure of Intelligence" (2019): intelligence as skill-acquisition efficiency over priors and experience; ARC.

## 4. The abstraction — compression plus what?

_Probably split 4a / 4b._

* **The reference machine** (from _Induction_), now for brains: evolution as the supplier of the prior.
* **Time and resources**: Levin's Kt, Schmidhuber's speed prior, **Bennett's logical depth** (a short program that takes long to run: understanding vs. depth); the metabolic cost of a spike (Laughlin et al. 1998) and energy-efficient coding.
* **Prequential length as learning speed**: Grant's claims 2 and 3 as one; _prequential.py_ or _compress.py_ reused with a shared pseudo-random start.
* **Action**: AIXI's reward; **active inference** (expected free energy) and its critics; **Schmidhuber's compression progress** (1991, 2009) — curiosity as the first derivative of compression.
* Candidate endpoint form: intelligence as a rate (compression gained per sample, per joule, toward a goal), not a level.

## 5. The payoff — does the definition unify?

_Before writing: search 2025–26 on each thread; report what changed the argument; flag anything recent and untested._

* Compression and capability in LLMs (Huang 2024, Xuyang 2025, cited); newer results.
* **Test-time training** and ARC-AGI-2/3 (2025–26): Grant's on-the-fly fine-tuning as a winning method.
* Hutter Prize records since fx2-cmix.
* **Brains and LLMs**: Schrimpf et al. (2021), Caucheteux–Gramfort–King (2023) on predictive hierarchies in cortex vs. GPT-2; newer work.
* Empirical tests of predictive coding in cortex (2024–26 mismatch-response studies); where the free-energy principle stands.
* Grant's test answered: is compression to intelligence what energy was to _vis viva_ — a reductive definition that unified — or a family resemblance?

***

## Side-file candidates (settle before stage 2)

* **Predictive coding and the free-energy principle in plain terms** (strong): from residual coding to Rao–Ballard to variational free energy as code length, with scripts; the technical home for the brain half.
* **Universal intelligence and AIXI** (candidate): Legg–Hutter worked on toy environments; could instead be an addendum to _solomonoff-and-the-universal-prior.md_.
* **Measuring intelligence: g and factor analysis** (candidate): Spearman's two-factor model worked on a 3 × 3 correlation matrix, Thomson's bonds, what _g_ is and isn't.

## Planned scripts (pure Python, no libraries; kept in GitHub)

* _residual.py_ (new): raw vs. residual coding of a pixel row; bits per pixel.
* _prequential.py_ (new, or _compress.py_ extended): a static model vs. one adapting on the fly from a shared pseudo-random start; code length against data seen.
* _factor.py_ (if the psychometrics side file is chosen).
* _aixi_toy.py_ (if chosen): universal intelligence over three tiny environments.
* Reused: _compress.py_, _shannon_game.py_, _solomonoff.py_, _taxi.py_.

## Threads to carry in

* **The bias** — evolution as the supplier of a brain's prior.
* **Prediction underdetermines mechanism** — Moravec; equal compression from different mechanisms.
* **Observation bounded by computation** — Kt, logical depth.
* **The record** and **the copy** — memorization vs. compression in brains (hippocampal replay?) only if it earns its place.
* **The division** — Markov blankets as the free-energy principle's cut between agent and world.
* **Causality** — action and intervention (stage 4), handed back.

## Guardrails

* Shape first; worked examples with small numbers; runnable scripts where they help.
* No second pass on Solomonoff, arithmetic coding, MDL, grokking, or the identity: link and build.
* Consciousness capped at a paragraph; IQ and group differences out of scope beyond what _g_ is as a construct.
* The free-energy principle is the largest risk of sprawl and of unfalsifiability: state its claims operationally or not at all.
* Claude is an instance of the systems studied; its sense of how it works is not evidence.
