# Compression Is Prediction

*Side file to* what-is-induction.md, *written at the close of the Induction exploration, October 2026. Shannon's guessing game to arithmetic coding to MDL to language models as compressors. Doubles as raw material for the post planned after* Emergence. *Runnable companions:* shannon_game.py, compress.py, taxi.py.

---

## 1. The identity

**If a predictor gives probability p to the symbol that actually comes next, that symbol can be encoded in −log₂ p bits, and no code does better on average.** A whole message costs the sum of those amounts, its *log loss*, to within 2 bits. So:

> compressed size = total surprise of the predictor = log loss.

Better prediction *is* a smaller file. Not by analogy: the predictor's probabilities are the code. The rest of this file is that sentence's history and consequences.

The bits come from *what-is-information.md* §4: entropy is the average of −log₂ p under the true distribution; coding with the wrong model Q costs the cross-entropy, which exceeds the entropy by exactly the relative entropy D(P‖Q). Worked: true probabilities ½, ¼, ⅛, ⅛ coded as if uniform cost 2 bits a symbol instead of 1.75; the extra 0.25 bits is D(P‖uniform).

---

## 2. Shannon's twin (1951)

"Prediction and Entropy of Printed English" asked people to guess the next letter of a passage, then the next guess if wrong, recording how many guesses each letter took. From those counts Shannon bounded the entropy of English at roughly 0.6–1.3 bits per letter, against log₂ 27 ≈ 4.75 for blind guessing among letters and space.

The argument that matters: imagine an identical twin who, in any situation, would make exactly the same guesses. Send the twin only the guess numbers. The twin guesses in its own order and stops at the number you sent, so it recovers the text. The guess numbers are the text, re-encoded; a good predictor turns text into mostly 1s, which compresses well.

*Worked:* guess counts of 1 (seven times), 2 (twice), 4 (once) over ten letters have entropy 0.36 + 0.46 + 0.33 ≈ 1.16 bits per letter.

*shannon_game.py*: a predictor using the last two letters, learning as it reads, gives 3.54 bits per letter on the first half of a short paragraph and 3.23 on the second; the twin decodes exactly. The improvement from first half to second is induction in progress.

---

## 3. From guesses to bits: arithmetic coding

Guess numbers are a code, but not an efficient one. Arithmetic coding (Rissanen 1976; Pasco 1976; practical form Witten–Neal–Cleary 1987) turns probabilities directly into bits.

**The picture.** Start with the interval [0, 1). For each symbol, divide the current interval in proportion to the predictor's probabilities and keep the piece belonging to the symbol that occurred. At the end, send enough binary digits to name a point inside the final interval. An interval of width w needs about −log₂ w bits, and w is the product of the probabilities of the symbols that occurred.

*Worked:* alphabet {A, B} with P(A) = 0.75. Message AAB.
- A: [0, 0.75)
- A: [0, 0.5625)
- B: [0.421875, 0.5625), width 0.140625 = 0.75 × 0.75 × 0.25
- −log₂ 0.140625 ≈ 2.83 bits; send 0.0111₂ = 0.4375, which lies inside: 4 bits, within the 2-bit allowance.

The decoder runs the same predictor, narrows the same intervals, and reads off which piece the point falls in. The predictor can change its probabilities at every step, provided the decoder can do the same. That is what makes adaptive prediction and compression one machine.

Mazor, Morgan and Pass (arXiv 2610.11031, October 2026; abstract only, untested) prove a converse with the same 2-bit gap: next-token predictors and *monotone* (order-preserving) compressors can each be built from the other.

---

## 4. Adaptive models: Laplace in a compressor

Where do the probabilities come from? Count. After n observations in a context, with k of them a particular symbol, Laplace's rule gives (k + 1)/(n + 2) for two symbols (*what-is-randomness.md* §3); the Krichevsky–Trofimov rule adds ½ instead of 1 and is the standard in coding theory.

