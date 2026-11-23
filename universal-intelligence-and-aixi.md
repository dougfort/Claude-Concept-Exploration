# Universal Intelligence and AIXI

_Side file to_ what-is-intelligence.md, _written at the close of the Intelligence exploration, November 2026. What has to be added to Solomonoff's predictor to make an agent, and what Legg and Hutter's definition of intelligence measures, worked on three tiny environments. Builds on_ solomonoff-and-the-universal-prior.md _(cite, don't repeat). Runnable companion:_ aixi_toy.py.

***

## 1. From predictor to agent

Solomonoff's predictor (_solomonoff-and-the-universal-prior.md_) watches a sequence and predicts the next symbol, weighting every program that fits the data by 2^(−length). It never acts.

An **agent** lives in a loop: it chooses an action, the environment returns an observation and a **reward**, and the loop repeats. To choose, it needs two things the predictor lacks:

* **a goal:** the reward signal, supplied by the environment;
* **a planning rule:** look ahead over possible action sequences and pick the one with the highest expected total reward.

***

## 2. AIXI in words

Hutter's AIXI (2000; _Universal Artificial Intelligence_, 2005) combines the two:

> At each step, consider every computable environment consistent with what has happened so far, weighted by 2^(−length of its shortest program). For each possible sequence of future actions, average the reward those environments would give. Take the first action of the best sequence.

Compression enters in one place only: the weighting of environments. The goal (reward) comes from outside.

**Properties.**

* **Uncomputable**, like Solomonoff's predictor. AIXItl (time- and length-bounded) is computable and hopelessly slow; MC-AIXI-CTW (Veness et al. 2011) approximated it with Monte Carlo search and context-tree weighting and learned small games such as a partially observable Pac-Man.
* **Wireheading** (Ring–Orseau 2011): an agent able to tamper with its reward channel prefers to. The goal can be gamed.
* **Laziness under bad priors** (Leike–Hutter 2015): with a bad enough reference machine, AIXI may judge exploration too risky and never test its beliefs. Prediction plus a goal doesn't guarantee exploration.

***

## 3. Universal intelligence

Legg and Hutter ("Universal Intelligence: A Definition of Machine Intelligence," 2007) surveyed about seventy informal definitions, distilled them as the ability to achieve goals in a wide range of environments, and made it a formula:

> **Υ(agent) = Σ over environments of 2^(−K(environment)) × V(agent, environment)**

where K is the environment's complexity and V the agent's expected reward there. AIXI maximizes Υ by construction.

***

## 4. Worked: three tiny environments

_aixi_toy.py._ Each environment hides a repeating pattern of correct actions; reward is 1 when the action matches. Actions are binary, so the reward also tells the agent the right action.

| environment           | pattern | K      | weight 2^−K |
| --------------------- | ------- | ------ | ----------- |
| A, "always 0"         | 0       | 3 bits | 0.1250      |
| B, "alternate"        | 0 1     | 5 bits | 0.0312      |
| C, "two ones, a zero" | 1 1 0   | 8 bits | 0.0039      |

Three agents, 12 steps each (random averaged over 200 runs):

* **always-0**, a specialist for the simplest world;
* **random**, coin flips;
* **occam**, a miniature Solomonoff learner: it weights every repeating pattern of period 1–4 by 2^−(2 + 2 × period), drops those the rewards contradict, and acts on the weighted vote.

```
agent         A(3)    B(5)    C(8)         U
always-0     1.000   0.500   0.333    0.1419
random       0.502   0.476   0.515    0.0797
occam        1.000   0.917   0.833    0.1569
```

**Readings.**

1. The learner wins, but narrowly: 0.157 against 0.142. Environment A carries 4 times B's weight and 32 times C's, so a specialist perfect in A is nearly as "intelligent" as a learner good everywhere. **Υ is dominated by the simplest environments.** (Stage 3b's specialist-versus-generalist example showed the same with invented numbers.)
2. The learner's losses are its learning: it needs a step or two to rule out simpler patterns in B, a few more in C. Its reward in C (0.833) is a prequential curve in miniature.

**Changing the reference machine.** Part 2 keeps every agent and every environment and changes only which pattern counts as simple (C becomes 3 bits, A 8):

```
agent         A(8)    B(5)    C(3)         U
always-0     1.000   0.500   0.333    0.0612
random       0.502   0.476   0.515    0.0812
occam        1.000   0.917   0.833    0.1367
```

The specialist falls **below random**. Nothing about the agents changed; only the measuring stick. This is the C-test's lesson (_ctest.py_: the test-maker's language scores 100%) and Leike–Hutter's, in a few lines of output.

***

## 5. Against Chollet

|            | Legg–Hutter Υ               | Chollet (2019)                                |
| ---------- | --------------------------- | --------------------------------------------- |
| reference  | a universal Turing machine  | human Core Knowledge priors                   |
| scores     | reward across environments  | skill gained per bit of priors and experience |
| priors     | free (built into the agent) | charged                                       |
| experience | free (any number of steps)  | charged                                       |
| computable | no                          | no (ARC is the proxy)                         |

_Position:_ both must choose a reference, and both say so. Legg–Hutter's choice is formally neutral and empirically arbitrary (Part 2); Chollet's is anthropocentric and fixed. Υ measures how much reward an agent collects, not how efficiently it learned to collect it; that is the difference the exploration's endpoint turns on (a rate, not a level).

***

## 6. Positions taken

* AIXI states its goal openly; compression only weights the environments.
* Prediction plus a goal is not enough without exploration, and the goal can be gamed.
* Universal intelligence is dominated by the simplest environments, so a specialist in simple worlds can rival a learner.
* Changing the reference machine can rerank agents with nothing about them changed (_aixi_toy.py_ Part 2).
* Υ is a level (reward collected); Chollet's measure is a rate (reward bought per bit), and the rate is the better definition.

***

## Suggested next steps

* Give _aixi_toy.py_ a fourth environment with a period-5 pattern and see how little it changes Υ.
* Add an agent that learns but starts with a wrong strong prior (it believes "always 1" with weight 0.9); compare its rewards to occam's, the _prequential.py_ lesson in agent form.
* Charge each agent for experience: score reward over the last 4 steps only, after 8 steps of learning, and see whether the ranking moves toward Chollet's.
* Reading: Legg and Hutter, "Universal Intelligence" (_Minds and Machines_, 2007), §1–4; Legg's thesis _Machine Super Intelligence_ (2008), ch. 2–4; Leike and Hutter, "Bad Universal Priors and Notions of Optimality" (COLT 2015); Veness et al., "A Monte-Carlo AIXI Approximation" (_JAIR_, 2011).
