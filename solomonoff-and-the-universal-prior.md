# Solomonoff and the Universal Prior

*Side file to* what-is-induction.md, *written at the close of the Induction exploration, October 2026. The technical home for stage 3a, in plain terms. Runnable companion:* solomonoff.py.

---

## 1. The problem Solomonoff set himself

Ray Solomonoff (1926–2009) attended the 1956 Dartmouth workshop that named artificial intelligence. He wanted a single formal answer to the question every induction problem asks: given everything seen so far, how probable is each continuation? His reduction, in "A Formal Theory of Inductive Inference" (*Information and Control* 7, 1964, Parts I and II; first circulated in Zator technical reports, 1960–62), was to treat every induction problem as the extrapolation of a long string of symbols. Weather, language, physics, anything: write the evidence as a string T and ask for the probability that a comes next.

Solomonoff was candid about the paper's status. Section 3 presents four "ostensibly different" models with heuristic arguments that three agree, and he warns that "no theorems or rigorous proofs are presented." The rigour came from Levin (1970s) and from Solomonoff himself in 1978.

He also explicitly evaluated the theory against intuition. The strongest evidence, he wrote, would be "the application of the methods to specific problems and comparison of the results with intuitive evaluations." Part II derives Laplace's rule of succession for a Bernoulli sequence as one such check.

---

## 2. Programs as hypotheses

**The move.** A hypothesis about a string is a program that prints it. Fix a universal machine, a computer that can run any program. Every program that outputs a string beginning with T is a hypothesis consistent with T.

**The weight.** Give each program p the weight 2^(−|p|), where |p| is its length in bits. Each extra bit halves the weight.

**Why it adds up.** For the weights to behave like probabilities, they mustn't sum to more than 1. That requires a *prefix-free* code: no program may be the beginning of another, so the machine knows where a program ends. The Kraft inequality then guarantees Σ 2^(−|p|) ≤ 1.

*Worked:* the prefix-free code {0, 10, 110, 111} has lengths 1, 2, 3, 3, and ½ + ¼ + ⅛ + ⅛ = 1. Add 11 and it is no longer prefix-free (11 begins 110 and 111), and the sum would be 1¼.

In *solomonoff.py*, numbers are written with a self-delimiting code of 2⌊log₂ n⌋ + 1 bits (Elias gamma: the length in unary, then the bits). The program "repeat 01" costs 1 bit to say which family, 3 bits for the length 2, and 2 bits for the pattern: 6 bits in all.

**Short or many.** A string's prior probability is the sum over *all* programs that print it, not just the shortest. Solomonoff (1964, §2): strings with "short and/or numerous" descriptions get high prior probability. "The assignment of high a priori probabilities to sequences with many descriptions corresponds to a feeling that if an occurrence has many possible causes, then it is more likely." Levin's coding theorem later showed the two are nearly the same: the total weight of a string's programs is within a constant factor of 2^(−K), where K is the length of the shortest.

**The monkey (§3.3).** An equivalent picture: feed the universal machine a stream of fair coin flips as its program and watch what it prints. A string with a short program is likely, because the coin only has to land right a few times. Solomonoff connects this to the principle of insufficient reason: treat all inputs of a given length as equally likely, because nothing distinguishes them.

*Position:* this is the decisive move. Laplace applied indifference to outcomes and Bertrand's paradox broke it, since "uniform" depended on the parametrization (*what-is-randomness.md* §3). Solomonoff applies indifference to programs, which are discrete, and a change of machine shifts every length by at most a constant. The arbitrariness is priced instead of unbounded.

---

## 3. The mixture

To predict the next symbol after T: take every program consistent with T, give each its weight, and let them vote on what comes next. Equivalently, P(a | T) = M(Ta) / M(T), where M(x) is the total weight of programs whose output begins with x.

*Worked by hand.* T = `0101`. Two survivors: "repeat 01" (6 bits, weight 1/64, predicts 0) and "repeat 01 four times, then 1s" (13 bits, weight 1/8192, predicts 1). P(next = 1) = (1/8192) / (1/64 + 1/8192) = 1/129 ≈ 0.008.

*Worked by program.* *solomonoff.py* lists all 63,700 programs of a tiny language with two families, "repeat pattern p" and "repeat p for n symbols, then repeat q" (the grue family):

