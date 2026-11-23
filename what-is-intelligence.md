# What Is Intelligence?

_Notes from a conversation, November 2026. From Aristotle's quick wit and Mach's economy of thought, through Spearman's g and Helmholtz's unconscious inference, to a fly's retina, a C-test whose own language scores 100%, a chapter of Fog's fiction compressed five ways, and a benchmark on which the same model scores 62.7% or 98.6% depending on what it remembers._

_Origin: 3Blue1Brown, "This algorithm changed how I think about compression" (Information theory, part 3, 17 November 2026), chapter 6, "Reflections on 'Compression is Intelligence'" (transcript supplied by Fog). Grant Sanderson proposes treating the phrase as a definition, judged like a physicist's definition of energy: reductive, but is it productive? By steering, the brain as a predictive compressor ran at equal weight with machines throughout. No argument map (no post planned)._

***

## 1. A working definition

**Compression is the currency of intelligence, not its definition. Intelligence is the rate at which a system turns experience, some of it chosen, into compression that serves goals compression doesn't supply, per unit of resource. It belongs to the whole learning system (prior, memory and learning rule), and its distinctively human form is a rate that increases: learning to learn.**

The first sentence answers Grant's test (§6, 5b). "Rate" is Aristotle's _anchinoia_ (§2), Chollet's skill-acquisition efficiency (§4), and the slope of a prequential code (§5). "Some of it chosen" is compression progress and information-directed exploration (§5). "Goals compression doesn't supply" is the finding that every repair for action adds one (§5). "Per unit of resource" is Kt, depth, ATP per bit, and the Hutter Prize's limits (§5). "The whole learning system" is ARC-AGI-3's harness effect (§6, 5a). "A rate that increases" is children's word learning (§6, 5b).

Working claim broken by the genealogy: **intelligence is compression: a system is intelligent to the degree that it finds short descriptions of its experience, and one measure ranks brains and machines alike.** It fails four times (§6): "short" has no owner-free meaning; compression scores passive observation and intelligence acts; cost changes the optimum; one measure doesn't rank everything.

Grant's three claims, as resolved:

1. **Compression and prediction are equivalent.** True by identity (_compression-is-prediction.md_); "good prediction needs a coherent model" is Barlow's 2001 position, and true where the model is the shortest description (Mach's atoms, §2).
2. **Understanding is something getting smaller.** True when time is free; reversed under time pressure (expertise is memoization, §5); in a prequential code what is rewarded is a prior weighted by its reliability, not smallness.
3. **Learning quickly counts.** The center of the matter: it is the rate in the definition, and claims 2 and 3 are one quantity (the prequential code length).

Distinctions worth keeping:

* **Currency vs. definition.** Bits are the common unit with exchange rates (time, ATP, priors); they don't say what an intelligent system does.
* **Skill vs. intelligence.** Skill can be bought with priors or experience; intelligence is the efficiency of the purchase (Chollet).
* **Level vs. rate.** Reward collected (Legg–Hutter's Υ) against reward bought per bit (Chollet); _nous_ against _anchinoia_.
* **Two accountings.** Hutter's (charge the model) and prequential (charge the learning); they agree when the prior is small and well matched.
* **Short-and-deep vs. long-and-shallow.** Understanding against expertise; which is better depends on how often the question comes.
* **Epistemic vs. pragmatic action.** Changing what you observe against changing the world; only the second reveals a world model.
* **Model vs. system.** Weights against weights plus memory of the episode.
* **First-order vs. second-order rate.** Learning fast against getting faster at learning.

Pattern: emergence began as a slogan; intelligence began as a _ranking_ (Spearman's single number) and a _speed_ (Aristotle's quick wit), and the genealogy is the story of the speed winning. (Position.)

***

## 2. The intuition — quick wit and economy of thought

_Selective prehistory by choice._

**Aristotle.** _Nous_ (grasp of first principles) against _anchinoia_, quick wit, hitting on the explanation in an imperceptible time (_Posterior Analytics_ I.34; his example: seeing at once that the moon's bright side faces the sun because it borrows its light). _Position:_ the first definition of intelligence was a rate, not a level. Hobbes and Leibniz in a line (_what-is-computation.md_ §1).

**Mach.** Mach bands (1865): the eye exaggerates where slope changes. Economy of thought (1882; _Die Mechanik_, 1883): a law is a way of not remembering cases. Refraction: a table of 90 angles at about 900 bits against sin(i) = n sin(r) with n = 1.33 (30° → 22.1°; 60° → 40.6°). Mach used economy against atoms. _Position:_ his measure was right and his bookkeeping wrong; atoms cost bits once and saved far more (two-part code); a model of what's going on is what a short description becomes when data are rich.

**Helmholtz.** Unconscious inference (_Physiological Optics_ vol. 3, 1867): sensations are signs; the pressed-eyeball phosphene. _Position:_ predictive coding is Helmholtz's inference scored by Mach's measure.

**Spearman and Binet.** The positive manifold (1904); loadings 0.9, 0.8, 0.7 reproduce correlations 0.72, 0.63, 0.56; ten tests, 10 numbers for 45 correlations. Binet (1905) refused a single quantity. _Position:_ g is a compression of a correlation table. (_measuring-intelligence.md_.)

**Turing (1950).** Replace the definition with a test; Lovelace's objection answered by the child machine. _Position:_ behaviour and learning at the center, not stored knowledge.

**Working example.** One row of pixels, 100 102 103 103 105 180 182 181: raw 64 bits, residuals 41; the expensive residual sits at the edge.

***

## 3. The dispute — what is being measured, and is it inside?

_Two strands at equal length by choice; Searle at a paragraph._

**Machines and tests.** Thomson's bonds (1916): six bonds, three tests sharing two each, every correlation 0.5, one factor fits exactly, no bond general; van der Maas's mutualism (2006) a third mechanism. Boring (1923): what the tests test. Dartmouth (1955–56); symbols (Newell–Simon) against networks (McCulloch–Pitts to PDP 1986; Fodor–Pylyshyn 1988). Moravec's paradox (1988). Searle (1980), set aside as a question about meaning. Block's Blockhead (1981): a lookup table for five-minute conversations needs about 27^1000 ≈ 10^1431 entries.

**Brains and perception.** Watson (1913); Tolman's sunburst maze (1948), mixed replications; Gestalt _Prägnanz_ (1923) and Hochberg–McAlister's minimum principle (1953); Craik's small-scale models for trying actions (1943); Gibson's invariants and affordances (1966, 1979); Marr's levels (1982).

_Positions:_ g is real as a description and undetermined as a mechanism; Boring's move is Turing's; symbols against networks was a dispute over who pays for the model, with no common measure; Blockhead is where compression first does work behaviour can't; Tolman's detour is Vafa's taxi test as a design; Craik's model is for action; Gibson's invariants are what makes input compressible and Helmholtz's model what exploits them; "compression is intelligence" is a claim at Marr's top level.

**Missing:** the redundancy of a source and the length of a model (Shannon 1948; Solomonoff–Kolmogorov 1964–65).

***

## 4. The formalization — two lines that meet at description length

### 3a: the brain as compressor

Attneave (1954): Shannon's guessing game on pictures; the 38-point cat. Barlow (1961) redundancy reduction, revised (2001) to redundancy exploitation. Srinivasan, Laughlin and Dubs (1982): the retinal surround as a predictor. _residual.py_: bright line 5.98 → 2.48 bits/pixel, dim 7.41 → 5.24; best predictor width 2 → 8 pixels as noise σ goes 0.5 → 16; centre-surround nonzero at 0.7% of pixels; Mach bands at ramps, not at steps. Olshausen–Field (1996), Rao–Ballard (1999), end-stopping. Variational free energy F = −log₂ p(data) + KL(q ‖ posterior), stated; _freeenergy.py_ (shadow or puddle: surprise 2 bits; F 2.000 at the posterior, 2.737 if certain of shadow). Addendum at Fog's request: _free-energy-in-plain-terms.md_; bits-back worked in _predictive-coding-and-free-energy.md_ (every choice nets exactly 2 bits at the posterior).

_Positions:_ Attneave was the first to treat a picture as a message; Barlow's revision turns compression from goal to evidence; the fly retina is the first place the compressor view predicted physiology; the retina's code is not the percept; Olshausen–Field's objective is a two-part code; end-stopping needs a model's content; for perception, minimizing F is minimizing code length under a generative model.

### 3b: the machine as compressor

**C-test** (Hernández-Orallo 1998). _ctest.py_: a four-constructor language, items graded by Kt; three outside solvers fall to zero above Kt ≈ 22–28 while the test-maker's language scores 100% by construction; unquestionable items 18.8% with 3 letters shown, 99.2% with 4; `yyyyyya → a` unquestionable in the language and odd to a person. Sanghi–Dowe (2003): a short program at human average on IQ sequence items.

**Hutter Prize** (Mahoney 1999; 2006; limits < 10 GB, < 50 h, one core).

**AIXI and universal intelligence** (Hutter 2000, 2005; Legg–Hutter 2007): Υ = Σ 2^−K × reward. Specialist 0.131 against generalist 0.094 with invented numbers; _aixi_toy.py_: always-0 0.142, occam 0.157, random 0.080; swap the reference machine and always-0 falls to 0.061, below random's 0.081. (_universal-intelligence-and-aixi.md_.)

**Chollet (2019), full section by choice.** Skill against intelligence; intelligence as skill-acquisition efficiency against priors, experience and generalization difficulty (illustrative: 500 bits ÷ 1,200 = 0.42 against 500 ÷ 21,000 = 0.024); Core Knowledge; ARC.

_Positions:_ item difficulty is well defined and every score relative to a reference machine; the Hutter Prize and pretraining measure one quantity under two accountings; Legg–Hutter already rejects the passive working claim (compression weights, reward scores); Υ is dominated by simple environments; Chollet's reference is the honest one for comparing machines with people; Chollet's measure is Hutter's accounting plus prequential accounting on new tasks; compression of a fixed corpus measures skill.

***

## 5. The abstraction — compression plus what?

### 4a: plus cost

**Time.** Kt = length + log₂ steps: 20 bits × 2³⁰ steps (Kt 50) against 35 bits × 2¹⁰ (Kt 45). Levin search; the speed prior.

**Depth.** Bennett (1988): random and repetitive strings shallow, Life soups and genomes deep. Chess masters' tens of thousands of chunks. _Position:_ "smaller is smarter" holds when time is free and reverses under time pressure; expertise is memoization.

**Energy.** 10⁴ ATP per bit at a synapse, 10⁶–10⁷ for graded or spike signals (Laughlin et al. 1998); brain about 20% of resting energy; cost per bit rising with rate (Niven et al. 2007). _Position:_ sparse coding is economical before it is short.

**Evolution as the prior.** Genome about 6 × 10⁹ bits (≈ 775 MB) against 10¹⁴–10¹⁵ synapses (Zador's genomic bottleneck); children 6 × 10⁶ words by 5, 3 × 10⁷ by 20, four or five orders of magnitude below LLMs (Frank 2023). _Position:_ human intelligence is efficiency, not size.

_**prequential.py**_ on _benefit-street-chapter-07.md_ (21,377 bytes), base text 200 KB of stdlib docstrings, order-0–4 context model: scratch 2.986 bits/byte; pretrained static 4.973; pretrained adapting 3.106; pretrained fast (4×) 3.038; light prior (1/20 weight) **2.507**; lzma 2.985. Static's worst block 7.07 (the 17 October transmission log). Hutter accounting adds 64,292 bytes for the model: scratch 7,980 bytes against light prior 70,991. _Positions:_ wrong priors held strongly cost more than none; learning rate shows in the code length; claims 2 and 3 are one number, rewarding a prior weighted by reliability; the accountings disagree by a factor of nine here.

### 4b: plus action

**AIXI's reward** stated openly; wireheading (Ring–Orseau 2011); laziness under bad priors (Leike–Hutter 2015).

**Active inference.** G = expected cost under preferences − information gain. _curiosity.py_ Part 2: drive on 2.749, slow down 3.474, look closer 1.294 (1.807 − 0.512); with flat preferences, look closer 1.073 against 1.585. Millidge–Tschantz–Buckley (2021): exploration does not follow from future free-energy minimization; without preferences, optimal Bayesian design.

**Compression progress** (Schmidhuber 1991, 2009). _curiosity.py_ Part 1, 3,000 steps × 5 runs on constant, noise, easy and hard streams: error-seeking 92–93% on noise (the noisy TV), comfort-seeking 92–93% on the constant (the dark room), progress-seeking moves constant → hard (30% in phase 2) → easy and ends 0.06 bits above the learnable floors against 0.59 and 0.64; it lingers on the learned stream at the end (a measurement artefact).

_Positions:_ prediction plus a goal isn't enough without exploration; active inference is expected utility plus an information bonus, with utility called a prior; compression progress is the bet's rate turned into a motive and still a designer's goal; epistemic action chooses data, pragmatic action changes the world (to _Causality_); compression is the currency, not the goal.

***

## 6. The payoff — does the definition unify?

### 5a: machines

_Search findings, November 2026:_ ARC 2024 figures confirmed (ARChitects 53.5%; MindsAI 55.5%, ineligible; o3 75.7% at the $10k limit, 87.5% at 172× compute; test-time training first seen with Cole and Osman, 2023). ARC-AGI-2 in 2025: Kaggle top 24.03% at $0.20/task; Opus 4.5 37.6% at $2.20; refinement on Gemini 3 Pro about 54% at about $30; Tiny Recursive Model (7M) about 45% on ARC-AGI-1; **CompressARC** (76K parameters, no pretraining, MDL per puzzle) 20% on ARC-AGI-1 at about 20 GPU-minutes per puzzle; Chollet's "knowledge-dependent overfitting." By November 2026 ARC-AGI-2 at about 95%. **ARC-AGI-3** (March 2026; interactive; scored by action efficiency, (human actions ÷ AI actions)² per level): under 1% at launch; by November, Standard harness Claude Fable 5.2 81.2%, GPT-6.2 Astra 70.3%, Gemini 4 Carbon 65.1%; Provider Adapter 97.7–100%; GPT-6 Astra 62.7% → 98.6% with only the memory harness changed; OpenAI: retaining reasoning and compaction gave about 3× the score with 6× fewer output tokens; Kaggle offline leader 75.56 on the public board (results 4 December 2026); Epoch's review: "Flawed." **Hutter Prize 2026:** three awards since June, almost 10%, the largest in its history; fx2-cmix-T (Ivanov, 24 July 2026) 100,424,672 bytes, a 6M-parameter transformer (about 3 MB at 4 bits) pretrained offline on GPUs replacing cmix's LSTM, saving about 8 MB; uncapped frontier 96.1 MB (zmix, September). Compression–capability correlation (Huang 2024, r beyond −0.93) not overturned. "Sampling Is Not Curiosity" (NeurIPS 2026 position): current LLM agents explore stochastically; a training-free graph explorer led early ARC-AGI-3 preview results.

_Positions:_ CompressARC shows compression as a method for novel tasks, paid for in computation; the harness effect is the endpoint observed directly and the clearest evidence against compression as a property of weights; headline ARC-AGI-3 scores aren't robust, the controlled comparison is; a prior earns its place when its bits are small against what it saves, which reconciles the two accountings; the compression–capability correlation measures skill across models, not learning rate within a task; current agents explore stochastically, and whether learning progress would raise action efficiency is open and testable. (Claude Fable 5.2 is an Anthropic model; its score was reported and nothing inferred from Claude's own sense of such systems.)

### 5b: brains

_Search findings, November 2026:_ signed, precision-weighted prediction-error neurons (auditory omission responses, 2025; L2/3 signed PE circuits, preprint September 2026); visual mismatch spatial rather than temporal (preprint 2025); an open multi-species, multi-area test finding predictable responses dominating in over 50% of neurons, limited predictive suppression; genuine prediction errors perhaps in prefrontal cortex (_TiCS_ 2025); the OpenScope community experiment unreported. Brain–LLM alignment rising with size (774M–65B; 82M–70B), then saturating (3B models matching 7–14B; peak at 2–8B training tokens; next-word correlation fading beyond human proficiency, AlKhamissi et al. 2025); confound critique (Hadidi, Feghhi et al. 2025, contested). Frank (August 2026 preprint): children's acceleration exponent κ ≈ 10.6–13.3, GPT-2 on 24M words of child-directed speech κ = 1.16; Feng–Tan–Frank (2026): model likelihoods track which words children learn. Active inference beats RL without directed exploration where people explore (Gijsen et al. 2022; Zhang et al. 2025); people monitor learning progress (Ten et al. 2021).

_Positions:_ the brain compresses at the periphery and models at the top, and the cortical middle isn't a pure residual coder; the theory's parts are found, its architecture not confirmed; better text compression makes models more brain-like only to human competence, so the brain is a compressor of a particular kind; brain scores alone are weak evidence; if Frank's result holds, the human advantage is a rising learning rate, learning to learn; support for active inference is support for information-directed exploration.

**Grant's test.** Energy unified physics as a currency with exchange rates (Joule's equivalent), not by defining motion. Bits appeared as the unit for perception (F), test difficulty (Kt), skill (Hutter, LLMs), learning (prequential length), curiosity (progress) and Chollet's measure, with exchange rates to time (≈ 10 bits per thousandfold slowdown), energy (10⁴–10⁷ ATP per bit) and priors (3 MB saving 8 MB). _Position:_ compression passes Grant's test in energy's role, as a currency, not as a definition.

### The bet, tested

_Opening bet: intelligence is not compression but the efficiency of compressing new data: how quickly a system's prequential code length drops on experience it hasn't seen, per sample and per unit of resource, in service of acting._

| Prediction                                                             | Result                                                                                                                                      |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Grant's claims 2 and 3 collapse into one                               | **Confirmed**, amended: a prior weighted by reliability, not smallness (4a); the accountings agree when the prior is small and matched (5a) |
| Periphery firm, cortex weak                                            | **Confirmed, sharper**: error cells exist, suppression doesn't                                                                              |
| Repairs for action smuggle in a goal                                   | **Confirmed** for AIXI, active inference, compression progress                                                                              |
| Chollet and on-the-fly adaptation are one proposal; TTT its experiment | **Confirmed**: TTT won ARC 2023–25; the ARC-AGI-3 harness effect is the within-episode version                                              |

**Amendments.** Intelligence belongs to the system, memory included, not the weights (5a). The human form is second-order (5b). "In service of acting" made precise: the goal comes from outside compression (4b).

***

## 7. The single line of thought

One question, asked with steadily more attention to speed: what does it take to find the short description, and how fast?

| Stage                                 | Intelligence is…                                | Measured by                            | What it yields                                |
| ------------------------------------- | ----------------------------------------------- | -------------------------------------- | --------------------------------------------- |
| Aristotle (4th c. BCE)                | finding the explanation fast                    | nothing yet                            | _anchinoia_: a rate                           |
| Mach, Helmholtz (1865–83)             | economy; inference to causes                    | intuition                              | the two halves of predictive coding           |
| Spearman to Boring (1904–23)          | a single ranked trait                           | correlation tables                     | _g_: a compression of people                  |
| Turing to Block (1950–81)             | behaviour                                       | tests                                  | Blockhead: behaviour can't tell               |
| Attneave to Rao–Ballard (1954–99)     | redundancy removed                              | bits per pixel                         | the predictive retina                         |
| Solomonoff to Legg–Hutter (1964–2007) | prediction, then reward, weighted by simplicity | Kt, Υ                                  | universal intelligence, relative to a machine |
| Chollet to ARC-AGI-3 (2019–26)        | efficiency of acquiring skill                   | bits of priors and experience; actions | a rate, of a system                           |
| Frank (2026)                          | a rate that rises                               | κ                                      | learning to learn                             |

Waves kept the space. Symmetry kept the group. Entropy kept the logarithm. Randomness kept the absence. Measurement kept the record. Computation kept the step. Space kept the relation. Time kept the correlation with a clock. Information kept the copy. Induction kept the bias. Emergence kept the closure. Intelligence kept the _rate_, and lost the size of the model, the single ranking, and compression as the goal.

***

## Runnable companions

Pure Python, no libraries; kept in GitHub.

* _residual.py_: the stage-1 row; raw against residual coding; predictor width against noise; centre-surround responses.
* _freeenergy.py_: shadow or puddle; F against the guess; Gaussian energies.
* _ctest.py_: a C-test; unquestionability by letters shown; four solvers by difficulty band.
* _prequential.py_: five learners on a supplied text (run: `python3 prequential.py benefit-street-chapter-07.md`); Hutter accounting; learning curves.
* _curiosity.py_: error-, comfort- and progress-seeking on four streams; expected free energy for looking closer.
* _factor.py_: the triad formula; g, bonds and mutualism (side file _measuring-intelligence.md_).
* _aixi_toy.py_: universal intelligence on three environments; changing the reference machine (side file _universal-intelligence-and-aixi.md_).
* Reused: _compress.py_, _shannon_game.py_, _solomonoff.py_, _taxi.py_.

## Suggested next steps

* In _prequential.py_, estimate κ: fit the learning curves to a power law in bytes seen and check whether any learner's proportional return rises (Frank's test on a count model; expect κ ≈ 1).
* Add a second-order learner to _prequential.py_: one that tunes its own back-off weight β as it reads, and see whether its curve accelerates.
* In _curiosity.py_, replace the moving-average progress measure with progress measured on held-out symbols, and see whether the late lingering on the learned stream disappears.
* Run _prequential.py_ on another chapter of _Benefit Street_, with chapter 7 as the base text, and compare the light and heavy priors when the prior is the right genre.
* Watch the ARC Prize 2026 results (4 December) and Epoch's follow-up review; check whether the Kaggle compute-limited entries keep pace with frontier systems on action efficiency.
* Reading: Chollet, "On the Measure of Intelligence" (2019), §I–III; Legg and Hutter (2007); Barlow, "Redundancy reduction revisited" (2001); Bogacz (2017); Frank, "Children, but not language models, show accelerating returns in word learning" (2026); the ARC-AGI-3 technical report (ARC Prize Foundation, 2026).
* Links forward: _free-energy-in-plain-terms.md_, _predictive-coding-and-free-energy.md_, _universal-intelligence-and-aixi.md_, _measuring-intelligence.md_ (side files); _Causality_ (epistemic against pragmatic action; Tolman's detour; interventions as the test of a world model).
