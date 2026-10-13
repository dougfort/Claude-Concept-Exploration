# Error-Correcting Codes, Classical to Quantum

_Side file, October 2026, written at the close of the information exploration. How a record survives noise: from the repetition code to Hamming's syndrome, the 45-year road to Shannon's limit, the quantum turn that had to protect what can't be copied, and the 2024–26 hardware that finally runs below threshold. Runnable companions: hamming.py, qsim.py, shor.py, surface.py._

***

## 1. The one idea

A code adds structured redundancy so that noise moves the message to a place where the damage is visible and, within limits, reversible. Every code in this file is a set of **checks**: parities that are zero on every valid codeword. The pattern of failed checks, the **syndrome**, depends only on the error, never on the message. Decoding is: read the syndrome, infer the most likely error, undo it.

The trade-off has three numbers. **Rate** k/n is message bits per transmitted bit. **Distance** d is the fewest flips that turn one codeword into another; a code corrects up to ⌊(d−1)/2⌋ errors. **Decoding cost** is what it takes to find the error from the syndrome. Shannon's theorem is about the first two; the history is mostly about the third.

***

## 2. Repetition and parity

**Repetition.** Send each bit n times; majority vote. At 10% flips: 10%, 2.8%, 0.86%, 0.27% for n = 1, 3, 5, 7 (_what-is-information.md_ §5). Distance n, rate 1/n: reliability bought at a rate that goes to zero.

**Parity.** One extra bit making the count of 1s even. Distance 2: detects a single error, can't locate it. Hamming's weekend relay computer could do exactly this, and abandoned the job.

_Position:_ the two extremes bracket the subject. Repetition locates and fixes everything and wastes almost everything; parity wastes almost nothing and fixes nothing. Every later code is a way to get location without repetition's cost.

***

## 3. Hamming and Golay: the syndrome as address

**Hamming (1950, developed 1947).** Parity bits at positions 1, 2, 4, …; parity p checks every position whose index has bit p set. A word is valid iff the XOR of the positions holding a 1 is zero; a flip at position k makes that XOR equal k. Worked in _what-is-information.md_ §4 and _hamming.py_ (1011 → 0110011; flip 6 → syndrome 110 = 6).

The family is Hamming(2^m − 1, 2^m − 1 − m): (7,4), (15,11), (31,26), … Rate approaches 1, distance stays 3. Every syndrome is used: 2^m − 1 nonzero syndromes, one for each position. Codes with this property are **perfect**.

**Golay (1949).** Golay's one-page paper appeared in print before Hamming's and gave the (23,12) code: 12 data bits, distance 7, corrects any 3 errors, also perfect. Apart from repetition codes of odd length, the Hamming parameters and the (23,12) Golay code are the only perfect binary codes (Tietäväinen, van Lint, 1973). An extended Golay code carried Voyager's colour images from Jupiter and Saturn.

**Hamming distance and the sphere picture.** Codewords as points in the n-dimensional cube of bit strings; distance as the number of differing bits; decoding as finding the nearest codeword. Correcting t errors means radius-t spheres around codewords don't overlap. A perfect code tiles the cube with them exactly. The Hamming bound counts how many spheres fit: Hamming(7,4) has 16 codewords × 8 strings per sphere = 128 = 2⁷, no waste.

_Position:_ priority goes to Golay for the best small code; the lasting contribution is Hamming's. He made distance the organizing concept and the syndrome the decoding method. The syndrome's independence from the data is a convenience in 1950 and the entire possibility of quantum error correction in 1995.

***

## 4. Shannon's gap: existence without construction

Shannon (1948) proved that at any rate below capacity, codes exist with error probability as small as you like. The proof: pick the codebook _at random_; on average it works; so some codebook works. (_shannon-and-information.md_ §3.)

Two obstacles separated the theorem from practice:

1. **Random codes have no structure to decode with.** Nearest-codeword decoding of a random code means comparing against 2^(nR) codewords. For general linear codes, maximum-likelihood decoding is NP-hard (Berlekamp, McEliece, van Tilborg 1978).
2. **Good small codes are far from capacity.** Hamming(7,4) at rate 0.57 on a channel of capacity 0.92 (_what-is-information.md_ §4).

_Position:_ **capacity is a statement about information; reaching it is a statement about computation.** Shannon showed the information is there; the next 45 years were about the decoding problem, which is where _Computation_'s complexity theory meets this one. The codes that closed the gap won by being decodable _approximately_, by local message passing, not by being optimal.

***

## 5. The road to capacity

