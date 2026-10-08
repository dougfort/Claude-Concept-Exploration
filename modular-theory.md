# Modular Theory: The State Defines the Time

_Side-file notes, October 2026. Written at the close of the time exploration (stage 4b), kept as a reference because both Space and Time now rest on it._

***

## 1. The idea in one sentence

**Give an observer an algebra of observables and a state that assigns no outcome probability zero; the pair determines a flow under which the state is in thermal equilibrium.**

Nothing else is supplied: no Hamiltonian, no clock, no time parameter. The flow is called the _modular flow_, its generator the _modular Hamiltonian_. Whether that flow is physical time is a separate claim (the thermal time hypothesis). The construction itself is a theorem.

***

## 2. The construction with a density matrix

**Ingredients.**

* An algebra M: what the observer can measure. For one qubit with full access, all 2×2 matrices.
* A faithful state ρ: every eigenvalue strictly positive.

**Steps.**

1. Write the state as an exponential: ρ = e^(−K), so K = −log ρ. This K is the modular Hamiltonian.
2. Use K as if it were a Hamiltonian: σ\_s(X) = e^(−iKs) X e^(iKs) = ρ^(is) X ρ^(−is).
3. ρ commutes with itself, so the flow leaves ρ unchanged. Every faithful state is stationary under its own flow.

**Worked example.** ρ = diag(0.8, 0.2).

* K = diag(−log 0.8, −log 0.2) ≈ diag(0.223, 1.609). Only the gap matters: log 4 ≈ 1.386.
* Diagonal observables don't move.
* The off-diagonal observable |0⟩⟨1| becomes 4^(is)|0⟩⟨1|: it rotates at frequency log 4 per unit of modular time.

Now give the qubit a real Hamiltonian H = diag(0, ε) and suppose ρ is its thermal state at inverse temperature β. Then 0.8/0.2 = e^(βε), so βε = log 4, and the modular rotation is the physical rotation with time rescaled by β. **For a thermal state, modular flow is ordinary time evolution, with temperature as the exchange rate.**

**Three boundary cases.**

| State                           | Modular flow           | Reading                           |
| ------------------------------- | ---------------------- | --------------------------------- |
| Pure, diag(1, 0)                | undefined (log 0)      | no uncertainty, no flow           |
| diag(0.8, 0.2)                  | nontrivial             | uncertain but not uniform: a time |
| Maximally mixed, diag(0.5, 0.5) | trivial (K ∝ identity) | infinite temperature: no time     |

***

## 3. The same thing without a density matrix

In quantum field theory a region's algebra is type III (Space, stage 4): no trace, no density matrix, infinite entanglement across the boundary. K = −log ρ can't be written. The construction survives by working with a vector in a larger space.

**Two-qubit model.** |Ω⟩ = √0.8 |00⟩ + √0.2 |11⟩, and M = all operators on qubit A.

* _Cyclic_: A's operators applied to |Ω⟩ reach every state of both qubits.
* _Separating_: no nonzero operator on A sends |Ω⟩ to zero.
* Both hold exactly when every Schmidt coefficient is nonzero.

**Tomita's operator.** Define S by S X|Ω⟩ = X†|Ω⟩ for every X in M: "take the adjoint, at the level of states." Split it as S = J Δ^(1/2).

* **Δ (modular operator)** = ρ\_A ⊗ ρ\_B^(−1). Its powers run A's flow forward and B's backward; restricted to A, they give σ\_s from §2.
* **J (modular conjugation)** swaps A and B with complex conjugation. It maps the observer's algebra onto the commutant: everything the observer can't touch.

Δ and J were built from |Ω⟩ and M alone. Every step works in type III. In field theory the vacuum is cyclic and separating for any local region (Reeh–Schlieder), so **every region of spacetime, with the vacuum, carries its own modular flow**.

***

## 4. The theorems

