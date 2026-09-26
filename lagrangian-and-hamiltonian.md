# The Lagrangian and the Hamiltonian

*Side-quest notes, September 2026. The action principle, and the two formulations of mechanics.*

---

## 1. The action principle

Newton is local in time: given position and velocity now, it gives acceleration now. The action principle is the global form: assign every possible path from A (at t₁) to B (at t₂) a single number, and the actual path is the one for which that number is stationary.

**Lineage.** Hero (light reflects along the shortest path) → Fermat (1662, least *time*, explains refraction) → Maupertuis and Euler (1740s) → Lagrange (1788) → Hamilton (1830s: mechanics and optics are the same formalism; where Schrödinger started).

**The formula.**

S[path] = ∫ L(x, ẋ, t) dt, with the Lagrangian L = T − V (kinetic minus potential).

The actual path makes S stationary under small deformations with fixed endpoints. Usually a minimum, not always; "least action" is a historical inaccuracy.

**The derivation.** Deform the path by εη(t), η vanishing at the endpoints. Expand to first order:

δS = ε ∫ [ (∂L/∂x) η + (∂L/∂ẋ) η̇ ] dt.

Integrate the second term by parts (boundary term dies), giving

δS = ε ∫ [ ∂L/∂x − (d/dt)(∂L/∂ẋ) ] η dt.

For this to vanish for *every* η, the bracket must vanish everywhere:

**Euler–Lagrange:** (d/dt)(∂L/∂ẋ) = ∂L/∂x.

Left side: rate of change of the conjugate momentum ∂L/∂ẋ. Right side: what drives it. If L doesn't depend on x, the momentum is constant — Noether's simplest case is Euler–Lagrange with one side missing.

**Check.** L = ½mẋ² − V(x) gives mẍ = −dV/dx: Newton. With T + V instead, particles would accelerate up potential hills. The minus sign is what makes it Newton; the deeper reason (L is the Legendre transform of energy) is below.

**Why bother:**
1. Holds in any coordinates — the derivation assumed nothing about x.
2. Constraint forces never appear; parametrize the constraint surface and they're gone.
3. One function encodes the whole theory; a theory *is* its Lagrangian.
4. Symmetry becomes checkable by inspection of S.

**Refinements.**
- A transformation is a symmetry if it changes L by at most a total derivative dF/dt, since ∫ dF/dt dt is a boundary term. Hence L is not unique: L and L + dF/dt give identical physics.
- For fields, S = ∫∫ 𝓛(φ, ∂φ) dx dt with a Lagrangian *density*; Euler–Lagrange becomes a PDE. Maxwell's equations come from 𝓛 = ½(E² − B²).

---

## 2. The one question the two formulations answer differently

Newton's law is second-order in time: the future needs position *and* velocity now.

**Lagrangian.** Position is fundamental; velocity is the slope of the path. Equations second-order, one per coordinate. Arena: **configuration space**, the space of positions (a circle for a pendulum, a torus for a double pendulum, 3N dimensions for N particles). A motion is a curve; the action picks the curve; velocity is a tangent, not a point.

**Hamiltonian.** If the state needs two numbers per degree of freedom, give it two coordinates: position q and momentum p, *independent*. Arena: **phase space**, twice the dimensions. A state is a point. Equations first-order. Time evolution is a flow.

Everything else follows from this difference.

---

## 3. The Legendre transform

Define p = ∂L/∂q̇ (mq̇ for the standard L; in general whatever L says). Then

H(q, p) = p q̇ − L, with q̇ eliminated in favor of p.

For L = T − V this gives H = T + V: the energy. So the minus sign in L is resolved — L is the thing whose Legendre transform is energy; T − V and T + V are one fact in two coordinate systems.

Conceptually: a convex curve can be described by its points or by its family of tangent lines. H is L described by its tangents in the velocity direction. Nothing is lost. The same transform takes internal energy to free energy in thermodynamics.

---

## 4. Hamilton's equations and phase portraits

Vary S = ∫ (p q̇ − H) dt with q, p independent:

q̇ = ∂H/∂p,  ṗ = −∂H/∂q.

Nearly symmetric; the sign is what makes everything below work.

**Harmonic oscillator,** H = p²/2m + ½kq²: the point (q, p) goes round an ellipse. Motion stays on a curve of constant H and moves along it at a definite rate.