**Algebraic codes.** Reed–Solomon (1960): codewords are evaluations of a polynomial; k symbols determine a degree-(k−1) polynomial; send n > k evaluations; any k recover it; up to (n−k)/2 corrupted symbols fixable. Symbols are bytes, so a burst of scratched bits is one or two symbol errors. Compact discs (cross-interleaved Reed–Solomon), QR codes, deep-space links, RAID-6, and most storage systems. Worked in plain terms: a line through two points; send four points; one wrong point is the one off the line through the other three. BCH codes (1959–60) are the binary relatives.

**Convolutional codes and Viterbi.** Elias (1955); Viterbi's decoding algorithm (1967) is dynamic programming over a trellis of encoder states, the same algorithm as shortest path or HMM decoding. Voyager paired a convolutional code with Reed–Solomon (concatenation, Forney 1966).

**Turbo codes (Berrou, Glavieux, Thitimajshima 1993).** Two simple convolutional encoders, the second fed an interleaved (shuffled) copy of the data. Two decoders exchange _soft_ beliefs, probabilities not bits, and iterate. Within about half a decibel of the Shannon limit. Reviewers initially assumed a measurement error.

**LDPC codes (Gallager 1960; rediscovered MacKay–Neal, and Sipser–Spielman expander codes, 1996).** Many sparse parity checks, each touching a few bits. The Tanner graph is bipartite: bits on one side, checks on the other. Belief propagation passes messages along edges: each check tells each bit what the other bits suggest, each bit combines what its checks say, repeat. In programming terms, a fixed-point iteration over a sparse graph, embarrassingly parallel. Gallager's 1960 hardware couldn't run it; 1990s hardware could. DVB-S2 (2005), Wi-Fi, 5G data channels, 10G Ethernet.

**Polar codes (Arıkan 2009).** The first explicit construction _proven_ to reach capacity with efficient decoding. The mechanism is **channel polarization**. Combine two uses of a binary erasure channel (erasure probability z) with the transform (u₁, u₂) → (u₁ ⊕ u₂, u₂): one synthetic channel gets worse (erasure 2z − z²), the other better (z²). Worked, from z = 0.5:

| Levels | Channels | Erasure probabilities                                  |
| ------ | -------- | ------------------------------------------------------ |
| 1      | 2        | 0.75, 0.25                                             |
| 2      | 4        | 0.938, 0.562, 0.438, 0.062                             |
| 3      | 8        | 0.996, 0.879, 0.809, 0.316, 0.684, 0.191, 0.121, 0.004 |
| 20     | \~10⁶    | 46% below 10⁻⁶, 46% above 1 − 10⁻⁶                     |

The channels split into nearly perfect and nearly useless, and the perfect fraction tends to the capacity, 1 − z = 50%. Send data on the good ones, fixed zeros on the bad. Polarization is slow at short lengths; practical polar codes add a CRC and list decoding (Tal–Vardy). Adopted for 5G control channels (3GPP, 2016).

_Position:_ polarization is the cleanest picture of what a code does. It doesn't make noise go away; it _moves_ it, concentrating all the uncertainty into channels you agree not to use. Information is relative to a reference (_what-is-information.md_ §4); polar coding is the relativity made into engineering: choose the reference (frozen bits) so that the rest is certain.

| Code                    | Year      | Idea                                    | Where it runs                |
| ----------------------- | --------- | --------------------------------------- | ---------------------------- |
| Hamming / Golay         | 1949–50   | syndrome as address; perfect codes      | ECC memory; Voyager          |
| Reed–Solomon            | 1960      | polynomial evaluations, byte symbols    | CDs, QR, storage, deep space |
| Convolutional + Viterbi | 1955–67   | trellis, dynamic programming            | Voyager, early cellular      |
| Turbo                   | 1993      | two codes exchanging soft beliefs       | 3G/4G, deep space            |
| LDPC                    | 1960/1996 | sparse checks, belief propagation       | Wi-Fi, DVB-S2, 5G data       |
| Polar                   | 2009      | channel polarization, provably capacity | 5G control                   |

***

## 6. The quantum turn

Three obstacles made quantum error correction look impossible in 1994: no-cloning (no repetition), measurement disturbs (no reading the data), and errors are continuous (infinitely many to correct). All three were answered in about two years.

**Shor's nine-qubit code (1995).** Repetition against bit flips inside each of three blocks, repetition of the blocks against phase flips. Corrects any error on any one qubit. _shor.py_:

