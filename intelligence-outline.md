# Stage 1: The intuition, quick wit and economy of thought

I've recorded your steering in _intelligence-outline.md_. Stage 1 follows. It's selective prehistory, with the brain half and the machine half at equal weight. There are five roots, and each one turns out to be ancestor to one of Grant's claims or to one part of the working claim.

## 1.1 Aristotle: intelligence as a speed

Aristotle has two words where we have one. _Nous_ is the grasp of first principles, a standing capacity. _Anchinoia_, "quick wit," gets one sentence near the end of the _Posterior Analytics_ (I.34). It is the ability to hit on the middle term instantly, meaning the term that explains why something holds. His example: someone notices that the moon's bright side always faces the sun and grasps the cause at once, namely that the moon borrows its light. Moving straight from the observation to the explanation is the talent.

**Position:** the first definition of intelligence in the Western record is a rate, not a stock: how quickly you find the explanation, not how much you know. _Nous_ is the level, _anchinoia_ the rate, and Aristotle kept them apart. The working claim merges them, and the opening bet sides with _anchinoia_.

Hobbes (1651) said reasoning is reckoning, and Leibniz dreamed of settling disputes by calculation. Both are covered in _what-is-computation.md_ §1. They matter here only for the assumption that thinking is something you can do by mechanical steps.

## 1.2 Mach: understanding as compression, 1865 and 1882

Ernst Mach supplies both halves of the exploration, decades apart.

**The brain half (1865).** Mach reported that where a smooth ramp of brightness meets a flat field, people see a bright or dark stripe that isn't in the light: the Mach bands. The visual system exaggerates edges. Stage 3a will show that this is what a predictive code does. Here is the idea on one line of a photograph, the example we'll carry through the exploration:

```
pixels:              100  102  103  103  105  180  182  181
predict "same as
previous"; residual:  —   +2   +1    0   +2  +75   +2   −1
```

Raw, that's 8 pixels × 8 bits = **64 bits**. Now send the first pixel in full, then only the residuals. Use a 1-bit flag plus 3 bits for small residuals (−4 to +3), and the flag plus 8 bits otherwise. That's 8 + (6 × 4) + (1 × 9) = **41 bits**. The only expensive residual sits at the edge. A code that sends what the prediction got wrong mostly sends the edges. A retina does something closely related: it compares each point with its neighbours on both sides, so it signals where the slope changes, which is exactly where Mach saw his bands. That's the standard textbook account. Stage 3a will check how far it holds, and _residual.py_ will run it.

**The machine half (1882).** In his lecture "The Economical Nature of Physical Inquiry," and again in _Die Mechanik_ (1883), Mach argued that science is economy of thought. A law is a way of not having to remember the cases. His own example was refraction. Instead of tables of how much light bends at every angle, you keep one rule:

* **The table:** angles of incidence 0° to 89° in steps of 1°, each with its refraction angle to 0.1°. That's 90 numbers at about 10 bits each, roughly **900 bits**.
* **The law:** sin(incidence) = n × sin(refraction), with n = 1.33 for water. That's one constant at about 10 bits, plus the rule.

Check it on two angles:

* 30° in: sin 30° = 0.5, and 0.5 / 1.33 = 0.376, so the ray leaves at **22.1°**.
* 60° in: sin 60° = 0.866, and 0.866 / 1.33 = 0.651, so it leaves at **40.6°**.

The law also gives angles nobody measured, and changing one number (n = 1.5) covers glass. The compression generalizes. Grant's "understanding is something becoming smaller in my mind" is Mach's position nearly word for word.

**The twist.** Mach used economy of thought to argue against atoms. He thought positing unseen entities added to the description, so a scientist should treat atoms as a convenience at most. Boltzmann fought him over this for years. Within a few years of Boltzmann's death in 1906, Perrin had measured Avogadro's number by more than ten independent methods and found they agreed.

**Position (not claimed as new):** Mach's measure was right and his bookkeeping was wrong. In two-part code terms (_compression-is-prediction.md_ §5), the atomic hypothesis costs something once, as part of the model. It then shortens an enormous amount of data: chemistry's fixed combining proportions, the gas laws, specific heats, Brownian motion. Mach charged for the model and never credited the savings. That also settles a tension inside Grant's argument. His first claim says good prediction needs "a coherent model of what's going on"; his second says smaller is better. Mach thought those conflicted. They don't: once the data are rich enough, a model of what's really going on is what the shortest description looks like.

## 1.3 Helmholtz: perception as inference, 1867

Helmholtz published the energy-conservation paper of 1847, so he's one of the real authors of the concept Grant used as his analogy. Twenty years later, in volume 3 of the _Handbook of Physiological Optics_ (1867), he proposed that perception is unconscious inference. Sensations are signs, not pictures. The mind infers from the signs to their most likely cause, without knowing it is doing so.

