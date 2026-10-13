**On side files:** both. A few candidates can be named now, and the rest are better caught as they come up.

* **Name now:** interests that span several explorations. The method writes these at the close, so knowing early lets me feed them as we go. I see two:

  * **Reconstructions of quantum theory.** This gathers Gleason (_Randomness_), Bell and Tsirelson's 2√2, Popescu–Rohrlich boxes, and the information-theoretic axioms, and it is where your stage 5 interest lands.
  * **Error-correcting codes, classical to quantum.** This runs from Hamming to polar codes to the three-qutrit code from _Space_ and today's surface codes. It's the most programmer-shaped topic in the arc.

* **As they come up:** overflow detours, meaning a stage that pulls past its cap. The two likely ones are the philosophy of meaning (stage 2) and a quantum-information primer (4b). When one starts to pull, I'll say so and you decide.

If either of the first two sounds like something you'd read, say so now. Otherwise I'll ask at the close.

I've recorded your steering in the outline, along with these changes:

* Stage 4 is split now. 4a covers aboutness as correlation and copying; 4b covers the five quantum results.
* Stage 5 is weighted toward your question and split. 5a asks whether quantum theory comes from information: Clifton–Bub–Halvorson, the reconstructions, PR boxes, and information causality, each with a worked example. 5b covers conservation, records, and the bet.

***

# Stage 1 — The intuition: form, sign, message

_A selective prehistory. The telegraph lineage from Nyquist to Hartley is in_ shannon-and-information.md _§1 and isn't repeated._

## The word: from shaping to telling

_Informare_ meant to give form to something, to shape it. It came to mean shaping a mind as well. Cicero used _informatio_ for an outline of a thing held in the mind before you meet it.

The philosophical root is Aristotle, _De Anima_ II.12. Perception is the reception of a thing's form without its matter, as wax takes the impression of a signet ring without taking the gold. The scholastics built their theory of knowledge on this: to know a thing is for the intellect to be "informed" by its form. By Chaucer's time, English "information" meant something told.

_Position:_ the signet ring is the first statement of carrier-independence, and it already contains the limit of that idea. The form passes from gold to wax unchanged, which is the independence. But it needs wax: a medium that can hold the impression. Bacon will make that condition explicit, and quantum mechanics will eventually make it the whole story. **Carrier-independence has always meant independence of which carrier, given a carrier capable of the distinctions.**

## The sign: natural and given

Augustine (_De doctrina christiana_ II) defined a sign as a thing that, beyond the impression it makes on the senses, brings something else to mind. He split signs into two kinds:

* **Natural signs** signify without anyone intending them: smoke for fire, a footprint for an animal.
* **Given signs** are signs by convention: words, flags.

The Stoics had already separated three things: the sound, what is said, and the thing it is about.

_Position:_ the natural sign is the version physics keeps. Smoke is "about" fire only because the two are reliably correlated. In stage 4, all aboutness becomes this kind: mutual information between two systems. Given signs survive as a special case, correlations that someone set up deliberately.

## Messages at a distance: what the channel carries

**The beacon.** In Aeschylus's _Agamemnon_ (458 BC), a chain of fires carries the fall of Troy to Argos in one night. Every fire carries the same single bit: lit or unlit. The meaning, "Troy has fallen," lives entirely in the prior agreement. The channel selects one of two messages agreed in advance.

**The alphabet.** Polybius (_Histories_ X) criticized an earlier water-clock system of Aeneas Tacticus. It could send only messages on a pre-agreed list, and the urgent ones are exactly those nobody anticipated. His fix was to put the alphabet in a 5×5 grid and send each letter with torches: some on the left for the row, some on the right for the column.

Worked: 5 × 5 = 25 cells hold the 24 Greek letters. Each torch signal selects one of 25 options, about log₂ 25 ≈ 4.6 bits. Any sentence becomes a string of such selections.

_Position:_ **Polybius made the decisive pre-modern move, more decisive than Bacon's.** He moved the codebook from messages to symbols. Before him, a channel carried a choice from a list of meanings. After him, it carried a choice from all strings, so it could carry the unanticipated. Hartley's later "eliminate psychological factors" is this move made into a definition.

## The codebreaker: statistics without content

Al-Kindi, a 9th-century Baghdad polymath, wrote a treatise on deciphering encrypted messages; the manuscript was rediscovered in Istanbul in the 1980s. It contains the first known description of frequency analysis: count the letters in the ciphertext, compare them with the counts in ordinary text in the same language, and match.

Worked, with a Caesar shift (every letter moved forward a fixed number of places):

* Ciphertext: `PHHW PH KHUH DW VHYHQ`
* Counts: H appears 7 times out of 17 letters; nothing else appears more than twice.
* E is the most common letter in English. H − E = 3, so guess a shift of 3.
* Shift back by 3: `MEET ME HERE AT SEVEN`.

In computational terms, a substitution cipher is a relabeling of symbols, and relabeling doesn't change the histogram's shape. `sorted(Counter(text).values())` is the same for the plaintext and the ciphertext. The cipher hides which symbol is which. It cannot hide the distribution.

_Position:_ al-Kindi is where the intuition's two halves first come apart in practice. The codebreaker reads the message's statistics, its measure, before knowing any of its content. Carrier-independence is the very property that makes the attack work: if a relabeled message carries the same information, it also carries the same statistics. Shannon's 1949 secrecy theory starts here, eleven centuries later (_shannon-and-information.md_ §2).

