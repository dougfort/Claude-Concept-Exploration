# Argument Map: "Inexplicable, Cosmic Accident"

_For the blog post that follows the induction and emergence explorations, October 2026. Claims only, each with its source and one objection to expect. Sources: what-is-induction.md (§ numbers refer to it as "Ind."), what-is-emergence.md ("Em."), and the side files. Scripts run as recorded there._

***

## The spine

Kevin Roose's _The AGI Chronicles_ (2026) calls the generality that came out of next-token prediction an "inexplicable, cosmic accident." Each of the three words makes a different claim, and each can be checked:

* **Accident:** no. The goal rested on a theorem, the method is literally compression, and the scaling was a published bet.
* **Inexplicable:** partly. That prediction yields generality is explained; _which_ parts of the world a finite compressor recovers as structure, and which as lookup, is settled only by testing.
* **Cosmic:** no. Sudden abilities, where real, are transitions of a kind physics has understood since the 1930s; often they are an artifact of how the abilities were scored; and when they happen is increasingly predictable.

***

## Part 1: "Accident" and "inexplicable" (from _Induction_)

**I1. Learning from examples always requires an assumption the examples don't supply.** Hume's problem is valid and has never been answered, only priced. Averaged over all possible worlds, every learner scores chance on unseen cases (no-free-lunch: 50.0% for every learner over all 256 functions of 3 bits). _Sources:_ Ind. §2–3; _nfl.py_; Wolpert (1996). _Objection to expect:_ "Real data have structure, so this is a philosopher's worry with no practical bite." (Agreed that it's the world's structure that pays; the point is that the bet is on the world, Ind. §3.)

**I2. "A perfect predictor must model the world" is a theorem, but about outputs, not mechanisms, and the perfect predictor is uncomputable.** Solomonoff (1964, 1978): total prediction error is bounded by the source's description length. A lookup table with the same outputs is indistinguishable from the mechanism. _Sources:_ Ind. §4 (3a); _solomonoff.py_; _solomonoff-and-the-universal-prior.md_; Solomonoff (1964), project file. _Objection to expect:_ "Solomonoff induction has nothing to do with transformers." (The bridges are compression bounds, the parameter-function map, and singular learning theory, Ind. §5.)

