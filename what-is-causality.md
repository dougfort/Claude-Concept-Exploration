# What Is Causality? — Outline

_Working plan for the twelfth exploration, October 2026. Arc settled before stage 1; open to steering. Steering is recorded below as it is given._

_Entry points, cited rather than repeated: reconstructions-of-quantum-theory.md (no-signalling, PR boxes, information causality); what-is-time.md §3 (Malament: relative, not conventional), §6 (the quantum switch; causal order definite where recorded); what-is-information.md §5 (aboutness as correlation plus a preparation history; every record points to the past); what-is-induction.md §2 (Hume's argument against induction), §6 (taxi.py: a detour is an intervention; the orbit transformer: prediction underdetermines mechanism); what-is-emergence.md §5 4b (Hoel's causal emergence as lumpability under a uniform intervention prior), §5 4a (the commuting square)._

**Steering:** _(none yet)_

***

## Carried in

* **From _Time_:** light-cone order survives relativity as an invariant; simultaneity is relative, not conventional (Malament 1977); the quantum switch makes order indefinite, and "causal order is definite where it is recorded."
* **From _Information_:** mutual information is symmetric; aboutness gets its direction from which system was prepared blank, and blanks come from the low-entropy gradient. Records need three inputs: symmetry, composition, gradient.
* **From _Induction_:** world models show up under intervention, not observation; prediction underdetermines mechanism; AIXI shows prediction doesn't settle action.
* **From _Emergence_:** causal emergence is a summary's quality scored under a chosen intervention prior; a level is a commuting square, which is what an intervention on a macro variable needs to be well defined.
* **The division, eleventh instance expected:** an intervention needs a cut between whatever sets a variable and the system it is set in.

## Working claim to be broken

**Causation is a relation between events in which the earlier produces the later: one directed, absolute order, fixed by the laws.**

Expected to break in four places:

1. **"Produces."** Hume finds no observable production, only regular succession; Russell (1913) finds no cause in the fundamental equations, only time-symmetric functional dependence. Production gets replaced by difference-making under intervention (Woodward; Pearl).
2. **"Fixed by the laws."** The laws are (nearly) time-reversal symmetric; the direction comes from the state: Reichenbach's fork asymmetry, Lewis's asymmetry of overdetermination, the low-entropy past.
3. **"Absolute order."** Relativity keeps an absolute order (the light cone) but drops a global one; quantum theory allows order to be indefinite (the switch) and breaks the classical common-cause principle (Bell, read as causal inference).
4. **"Between events."** Pearl's causation relates variables in a model, at a chosen level of description; the same system can have good and bad causal levels.

## Opening bet (a position to test, not a result)

