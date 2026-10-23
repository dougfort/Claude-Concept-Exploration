# Emergence from next-token prediction — starting point

## Origin
Prompted by the epilogue of Kevin Roose's *The AGI Chronicles* (2026). Roose describes the generality of LLMs, which arose from next-token prediction, as an "inexplicable, cosmic accident." We are examining that claim on its own terms, independent of the book.

## Working position (Claude's, open to challenge)
**Not an accident, but still largely unexplained.**
- *Not an accident:* next-token prediction was chosen because researchers believed prediction and understanding are deeply linked. Lineage: Shannon's prediction experiments on English (1948/1951); Solomonoff induction and compression-as-intelligence (Hutter Prize, 2006); OpenAI's "sentiment neuron" (2017); GPT-2 and unsupervised multitask learning (2019).
- *Still unexplained:* the argument that "a perfect predictor must model the world" applies to an ideal predictor. It does not show that a finite network trained by gradient descent will find a world model rather than shallow shortcuts. Why over-parameterized networks generalize so well is an open problem in deep-learning theory.

## Threads
1. **History:** how "prediction implies understanding" ran from Shannon to the scaling bet.
2. **The gap:** optimal-predictor arguments vs. what trained networks actually do. Key source: Zhang et al. 2017, which showed networks can fit random labels, so classical complexity measures can't explain why they generalize. *(Recommended first.)*
3. **Is emergence real?** Wei et al. 2022 vs. Schaeffer et al. 2023 (measurement artifact); grokking (Power et al. 2022); induction heads (Olsson et al. 2022).
4. **The physics connection:** Anderson, "More Is Different" (1972); phase transitions and order parameters; scaling laws vs. critical phenomena; Michaud et al. 2023, the quantization model of neural scaling.
5. **What "emergence" means:** weak vs. strong emergence. "Cosmic" implies the strong kind.

## Open questions for Fog
- How technical should this get (conceptual vs. real stat mech / information theory)?
- Which thread to start with?
- Study for its own sake, or headed toward Substack/Tumblr posts?

## Primary sources (in project files)
| Thread | Source | Where to get it |
|---|---|---|
| 1 | Shannon, "Prediction and Entropy of Printed English," *Bell System Technical Journal* 30(1), 1951 | sites.socsci.uci.edu/~rfutrell/teaching/itl-davis/readings/shannon1951prediction.pdf |
|  |              |  |
| 2 | Zhang, Bengio, Hardt, Recht, Vinyals, "Understanding Deep Learning Requires Rethinking Generalization," ICLR 2017 | arxiv.org/abs/1611.03530 |
| 3 | Wei et al., "Emergent Abilities of Large Language Models," TMLR 2022 | arxiv.org/abs/2206.07682 |
| 3 | Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?," NeurIPS 2023 | arxiv.org/abs/2304.15004 |
| 3 | Power et al., "Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets," 2022 | arxiv.org/abs/2201.02177 |
| 3 | Olsson et al., "In-context Learning and Induction Heads," 2022 | arxiv.org/abs/2209.11895 |
| 4 | Anderson, "More Is Different," *Science* 177(4047):393–396, 1972 | mit.edu/~kardar/research/seminars/EPB/PWA-Science72.pdf |
| 4 | Michaud, Liu, Girit, Tegmark, "The Quantization Model of Neural Scaling," NeurIPS 2023 | arxiv.org/abs/2303.13506 |

## Caveat
Claude is an instance of the systems being studied. Its intuitions about how it works are not evidence.
