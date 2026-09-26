# Shannon and the Measure of Information

*Side-quest notes, September 2026. How an engineering theory with no physics in it arrived at Gibbs's formula, and who knew.*

---

## 1. The telegraph lineage

Information theory grew out of telegraphy — Heaviside's world in the wave notes. The practical question: how much traffic can a line carry?

- **Nyquist (1924):** the speed at which a line transmits "intelligence" goes as the logarithm of the number of distinguishable signal levels.
- **Hartley (1928):** made it a definition. The information in a message is H = n log s: n symbols, each chosen from s possibilities. And the move that defines the field: eliminate "psychological factors." What a message means is irrelevant; what matters is how many messages it *could* have been.

Hartley's measure is log W — the logarithm of the number of equally likely alternatives. It is Boltzmann's 1877 formula, arrived at with no knowledge of Boltzmann, and with the same defect: it can't handle unequal probabilities. E and Z are not equally likely, and treating them so wastes capacity. Morse knew this in practice — he set code lengths by counting type in a printer's case — but there was no theory.

---

## 2. Shannon's route

- **1937:** master's thesis showing Boolean algebra describes relay circuits (belongs to the *Computation* arc).
- **1939:** letter to Vannevar Bush sketching a general theory of the "transmission of intelligence."
- **1941–45, Bell Labs:** war work on fire control and cryptography, including the security analysis of SIGSALY, the encrypted voice link between Roosevelt and Churchill.
- **1945:** classified memo on cryptography (published 1949 as "Communication Theory of Secrecy Systems"). It already contains the entropy measure, redundancy, and the proof that the one-time pad is perfectly secure.

Cryptography forces the probabilistic view. A cipher is a channel whose "noise" is deliberate; the codebreaker works by exploiting the statistical structure of language; and how much a ciphertext reveals depends on *what the interceptor already knows*. Conditional, observer-relative uncertainty was present from the start. Shannon said later the two subjects were too close to separate.

Turing visited Bell Labs in 1943 to inspect SIGSALY; the two met regularly and talked about thinking machines, not cryptography, which neither was cleared to discuss with the other.

---

## 3. The 1948 paper

"A Mathematical Theory of Communication." What it did that Hartley couldn't:

**The source is a stochastic process.** English modelled as a Markov chain, with printed successive approximations — random letters, then correct letter frequencies, then correct pair frequencies, and so on — each looking more like English. (Markov himself had done the vowel–consonant statistics of *Eugene Onegin* in 1913.) Result: English is roughly half redundant; Shannon's 1951 letter-guessing experiments pushed the estimate higher.

**The uniqueness theorem.** Require a measure of uncertainty that is continuous, grows with the number of equally likely options, and is consistent when a choice is broken into stages. Exactly one function qualifies:

H = −Σ p log p.

With log base 2 the unit is the bit (Tukey's word). A fair coin: 1 bit. A coin with p = 0.9: about 0.47 bits — most tosses tell you little.

**The source coding theorem.** H is the minimum average number of bits per symbol in any faithful encoding — equivalently, the expected number of yes/no questions needed to identify the outcome. H is not a plausible index; it is the answer to a concrete question.

**The noisy channel theorem.** Engineers assumed noise forced a smooth trade-off: more reliability, lower rate, all the way to zero. Shannon proved every channel has a capacity C, and at any rate below C the error probability can be made arbitrarily small. For a band-limited channel with Gaussian noise, C = W log₂(1 + S/N). The proof uses random codes and is non-constructive; codes approaching the limit in practice took until the 1990s.

**Conditional entropy and mutual information.**

- H(X|Y): the uncertainty remaining in X once Y is known.
- I(X;Y) = H(X) − H(X|Y): how much knowing Y reduces uncertainty about X. Symmetric in X and Y. Channel capacity is its maximum over input distributions.

Mutual information is the tool the demon needs: the demon's record of the molecule is a correlation of exactly this kind, and the work it can extract is bounded by kT times it (*what-is-entropy.md*, §5).

---

## 4. What he knew about the physics

Enough to recognize the formula. The paper says the form of H will be recognized from statistical mechanics, cites Tolman's textbook, and names Boltzmann's H-theorem — the usual explanation for the letter. It claims nothing further.

Others were readier:
- **Wiener** reached the same measure independently through wartime prediction theory and asserted the physical identity outright (*Cybernetics*, 1948).
- **Brillouin** (early 1950s): the "negentropy principle of information."
- **Jaynes** (1957) supplied the actual argument.

Shannon's 1956 editorial "The Bandwagon" warns against stretching information theory into fields where it hadn't earned a place. He never took up thermodynamics himself. Other people connected him to it.

---

## 5. Von Neumann and Szilard

The story: von Neumann advised Shannon to call the quantity "entropy" — partly because the formula already had that name, partly because nobody understood the word, so he'd win arguments. It comes via Myron Tribus, who said Shannon told it to him in 1961; Shannon did not clearly confirm it later.

*Position:* whether or not the quip happened, von Neumann is the plausible channel, and the fact about him is more interesting than the anecdote. He was probably the one person alive who held both halves. He had put −Tr ρ log ρ into quantum mechanics (1927), and he was a close friend of Szilard, whose 1929 paper on Maxwell's demon had already argued that acquiring one binary piece of information carries an entropy cost of k ln 2. Von Neumann discusses that paper in his 1932 book.

So the physical link between information and entropy predates Shannon by nineteen years — made from the thermodynamic side, in German, in a paper apparently no one at Bell Labs had read.

---

## 6. One fact, found three times

The step from Hartley to Shannon is, in structure, the step from Boltzmann to Gibbs: from counting equal alternatives to weighting unequal ones. Shannon retraced it in a different subject.

| | Equal alternatives | Unequal alternatives |
|---|---|---|
| Physics | Boltzmann, S = k log W (1877) | Gibbs, −k ∫ ρ log ρ (1902) |
| Communication | Hartley, H = n log s (1928) | Shannon, −Σ p log p (1948) |

In between, Szilard (1929) — the only one who found it *as a bridge*.

*Position on "was it a coincidence?":* no. There is one mathematical fact — the unique additive measure of undetermined alternatives — and the logarithm is forced in each case by the same requirement, that independent parts add. Shannon built the theory of information with no physics in it; Szilard had found that physics requires such a theory; Jaynes and then Landauer are where the two meet. What Shannon added that physics lacked was the operational meaning (coding theorems) and the clean separation from meaning. What physics added that Shannon lacked was the price: kT ln 2 per bit forgotten.

---

## Suggested next steps

- Compute H for English letter frequencies (single letters, about 4.1 bits against log₂ 26 ≈ 4.7) and see redundancy appear at the first approximation.
- Build a Huffman code for a small skewed alphabet and check that the average length lands between H and H + 1.
- For a binary symmetric channel with flip probability ε, compute C = 1 − H(ε) and look at what it says at ε = 0.5.
- Verify I(X;Y) = H(X) + H(Y) − H(X,Y) on a 2×2 joint distribution, then apply it to the Szilard engine's memory and molecule.
- Reading: Shannon's 1948 paper itself (the first two sections are readable cold); Szilard (1929) in translation; Tribus and McIrvine, "Energy and Information" (1971), for the anecdote at its source.