**The working claim fuses two things. One is a _dependency structure_ fixed by the laws: symmetric in time, saying what can depend on what (light cones, no-signalling, the dynamics' dependency graph). The other is a _direction_, which the laws don't supply and which comes from where the direction of records comes from. An intervention is the preparation of a variable in a state uncorrelated with its own past: writing to a blank. So the do-operator presupposes the same three inputs _Information_ found records need: a correlating dynamics (symmetry), mechanisms that can be changed one at a time (composition; Pearl's modularity), and fresh, uncorrelated sources (gradient).**

Predictions:

* (a) Russell is right about fundamental laws and wrong that causation is dispensable: causal structure returns wherever a system can be divided into a modular mechanism and something that sets its inputs. **Causation is a regime, not a law.**
* (b) Every way of reading causal direction off passive data (forks, colliders, independence of cause and mechanism) needs an independence assumption about initial conditions, and that assumption is the low-entropy past in statistical form.
* (c) In relativity the causal order is absolute but its orientation is a global choice the local laws don't make.
* (d) In quantum theory the classical common-cause principle fails, a quantum version survives, and order is indefinite only where unrecorded; no physically realizable process violates a causal inequality (to be checked).
* (e) For learners: passive prediction can't reach interventional knowledge without assumptions (the causal hierarchy), but text contains records of interventions, so the answer for LLMs is "partly," as in _Induction_.

_Prior work to credit before presenting any of this as new:_ the thermodynamic account of causal direction (Reichenbach 1956; Albert 2000; Loewer 2007; Price, agency and perspectivalism; Ismael); modularity in Woodward (2003) and Pearl. The candidate new framing is the mapping of interventionism's assumptions onto the series' three inputs; search for it before stage 4 states it.

## Open question carried

Is causal direction anything beyond the thermodynamic arrow written into records, and does causal order survive where no record is made?

***

## 1. The intuition — what makes things happen

* Aristotle's four causes; the efficient cause as the one that survives. Brief.
* **Al-Ghazali** (_Incoherence_, c. 1095): fire and cotton, conjunction without necessity; Hume's analysis six centuries early. Malebranche's occasionalism.
* **Newton:** gravity as a law of dependence with no mechanism ("hypotheses non fingo"); action at a distance as the first great dispute over what a cause must be.
* **Hume on necessary connection** (the induction argument cited, not repeated): the billiard balls; the two definitions, constant conjunction and "if the first had not been, the second never had existed," the seed of both regularity and counterfactual accounts.
* **Kant's Second Analogy:** causation as what makes an objective time order (the ship downstream against the house). Links _Time_ §2–3.
* **Laplace's demon:** causation total, and already time-symmetric (the demon sees past and future alike).
* **Mill's methods** (1843): the method of difference as the first statement of a controlled experiment.
* Working example to carry: a **switch and a lamp** (later: a sprinkler, rain, and wet grass).

## 2. The dispute — is there anything to causation beyond the equations?

* **Russell, "On the Notion of Cause" (1913):** the law of causality a relic; physics has functional dependence, symmetric in time. Mach before him.
* **Fisher and the randomized experiment** (1925, 1935): randomization as the invention of a formal intervention; Fisher against the smoking–cancer link (a confounding gene), the dispute that showed correlation could not settle it.
* **Simpson's paradox** worked with small numbers (the kidney-stone data): the same table supports opposite conclusions depending on a causal story the table doesn't contain.
* **Reichenbach** (1956): the common cause principle; the fork asymmetry; the causal theory of time against time as prior.
* **Suppes** (1970) probabilistic causation; **Lewis** (1973, 1979) counterfactuals and the asymmetry of overdetermination.
* **Cartwright** (1979): causal laws are needed for effective strategies; Russell's elimination fails for agents.
* Missing concepts: a formal object for intervention; a representation separating structure from statistics; an account of direction.

## 3. The formalization — causation formalized twice

_Probably 3a / 3b. Two independent lineages: physics formalized the possibility of influence, statistics its actuality._

**3a: causal order in spacetime.** Robb (1914, 1936): Minkowski space axiomatized by a "before" relation alone. Zeeman (1964): maps preserving causal order are Lorentz transformations plus dilations. Hawking–King–McCarthy (1976) and Malament (1977): causal order fixes the conformal geometry, everything but a volume scale. Causal sets (Bombelli–Lee–Meyer–Sorkin 1987): "order plus number equals geometry." Worked: _causet.py_, sprinkling points in a 1+1 diamond and recovering dimension from how many pairs are ordered (Myrheim–Meyer).

**3b: causal models.** Wright's path analysis (1921); Rubin's potential outcomes (1974); Spirtes–Glymour–Scheines and the PC algorithm (1993); Pearl's do-calculus (1995; _Causality_ 2000); Woodward (2003). Worked: chain, fork, and collider on three binary variables; why chain and fork are observationally identical and the collider is not; seeing against doing (conditioning vs. do); Simpson resolved by back-door adjustment. _causal.py_, _simpson.py_.

* Position to argue: the two formalizations answer different questions (what _can_ influence what; what _does_ depend on what under intervention) and meet only at no-signalling.

## 4. The abstraction — causation without production

**4a: direction and level.** Where the arrow comes from: fork asymmetry, Albert–Loewer's Past Hypothesis, Price's perspectivalism, Ismael; independence of mechanism and input (Janzing–Schölkopf) as the statistical trace of the gradient; the bet's three-inputs mapping tested here. Level: macro-causation, exact transformations between causal models (Rubenstein et al. 2017) as the commuting square; causal emergence cited from _Emergence_ §5. _fork.py_ (candidate): a reversible toy dynamics where forks open toward the future only from a low-entropy start.

**4b: quantum causal structure.** Bell as causal discovery: classical causal models of Bell correlations need fine-tuning (Wood–Spekkens 2015); quantum causal models (Costa–Shrapnel 2016; Allen–Barrett–Horsman–Lee–Spekkens 2017; Barrett–Lorenz–Oreshkov 2019) and a quantum common-cause principle; process matrices and causal inequalities (Oreshkov–Costa–Brukner 2012); the switch cited from _Time_ §6; no-signalling and information causality cited from the reconstructions file.

## 5. The payoff

_Before writing: search 2024–26 on each thread. Report what changed the argument; flag recent and untested work._

**5a: physics.** Indefinite causal order, realizability, and time-delocalized subsystems; whether any causal-inequality violation is physical; causal sets and quantum-gravity causal structure; the open question answered or not.

**5b: learners.** Pearl's ladder and the causal hierarchy theorem (Bareinboim–Correa–Ibeling–Icard); Richens–Everitt (2024), robust agents must learn causal models; causal representation learning; LLM causal reasoning evaluations; _taxi.py_ revisited as the interventional test.

***

## Side-file candidates (settle before stage 2)

* **Causal graphs in plain terms** (strong): d-separation, the three rules of do-calculus, back-door and front-door, the PC algorithm, with _causal.py_. Technical home for 3b, as the RG file was for _Emergence_.
* **The arrows of time** (candidate, cross-exploration, written at the close): thermodynamic, radiative, record, causal, and intervention arrows, and which reduce to which. Touched by _Entropy_, _Time_, _Information_, and this exploration.
* **Quantum causal models and process matrices** (candidate): only if 4b overflows; otherwise the reconstructions file plus 4b suffice.
* _Overflow only:_ the causal theory of spacetime (Robb to causal sets), if 3a overflows.

## Planned scripts (pure Python, no libraries)

* _simpson.py_: kidney-stone table; naive vs. adjusted comparison.
* _causal.py_: sample chain, fork, collider; independence tests; seeing vs. doing; a small PC run.
* _causet.py_: sprinkle in a 1+1 causal diamond; ordering fraction; dimension estimate.
* _fork.py_ (candidate): fork asymmetry from a low-entropy initial state.
* Reused: _gpt.py_ (PR boxes), _taxi.py_ (detours), _qsim.py_ (the switch).

## Threads to carry in

The division; the record; the copy; three inputs; regimes, not laws; prediction underdetermines mechanism; the commuting square; the bias (the intervention prior); locality; law vs. state; symmetry as the source of a number (time-reversal symmetry of laws).

## Guardrails

* Hume's induction argument, the switch's worked example, causal emergence, PR boxes, and information causality are cited, not redone.
* Philosophy of causation (Lewis, mechanisms, metaphysics of powers) capped at what stages need.
* LLM claims sourced and dated; Claude's sense of how it works is not evidence.
