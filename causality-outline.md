# What Is Causality? — Outline

_Working plan for the twelfth exploration, October 2026. Arc settled before stage 1; open to steering. Steering is recorded below as it is given._

_Entry points, cited rather than repeated: reconstructions-of-quantum-theory.md (no-signalling, PR boxes, information causality); what-is-time.md §3 (Malament: relative, not conventional), §6 (the quantum switch; causal order definite where recorded); what-is-information.md §5 (aboutness as correlation plus a preparation history; every record points to the past); what-is-induction.md §2 (Hume's argument against induction), §6 (taxi.py: a detour is an intervention; the orbit transformer: prediction underdetermines mechanism); what-is-emergence.md §5 4b (Hoel's causal emergence as lumpability under a uniform intervention prior), §5 4a (the commuting square)._

**Steering (2026-10-29, before stage 1):** selective prehistory in stage 1; spacetime order (3a) and statistical intervention (3b) at equal weight; **all four side files** to be written: _Causal graphs in plain terms_, _The arrows of time_ (at the close), _Quantum causal models and process matrices_, and _The causal theory of spacetime_ (Robb to causal sets; no longer overflow-only, so 3a can defer technical lineage to it); stage 5 weighted toward **learners** (5a physics kept short; 5b the main payoff, continuing the AGI-Chronicles thread).

**Stage 1 note (2026-10-29):** _billiards.py_ added (Hume's billiard balls as a reversible program; Hume's counterfactual definition computed in both film directions).

**Steering (2026-10-30, before stage 2):** Russell compact; _simpson.py_ built in stage 2 (reused in 3b for back-door adjustment); Lewis in one paragraph.

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

_Prior work to credit before presenting any of this as new:_ the thermodynamic account of causal direction (Reichenbach 1956; Albert 2000; Loewer 2007; Price, agency and perspectivalism; Ismael); modularity in Woodward (2003) and Pearl; Lewis (1979) on the asymmetry of overdetermination, which already ties counterfactual direction to the abundance of future traces. The candidate new framing is the mapping of interventionism's assumptions onto the series' three inputs; search for it before stage 4 states it.

## Open question carried

Is causal direction anything beyond the thermodynamic arrow written into records, and does causal order survive where no record is made?

***

## 1. The intuition — what makes things happen _(done)_

Aristotle's efficient cause; al-Ghazali's fire and cotton; Newton's law without mechanism; Hume's two definitions, with _billiards.py_; Kant's ship and house; Laplace's demon; Mill's method of difference (the switch and the lamp; `git bisect`).

## 2. The dispute — is there anything to causation beyond the equations?

* **Russell, "On the Notion of Cause" (1912–13), compact.**
* **Fisher and the randomized experiment** (1925, 1935); Fisher against the smoking–cancer link; Cornfield's inequality (1959) as the first sensitivity analysis.
* **Simpson's paradox**: the kidney-stone data, _simpson.py_.
* **Reichenbach** (1956): common cause principle; the fork asymmetry.
* **Suppes** (1970) in brief; **Lewis** (1973, 1979) in one paragraph.
* **Cartwright** (1979): effective strategies.
* Missing concepts.

## 3. The formalization — causation formalized twice

_3a / 3b at equal weight (steering). Two independent lineages: physics formalized the possibility of influence, statistics its actuality._

**3a: causal order in spacetime.** Robb (1914, 1936): Minkowski space axiomatized by a "before" relation alone. Zeeman (1964): maps preserving causal order are Lorentz transformations plus dilations. Hawking–King–McCarthy (1976) and Malament (1977): causal order fixes the conformal geometry, everything but a volume scale. Causal sets (Bombelli–Lee–Meyer–Sorkin 1987): "order plus number equals geometry." Worked: _causet.py_, sprinkling points in a 1+1 diamond and recovering dimension from how many pairs are ordered (Myrheim–Meyer). Technical lineage deferred to _The causal theory of spacetime_.

**3b: causal models.** Wright's path analysis (1921); Rubin's potential outcomes (1974); Spirtes–Glymour–Scheines and the PC algorithm (1993); Pearl's do-calculus (1995; _Causality_ 2000); Woodward (2003). Worked: chain, fork, and collider on three binary variables; why chain and fork are observationally identical and the collider is not; seeing against doing (conditioning vs. do); Simpson resolved by back-door adjustment, reusing _simpson.py_. _causal.py_. Technique deferred to _Causal graphs in plain terms_.

* Position to argue: the two formalizations answer different questions (what _can_ influence what; what _does_ depend on what under intervention) and meet only at no-signalling.

## 4. The abstraction — causation without production

**4a: direction and level.** Where the arrow comes from: fork asymmetry, Albert–Loewer's Past Hypothesis, Price's perspectivalism, Ismael; independence of mechanism and input (Janzing–Schölkopf) as the statistical trace of the gradient; the bet's three-inputs mapping tested here. Level: macro-causation, exact transformations between causal models (Rubenstein et al. 2017) as the commuting square; causal emergence cited from _Emergence_ §5. _fork.py_ (candidate): a reversible toy dynamics where forks open toward the future only from a low-entropy start; also friction added to _billiards.py_ as the tell the two-ball film lacks.

**4b: quantum causal structure.** Bell as causal discovery: classical causal models of Bell correlations need fine-tuning (Wood–Spekkens 2015); quantum causal models (Costa–Shrapnel 2016; Allen–Barrett–Horsman–Lee–Spekkens 2017; Barrett–Lorenz–Oreshkov 2019) and a quantum common-cause principle; process matrices and causal inequalities (Oreshkov–Costa–Brukner 2012); the switch cited from _Time_ §6; no-signalling and information causality cited from the reconstructions file. Detail deferred to _Quantum causal models and process matrices_.

## 5. The payoff

_Before writing: search 2024–26 on each thread. Report what changed the argument; flag recent and untested work. Weighted toward learners (steering)._

**5a: physics (short).** Indefinite causal order, realizability, and time-delocalized subsystems; whether any causal-inequality violation is physical; causal sets and quantum-gravity causal structure; the open question answered or not.

**5b: learners (main).** Pearl's ladder and the causal hierarchy theorem (Bareinboim–Correa–Ibeling–Icard); Richens–Everitt (2024), robust agents must learn causal models; causal representation learning; LLM causal reasoning evaluations; _taxi.py_ revisited as the interventional test. Feeds a possible addendum to the post's argument map.

***

## Side files (settled 2026-10-29: all four)

* **Causal graphs in plain terms**: d-separation, the three rules of do-calculus, back-door and front-door, the PC algorithm, with _causal.py_. Technical home for 3b.
* **The causal theory of spacetime**: Robb, Zeeman, Hawking–King–McCarthy, Malament, causal sets, _causet.py_. Technical home for 3a.
* **Quantum causal models and process matrices**: Wood–Spekkens, quantum common causes, process matrices, causal inequalities, realizability. Technical home for 4b.
* **The arrows of time** (cross-exploration, written at the close): thermodynamic, radiative, record, causal, and intervention arrows, and which reduce to which. Touched by _Entropy_, _Time_, _Information_, and this exploration.

## Planned scripts (pure Python, no libraries)

* _billiards.py_ (stage 1, done): reversible two-ball collisions; counterfactual dependence in both film directions.
* _simpson.py_ (stage 2, done): kidney-stone table; adjusted comparison; simulated observational study vs. randomized trial; the same counts under a mediator story.
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