*compress.py* predicts each byte from the last k bytes for k = 0 to 5. When a long context has been seen too few times, it leans on the next-shorter context (back-off, the idea behind PPM, Cleary–Witten 1984). On 170 KB of English documentation text, in bits per byte (first 10% / whole):

```
order-0 context        4.613  4.847
order-1 context        3.757  3.861
order-2 context        3.077  3.025
order-3 context        2.788  2.527
order-4 context        2.741  2.395
order-5 context        2.752  2.392
mixture of all six     2.741  2.392
zlib (gzip's method)   2.851  2.593
bz2                    2.835  2.376
lzma (xz)              2.785  2.342
```

Three lessons:
1. **The forecaster is the compressor.** About sixty lines of next-byte counting beat gzip and roughly tie bz2; nothing in the program knows about compression except −log₂ p.
2. **Bias–variance appears inside a compressor.** On the first tenth, order 5 is worse than order 4: not enough data to fill the longer contexts. On the whole file, longer contexts pay. The best model depends on how much has been seen.
3. **Mixtures are cheap insurance.** Weighting six models by their track record costs at most log₂ 6 ≈ 2.6 bits over the best one for the whole file: Solomonoff's convergence bound with six programs (*solomonoff-and-the-universal-prior.md* §4).

**The road to the Hutter Prize.** Context mixing (Mahoney's PAQ series from 2002; Knoll's cmix) combines thousands of predictors, by now including small neural networks trained as they compress. The Hutter Prize (from 2006; 1 GB of Wikipedia since 2020, €500,000 pool) is won by such programs: the record is fx2-cmix (Orav and Knoll, September 2024), about 110.8 MB *including the decompressor*. Mahoney (1999) had proposed text compression as a test for AI; Hutter's prize put that proposal into practice.

---

## 5. Description length: two ways to count the model

Minimum description length (Rissanen 1978) asks for the shortest description of the data, model included. There are two ways to count the model.

**Two-part code.** Send the model, then the data coded with it. *Worked:* 1,000 bits with 900 zeros. Literal: 1,000 bits. "Biased coin, P(0) = 0.9": about ½ log₂ 1,000 ≈ 5 bits for the bias, plus 1,000 × H(0.1) ≈ 469 bits for the data, 474 in all. Memorize ("print exactly this"): about 1,000 bits of model and nothing for the data. Overfitting is paying for a model in bits you then fail to recover.

**Prequential (predictive sequential) code.** Never send the model. Predict each symbol with a model fitted to everything before it; the decoder refits the identical model as it decodes. *compress.py* is a prequential code: its sizes are complete, with nothing to add for the counts. Dawid (1984) named the idea; Blier and Ollivier ("The Description Length of Deep Learning Models," NeurIPS 2018) applied it to neural networks and found prequential codes far shorter than two-part codes for deep models.

*Position:* the prequential code is the right accounting for pretraining. A language model trained in a single pass predicts every batch before it trains on it, so the area under its training-loss curve is a valid compressed size of its corpus, with no weights sent. Memorization can't lower that number, since nothing is predicted after being seen. In single-pass training every training loss is a test loss.

---

## 6. Language models as compressors

**Delétang et al., "Language Modeling Is Compression" (ICLR 2024).** With arithmetic coding, Chinchilla 70B, trained mostly on text, compressed ImageNet image patches to 43.4% of raw size and LibriSpeech audio to 16.4%, beating PNG (58.5%) and FLAC (30.3%). The same paper does the honest two-part accounting: count the parameters and large models lose badly on a 1 GB file. Pretrained knowledge came from outside the file, which is why the Hutter Prize counts the decompressor.

**Compression and capability.** Huang et al. (2024): across 31 LLMs and 12 benchmarks, average benchmark score is almost linear in how well a model compresses held-out text. Xuyang et al. (2025), on code models: the relation is logarithmic, and the linear fit may be one stretch of the curve. The correlation stands; its shape is contested.