* **Tomita (1967), Takesaki (1970).** For any von Neumann algebra and cyclic separating vector: Δ^(is) M Δ^(−is) = M, and J M J = M′ (the commutant). The modular flow is always a symmetry of the observer's algebra; J is a mirror between inside and outside.
* **KMS condition** (Kubo 1957; Martin–Schwinger 1959; Haag–Hugenholtz–Winnink 1967). Equilibrium without a density matrix: ⟨A B(t + iβ)⟩ = ⟨B(t) A⟩. For infinite systems this is the definition of thermal equilibrium.
* **Takesaki.** Every faithful state is KMS for its own modular flow (temperature 1, in a sign convention). Every faithful state is thermal relative to some time: its own.
* **Connes's cocycle theorem (1973).** Different faithful states on one algebra have modular flows differing only by inner transformations. Up to those, **the algebra itself carries a canonical flow**. Connes used its spectrum to classify type III factors (III₀, III\_λ, III₁). Local algebras of relativistic field theory are type III₁.
* **Araki's relative entropy (1976).** S(ψ‖φ) is defined from the relative modular operator Δ\_{φ,ψ}. For density matrices it reduces to Tr ρ(log ρ − log σ). Unlike entanglement entropy, it stays finite in type III, which is why entropy _differences_ survive where entropies don't.
* **Takesaki duality (1973).** The crossed product of a type III algebra by its modular flow is semifinite (type II∞): a trace exists. This is the mathematical core of the crossed-product constructions in §5.

**The ordering asymmetry, in numbers.** With ρ = diag(0.8, 0.2), σ₊ = |0⟩⟨1|, σ₋ = |1⟩⟨0|:

* ⟨σ₊σ₋⟩ = 0.8 and ⟨σ₋σ₊⟩ = 0.2. The ratio 4 = e^(βε) is the temperature, and the asymmetry is the flow's orientation.
* In the maximally mixed state both are 0.5. A tracial state, ω(ab) = ω(ba), has no ordering asymmetry, no orientation, and a trivial flow.

***

## 5. Where the series uses it

* **Bisognano–Wichmann (1975–76).** For the Rindler wedge and the Minkowski vacuum, the modular flow is a Lorentz boost and J is CPT. Matching modular time to an accelerated observer's proper time gives T = a/2π: the Unruh effect with no detector model. The same structure gives Hawking and Gibbons–Hawking temperatures.
* **Thermal time (Connes–Rovelli 1994; Time 4b).** Physical time is the modular flow of the physical state. Correct where the state is locally thermal; with two subsystems at different temperatures, the flow gives each its own rate and no single time serves both. A regime, not a law.
* **Entropy as generator (Time 4b).** ⟨K⟩ = −Tr ρ log ρ = S. The operator that generates the flow has the entropy as its average. Positive-temperature KMS states are exactly the completely passive ones (Pusz–Woronowicz 1978): no cyclic process extracts work. The orientation of modular flow is a form of the second law, statically.
* **The crossed product and the observer (Space 5; Time 4b, 5b).** Add an observer's clock and impose the constraint H + H\_obs = 0. The invariant algebra is the crossed product of the type III algebra by its modular flow (Takesaki duality → type II∞). In de Sitter, bounding the clock's energy below (Pauli) cuts it to type II₁: a maximum-entropy state exists, it is tracial, and its modular flow is trivial. Without a clock, the invariant algebra is trivial.
* **Observer-dependence (Time 5b).** Different clocks are different quantum reference frames, giving different crossed products and different entropies (De Vuyst–Eccles–Höhn–Kirklin 2025).

**Open, as of October 2026.** Whether the de Sitter tracial state survives beyond a scrambling time is contested: a July 2026 preprint argues the Hartle–Hawking state is not a trace on the crossed product once horizon shockwave effects are included. With a dynamical cosmological constant, there may be no maximum-entropy state at all (type II∞).

***

## 6. Positions

