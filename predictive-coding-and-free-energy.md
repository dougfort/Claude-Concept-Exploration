# Predictive Coding and the Free-Energy Principle in Plain Terms

_Side file to_ what-is-intelligence.md, _written at the close of the Intelligence exploration, November 2026. From residual coding to Rao–Ballard to the bits-back argument, then expected free energy and where the evidence stood in November 2026. Operational statements only, by steering. The basics of free energy (the shadow-or-puddle example; F = surprise + error of the guess; precision) are in_ free-energy-in-plain-terms.md _and are cited, not repeated. Runnable companions:_ residual.py, freeenergy.py, curiosity.py.

***

## 1. Residual coding

Send what the prediction got wrong, not the signal. On the stage-1 row of eight pixels, raw costs 64 bits and residuals 41 (_residual.py_ Part 1). On a 4,096-pixel synthetic line, bright: 5.98 → 2.48 bits per pixel; dim: 7.41 → 5.24 (Part 2). Noise can't be predicted, so it can't be compressed. This is Attneave (1954) and Barlow (1961) in one operation.

***

## 2. The retina: Srinivasan, Laughlin and Dubs (1982)

Lateral inhibition reinterpreted: the surround predicts the centre from its neighbours and subtracts. Coding theory predicts the surround should widen as noise grows, and it does (_residual.py_ Part 3: best predictor width 2 → 8 pixels as noise grows 32-fold; physiology: surrounds weaken and spread in dim light).

A centre-surround cell responds only where slope changes: on the clean line, at 0.7% of pixels (Part 4), negative at the foot of a ramp, where Mach saw his dark band. **Caveat:** the same cell gives a large ± pair at a sharp step, where people generally see no Mach band. The retina's code is not the percept.

***

## 3. The cortex: sparse coding and Rao–Ballard

* **Olshausen–Field (1996):** ask for a dictionary that rebuilds natural-image patches accurately using few active entries per patch. The answer looks like V1 simple cells (small, oriented edge detectors). The objective is a two-part code length: reconstruction error plus the cost of naming the active entries. Sparsity is also cheap in energy (Laughlin et al. 1998; _What Is Intelligence?_ 4a).
* **Rao–Ballard (1999):** each level predicts the level below and sends the prediction down; each level sends up only the residual. Explains **end-stopping**: a V1 cell fires less for a long bar than a short one, because long lines are what higher levels predict in natural images.

***

## 4. Why free energy is a real code length: bits-back

_free-energy-in-plain-terms.md_ §4 showed that naming one cause and then the data costs at least 2.737 bits for the dark patch, more than its 2-bit surprise. The **bits-back argument** (Hinton–van Camp 1993; Frey–Hinton) shows how a sender actually achieves the free energy F.

**The trick.** The sender has the data and some other message waiting to be sent (any random-looking bits). To choose which cause to name, instead of always naming the best one, the sender **uses bits of the other message as the random choice**, picking each cause with probability q(cause). Then:

1. Send the cause: −log₂ p(cause) bits.
2. Send the data given the cause: −log₂ p(data | cause) bits.
3. The receiver decodes both, recomputes q from the data, and so recovers which random bits drove the choice: −log₂ q(cause) bits of the other message arrive **for free**.

Net cost = −log₂ p(cause) − log₂ p(data | cause) + log₂ q(cause), and its average over the choice is exactly F.

**Worked, with the exact posterior** (q = 0.6 shadow, 0.4 puddle):

| cause chosen | name cause | data given cause | bits back | net       |
| ------------ | ---------- | ---------------- | --------- | --------- |
| shadow (60%) | 0.415      | 2.322            | 0.737     | **2.000** |
| puddle (40%) | 2.000      | 1.322            | 1.322     | **2.000** |

Every choice nets exactly **2 bits**, the surprise. With the exact posterior there is no waste at all, whichever cause the random bits pick.

**With a worse guess** (q = 0.8 shadow): shadow nets 0.415 + 2.322 − 0.322 = 2.415, puddle 2.000 + 1.322 − 2.322 = 1.000; the average is **2.132**, which is F(0.8) in the free-energy table. **With certainty** (q = 1.0 shadow) nothing comes back and the cost is **2.737**.

**Position:** bits-back is why "minimize free energy" is literally "minimize the length of a real message," not a metaphor. It is also the clearest reason the entropy term in F rewards keeping alternatives open: a spread-out guess pays you back.

