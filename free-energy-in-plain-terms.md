# Free Energy in Plain Terms

_Side file to_ What Is Intelligence? _(stage 3a), written 2026-11-21 at Fog's request from the addendum to stage 3a. One example (a dark patch on the road: shadow or puddle), worked in bits, from the problem free energy solves to perception, learning, prediction errors, and the name. The bits-back argument is left to_ predictive-coding-and-free-energy.md. _Runnable companion:_ freeenergy.py. _Builds on_ compression-is-prediction.md _§1 (log loss = code length) and_ what-is-entropy.md _(Gibbs, Jaynes: statistical mechanics as inference)._

***

## 0. What it is not

Variational free energy is not energy in joules and has nothing to do with the brain's metabolism. It is a number of **bits**. It is called free energy because its formula has the same shape as free energy in thermodynamics (§7).

***

## 1. The problem: inference is a sum you can't do

A perceiver receives data (light on the retina) and wants the hidden **cause** (what is out there). This is Helmholtz's unconscious inference (_What Is Intelligence?_ stage 1).

**The example.** You see a dark patch on the road. It is a **shadow** or a **puddle**. Your model holds two kinds of knowledge:

| cause  | prior (how common) | likelihood (chance it looks like a dark patch) | joint (both together) |
| ------ | ------------------ | ---------------------------------------------- | --------------------- |
| shadow | 0.75               | 0.2                                            | 0.75 × 0.2 = **0.15** |
| puddle | 0.25               | 0.4                                            | 0.25 × 0.4 = **0.10** |

From the joint column:

* **Surprise.** p(dark patch) = 0.15 + 0.10 = **0.25**; −log₂ 0.25 = **2 bits**. By _compression-is-prediction.md_ §1, also the shortest code the model allows for this observation.
* **Posterior** (what caused it). Divide by the total: shadow 0.15/0.25 = **0.6**, puddle 0.10/0.25 = **0.4**.

Both need the **sum over all causes**. With two causes it is trivial. A real scene has astronomically many possible causes (every arrangement of surfaces, lights, objects), and neither a brain nor a computer can do that sum. **Exact inference is intractable.** Free energy is the workaround.

***

## 2. The workaround: guess, then score the guess

Hold a **guess** _q_, a probability for each cause. Score it with one number computed only from things you _can_ get: the guess, and the joint p(data, cause), which the model gives for any single cause without a sum.

> **F(q) = energy − entropy**

* **Energy:** the average, under the guess, of −log₂ p(data, cause): the bits needed to say "this cause happened and produced this data." Shadow: −log₂ 0.15 = 2.737 bits. Puddle: −log₂ 0.10 = 3.322 bits. A guess favouring cheap explanations has low energy.
* **Entropy:** how spread out the guess is, in bits. Certainty: 0. Fifty–fifty: 1. Spreading is rewarded.

Every guess, from _freeenergy.py_:

```
q(shadow)   energy   entropy   F = E - H   F - surprise
  1.0       2.737     0.000     2.737        0.737
  0.9       2.795     0.469     2.326        0.326
  0.8       2.854     0.722     2.132        0.132
  0.7       2.912     0.881     2.031        0.031
  0.6       2.971     0.971     2.000        0.000   <- the true posterior
  0.5       3.029     1.000     2.029        0.029
  0.4       3.088     0.971     2.117        0.117
  0.2       3.205     0.722     2.483        0.483
  0.0       3.322     0.000     3.322        1.322
```

***

## 3. Three facts, true for every model

1. **F never falls below the surprise** (2 bits): a computable upper bound on a quantity you can't compute.
2. **F is lowest at the true posterior**, where it equals the surprise. Lowering F by adjusting the guess _is_ inference, reached without the impossible sum.
3. **The gap is the guess's error**, in bits: the relative entropy KL(q ‖ posterior) (_what-is-information.md_ §4). Certain-shadow costs 0.737 extra bits; certain-puddle 1.322.

So:

> **F = surprise + error of the guess** = −log₂ p(data) + KL(q ‖ posterior)

***

## 4. Why energy and entropy pull against each other

Energy alone picks the cheapest single explanation and commits fully ("shadow, 100%," F = 2.737): jumping to a conclusion. Entropy rewards keeping alternatives open. The minimum balances them: **commit as far as the evidence supports, and no further.** Too certain or too vague both cost bits.

