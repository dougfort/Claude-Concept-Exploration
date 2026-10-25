# What Is Induction? — Outline

_Working plan for the tenth exploration, October 2026. Arc settled before stage 1; open to steering. Split from Emergence at Fog's choice: Induction now, Emergence next, one blog post after both._

***

## Origin

Kevin Roose's _The AGI Chronicles_ (2026) calls the generality that came out of next-token prediction an "inexplicable, cosmic accident." That sentence holds two questions. _Why does prediction training produce models with broad competence?_ and _What remains unexplained even if it does?_ This exploration keeps both visible.

## Working claim to be broken

**A learner generalizes by fitting its data with the simplest hypothesis that works. It is safe from memorizing only when it has few parameters relative to its data.**

This was textbook doctrine until 2017. The genealogy is expected to break it in three places:

1. **"Simplest" has no meaning without a choice of language.** Simplicity depends on the description language. Solomonoff fixes the language up to a constant (the invariance theorem, cited from _what-is-randomness.md_), but that constant can be large.
2. **"Few parameters" is the wrong measure.** Zhang et al. (2017) showed that a network which generalizes on real labels can also memorize random labels perfectly. Capacity counts what a model _could_ fit, not what training _does_ fit.
3. **"Fitting" is not the endpoint.** Double descent (Belkin et al. 2019) shows test error falling again after a model can fit the training data exactly. Among all the exact fits, the training procedure matters.

## Opening bet (a position, to be tested, not a result)

**"The perfect predictor models the world" is Solomonoff's theorem, and it is sound. It is also uncomputable. What remains unexplained is why gradient descent on a transformer approximates a simplicity prior well enough to recover latent structure from finite, biased text.**

So Roose's "accident" is wrong about the goal and right that the mechanism isn't understood. The bet predicts four findings. No capacity-based bound explains large models. The best available explanations are simplicity bias, compression, and singular learning theory. Internal world models appear in some domains and fail in others. The residual gap narrows but does not close.

## The question carried in

From _Information_: aboutness is mutual information plus a preparation history. From _Randomness_: a probability is a property of a description, and de Finetti's exchangeability is what licenses learning from frequencies. So induction asks: _what licenses projecting a pattern from observed to unobserved, and does a trained network have that license or only a useful behavior?_ 

***

## 1. The intuition — the future like the past

* Aristotle's _epagogē_, and the Epicurean sign-inference, briefly.
* Bacon's tables and Mill's methods: induction as a procedure.
* **Hume** (1739/1748): no non-circular justification that the future resembles the past; custom as the answer.
* **Laplace's rule of succession**. Cite _what-is-randomness.md_, don't repeat it. Worked: the sun has risen n times, so the probability it rises tomorrow is (n+1)/(n+2).
* **Peirce**: abduction, and induction as self-correcting in the long run.
* **Shannon's guessing game** (1951): people predicting the next letter of English as a measurement of its entropy. This is the first time prediction becomes a measure of knowing a source.
* What the intuition contains: regularity, projection, and the sense that good prediction means understanding. That is the working claim.

## 2. The dispute — which generalization?

* **Goodman's "grue"** (1955): the data are consistent with infinitely many projections, so the problem is which predicates to project, not whether to project. Worked: green/grue on a small table.
* **Popper**: no induction, only conjecture and refutation. Simplicity as falsifiability.
* **Occam** and simplicity as a prior, against counting hypotheses.
* **Wolpert's no-free-lunch theorem** (1996): averaged over all target functions, no learner beats any other. Worked on 3-bit functions by enumeration. A learner works only in worlds that match its bias.
* **Breiman's puzzle** (1995): why don't heavily parameterized networks overfit?
* Missing concepts: a measure of simplicity that does not depend on notation; a notion of a learner's bias as a formal object; a separation between the class of models and the procedure that selects among them.

## 3. The formalization — two rival answers

_The center of the exploration's history. Possibly split 3a/3b._

* **Solomonoff** (1964): weight every program that outputs the data by 2^(−length); predict with the mixture. Convergence: total prediction error is bounded by the complexity of the true source.
* **Gold** (1967): identification in the limit; what can't be learned from positive examples alone. Brief.
* **Vapnik–Chervonenkis** (1971) and **Valiant's PAC learning** (1984): guarantees from limiting the patterns a model class can fit (shattering, VC dimension). Worked: thresholds on a line shatter one point, not two.
* **Rissanen's minimum description length** (1978) as the computable compromise: compression as model selection.
* **Bias–variance** as the working practitioner's form of the working claim.
* Position to take: Solomonoff and VC are answers to different questions. Solomonoff asks what the ideal prior is. VC asks what a model class can guarantee whatever the prior. The working claim is VC's answer.
* What the formalization cost: the ideal is uncomputable, the guarantee is worst-case, and real learners sit between them.

