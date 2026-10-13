# What Is Information?

_Notes from a conversation, October 2026. From the signet ring to Bacon's two typefaces to Hamming's syndrome to the qubit that can't be copied._

***

## 1. A working definition

**Information is distinguishability relative to a reference, held as a correlation between physical systems. Classical information is the copyable sector of that correlation: the states some interaction can copy, compare, and regenerate. Records are made of it, and making them requires three things information theory takes as given: a symmetry that supplies correlating dynamics, a composition rule that makes parts well defined, and a low-entropy gradient that supplies blanks.**

The first clause is relative entropy (Kullback–Leibler 1951) and mutual information. The second is no-cloning (Wootters–Zurek, Dieks 1982) and the GPT broadcasting theorem (Barnum–Barrett–Leifer–Wilce 2007). The third is the reconstructions (Hardy 2001; Chiribella–D'Ariano–Perinotti 2011; Masanes–Müller 2011) plus Landauer–Bennett and the Past Hypothesis.

Working claim broken by the genealogy: **information is the content of a message: what it says about something, independent of the physical carrier that holds it.** It fails three times: not content, not intrinsically about, not carrier-independent (§6).

Question carried from _Time_: **is information the record, and does the possibility of records explain itself or remain an input?** Answer: classical information is the record; the possibility of records remains an input, resolved into three (§6).

Distinctions worth keeping:

* **Measure vs. meaning.** Every successful measure moved meaning out of the message into whatever supplies the ensemble.
* **Flow vs. stock.** Shannon's entropy of a source is what a message delivers; Wiener's negentropy is what a state holds. Same transaction, opposite bookkeeping; both are D(P‖uniform).
* **Fisher vs. Shannon.** Information about a parameter vs. about an outcome; the same distinguishability at two scales (Fisher is the curvature of relative entropy).
* **Correlation vs. aboutness.** Mutual information is symmetric; aboutness has a direction, supplied by which system was prepared blank.
* **Copy vs. overwrite.** `y ^= x` into a blank is reversible and free; `y = x` over a used register erases a bit and costs kT ln 2.
* **Description vs. accessible information.** A qubit takes continuous parameters to describe and yields at most one bit (Holevo).
* **Classical sector vs. classical carrier.** "Classical" is the basis an interaction copies, not a kind of stuff.
* **Language vs. source.** Information is the clearest language for quantum theory without being its source.

Pattern: waves and symmetry began as intuitions, entropy as a formula, randomness as metaphysics, measurement as practice. Information began as a _word for forming_ (in-formare) and became a theory only by discarding what the word meant. (Position.)

***

## 2. The intuition — form, sign, message

_Telegraph lineage from Nyquist to Hartley in shannon-and-information.md §1._

**The word.** Aristotle's signet ring (_De Anima_ II.12): form received without matter, as wax takes the seal's impression without the gold. Cicero's _informatio_; scholastic information of the intellect; by Chaucer, something told. _Position:_ the ring is the first statement of carrier-independence and already contains its limit: the form passes unchanged, but only into a medium capable of the distinctions.

**The sign.** Augustine: natural signs (smoke for fire, no intent) and given signs (words, flags); the Stoic sound / sayable / object. _Position:_ the natural sign is the version physics keeps.

**The channel.** Aeschylus's beacon chain: one bit, all meaning in the prior agreement. Polybius's 5×5 torch alphabet (\~4.6 bits per signal) against Aeneas Tacticus's list of prearranged messages. _Position:_ Polybius made the decisive pre-modern move: the codebook moved from messages to symbols, so the channel could carry the unanticipated. Hartley's "eliminate psychological factors" is this move as a definition.

**The codebreaker.** Al-Kindi (9th century): frequency analysis. Worked: `PHHW PH KHUH DW VHYHQ`, H 7 of 17, H − E = 3, MEET ME HERE AT SEVEN. A substitution relabels symbols and leaves the histogram's shape unchanged. _Position:_ measure separated from meaning in practice, eleven centuries before Shannon; carrier-independence is what makes the attack work.

**The bit.** Bacon's biliteral cipher (1623): five binary choices per letter (2⁵ = 32 ≥ 24); H = aabbb, I = abaaa; any "twofold difference" will do (typefaces, bells, cannon). The clearest pre-modern statement of carrier-independence, with its first cost accounting (ten cover letters for two). Leibniz supplied the arithmetic, not the communication idea.

**Weighting.** Chappe's semaphore: 92 × 92 = 8,464 codebook entries per pair (\~13 bits). Morse–Vail frequency weighting. Worked: probabilities ½, ¼, ⅛, ⅛ with codes 0, 10, 110, 111 average 1.75 bits against 2 fixed, equal to the entropy. Morse is not prefix-free (E begins I) and needs gaps; Huffman (1952) made weighted prefix codes optimal.

**What the intuition contains.** (1) Information is content. (2) It is about something. (3) Any carrier will do, given enough distinctions. (4) Some messages are cheaper. The first three are the working claim; the fourth grows into the measure. Lacking: a quantity, and the receiver's set of alternatives as an object of study.

***

## 3. The dispute — meaning against measure

**Fisher (1922–25).** Information about a parameter: 1/(p(1−p)) per toss, additive; Cramér–Rao bounds the estimate's variance by its inverse. Worked: 10 tosses at p = 0.5 give 40 (spread ≈ 0.16); at p = 0.9, 111 (spread ≈ 0.095) while Shannon entropy per toss falls from 1 to 0.47 bits. The two measures move oppositely: a dull message can be a sensitive probe. Bridge: Fisher is the curvature of relative entropy; D(0.5‖0.6) ≈ 0.0294 bits vs. ½·I·Δp² ≈ 0.0289. _Position:_ Fisher and Shannon measure one structure, distinguishability among supplied alternatives, at two scales; the real dispute is both against anyone wanting information without a supplied space. Wootters (1981): statistical distance between quantum preparations equals Hilbert-space angle; Frieden (1998) overreaches.

**Shannon and Weaver.** Levels A (technical), B (semantic), C (effectiveness); only A formalized. _Position:_ Shannon didn't ignore meaning, he presupposed it in the choice of ensemble; every attempt at B is an attempt to say what fixes the ensemble.

**Wiener's sign.** Worked with the 0.9 coin: uncertainty 0.469 → 0, order 0.531 → 1; the change is 0.469 either way. _Position:_ Shannon measures a flow (what a source delivers), Wiener a stock (what a state holds); physics needs the stock (Brillouin, Szilard's memory, Bennett's blank tape).

**MacKay and the Macy conferences.** Structural (Gabor's logons), metrical (Fisher), selective (Shannon); meaning as the selective function on a receiver's repertoire of readiness. _Position:_ closest to the final answer; meaning is a relation between a message and a receiver.

**Bar-Hillel–Carnap (1952).** Semantic information as excluded state descriptions. Worked with p, q: tautology 0 bits, p∨q 0.415, p 1, p∧q 2, p∧¬p ∞ — the paradox. _Position:_ exclusion measures narrowing without a world to be correlated with; the missing ingredient is truth.

**Afterlife (capped).** Dretske: information as lawful correlation with probability 1; Floridi: veridicality. _Position:_ Dretske right about structure, wrong about the threshold (mutual information grades it); Floridi stipulates the answer into "true."

**Why unresolved.** Every measure was relative to an ensemble supplied by someone else: statistician, engineer, receiver, logician. Missing: the receiver's alternatives as a physical fact (the division); correlation as aboutness; the carrier as a physical system. _Position:_ dissolved, not won; clause 1 of the working claim breaks here.

***

## 4. The formalization — Shannon and Kolmogorov, and what each left out

_Shannon's theorems in shannon-and-information.md §3; Kolmogorov complexity in what-is-randomness.md §5._

**Hamming (1950).** Hamming(7,4): parity bits at 1, 2, 4, each checking positions with that index bit set. Worked: 1011 → 0110011; flip position 6 → checks fail as 110 = 6. A codeword is valid iff the XOR of the positions holding a 1 is zero; flip position k and the XOR becomes k (_hamming.py_). On a 1% channel: 3.9% bare vs. 0.2% coded, at rate 0.57 against capacity 0.92. The road to capacity: Reed–Solomon (1960), Gallager's LDPC (1960, forgotten), turbo (1993), LDPC rediscovered (1996), polar (Arıkan 2009; 5G control channels). _Position:_ Hamming's contribution is the syndrome, which reads the error and not the data; that is what makes quantum error correction possible.

**Data processing inequality.** I(X;Z) ≤ I(X;Y). Worked: two 10% hops, 0.531 → 0.320 bits. With 3-fold repetition: forwarding noise gives 8.6% error, regenerating at the repeater 5.4%. _Position:_ a record degrades unless regenerated, and regeneration is an irreversible decision with a Landauer price; digital information is information plus a standing commitment to erase noise.

**Relative entropy.** D(P‖Q) = Σ P log(P/Q): ≥ 0, asymmetric. Worked: wrong-model coding cost 2 − 1.75 = 0.25 bits = D(P‖uniform); D(fair‖0.9) ≈ 0.737, D(0.9‖fair) ≈ 0.531 (Stein: error ≈ 2^(−nD), ≈ 0.6% after 10 tosses); D(0.9‖uniform) = 0.531 = Wiener's order. Identities: entropy = log N − D(P‖uniform); mutual information = D(joint‖product); Fisher = curvature; F − F\_eq = kT·D(ρ‖ρ\_eq); Sagawa–Ueda's bound. Monotone under noisy maps (the second law, the data processing inequality); invariant under change of coordinates where differential entropy isn't (uniform \[0,1] → 0 bits, \[0,2] → 1 bit: Bertrand again). Quantum: Umegaki, Araki (_modular-theory.md_). _Position:_ relative entropy is the primitive; entropy is the special case relative to a chosen uniform reference; information is how distinguishable something is from what you expected.

**Rate–distortion (1959).** Fair bits, Hamming distortion: R(D) = 1 − H(D); 10% error tolerated → 0.531 bits per bit. _Position:_ meaning re-enters as the distortion measure someone supplies; a perceptual codec is a model of a receiver.

**Kolmogorov's bridge.** Expected K ≈ nH + O(log n) for computable sources. Worked with zlib: 1,000 zero bits → 12 bytes; 1,000 fair bits → 136 (larger than raw); 8,000 bits at p = 0.1 → 590 against Shannon's 469, the gap being wrong-model cost.

**What each left out.** Shannon: meaning, the individual. Kolmogorov: computability, resources. Both: the carrier. _Position:_ information became exact by becoming relative; every working measure is a comparison, never a property of a message alone.

***

## 5. The abstraction — the carrier enters

### Classical: aboutness as correlation (4a)

_Landauer, Bennett, the Szilard ledger in what-is-entropy.md §5; quantum Darwinism in what-is-measurement.md §4._

**"Information is physical"** (Landauer 1961, 1991). _Position:_ right and under-specified: a cost (erasure, proven and measured) and rules fixed by the carrier (tested in 4b).

**Mutual information as aboutness.** Worked: fire 10%, smoke 90% given fire, 5% otherwise: I = 0.266 bits; P(fire) from 10% to 67% on smoke, \~1% without. Dretske's threshold would give zero. Symmetric: the fire is as much about the smoke. Meaning: a correlation some system uses (MacKay); Millikan adds selection.

**Bennett's copy in code.** `y = 0; y ^= x` copies reversibly and undoes with `y ^= x`; `y = x` maps four states to two and erases a bit. The copy is free; the blank was paid for when it was prepared. Classical carrier-independence is the existence of reversible copy operations between all classical carriers.

**Repetition code.** Majority of n copies at 10% flip: 10%, 2.8%, 0.86%, 0.27% for n = 1, 3, 5, 7. _Position:_ redundancy as objectivity and the repetition code are one structure; objectivity is a code distance.

**Direction.** Candidates: causal order (names the asymmetry), which system is the copy (history only), the arrow (Reichenbach 1956, Albert 2000). _Position:_ aboutness is mutual information plus a preparation history: a system is about another when it was prepared blank and then correlated with it; blanks come from the gradient, so every record points to the past. Clause 2 breaks: aboutness is relational with a past.

### Quantum: what the carrier decides (4b)

_All examples in qsim.py._

* **No-cloning.** CNOT copies |0⟩ and |1⟩; on |+⟩ it gives \[0.707, 0, 0, 0.707], a Bell pair, not \[0.5, 0.5, 0.5, 0.5]. Copying multiplies amplitudes; linear maps can't. One basis per copier. _Position:_ classical information is the basis an interaction can copy; a sector, not a carrier.
* **Holevo.** Four states 0, 1, +, − carrying two bits; Z or X measurement recovers 0.5 bits, no measurement more; 1 bit per qubit at most. _Position:_ a quantum state is a description, not a stock of retrievable bits; complementarity in information terms.
* **Superdense coding and teleportation.** One shared Bell pair; Alice's I, X, Z, XZ give Bob 00, 01, 10, 11 with certainty; ψ = \[0.6, 0.8] arrives in all four branches, Bob's qubit maximally mixed before the call, Alice's copy destroyed. 1 ebit + 1 qubit = 2 bits; 1 ebit + 2 bits = 1 qubit. _Position:_ entanglement is correlation with nothing to be about: 2 bits of mutual information, no message, no preparation history, a resource rather than a record.
* **Negative conditional entropy.** Bell pair: S(AB) = 0, S(B) = 1, S(A|B) = −1; classical correlation gives 0. State merging (Horodecki–Oppenheim–Winter 2005): negative means ebits to spare. _Position:_ the negative region is the uncopyable sector, measured.
* **Bit-flip code.** 0.6|000⟩ + 0.8|111⟩ by entangling, not copying; parities of (0,1) and (1,2) give syndromes 10, 11, 01 for flips on qubits 0, 1, 2, deterministically, and the data survives. Phase flips, continuous errors, thresholds in the codes side file. _Position:_ quantum error correction is the copyable sector put to work protecting the uncopyable; the syndrome is classical, the data never read.
* Schumacher (1995): compression to S(ρ) qubits.

Clause 3 breaks: carrier-independence holds only in the copyable sector. Bet, first half: confirmed.

***

## 6. The payoff — does quantum theory come from information, and do records explain themselves?

### 5a: reconstructions

_Search findings, October 2026:_ generalized information causality claimed to give the exact quantum boundary in the simplest Bell scenario (Gachechiladze–Miklin, arXiv 2609.10508, Sept 2026); information causality shown not to single out the quantum set with three or more settings (Pompili–Weilenmann, arXiv 2610.06604, Oct 2026). Both unrefereed and compatible. Redundant-information IC (Yu–Scarani, _PRA_ July 2026). Complete quantum statistics in the minimal Bell scenario (Barizien–Bancal, _Nature Physics_ 2025). Real QT excluded under partial source independence (Weilenmann–Gisin–Sekatski 2025). QBist reconstruction from one 3-design reference measurement (Weiss, Sept 2026 thesis).

**Motive.** Wheeler's it from bit (1989); Zeilinger's one bit per elementary system (1999); Clifton–Bub–Halvorson (2003): no signalling, no broadcasting, no bit commitment pick quantum theory among C\*-algebraic theories. _Position:_ true theorem, inflated moral; C\*-algebras already contain most of the structure (Timpson).

**Theories as shapes (gpt.py).** Segment (classical bit), disk or ball (qubit), square (gbit). Copying test: a state with two decompositions into pure states forbids a linear copier (square centre: ⟨X₁Y₂⟩ = +1 and −1 at once; disk: 0 and +0.5). Broadcasting possible iff the shape is a simplex (BBLW 2007). _Position:_ no-cloning is the definition of non-classical, not a quantum principle; it can't separate quantum theory from the square.

**Axioms.** Continuity/symmetry kills segment and square. Local tomography kills the disk: rebit K = 3, pair 10 ≠ 9; qubit 4 and 16. Purification kills classical: all ignorance is entanglement with something. Gleason, recapped: questions force the measure; reconstructions derive the questions.

**Correlations route.** CHSH: 2, 2√2, 4 (win 0.75, 0.854, 1). PR box as random-access memory: one bit sent, either of two bits recovered (van Dam: communication complexity trivial). Information causality: one level breaks at p ≈ 0.89, nested exactly at 0.854 (2E² = 1). Almost-quantum correlations satisfy known bipartite principles (Specker excludes them). _Position:_ one communication principle can't single out quantum correlations in general; what's missing is composition.

**What isn't information.** Continuity (a Lie group, _Symmetry_), the composition rule (the division), finiteness and the reals. _Position:_ **quantum theory is information plus symmetry plus composition**; given symmetry and composition, no-cloning, Holevo, purification, and Tsirelson follow. Information is the right language without being the source. Purification conserves information and is silent about records.

### 5b: conservation, constructor theory, records

_Search findings:_ constructor theory tests reviewed (Marletto–Deutsch–Vedral, June 2026), photonic homogeniser experiment performed, gravity test not; Aziz–Howl (_Nature_ 2025) vs. Marletto on whether classical gravity can entangle; Struyve (2025–26) on semiclassical models; closed universes need an observer for a non-trivial Hilbert space (Akers et al. _JHEP_ 2025); entropy production dominated by mutual-information growth in a quantum field simulator (Aimet et al. _Nature Physics_ 2025); operational redundancy measure (preprint 2025); below-threshold QEC (_Nature_ 2025) and 2025 logical-beats-physical results.

**Conservation.** _Position:_ a law about the whole; records are about parts, and conservation works against them: it makes blanks and regeneration costly, not records possible. An equilibrium universe conserves everything and records nothing.

**Constructor theory.** Information variables (permutable, copyable), media, interoperability, distinguishability defined by copyability, superinformation. Worked: Z-copier copies {0, 1}, X-copier copies {+, −}, neither copies the union: a qubit is a superinformation medium. Box world: all reversible dynamics trivial (Gross–Müller–Colbeck–Dahlsten 2010), so no free reversible copy. _Positions:_ reversible copying is a substantive physical property, supplied by the symmetry axiom; interoperability is the copyable sector stated as a law, an input made testable, not explained.

**Records and holographic codes.** Darwinism, the shared tick, and the repetition code as one structure. Non-isometric codes for the black-hole interior (Akers–Engelhardt–Harlow–Penington–Vardhan 2022), observers in holographic maps (2025). _Position:_ geometry is a record that holds up only for observers who can't compute too much; the two side files meet here.

### The bet, tested

_Classical information is the copyable sector; information theory assumes copyability; quantum theory says which observables; nothing says why a stable copyable sector exists; constructor theory restates the input; it from bit runs backwards._

1. Copyable sector: **confirmed, exact** (no-cloning; simplex theorem).
2. Information theory assumes copyability: **confirmed** (box world shows it's not free in every world).
3. Quantum theory gives the copyable observables: **confirmed** (einselection; reversible correlating dynamics from the symmetry axiom).
4. Nothing explains a stable copyable sector: **confirmed and refined** into three inputs: symmetry, composition, gradient.
5. Constructor theory restates the input: **confirmed, upgraded** to an input stated as a testable law.
6. It from bit runs backwards: **partly confirmed**; information is the language, not the source.

Confirmed more strongly than _Space_'s or _Time_'s bets.

**Working claim, broken three times.** Not content (overturned: relative to a supplied ensemble). Not intrinsically about (overturned: correlation plus preparation history). Not carrier-independent (replaced by a regime: the copyable sector of any carrier, existing only where reversible copying exists).

**Endpoint.** Classical information is the record; information in general is more (uncopyable correlation, a resource until copied out). A measurement, a shared tick, an objective fact, and a stored bit are one act: moving information from the uncopyable whole into the copyable sector, at an entropy cost, in the gradient's direction. The possibility of records remains an input, resolved into symmetry (_Symmetry_), composition (_Space_), and gradient (_Entropy_, _Time_), all three required at once.

***

## 7. The single line of thought

One question, asked with steadily less confidence that a message carries its own meaning: what does a carrier have to allow for one thing to be about another, and for the aboutness to be shared?

| Stage                                 | Information is…                                                 | Relative to                                   | What it yields                                                |
| ------------------------------------- | --------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------- |
| Signet ring to Morse                  | form passed to a carrier; a chosen message                      | a codebook, a language                        | carrier-independence given distinctions; cheap common symbols |
| Fisher to Bar-Hillel–Carnap (1925–52) | a measure: of a parameter, of selection, of order, of exclusion | a supplied ensemble                           | the dispute dissolved; meaning in what selects the ensemble   |
| Shannon to Kolmogorov (1948–65)       | relative entropy; a shortest program                            | a reference distribution; a universal machine | codes, capacity, compression; the individual uncomputable     |
| Landauer to Bennett (1961–82)         | correlation in a physical carrier                               | a division and a preparation history          | aboutness as correlation; free copies, costly blanks          |
| Quantum information (1973–2005)       | a state that can't be copied or fully read                      | a basis selected by a copier                  | the copyable sector; ebits; S(A\|B) < 0; codes without copies |
| Reconstructions (2001–26)             | the language quantum theory is clearest in                      | symmetry and composition                      | quantum theory = information + symmetry + composition         |
| Constructor theory, records (2015–26) | what tasks are possible on a medium                             | interoperability; a gradient                  | copyability as law; records need all three inputs             |

Waves kept the space and lost the substrate. Symmetry kept the group and lost the object. Entropy kept the logarithm. Randomness kept the absence. Measurement kept the record. Computation kept the step. Space kept the relation. Time kept the correlation with a clock. Information kept the _copy_, and lost the content, the aboutness, and the indifference to its carrier.

***

## Suggested next steps

* Run _hamming.py_, then extend it to Hamming(15,11) by changing the parity positions to 1, 2, 4, 8 and confirm the XOR-of-positions rule still decodes every single error.
* Repeat the smoke–fire calculation with smoke 50% given no fire, and watch the mutual information and P(fire | smoke) fall.
* Compute D(P‖Q) and D(Q‖P) for P = (0.5, 0.5), Q = (0.99, 0.01); explain the asymmetry with Stein's lemma.
* In _qsim.py_, extend the bit-flip code to Shor's nine-qubit code and show a phase flip (Z) on one qubit is corrected.
* In _gpt.py_, add a triangle (a classical trit) and confirm every mixed state has one decomposition; add a hexagon and find two decompositions.
* Run the PR-box random-access protocol with a noisy box (win probability p) and estimate Bob's success rate for p = 0.75, 0.854, 0.9.
* Reading: Shannon (1948), first two sections; Weaver (1949); Bar-Hillel and Carnap, "An Outline of a Theory of Semantic Information" (1952); Hamming (1950); Cover and Thomas, _Elements of Information Theory_, ch. 2; Bennett, "The Thermodynamics of Computation — a Review" (1982); Nielsen and Chuang ch. 1, 10, 12; Hardy, "Quantum Theory From Five Reasonable Axioms" (2001); Müller, "Probabilistic theories and reconstructions of quantum theory" (SciPost lecture notes 2021); Pawłowski et al., "Information causality as a physical principle" (2009); Deutsch and Marletto, "Constructor theory of information" (2015).
* Links forward: _error-correcting-codes.md_ and _reconstructions-of-quantum-theory.md_ (side files written at this close); _Causality_ (information causality, no-signalling, the quantum switch); _Proof_ (Chaitin's information-theoretic incompleteness); _The continuum_ (Fisher information on a continuum; infinite precision as infinite information).