As a code: naming one cause and then the data costs 2.737 bits at best, not 2. The 0.737 vanishes only if the choice of which cause to name is itself spread according to the posterior; why that spread can be recovered as real saved bits is the bits-back argument (_predictive-coding-and-free-energy.md_).

***

## 5. Perception, learning, action

F depends on things you can change, and each change is a different activity:

* **Change the guess _q_** (model fixed): **perception**. "Probably a shadow, maybe a puddle."
* **Change the model** (priors, likelihoods): **learning**. If dark patches keep turning out to be puddles, raise the puddle prior; future observations become less surprising, so their code shortens. Compression in Grant Sanderson's ordinary sense.
* **Change the data** (move the eyes, step closer): **action**. Friston's boldest claim is that action also lowers F; tested in _What Is Intelligence?_ stage 4.

***

## 6. Prediction errors

For numerical data with Gaussian noise, the energy term is the squared prediction error scaled by the noise. If the model predicts a value μ with noise σ, seeing _x_ costs (x − μ)² / 2σ² nats, plus a constant. In bits, from _freeenergy.py_:

```
prediction error      1      2      4
sigma 1 (bright)    0.72   2.89  11.54  bits
sigma 4 (dim)       0.05   0.18   0.72  bits
```

So "minimize free energy" becomes **"minimize prediction errors, each weighted by how reliable its signal is."** That is why the predictive-coding circuits of stage 3a (residuals up, predictions down) count as minimizing F, and the weighting is Srinivasan–Laughlin–Dubs: in dim light an error of 4 costs 0.72 bits, barely worth correcting, so the retina averages more widely (_residual.py_: best predictor width 2 → 8 pixels as noise grows 32-fold). Friston calls the weighting _precision_, 1/σ²; in his account, adjusting precision is attention (stage 4).

***

## 7. Where the name comes from

Thermodynamic (Helmholtz) free energy is F = U − TS: average energy minus temperature times entropy. At fixed temperature a system settles into the distribution minimizing it, the Boltzmann distribution, with probability ∝ e^(−E). Define a cause's "energy" as −log p(data, cause), set the temperature to 1, and the same minimization picks out the posterior. Same mathematics, different reading.

Feynman used the variational form as an approximation method in physics; Hinton and colleagues brought it into machine learning (Hinton–van Camp 1993; Hinton–Zemel 1994; Dayan–Hinton–Neal–Zemel's Helmholtz machine 1995). _what-is-entropy.md_ covers the Gibbs–Jaynes reading of statistical mechanics as inference, which is the reading used here. The Helmholtz of "Helmholtz free energy" is the Helmholtz of unconscious inference; the 1995 machine was named with both in mind.

***

## 8. In one sentence

Free energy is a computable upper bound, in bits, on how surprising your senses are under your model; lowering it by adjusting your guess about causes is perception, by adjusting the model is learning, and both are compression.

***

## 9. Positions taken

* Nothing in free energy needs the word "energy": it is a description length with a physicist's name, and reading it as bits is what lets the free-energy principle be stated operationally.
* Minimizing F over the guess is exact inference when the guess can reach the posterior and the best available approximation when it can't; the gap is measured in bits.
* The entropy term is the formal content of "don't jump to conclusions."
* For Gaussian models, minimizing F is precision-weighted prediction-error minimization, which is the bridge from the formula to the circuits of stage 3a.
* For perception and learning, the free-energy principle is a restatement of predictive coding; only its claim about action is new (stage 4).

***

## Suggested next steps

* Change the likelihoods in _freeenergy.py_ so a shadow and a puddle look equally dark; the posterior should equal the prior, and F's minimum should move to q(shadow) = 0.75.
* Add a third cause (an oil stain, prior 0.05, likelihood 0.9) and rerun; note how much F the two-cause guess now wastes.
* Learning by hand: after ten dark patches, seven of them puddles, update the puddle prior (Laplace's rule, _what-is-randomness.md_ §3) and recompute the surprise of the next patch.
* Reading: Bogacz, "A tutorial on the free-energy framework for modelling perception and learning" (_J. Math. Psychology_, 2017), the most plain-terms technical introduction; MacKay, _Information Theory, Inference, and Learning Algorithms_, ch. 33 (variational methods).