## The bit, stated: Bacon's biliteral cipher

Francis Bacon (_De Augmentis Scientiarum_, 1623, describing an idea from his youth in Paris) encoded each letter as five choices between two symbols, _a_ and _b_.

Worked:

* 2⁴ = 16 is too few for a 24-letter alphabet, and 2⁵ = 32 is enough. So: five binary choices per letter.
* In Bacon's table, A = aaaaa, B = aaaab, and so on: the letter's position in the alphabet written in binary, with _a_ = 0 and _b_ = 1. H is position 7, binary 00111, so _aabbb_. I is 8, binary 01000, so _abaaa_. In code: `format(i, '05b')`.
* To hide "HI", set any innocent ten-letter text in two slightly different typefaces, roman for _a_ and italic for _b_. The secret rides on a distinction the reader isn't looking at.

Bacon stated the general principle himself: anything capable of a twofold difference will do. Bells, trumpets, lights, and cannon shots all qualify.

This is the clearest pre-modern statement of the working claim's third clause. Content is independent of the carrier, provided the carrier can make the distinctions. It also contains the first cost accounting: hiding two letters took ten letters of cover. Leibniz's binary arithmetic (1679, published 1703) supplied the arithmetic but not the communication idea.

## Frequency weighting: the semaphore and Morse

Chappe's optical telegraph (Paris–Lille, 1794) used semaphore arms on towers. Operators sent pairs of signals: one chose a page of a codebook, the other a line on that page. With 92 usable signals, a pair selects one of 92 × 92 = 8,464 words and phrases, about 13 bits per pair.

This is Polybius and the beacon combined. The symbols form an alphabet of signals, but the codebook brings back word-level meaning to save transmissions.

Morse and Vail's code (1830s–40s; Vail is usually credited with counting type in a printer's case) gave common letters short codes: E is a single dot, T a single dash, Q is dash-dash-dot-dash.

Worked, with a four-letter alphabet whose letters occur with probabilities ½, ¼, ⅛, ⅛:

| Letter | Probability | Fixed-length code | Weighted code |
| ------ | ----------- | ----------------- | ------------- |
| A      | 1/2         | 00                | 0             |
| B      | 1/4         | 01                | 10            |
| C      | 1/8         | 10                | 110           |
| D      | 1/8         | 11                | 111           |

* The fixed-length code averages 2 bits per letter.
* The weighted code averages ½·1 + ¼·2 + ⅛·3 + ⅛·3 = 1.75 bits per letter.
* 1.75 is also −Σ p log₂ p for these probabilities, the Shannon entropy. Here the weighted code reaches the limit exactly.

A programmer's footnote: Morse code is not a prefix code. "E" (one dot) is the start of "I" (two dots), so Morse needs gaps between letters, and the gap is effectively a third symbol. The weighted code in the table is prefix-free: no codeword begins another, so it decodes without delimiters. Huffman (1952) made this kind of code optimal and constructible. Morse had the weighting by practice; he had neither the theory nor the prefix property.

## What the intuition contains

Four tenets, all held without examination by 1900:

1. **Information is content.** A message says something, and that something is what counts. The beacon's meaning, the codebook's phrases, Cicero's mental outline.
2. **It is about something.** Signs point beyond themselves, to fire, to Troy, to the enemy's plans.
3. **Any carrier will do, given enough distinctions.** The signet ring, Polybius's torches, Bacon's "twofold difference."
4. **Some messages are cheaper than others.** Morse's frequency weighting and al-Kindi's statistics. Practitioners exploited this constantly and no one theorized it.

The first three are the working claim. The fourth is the seed that grows into the measure.

**What it lacked.** First, a quantity: Morse knew E is cheap and couldn't say how cheap it could be made. Second, a clear statement of the receiver's set of alternatives. The beacon's whole content lies in the agreed list, and Polybius's advance was enlarging that list, but nobody made "the set of possible messages" the object of study.

The practice also already showed tenets 1 and 4 pulling apart. Al-Kindi measured without meaning; a codebook supplies meaning without measure. Once someone tries to quantify information, those two pull fully apart, and that is stage 2.

|                | What the channel carries                        | Where the meaning is                   |
| -------------- | ----------------------------------------------- | -------------------------------------- |
| Beacon         | one of two agreed messages                      | entirely in the prior agreement        |
| Polybius       | one of 25 symbols, then any string              | in the language                        |
| Al-Kindi       | statistics, readable without content            | (ignored)                              |
| Bacon          | five binary choices per letter, in any medium   | in the language; the carrier is hidden |
| Chappe / Morse | weighted selections from a codebook or alphabet | split between codebook and language    |

***

**Steering for stage 2 (meaning against measure).** The outline gives Fisher information real weight. It is the measure that is _about_ something (a parameter), the road Shannon didn't take. Fisher information also reappears in 5a: some reconstructions and quantum metrology lean on it.

1. Keep Fisher at full weight, or reduce it to a contrast so more room goes to Shannon–Weaver and Bar-Hillel–Carnap?
2. Do you want Wiener's opposite sign worked in numbers (the same coin seen as order gained versus uncertainty resolved), or stated in a paragraph?