**Compression and generalization.** Lotfi et al. (ICML 2024): the first non-vacuous generalization bounds for pretrained LLMs (nearly a billion parameters), via a compression bound and a low-dimensional reparametrization (SubLoRA); larger models are *more* compressible and get *better* bounds. PAC-Bayes in plain terms: the generalization gap is bounded by roughly √(bits needed to describe the trained model beyond the prior / 2n). At n = 50,000: 1,000 bits → at most 8%, 5,000 bits → 19%, 52 million raw bits → vacuous.

---

## 7. Where the identity stops

**Compressible is not predictable, for an efficient learner.** If one-way functions exist, there are data generated by short programs that no efficient predictor can predict: encrypted text is short given the key and unpredictable without it. Mazor–Morgan–Pass connect this to their equivalence: monotonicity is needed exactly when one-way functions exist. *Position (from the abstract):* "compressible in principle" doesn't imply "predictable in practice"; cryptography lives in that gap, and so does the computational form of Hume's problem.

**Compression is not a world model.** A compressor scored on outputs can compress with a lookup where a mechanism would also do. *taxi.py*: a counting predictor on taxi rides predicts a legal next move 99.4% of the time on unseen rides, yet allows the same next moves from the same intersection only 21% of the time when histories differ, completes 13% of held-out rides, and fails 30% of familiar ones under 10% random detours; a learner with a map is perfect throughout. Vafa et al.: transformers trained on Manhattan shortest paths behave like the counting predictor, those trained on random walks like the map; a transformer predicting orbits with R² > 0.9999 implies a different, nonsensical force law per sample. *Position:* a learner builds a world model where the world model is the shortest description of its data. Compression explains why prediction training finds structure; it doesn't promise the structure is the mechanism.

**Compression is not intervention.** All the above scores what will be observed. What happens if you act (a detour, an experiment) is a further question, *Causality*'s.

---

## 8. Positions taken

- Prediction and compression are one act; log loss is code length, by identity.
- Laplace's rule is the first adaptive compressor; PPM and context mixing are its descendants.
- A mixture over models is cheap insurance with a bounded premium, Solomonoff's bound in miniature.
- Prequential coding is the right accounting for single-pass pretraining: the training curve is a compressed size of the corpus, and every training loss is a test loss.
- The compressions that explain generalization are of the trained model (PAC-Bayes), not of the model class.
- Compressible doesn't mean efficiently predictable (one-way functions), and compression doesn't mean mechanism (taxis, orbits).

---

## 9. Lines for the post

Raw material, not drafts.

- Shannon's twin: if I could guess every next letter you'd write, you'd only need to send me the letters I got wrong. That is what a compressor is, and what a language model is trained to be.
- "Predict the next word" sounds like autocomplete. Information theory says it is "compress everything ever written," and the two are the same instruction.
- The bet was public: Shannon in 1951, Solomonoff in 1964, a €50,000 prize for compressing Wikipedia in 2006, a paper titled "Language Models are Unsupervised Multitask Learners" in 2019. Whatever this was, it wasn't an accident.
- The honest mystery isn't that prediction produced generality. It's which parts of the world a compressor rebuilds as a map, and which it fakes with a lookup table, and we only find out by sending it on a detour.
- A model that predicted planets perfectly turned out to believe a different law of gravity for every solar system. Kepler without Newton, a hundred times over.
- (For after *Emergence*:) "accident" fails on the goal; "cosmic" is a claim about suddenness, and that is the other half of the story.

---

## Suggested next steps

- Run *compress.py* on your own prose and on a translation of the same text; compare bits per byte and the best context length.
- Add a word-level model to *compress.py* (predict the next byte from the current partial word) and mix it in; see what it buys.
- Code the AAB example above by hand for P(A) = 0.9; compare the bits with −log₂ of the product.
- Reading: Shannon, "Prediction and Entropy of Printed English" (1951); Witten, Neal and Cleary, "Arithmetic Coding for Data Compression" (CACM 1987); Grünwald, *The Minimum Description Length Principle* (2007), ch. 1–2; Blier and Ollivier (2018); Delétang et al. (2024); MacKay, *Information Theory, Inference, and Learning Algorithms*, ch. 4–6.