***

## 5. The free-energy principle, operationally

Friston (2005, 2010): the brain minimizes variational free energy.

| claim                                 | operational content                                                                                   | status (Nov. 2026)                                                                                                                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| perception minimizes F over the guess | approximate Bayesian inference; for Gaussian models, precision-weighted prediction-error minimization | well supported at the sensory periphery                                                                                                                                                    |
| learning minimizes F over the model   | the model shortens the code for its data                                                              | a restatement of learning by maximum likelihood / MDL                                                                                                                                      |
| errors go up, predictions go down     | dedicated prediction-error cells; feedforward residuals                                               | error cells found (signed, precision-weighted, 2025–26 preprints); predictive **suppression** limited (OpenScope multi-area study: predictable responses dominate in over half of neurons) |
| precision is attention                | gain on error signals set by their reliability                                                        | consistent with data; not distinctive to the theory                                                                                                                                        |
| action minimizes expected free energy | expected utility (preferences as log-probabilities) minus information gain                            | see §6                                                                                                                                                                                     |

_Position:_ for perception and learning, the principle is predictive coding with a physicist's name. Its distinctive claims are about cortical architecture (mixed evidence) and action (§6).

***

## 6. Expected free energy

For choosing actions, active inference scores each plan by

> **G = expected cost of outcomes under preferences − expected information gain about hidden causes.**

_curiosity.py_ Part 2, the dark patch while driving (P(puddle) = 0.4; preferences fine 0.90, delay 0.09, skid 0.01):

```
policy                    cost   info gain      G
drive on                 2.749     0.000     2.749
slow down                3.474     0.000     3.474
look closer, then act    1.807     0.512     1.294
```

With equal preferences, looking closer still wins on information alone (G 1.073 against 1.585): curiosity.

**Three operational points.**

1. **Preferences are a goal.** A distribution over the outcomes you _want_ is not a belief about what _will_ happen; calling it a prior relabels a goal.
2. **The information term is a design choice.** Millidge, Tschantz and Buckley (2021) showed that exploration does not follow directly from minimizing free energy into the future. Remove the preferences and active inference becomes optimal Bayesian experimental design.
3. **The dark room.** Minimizing surprise alone favours a dark room where nothing happens (_curiosity.py_ Part 1: a comfort-seeker spends 92–93% of its time on the constant stream). Active inference escapes through preferences and the information term, that is, through points 1 and 2.

**Evidence.** On human choice tasks, active inference beats reinforcement-learning models without directed exploration where people explore to reduce uncertainty (Gijsen et al. 2022: better on two of four datasets, similar on the rest; about half of participants sensitive to information gain; Zhang et al., _eLife_ 2025). People also monitor learning progress (Ten et al. 2021).

_Position:_ the evidence supports information-directed exploration in people, not the free-energy principle as such; the fair comparison is against reinforcement learning _with_ an exploration bonus.

***

## 7. Positions taken

* Predictive coding is real at the periphery; the cortical middle is not a pure residual coder (limited predictive suppression; genuine prediction errors may arise in prefrontal cortex).
* Sparse coding is economical before it is short.
* Bits-back makes free energy the length of a real message; with the exact posterior every choice nets the surprise exactly.
* For perception and learning, the free-energy principle restates predictive coding and MDL.
* Operationally, active inference is expected utility plus an information bonus, with utility called a prior; its curiosity is a design choice, and its empirical support is support for information-directed exploration.

***

## Suggested next steps

* Run _freeenergy.py_ with q = 0.8 and check the bits-back table above by hand.
* In _residual.py_, replace "previous pixel" with "average of the left and right neighbours" for coding (not just display) and see why a decoder can't use it: the right neighbour hasn't arrived yet. That is why the brain needs predictions from higher levels, not just neighbours.
* In _curiosity.py_, add a reinforcement-learning agent with an exploration bonus (an upper-confidence rule) to Part 2 and compare its choices with expected free energy.
* Reading: Bogacz, "A tutorial on the free-energy framework" (_J. Math. Psych._, 2017); Rao and Ballard (_Nature Neuroscience_, 1999); Hinton and van Camp (COLT 1993); Millidge, Tschantz and Buckley, "Whence the expected free energy?" (_Neural Computation_, 2021); Aizenbud et al., "Neural mechanisms of predictive processing: a collaborative community experiment through the OpenScope program" (2025).