**I3. Counting a model's capacity can't explain why large networks generalize; generalization belongs to the training procedure and the data together.** The same network that gets 85.75% on real CIFAR-10 labels fits random labels perfectly and scores 9.78%. A capacity-based guarantee for it would need about 6.6 billion examples. _Sources:_ Ind. §4 (3b), §5 (4a); Zhang et al. (2017), project file; _shatter.py_; _double_descent.py_. _Objection to expect:_ "Newer generalization bounds do work for deep networks." (They do, and they're compression bounds that depend on the trained model, not capacity bounds, Ind. §5.)

**I4. Trained networks enact a simplicity prior, but simplicity in their own language.** Gradient descent lands on minimum-norm, maximum-margin, or low-rank fits; random weights already favour simple functions; the learning coefficient λ measures effective complexity. High-degree parity is short to write and hard for networks: "simple" isn't universal. _Sources:_ Ind. §5; _implicit_bias.py_; _slt.py_. _Objection to expect:_ "The parameter-function-map evidence comes from tiny networks." (True, and flagged in Ind. §5.)

**I5. Pretraining is compression, by identity, not analogy.** Log loss equals code length; in single-pass training every batch is predicted before it's trained on, so the training curve is a compressed size of the corpus. Sixty lines of next-byte counting beat gzip (_compress.py_). _Sources:_ Ind. §6 (5a); _compression-is-prediction.md_; Delétang et al. (2024). _Objection to expect:_ "Compression isn't understanding." (Agreed: compressible doesn't mean efficiently predictable, and compression doesn't mean mechanism, Ind. §6.)

**I6. A learner builds a model of the world where that model is the shortest description of its data, and shortcuts where shortcuts are shorter.** A counting model of taxi rides gets 99.4% of next moves right and 13% of whole held-out rides; a map-based model gets 100% of both. Vafa's transformers trained on shortest paths fail under detours; trained on random walks, they don't. _Sources:_ Ind. §6 (5b); _taxi.py_; Vafa et al. (2024, 2025). _Objection to expect:_ "Othello-GPT and similar probes show LLMs build world models." (In random-play data, where the world model is shortest; the claim is that the data decide, Ind. §6.)

**I7. It was not an accident.** The goal rested on a theorem (Shannon 1951, Solomonoff 1964), the method is compression, and the scaling was a published bet (Kaplan 2020, Hoffmann 2022). _Sources:_ Ind. §6 (5a). _Objection to expect:_ "That's hindsight; nobody predicted how much or how soon." (Conceded: degree and timing surprised, and timing is the emergence half.)

**I8. What remains inexplicable is which structure a model recovers.** No theorem says in advance whether a finite compressor will find the mechanism or a lookup table for a given part of the world; only interventional tests (detours) reveal it. _Sources:_ Ind. §6. _Objection to expect:_ "Mechanistic interpretability will eventually explain it." (Possibly case by case; there's no general theory yet.)

***

## Part 2: "Cosmic" (from _Emergence_)

**C1. Much of the reported suddenness is in the scoring, not the model.** Score smoothly improving models with an all-or-nothing metric and you get apparent jumps. The test: a metric mirage moves with task length but never narrows (_mirage.py_: the switch is 3.35 decades wide whether answers are 1, 20, or 1,000 tokens long); a real transition narrows as its size grows. _Sources:_ Em. §6 (5a); Schaeffer, Miranda, Koyejo (2023), project file; _mirage.py_; Em. §4 (finite-size scaling). _Objection to expect:_ "Some jumps survive smooth metrics" (Du et al. 2024; Zhao et al. 2026). (Agreed: that's C2.)

**C2. Real sudden changes exist, and they're a familiar kind: first-order transitions, one solution replacing another.** Grokking (a memorized table replaced by a Fourier circuit); knowledge acquisition that switches at a critical data mix (near 0 at mixing ratio 0.3, about 80% at 0.4, for a 410M model); success or failure splitting across random seeds. They show the fingerprints of water freezing: coexistence, delay before switching, waiting times that grow near a threshold. In _grok.py_, every run memorizes by step 50; with weight decay, 10 of 30 later generalize, without it 0 of 9; at 60–70% data some seeds switch and others never do. _Sources:_ Em. §4 (3a), §5 (4b), §6; _landau.py_; _transition.py_; _grok.py_; Power et al. (2022), project file; Rubin, Seroussi, Ringel (2023); Gu et al. (2025); Zhao et al. (2026, preprint); Ersoy and Wiesner (2026, workshop poster). _Objection to expect:_ "These are toy models (modular arithmetic, synthetic biographies), not frontier LLMs." (Fair; induction heads in C3 are the real-model case.)

**C3. A second source of real suddenness is composition.** A behavior that needs several smoothly learned parts at once switches on like their product. Induction heads, the circuit behind in-context copying, form in a sudden phase change in every model with two or more layers (34 models, 13M to 13B parameters); their three subcircuits each learn smoothly alone. _Sources:_ Em. §6 (5b); Olsson et al. (2022); Singh et al. (2024). _Objection to expect:_ "Then 'emergence' is just multiplication and means nothing." (It means the mechanism genuinely needs all the parts; but it is the same algebra as the mirage, and nothing shows the switch sharpening with size.)

**C4. What is sudden is when, not what.** For a single training run, the moment of a switch can be hard to forecast. What appears is a circuit with its own rule, a description that "closes" like a glider in the Game of Life. In aggregate, timing is increasingly predictable: induction heads by a law in batch size and context length that doesn't depend on model size from 50M to 7B parameters; emergence forecast from fine-tuned small models up to 4× compute ahead; knowledge thresholds by a power law in model size. _Sources:_ Em. §5 (4a: the commuting square; _life.py_), §6; Aoyama, Wilcox, Schneider (2026, preprint, untested); Snell et al. (2024); Gu et al. (2025). _Objection to expect:_ "Abilities like multi-step reasoning are new in kind, not just in timing, and no one has found their circuit." (True; the claim is shown for mechanisms that have been found, not yet for the large abilities.)

**C5. Smooth scaling laws and sudden abilities don't conflict.** A smooth power law is what many small abrupt steps look like when added up, the way a smooth melting curve hides grains freezing one by one. Skills needed with frequency ∝ 1/k², learned one at a time, leave residual loss 0.095 after 10 skills and 0.00995 after 100: a smooth law built from steps. _Sources:_ Em. §6 (5a); Michaud et al. (2023). _Objection to expect:_ "The quanta picture is a hypothesis." (Yes; two alternatives, critical data and an RG fixed point in learning, are preprints, Em. §6.)

**C6. "Emergence" in the LLM literature is partly borrowed and partly earned.** Borrowed where it means a curve rose fast under a threshold metric: Wei et al.'s definition is Lewes's 1875 test applied to a plot, and cites Anderson without using his mechanism. Earned where a stable new internal variable switches on through a transition. Even then it's Anderson's concept at the first-order level ("ice forming, not a magnet at its Curie point"), and universality, the deepest part of his picture, is untested. _Sources:_ Em. §2, §3, §6; Anderson (1972), project file; Wei et al. (2022), project file; Krakauer, Krakauer, Mitchell (2025). _Objection to expect:_ "Machine learning can define 'emergence' its own way; this is a quibble about words." (Fine, but then it shouldn't borrow physics' authority for novelty that physics doesn't grant.)

**C7. The verdict: not an accident, partly inexplicable, not cosmic.** The abilities that seem to arrive from nowhere arrive the way ice does: one arrangement replacing another, sudden in each sample, predictable in the aggregate, and new only in the sense that a glider is new, a pattern with its own rule, made entirely of the old one. _Sources:_ Ind. §6; Em. §6. _Objection to expect:_ "Roose meant 'cosmic' as awe, not as a technical claim about phase transitions." (Probably; the post should say so, and argue that the awe is better spent on the explanation.)

***

## Not established; don't claim

* That any LLM capability shows **universality** (criterion (c)); Aoyama's size-independence is a weak candidate only.
* That any learning-system transition **narrows with a named size**; no one has measured it.
* Whether grokking's waiting time grows **exponentially** (barrier crossing) or as a **power** (critical slowing down); _grok.py_'s five seeds can't tell.
* Ersoy–Wiesner's mechanism (workshop poster, abstract only) and Aoyama's law (preprint, untested) as settled results.
* That the first-order reading of grokking is ours: it's Rubin, Seroussi, Ringel (2023).
* Anything from Claude's own sense of how it works; it wasn't used as evidence.

## Numbers you can quote

| Number                                 | What it shows                                            | Source              |
| -------------------------------------- | -------------------------------------------------------- | ------------------- |
| 85.75% vs. 9.78% test; 100% train both | same network, real vs. random labels                     | Zhang et al. 2017   |
| 99.4% next moves, 13% whole rides      | a lookup passes next-step tests and fails whole tasks    | _taxi.py_, Ind. §6  |
| 3.35 decades, at any answer length     | a metric mirage moves, never narrows                     | _mirage.py_, Em. §6 |
| \~10³ vs. \~10⁶ steps                  | grokking's delay, division mod 97                        | Power et al. 2022   |
| 0/9 vs. 10/30                          | generalization without vs. with weight decay             | _grok.py_, Em. §6   |
| 34 models, 13M–13B                     | induction-head phase change in every model of ≥ 2 layers | Olsson et al. 2022  |
| 0.3 → 0.4 mixing ratio: \~0% → \~80%   | knowledge acquisition switch, 410M model                 | Gu et al. 2025      |
| 2.269, and 0.610 / 0.608 / 0.611       | Onsager's T_c, recovered from 8-, 16-, 32-spin lattices  | _ising.py_, Em. §4  |