```
none                     Z-checks ++++++  X-checks ++  -> [+0.600, +0.800]
X on 4                   Z-checks ++--++  X-checks ++  -> [+0.600, +0.800]
Z on 4                   Z-checks ++++++  X-checks --  -> [+0.600, +0.800]
Y on 7 (X and Z)         Z-checks ++++--  X-checks +-  -> [+0.600, +0.800]
rotation 0.3 rad on 2    Z-checks ++++++  X-checks ++  -> [+0.600, +0.800]

The rotation, 2000 times: how often does the syndrome say 'flip on 2'?
  0.092   (sin^2 0.3 = 0.087);  decoded to [0.6, 0.8] in 2000/2000 runs
```

The last block answers the third obstacle. A small rotation is a superposition of "nothing happened" and "a flip happened"; measuring the syndrome forces one or the other, with probabilities cos²θ and sin²θ, and both are correctable. **Syndrome measurement discretizes the error.** Measurement, the problem, is the solution.

**CSS codes and Steane's seven-qubit code (Calderbank–Shor, Steane, 1996).** Take a classical code whose checks also satisfy its own dual. Use its checks as Z-checks (catching bit flips) _and_ as X-checks (catching phase flips). X-checks and Z-checks commute when every pair overlaps on an even number of qubits. Hamming(7,4)'s three checks overlap pairwise on 2 positions and with themselves on 4:

```
overlaps of Hamming's check rows: [[4, 2, 2], [2, 4, 2], [2, 2, 4]]   all even
```

So Hamming's code, used twice, is Steane's \[\[7,1,3]] quantum code: 7 qubits, 1 logical qubit, distance 3. The smallest code correcting any single-qubit error is \[\[5,1,3]] (Laflamme et al.; Bennett et al., 1996).

_Position:_ **quantum error correction is classical error correction applied twice, to complementary questions.** Bohr's complementarity (X and Z can't both be read) becomes a design constraint: the two classical codes must fit together (dual-containing). Hamming's 1950 code was already half of the answer.

**The stabilizer formalism (Gottesman 1997).** Describe a code by its checks (the stabilizer group) instead of its amplitudes. Corollary (Gottesman–Knill): circuits of stabilizer operations with Pauli errors can be simulated classically. That is why _surface.py_ needs only bitmasks, and why decoders run on ordinary computers.

**The threshold theorem (Aharonov–Ben-Or; Knill–Laflamme–Zurek; Kitaev, 1996–97).** If each component fails with probability p below a threshold, encoding recursively drives the logical error as low as you like with polylogarithmic overhead. Concatenation in one line: one level turns p into about c·p²; threshold p\_th = 1/c. Worked with c = 100:

| Physical p | Level 1    | Level 2    | Level 3     |
| ---------- | ---------- | ---------- | ----------- |
| 0.001      | 1.0 × 10⁻⁴ | 1.0 × 10⁻⁶ | 1.0 × 10⁻¹⁰ |
| 0.005      | 2.5 × 10⁻³ | 6.3 × 10⁻⁴ | 3.9 × 10⁻⁵  |
| 0.02       | 4 × 10⁻²   | 0.16       | > 1         |

Below 1%, each level squares the advantage; above, each level makes things worse. This is von Neumann's 1956 "reliable organisms from unreliable components" (_what-is-computation.md_), finished for quantum information.

_Position:_ **an error-corrected quantum computer is a refrigerator for its code.** Each round measures syndromes into fresh ancillas and resets them: each reset is a Landauer erasure. Errors are entropy entering the code; correction pumps it out, into the ancillas and then the environment. The threshold theorem says the pumping can outrun the leak, _given a continuous supply of blanks_. This is the information exploration's third input, the low-entropy gradient, as an engineering requirement.

***

## 7. The surface code

**Kitaev's toric code (1997; Bravyi–Kitaev planar version, 1998).** Qubits on the edges of a lattice; star (X) and plaquette (Z) checks, each touching four nearby qubits. On a torus the code holds two logical qubits; in the planar or rotated version, one. Logical operators are strings stretching across the whole lattice; errors cause a logical failure only if they form a chain from one boundary to the other. **The distance is the lattice width.** Every check is local, weight 4, nearest neighbours only, which is why it suits a chip.

**surface.py: the rotated d = 3 code.** 9 data qubits, 4 X-checks, 4 Z-checks, 1 logical qubit. Bit flips only (phase flips are the same with roles swapped); lowest-weight lookup decoder.