His standard example: press gently on the outer side of a closed eye, and you see a spot of light on the opposite side of your visual field. The pressure stimulates the retina in a spot that normally receives light from that opposite direction. Your brain infers the usual cause, even though you know the real one. The inference is fast, automatic, and can't be overridden by knowledge.

This is the ancestor of predictive processing, which Grant summarizes as the brain sending predictions down and only errors up. Helmholtz said nothing about economy. His point was that a perceiver models the causes behind the signals, which is what Mach declined to do.

**Position:** Mach and Helmholtz split the idea between them. Mach had the measure (shortness) without the hidden causes. Helmholtz had the hidden causes without the measure. Predictive coding is Helmholtz's picture, inference to causes, scored by Mach's measure, bits saved. That merger doesn't happen until Barlow and Attneave in the 1950s, which is why stage 3a starts there.

## 1.4 Spearman and Binet: one number or many?

In 1904 Charles Spearman looked at schoolchildren's marks in classics, French, English and mathematics, alongside tests such as pitch discrimination. He found that every pair of scores correlated positively, with no negatives. He explained the pattern with one general factor, _g_, plus a specific factor for each test.

Spearman's _g_ is itself a compression, of data about people rather than data from the world. Suppose three tests have loadings 0.9, 0.8 and 0.7 on _g_. A loading is how strongly a test tracks the general factor, and the one-factor model predicts each correlation as the product of two loadings:

| Pair          | Predicted correlation |
| ------------- | --------------------- |
| tests 1 and 2 | 0.9 × 0.8 = 0.72      |
| tests 1 and 3 | 0.9 × 0.7 = 0.63      |
| tests 2 and 3 | 0.8 × 0.7 = 0.56      |

With three tests, three loadings reproduce three correlations, so nothing is saved. With ten tests, ten loadings reproduce **45** correlations, if the model fits. The first measurement of intelligence was a short description of a correlation table.

A year later Alfred Binet and Théodore Simon built their scale of 30 graded tasks to find children who needed extra help at school. Binet explicitly refused to treat intelligence as a single quantity like height. So the "one measure" in the working claim was disputed from the beginning.

**Position:** _g_ is a fact about a correlation table, the fact that all the correlations are positive. Whether it is also a single thing inside the head is a separate question, and that question is stage 2's dispute. The side file _measuring-intelligence.md_ will carry the factor analysis and Thomson's demonstration (1916) that many small independent "bonds" produce the same table with no single factor.

## 1.5 Turing: replace the definition with a test, 1950

Turing's "Computing Machinery and Intelligence" (1950) opens by setting aside "Can machines think?" as too meaningless to discuss and substitutes the imitation game. Two things in it matter here.

1. **The test is behavioural.** It judges a system by what it does in an exchange, not by any internal description. That's closer to _action_ than to compression, and action is the piece the working claim leaves out.
2. **The paper's last section is about learning.** Turing proposes building a "child machine" and educating it rather than programming an adult mind. Grant's third claim, that learning fast is intelligence, sits at the end of the founding paper of AI.

## What the intuition contains

| Root                     | Idea                                                 | Becomes                                   |
| ------------------------ | ---------------------------------------------------- | ----------------------------------------- |
| Aristotle, _anchinoia_   | intelligence as the speed of finding the explanation | Grant's claim 3; the opening bet's "rate" |
| Mach, economy of thought | understanding as a shorter description               | Grant's claim 2; MDL                      |
| Mach bands, Helmholtz    | perception as prediction of hidden causes            | Grant's claim 1; predictive processing    |
| Spearman, Binet          | one measure, or many?                                | the working claim's "one measure for all" |
| Turing                   | judge by behaviour; build a learner                  | the action gap; learning as central       |

So the working claim, "intelligence is compression, one measure for all," takes Mach's economy and Spearman's single number and drops the other three roots: Aristotle's speed, Helmholtz's hidden causes and Turing's behaviour. My expectation is that the genealogy will put them back.

**Positions taken in this stage**

* The first definition of intelligence was a rate (_anchinoia_), not a level (_nous_).
* Mach's measure was right and his bookkeeping wrong: atoms cost bits once and saved far more. A model of what's really going on is what a short description becomes when the data are rich.
* Predictive coding is Helmholtz's inference scored by Mach's measure.
* _g_ is a compression of a correlation table, so whether it is a single thing in the head is a further question.
* Turing's founding paper puts behaviour and learning at the centre, not stored knowledge.

**Steering for stage 2.** I plan two strands of equal length:

* **Machines and tests:** Spearman against Thomson and Thurstone, Boring's "what the tests test," Turing, Dartmouth, symbols against neural networks, and Searle in a paragraph.
* **Brains:** Helmholtz against Gibson's direct perception, with Craik's "small-scale models" (1943) as the bridge.

Both end on what the dispute lacked: a measure of structure that doesn't depend on any particular test. Would you rather put more weight on one strand? And should Searle stay at a paragraph or be dropped?