**Pendulum:** phase space is a cylinder (angle around, momentum up). Closed curves near the bottom (swinging); curves wrapping the cylinder at high energy (whirling); the separatrix through the unstable upright point between them. The whole behaviour is a picture, visible without solving anything. **Dynamics becomes geometry.**

---

## 5. Liouville: the flow is incompressible

A blob of initial states deforms under the flow — stretches, folds — but its volume never changes. Divergence of the flow is ∂²H/∂q∂p − ∂²H/∂p∂q = 0.

Not true in configuration space, nor for Newton in (position, velocity) generally. A special property of (q, p), and the reason phase space is the arena of statistical mechanics: a probability distribution over states moves like an incompressible fluid, and "the number of states" is a meaningful count. Boltzmann and Gibbs start here; so will the entropy exploration.

---

## 6. Poisson brackets: everything is generated

{f, g} = ∂f/∂q ∂g/∂p − ∂f/∂p ∂g/∂q.

For any observable f: **df/dt = {f, H}.** Hamilton's equations are the cases f = q, f = p. H *generates* time evolution.

The bracket satisfies antisymmetry and the Jacobi identity — it is a Lie bracket. **The observables on phase space form a Lie algebra.** Any observable G generates a transformation via {·, G}:
- p generates translations ({q, p} = 1);
- angular momentum generates rotations;
- H generates time translation.

**Noether as an identity.** G is conserved iff {G, H} = 0. By antisymmetry, that's {H, G} = 0: H is unchanged under the flow G generates — G's flow is a symmetry. Conserved quantity and symmetry generator are the same object seen from two sides of one bracket. In the Lagrangian picture Noether is a theorem; here it's one line.

---

## 7. The road to quantum mechanics

**Dirac (1925):** replace {f, g} by (1/iħ)[F, G], the commutator. Everything carries over: observables become self-adjoint operators, H generates time evolution (Heisenberg picture), momentum generates translations, angular momentum rotations. Phase space is replaced by Hilbert space; the Lie algebra of observables survives with its brackets intact. Hamiltonian mechanics was already the structure of quantum mechanics, minus the ħ.

**Feynman (1948):** the amplitude from A to B is a sum over *all* paths of e^{iS/ħ}. Paths far from the stationary one have rapidly varying phase and cancel; the classical path is where contributions add. The action principle is the classical limit of interference. Fermat's least time and Hamilton's principle are the same thing for the same reason.

So: Hamiltonian → operators and Hilbert space; Lagrangian → the path integral. Two coordinate systems on the same object, quantum as classical.

---

## 8. Which to use when

**Lagrangian** when time should not be singled out: relativity, field theory, the whole gauge construction. Symmetries visible by inspection. The Hamiltonian picks a time coordinate and hides Lorentz invariance.

**Hamiltonian** when the question is about *state*: chaos (Poincaré is entirely phase-space geometry), statistical mechanics, integrability, perturbation theory, canonical quantization.

*Position:* the two formulations divide "a mechanical system" along the same line the symmetry exploration drew between law and state. The Lagrangian is the law — a rule assigning numbers to histories. The Hamiltonian is the state — a point in a space whose geometry (the bracket, the preserved volume) is the invariant content of mechanics. That geometry is called symplectic; the modern view is that mechanics is the study of symplectic manifolds with a preferred function H, and the Lagrangian is the special case where the manifold is the tangent bundle of a configuration space.

---

## 9. Loose end: constraints and gauge

When the Legendre transform is degenerate — p = ∂L/∂q̇ can't be inverted for q̇ — the passage to H fails and constraints appear. This is exactly the electromagnetic case: A has a component with no time derivative in L. Dirac's constraint theory handles it, and the constraints turn out to be the generators of gauge transformations. The "gauge symmetry is a redundancy" position has a Hamiltonian form: gauge transformations are the flows generated by the constraints, and the physical phase space is what remains after quotienting them out. A conversation on its own if the redundancy question persists.

---

## Suggested next steps

- Draw the pendulum phase portrait by hand from H = p²/2mℓ² − mgℓ cos θ: level curves of H on the cylinder, and locate the separatrix.
- Verify Liouville for the harmonic oscillator: a rectangle of initial conditions rotates without changing area.
- Check {L_z, H} = 0 for a central potential and read off that angular momentum both is conserved and generates rotations.
- Read Dirac's *Lectures on Quantum Mechanics* (1964), the first two lectures, for the constraint theory and its link to gauge freedom.