```
d = 3: 9 data qubits, 4 X-checks, 4 Z-checks, 1 logical qubit
  Z-checks (catch bit flips): [[0, 3], [1, 2, 4, 5], [3, 4, 6, 7], [5, 8]]

2. Every single flip, and every pair of flips
  weight 1: 9 patterns, 0 end in a logical error
  weight 2: 36 patterns, 18 end in a logical error

3. Logical error rate per round, bit flips at rate p on every qubit
     p      d=3       d=5     ratio d3/d5
   0.01   0.0017   0.0003        5.4
   0.03   0.0152   0.0058        2.6
   0.05   0.0383   0.0246        1.6
   0.08   0.0835   0.0769        1.1
   0.12   0.1590   0.1767        0.9
   0.16   0.2381   0.2808        0.8
```

(Monte Carlo, 50,000 trials per cell.) Exact by enumeration of error patterns: at p = 1%, 1.73 × 10⁻³ (d = 3) against 2.71 × 10⁻⁴ (d = 5), ratio 6.4; at p = 0.1%, 1.8 × 10⁻⁵ against 2.9 × 10⁻⁷, ratio 62.

Reading the table:

* **Distance 3 corrects every single flip and fails on half the pairs.** Distance 5 corrects every pair and fails on 292 of the 2,300 triples.
* **The crossing near 9–10% is the threshold** for this noise model; the known value with an optimal-matching decoder is about 10.3% (Dennis–Kitaev–Landahl–Preskill 2002, via the random-bond Ising model). Below it, bigger codes are better; above it, worse.
* **The ratio d3/d5 is Λ**, the error suppression factor reported by experiments. Far below threshold it is large; near threshold it falls to 1. Roughly Λ ≈ p\_th / p per step of 2 in distance.

The toy uses "code-capacity" noise: perfect checks, errors only on data. Real hardware has faulty measurements, faulty gates, and leakage, so the circuit-level threshold is about 1%, and syndromes must be repeated over time (decoding becomes a 3D matching problem).