```
after 0101               P(next=1) = 0.139   weight on switch (grue) programs = 0.3366
after 010101             P(next=1) = 0.023   weight on switch (grue) programs = 0.2365
after 0000               P(next=1) = 0.026   weight on switch (grue) programs = 0.1460
after 0000000000000000   P(next=1) = 0.001   weight on switch (grue) programs = 0.0615
after 01101              P(next=1) = 0.915   weight on switch (grue) programs = 0.2775
```

Most grue programs switch at some later point, so they agree with "repeat" about the very next symbol; that's why a third of the weight on grue programs yields only 0.139. Each longer run of agreement costs the switching hypotheses more bits (naming a later switch time takes more), so their weight decays without ever reaching zero. That is Hume's problem with a number on it.

**§3.4, all methods voting.** Solomonoff's fourth model mixes every computable probability-assigning method, weighted by complexity, and argues that on enough data the mixture does at least as well as any method one could propose. This is the form modern treatments use: M dominates every computable measure μ, in the sense M(x) ≥ 2^(−K(μ))·μ(x) for all x.

---

## 4. The convergence theorem

**Statement (Solomonoff 1978, "Complexity-Based Induction Systems," *IEEE Trans. Inf. Theory*).** If the data come from any computable probability distribution μ, the mixture's total expected squared prediction error, summed over all time, is finite and bounded by a constant times K(μ), the length of the shortest program for μ. For a binary alphabet the constant is (ln 2)/2. The mixture makes a bounded number of real mistakes and then essentially stops.

**Deterministic case, in four lines.**
1. The true program is one of the voters, and it is never wrong.
2. When the mixture puts probability q on what actually happens, every voter that disagreed is eliminated, so the true program's share is multiplied by 1/q, that is by 2ˢ for s = −log₂ q bits of surprise.
3. Its share starts at 2^(−L), with L its length, and can never exceed 1.
4. So total surprise, added up over all time, is at most L bits.

*solomonoff.py* checks it over 40 symbols:

```
source R(0)         program length  3 bits   total surprise =  2.01 bits
source R(011)       program length  7 bits   total surprise =  5.84 bits
source R(01101)     program length 11 bits   total surprise =  9.84 bits
source S(0,12,1)    program length 12 bits   total surprise = 11.09 bits
```

The last source is grue (zeros, then ones from symbol 12). The mixture pays to learn the switch, but no more than the switch costs to describe.

**Stochastic case.** The same argument works with log loss: the mixture's cumulative log loss exceeds the true source's by at most −log₂ of the source's prior weight, about K(μ) bits. This is the bound that becomes, in *compress.py*, "the mixture pays at most log₂ 6 bits over the best of six models."

*Position:* this is the precise content of "a perfect predictor must model the world," and it says less than it sounds like. (1) It needs a computable source and an uncomputable predictor. (2) "Models" means predicts the outputs as well as the source's shortest program. Two programs with identical outputs on the data seen are indistinguishable, so the mixture learns what will be seen, not why. Vafa et al.'s orbit model (*what-is-induction.md* §6) is this warning come true.

---

## 5. The invariance theorem and its constant

**Statement.** For two universal machines U and V there is a constant c, the length of a program by which U simulates V, such that K_U(x) ≤ K_V(x) + c for every x. Solomonoff gives the argument informally in §3.1.2.3: M₁ can always code anything by using M₂'s code prefixed by the simulation instructions. Since weights are 2^(−length), changing machines changes every prior probability by at most a factor 2^c.

**What it buys.** For a long enough string the choice of machine stops mattering: a fixed 2^c is swamped once the data's own regularities are worth many more bits. Solomonoff suggested LISP as a sensible reference machine.

**What it doesn't.** For any finite amount of data, c can decide everything. A machine whose primitives are grue and bleen makes grue the short hypothesis. Leike and Hutter ("Bad Universal Priors and Notions of Optimality," 2015) showed that a badly chosen reference machine can make the agent built on this prior (AIXI) behave arbitrarily badly for as long as you like. Raatikainen's objection to Chaitin's constant (*what-is-randomness.md* §5) applies here too.

*Position:* invariance turns Goodman's paradox into a price, and the price is real. "Simplicity" is objective only asymptotically and only up to a translation cost; for finite data it remains a choice of language.

---

## 6. Uncomputability and the approximations

**Why it can't be computed.** Listing "every program that prints T" requires knowing which programs halt. M is *lower semicomputable*: run all programs in parallel and add weight as they print matching output, and the estimate rises toward M without ever certifying it has arrived. It is the same object as Chaitin's Ω (the total weight of halting programs), asked a different question. Solomonoff saw the problem (§3.1.1.1) and conjectured the whole expression is "not effectively computable."