* **Modular theory is the formal content of "time is relational."** Page–Wootters needs a clock factor; modular theory needs a subalgebra. Both need a division and neither derives one. A global pure state with the full algebra has no modular flow, exactly as an unconditioned Wheeler–DeWitt state has no evolution.
* **The state does the work the law used to do.** Newton's time was the parameter in which the laws hold; modular time is the parameter in which the _state_ is at equilibrium. This is the law-versus-state thread at its sharpest.
* **Temperature is a conversion rate between clocks.** β converts modular time to the Hamiltonian's time. Infinite temperature means the state supplies no time; zero temperature (a pure state) means the construction fails. Time lives in between.
* **It is a symmetry result of the Curry–Howard kind:** the state, the flow, and the equilibrium condition are three descriptions related by an exact dictionary. What it doesn't settle is whether the modular flow is _the_ time or _a_ time; that is the thermal time hypothesis, and the evidence (Time 4b) says: the time, where the state is locally thermal.

***

## 7. Where it came from

* **Murray–von Neumann (1936–43).** Rings of operators and the type classification (I, II, III). Type III was a curiosity; its examples were hard to construct.
* **Kubo, Martin–Schwinger (1957–59).** The KMS condition, in condensed-matter calculations, as a property of thermal Green's functions.
* **Haag–Hugenholtz–Winnink (1967).** KMS as the definition of equilibrium for infinite systems; thermal states shown to be type III.
* **Tomita (1967).** The construction, in lecture notes not widely read at first.
* **Takesaki (1970).** Clarified and published Tomita's theory and proved the KMS connection. Physics and mathematics found the same object independently.
* **Araki (1964–76)** in the physics of local algebras; relative entropy.
* **Connes (1973).** The cocycle theorem and the classification of type III factors; Fields Medal 1982.
* **Bisognano–Wichmann (1975–76), Unruh (1976).** The modular flow of a wedge is a boost; the vacuum is thermal for accelerated observers.
* **Connes–Rovelli (1994).** Thermal time.
* **Witten; Chandrasekaran–Longo–Penington–Witten (2022–23).** Crossed products and observers in gravity; modular theory moves from mathematical physics into quantum gravity.

***

## 8. Links

* _Space_ §4: the type classification and Reeh–Schlieder; §5: the crossed product and the observer in de Sitter.
* _Time_ 4b: the construction and thermal time; 5b: the tracial-state question and observer-dependent entropy.
* _Entropy_: ⟨K⟩ = S; passivity as Kelvin's law.
* _Measurement_: POVMs and the commutant as "what the observer can't touch."
* _Lagrangian and Hamiltonian_: the modular Hamiltonian is a Hamiltonian in every formal sense except that a state, not a law, supplies it.

***

## Suggested next steps

* In Python with NumPy/SciPy: take ρ = diag(0.8, 0.2), compute K = −logm(ρ), apply σ\_s to |0⟩⟨1| for a few values of s, and confirm the phase 4^(is). Then try a non-diagonal ρ (rotate it by any unitary) and check the flow still fixes ρ.
* For the two-qubit state, build S as a matrix acting on the 4-dimensional space (define it on the basis X|Ω⟩ for X running over a basis of 2×2 matrices; note S is antilinear, so handle the conjugation explicitly), compute its polar decomposition, and check Δ = ρ\_A ⊗ ρ\_B^(−1).
* Check the ordering asymmetry: compute ⟨σ₊σ₋⟩ and ⟨σ₋σ₊⟩ for several thermal states and confirm the ratio is e^(βε).
* Reading: Witten, "APS Medal for Exceptional Achievement in Research: Invited article on entanglement properties of quantum field theory" (Rev. Mod. Phys. 2018), §§2–4, the clearest physicist's introduction to Tomita–Takesaki; Sorce, "Notes on the type classification of von Neumann algebras" (2023); Connes–Rovelli, "Von Neumann algebra automorphisms and time–thermodynamics relation" (1994); Takesaki, _Theory of Operator Algebras II_ for the full mathematics.