_Position:_ **classical and quantum protection are opposite strategies for the same quantity.** A classical record is protected by being _everywhere_: copies in many places (repetition, quantum Darwinism's redundant fragments). A topological quantum record is protected by being _nowhere_: no small region holds any of it, and only a string across the whole lattice can touch it. Both are code distance. Redundancy as objectivity and topological order are the two ends of one scale.

***

## 8. Below threshold: 2024–26

* **Google Quantum AI, Willow** ([_Nature_ 638, 2025; online Dec 2024](https://www.nature.com/articles/s41586-024-08449-y)). Surface codes at d = 3, 5, 7 on a 105-qubit chip. **Λ = 2.14 ± 0.02**; d = 7 logical error **0.143% per cycle**; logical lifetime 291 μs, **2.4× the best physical qubit**. Real-time decoding at a 1.1 μs cycle with 63 μs average latency on the 72-qubit device. Repetition codes to d = 29 hit a floor near 10⁻¹⁰ from rare correlated bursts about once an hour.
* **Dynamic surface codes** (Google, _Nature Physics_; [blog, Jan 2026](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/)). Alternating circuit constructions: hexagonal connectivity (3 couplers per qubit) with suppression 2.15 from d = 3 to 5; "walking" codes that swap data and measure roles, cutting time-correlated errors by over an order of magnitude; iSWAP-based circuits at 1.56.
* **Quantinuum, trapped ions, 2025** ([overview](https://postquantum.com/quantum-computing/qec-below-threshold-experiments/)): a logical controlled-Hadamard with error ≤ 2.3 × 10⁻⁴ against \~10⁻³ physical, using a \[\[6,2,2]] code with post-selection; a logical magic state at infidelity ≤ 5.1 × 10⁻⁴, \~2.9× better than the best physical two-qubit gate. Logical operations beating physical ones, not distance scaling.
* **Harvard neutral atoms, 448-atom processor, Nov 2025** (same overview): below-threshold operation with transversal logical gates and qubit reuse; distance-scaling numbers not given in the source I checked.
* Claims circulating in 2026 summaries (for example, "96 logical qubits") I could not trace to primary sources; not included.

Reading Willow against the toy: Λ ≈ 2 means circuit-level noise is roughly half the circuit-level threshold. Each two steps in distance halves the error, so getting from 1.4 × 10⁻³ at d = 7 to 10⁻⁶ per cycle takes about ten more halvings, d in the high twenties, and well over a thousand physical qubits per logical qubit. That overhead is why the next direction matters.

**qLDPC codes.** Bravyi, Poulin, and Terhal (2010): codes with only local checks in 2D satisfy k·d² = O(n), so the surface code's one logical qubit per patch is close to the best locality allows. Codes with long-range checks escape the bound. IBM's bivariate bicycle "gross" code \[\[144,12,12]] (Bravyi et al., _Nature_ 2024) holds 12 logical qubits at distance 12 in 288 physical qubits, where surface codes would need about ten times as many, at the price of long-range connectivity.

_Position:_ **locality costs rate.** The surface code's virtue (every check is local) is also its overhead. _Space_'s locality theme reappears as an engineering trade-off: the geometry of the hardware bounds how efficiently information can be protected in it.

***

## 9. Where codes become space

_The three-qutrit code and Ryu–Takayanagi are in what-is-space.md; non-isometric codes in what-is-information.md §6._

* **Three qutrits** (Cleve–Gottesman–Lo 1999): one qutrit encoded so any two of three shares recover it, any one alone knows nothing. Almheiri–Dong–Harlow (2015): bulk locality in AdS/CFT _is_ this property. A bulk point deep inside is recoverable from many boundary regions, none necessary: depth as code distance.
* **HaPPY codes** (Pastawski–Yoshida–Harlow–Preskill 2015): perfect tensors (built from the \[\[5,1,3]] code) tiled on a hyperbolic disk. A toy hologram: bulk logical qubits, boundary physical qubits, and the Ryu–Takayanagi formula as a count of cut tensor legs.
* **Non-isometric codes** (Akers–Engelhardt–Harlow–Penington–Vardhan 2022): the black-hole interior's effective description has more states than the fundamental one; the discrepancy is invisible to any efficient observer. Observers in closed universes (Akers et al. 2025): the observer's degrees of freedom are cut out of the holographic map, making an effective boundary at the observer.

_Position:_ in holography, error correction is the structure of a protected record and the structure of space at once. The surface code protects a qubit by being nowhere locally; the bulk is protected by being reconstructible from many places; the interior is protected, past the Page time, only by computational hardness. Three kinds of code distance: geometric (lattice width), redundant (many boundary regions), computational (exponential decoding cost).

***

## 10. The single line

| Code            | Protects by                                     | Distance is       | Cost paid in                             |
| --------------- | ----------------------------------------------- | ----------------- | ---------------------------------------- |
| Repetition      | copies everywhere                               | number of copies  | rate                                     |
| Hamming / Golay | parity checks; syndrome as address              | 3 / 7             | a little rate                            |
| Reed–Solomon    | overdetermined polynomial                       | n − k + 1 symbols | algebra                                  |
| Turbo / LDPC    | sparse checks, soft beliefs                     | large, typical    | iteration                                |
| Polar           | concentrating noise into frozen channels        | grows with length | length, list decoding                    |
| Shor / Steane   | entanglement; two complementary classical codes | 3                 | qubits; fresh ancillas                   |
| Surface         | nowhere locally; strings across the lattice     | lattice width     | \~2d² qubits; continuous entropy pumping |
| qLDPC           | long-range sparse checks                        | grows with n      | connectivity                             |
| Holographic     | reconstructible from many regions; hardness     | depth; complexity | spacetime geometry                       |

The classical half moves noise to where it can be seen and discarded. The quantum half does the same without ever looking at the data: it reads only the noise, and it pays for every reading with a fresh blank.

***

## Suggested next steps

* Extend _hamming.py_ to (15,11) and check that the XOR-of-positions rule still decodes every single error.
* Write a Reed–Solomon toy over integers mod 7: encode 2 symbols as a line, send 4 points, corrupt one, and recover by finding the three collinear points.
* In _surface.py_, add phase-flip errors and the X-checks (swap the roles), then run both together and confirm the logical error rate roughly doubles.
* In _surface.py_, add measurement errors: flip each syndrome bit with probability q and repeat the syndrome 3 times; watch the threshold fall.
* Build the Steane code in _qsim.py_ from Hamming's three checks, applied as Z-checks and X-checks, and compare with _shor.py_.
* Polarize a binary erasure channel at z = 0.2 for 10 levels and compare the fraction of good channels with 1 − z.
* Reading: Hamming, "Error Detecting and Error Correcting Codes" (1950); MacKay, _Information Theory, Inference, and Learning Algorithms_ (free online), chs. 1, 47–49; Arıkan (2009); Gottesman's thesis (1997), ch. 3; Fowler et al., "Surface codes: towards practical large-scale quantum computation" (2012); Google Quantum AI (2025); Harlow, "TASI lectures on the emergence of bulk physics in AdS/CFT" (2018).
* Links: _what-is-information.md_ (§4 Hamming and regeneration; §5 repetition and the bit-flip code; §6 holography); _what-is-computation.md_ (von Neumann's reliable logic; decoding hardness); _what-is-space.md_ (the three-qutrit code); _what-is-measurement.md_ (redundancy as objectivity).