**His remedy, and its descendants.**
- *Time limits* (§3.1.2.1): count only programs that finish within r steps, then let r grow.
- *Levin search* (1973): run all programs, each getting time in proportion to 2^(−length); finds a solution within a constant factor of the fastest program, the constant being exponential in that program's length.
- *The speed prior* (Schmidhuber 2002): weight programs by length and running time, making the prior computable.
- *Context-tree weighting and its relatives*: exact Bayesian mixtures over restricted families (variable-order Markov models), the practical core of strong compressors.
- *Learned universal predictors* (Grau-Moya et al., ICML 2024): train networks on outputs of random programs run on a universal machine (a Brainfuck variant); they approach Solomonoff-style prediction, matching the optimal CTW predictor on Markov sources, with transformers transferring best to formal-language tasks. Theory: under unlimited data and capacity, such training converges to Solomonoff variants.
- *Robustness of approximations* (Li–Teng, arXiv 2610.29289, 2026; abstract only): an approximation within η (in KL) of the mixture keeps bounded error on average under the prior, but its excess error in an environment of prior weight w can be as large as Θ(η/w). Approximate universal predictors are reliable where the prior puts weight and fragile where it doesn't.

*Position:* every real learner is a computable approximation to M with its own reference language, and the interesting question is never "is it Solomonoff?" but "where does its language differ from a sensible universal one?" Parity for gradient-trained networks (*what-is-induction.md* §5) and Newton for the orbit transformer are two answers.

---

## 7. AIXI

Hutter (2000; *Universal Artificial Intelligence*, 2005) combined Solomonoff's mixture over environments with expected-reward maximization: AIXI acts to maximize reward as predicted by the mixture. It is the theoretical template of an ideal agent and is incomputable. Approximations (AIXItl; Monte Carlo AIXI, Veness et al. 2011, which learned to play small games such as Pac-Man variants) are tractable only on toy problems. Leike–Hutter (2015): AIXI's optimality claims depend on the reference machine. *Position:* AIXI shows prediction is not enough for action; choosing well needs a theory of what interventions do, which is *Causality*'s subject, and a mixture over environments learned by observation does not supply it for free.

---

## 8. Solomonoff, Kolmogorov, Chaitin, Rissanen

| | Question | Object | Status |
|---|---|---|---|
| Solomonoff (1964) | What comes next? | the mixture M | uncomputable; optimal prediction |
| Kolmogorov (1965) | How much information is in this string? | K(x) | uncomputable; randomness as incompressibility |
| Chaitin (1966, 1975) | What can a formal system prove about K? | Ω | incompleteness as the generic case |
| Rissanen (1978) | Which model in my class? | two-part and prequential code length | computable; needs a chosen class |

*Position:* one measure read in four directions. Solomonoff and Kolmogorov meet in Levin's coding theorem (−log₂ M(x) ≈ K(x)); Chaitin is the same sum asked about halting; Rissanen is the same accounting restricted to a class you choose, which is what makes it usable.

---

## 9. Positions taken

- §3.3's indifference over programs, not outcomes, is the decisive move; it turns Bertrand's unbounded arbitrariness into a bounded constant.
- Solomonoff and Kolmogorov found one measure from opposite directions; induction and randomness are its two readings.
- "A perfect predictor models the world" is a theorem about outputs, conditional on a computable world and an uncomputable predictor; it promises nothing about mechanism.
- Invariance makes simplicity objective only asymptotically and up to a translation cost; for finite data it remains a choice of language.
- Every real learner is a computable approximation with its own reference language; the questions worth asking are where its language departs from a sensible universal one, and how badly approximation hurts in the tails.
- AIXI shows prediction doesn't settle action.

---

## Suggested next steps

- In *solomonoff.py*, add a third family ("count up in binary") and see how many symbols of `0110111001011101111` the mixture needs before it predicts confidently.
- Change the family-selection bit so switch programs cost 1 bit less than repeat programs; measure how long the "grue-speaking" machine keeps its preference after `0000…`.
- Prove the Kraft inequality for a prefix-free code of three words by drawing the binary tree.
- Reading: Solomonoff (1964), Part I §§2–3 (project files); Solomonoff, "Complexity-Based Induction Systems" (1978); Li and Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, ch. 4–5; Hutter, *Universal Artificial Intelligence*, ch. 2–3; Rathmanner and Hutter, "A Philosophical Treatise of Universal Induction" (2011); Grau-Moya et al., "Learning Universal Predictors" (ICML 2024).