## 4. The abstraction — generalization as a property of the procedure

_Possibly split 4a/4b._

* **Zhang et al. 2017**: random labels, and the end of capacity as the explanation.
* **Double descent** (Belkin et al. 2019): the interpolation threshold and the second descent. Runnable worked example: minimum-norm polynomial or random-feature regression on a few points, test error against degree/features.
* **Implicit bias**: among all exact fits, gradient descent from small initial weights finds a particular one (minimum norm; max margin, Soudry et al. 2018). Inductive bias moved from the hypothesis class to the optimization path.
* **Flat minima** (Hochreiter–Schmidhuber 1997; Keskar et al. 2017) and PAC-Bayes; the first non-vacuous bounds for deep networks (Dziugaite–Roy 2017).
* **Simplicity bias of the parameter-function map** (Valle-Pérez et al. 2019; Mingard et al. 2021): most parameter settings compute simple functions, so even random choice favors simplicity. The architecture implements a prior.
* **Inductive bias as symmetry**: convolution as translation invariance, attention and permutation; de Finetti's exchangeability as the symmetry that licenses induction. Link _what-is-symmetry.md_.
* **Singular learning theory** (Watanabe 2009): for models like neural networks, the effective complexity is the learning coefficient, not the parameter count. Conceptual only. Overlap with Emergence; keep to one page.

## 5. The payoff — does prediction training find the world?

_Before writing this stage: search for developments from 2025–26 on each thread below\._

* **The engineering lineage of "prediction implies understanding"**: Hutter Prize (2006) and AIXI; the sentiment neuron (Radford et al. 2017); GPT-2 and unsupervised multitask learning (2019); scaling-law evidence through Chinchilla and beyond.
* **Prediction is compression**: log loss equals code length (link _what-is-information.md_, _shannon-and-information.md_); "Language Modeling Is Compression" (Delétang et al. 2024).
* **World models or shortcuts**: Othello-GPT and linear board-state probes (Li et al. 2023; Nanda); Vafa et al. 2024 on incoherent implicit world models (taxi routes); grokking's mechanism for modular arithmetic.
* **The gap stated precisely**: what Solomonoff guarantees, what a finite network trained by gradient descent gets, and which bridge (simplicity bias, compression, SLT) carries the most weight.
* Search targets for 2025–26: theory of generalization in LLMs; simplicity bias and Solomonoff-style accounts of transformers; world-model probing results and critiques; compression and predictive coding in language models.
* The endpoint question: was generality from next-token prediction an accident, and if not, what is still unexplained?

***

## Side files (both to be written at the close; Fog keeps them in GitHub)

* **Solomonoff and the universal prior**: a plain-terms technical home for stage 3. Program-length priors, the mixture, the convergence bound, the invariance theorem's constant, AIXI, and computable approximations.
* **Compression is prediction**: Shannon's game, arithmetic coding, log loss as code length, MDL, the Hutter Prize, and LLMs as compressors. Doubles as raw material for the post.

## Planned scripts (pure Python)

* _nfl.py_: no-free-lunch by enumeration over all boolean functions on 3 bits.
* _shatter.py_: shattering for thresholds and intervals; the counting bound with real numbers.
* _solomonoff.py_: a toy universal predictor over a tiny program language.
* _double\_descent.py_: minimum-norm regression, test error against model size.

## Threads to carry in

* **What probability is when nothing is random**: de Finetti's exchangeability as the license for induction.
* **Unprovable of the individual, true of almost all**: no-free-lunch (almost all functions are unlearnable) and the counting bound.
* **Observation bounded by computation**: Solomonoff's ideal is uncomputable; every real learner is a computable approximation.
* **Symmetry as the source of a number**: inductive bias as invariance.
* **Equality and sameness**: Goodman's grue as a choice of which things count as the same.
* **The record** and **the copy**: training data as records; memorization as copying, generalization as compression.

## Threads to hand off

* **Emergence**: sudden abilities, grokking as a transition, SLT phase transitions, scaling laws as critical phenomena.
* **Causality**: prediction against intervention (a predictor need not know what happens under a do-operation).
* **Proof**: none expected.

## Guardrails

* Conceptual level wherever possible; worked examples in plain terms with small numbers; runnable scripts where they help.
* Cite _what-is-randomness.md_ for Laplace, de Finetti, Kolmogorov complexity, and the invariance theorem; cite _what-is-information.md_ for log loss and relative entropy; no second pass.
* The LLM material carries a risk of hype in both directions: every claim about model behavior is sourced and dated, and the 2025–26 search decides what stands.
* Claude is an instance of the systems studied; its sense of how it works is not evidence.
* Project files in use: zhang2017.pdf, belkin2019.pdf, solomonoff1964.pdf (stages 3–4); wei2022.pdf and schaeffer2023.pdf are held for Emergence.
