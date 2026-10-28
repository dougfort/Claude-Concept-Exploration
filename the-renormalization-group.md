# The Renormalization Group in Plain Terms

*Side file, written at the close of the emergence exploration, October 2026. The technical home for* what-is-emergence.md *§4 (stage 3b). Scripts: blockspin.py, ising.py, landau.py.*

*Question it answers: why do some coarse descriptions (pressure, temperature, magnetization) obey closed laws of their own while most don't, and why do very different materials share the same numbers near a transition?* (what-is-entropy.md *§4 asked the first;* what-is-emergence.md *§4 needed both.)*

---

## 1. The idea in one paragraph

Take a description of a system with some parameters (couplings). Zoom out: throw away detail below a certain scale and rewrite the description at the new scale. You get a description of the *same form* with *new* parameters. Repeat. The renormalization group (RG) is the study of where the parameters go under repetition. Most parameters shrink to nothing: they're **irrelevant**, which is why detail can be ignored. A few grow: they're **relevant**, and they are the handful of numbers a coarse description needs. Points where the parameters stop changing are **fixed points**. A phase is a basin that flows to a stable fixed point; a transition is an unstable fixed point between basins; a universality class is everything that flows near the same unstable fixed point.

Programmer's version: an RG step is a lossy downsampling `coarse()` followed by asking which update rule `step'` the downsampled data obeys. Iterating asks which descriptions survive arbitrarily many rounds of compression. (The commuting square of *what-is-emergence.md* §5: coarse ∘ step = step′ ∘ coarse.)

---

## 2. Coupling and temperature

For the Ising model, spins are ±1 and the weight of a configuration is e^(K × number of agreeing neighbour pairs − K × number of disagreeing), up to a constant. **K = J/T**: the coupling strength over temperature. Large K is cold and ordered, small K hot and disordered. Every RG step below is a rule K → K′.

---

## 3. One dimension, exactly: decimation

**Sum out every second spin of a chain.** Spins s₁, s, s₂ in a row, s in the middle. The middle spin contributes

  e^(K s₁ s) e^(K s s₂), summed over s = ±1  =  2 cosh(K(s₁ + s₂)).

That depends only on whether s₁ and s₂ agree:
- agree (s₁ + s₂ = ±2): 2 cosh 2K
- disagree (s₁ + s₂ = 0): 2

We want a direct bond of the same form, A·e^(K′ s₁ s₂), giving A·e^(K′) when they agree and A·e^(−K′) when they don't. Divide: e^(2K′) = cosh 2K, so

  **K′ = ½ ln cosh 2K**, equivalently **tanh K′ = tanh² K.**

Check with K = 1: cosh 2 = 3.762, ½ ln 3.762 = 0.6625. From blockspin.py:

| start K | flow |
|---|---|
| 0.5 | 0.500 → 0.217 → 0.046 → 0.002 → 0 |
| 1.0 | 1.000 → 0.663 → 0.350 → 0.114 → 0.013 → 0 |
| 3.0 | 3.000 → 2.653 → 2.307 → 1.960 → 1.614 → 1.268 → 0.925 → … → 0 |

Since tanh K < 1, squaring shrinks it: every finite K flows to 0. The only fixed points are K = 0 (stable: disorder) and K = ∞ (unstable: perfect order at T = 0). No transition at any T > 0, which is Ising's 1925 result.

**The correlation length makes it vivid.** In the 1D chain, spins r apart are correlated as (tanh K)^r = e^(−r/ξ), with ξ = −1/ln tanh K. Decimation halves distances, and tanh K′ = tanh² K means ξ′ = ξ/2 exactly. The RG step is "the correlation length in new units." Fixed points are where ξ′ = ξ: either ξ = 0 (no correlation) or ξ = ∞ (correlation at every scale). **A critical point is a place where the correlation length is infinite, so zooming out changes nothing.**

---

## 4. Two dimensions: why decimation fails, and Migdal–Kadanoff

In 2D, summing out every second spin (a checkerboard) leaves the survivors coupled not only to nearest neighbours but to next-nearest neighbours and in groups of four. The description doesn't keep its form. Exact RG generates infinitely many couplings; every practical scheme truncates.

**Migdal–Kadanoff (1975–76): move bonds, then decimate.** Slide every second row of vertical bonds onto its neighbour (those bonds double, K → 2K) and likewise for horizontal ones. What's left is 1D chains in each direction, which decimate exactly:

  tanh K′ = tanh²(2K)

The doubling (more bonds per survivor) fights the shrinking (squaring tanh), and now an **unstable fixed point** appears. The other order (decimate first, then move) gives K′ = 2 artanh(tanh² K). From blockspin.py:

| | move, then decimate | decimate, then move | exact (Onsager) |
|---|---|---|---|
| K* | 0.3047 | 0.6094 | 0.4407 |
| T_c = 1/K* | 3.28 | 1.64 | 2.269 |
| slope λ at K* | 1.679 | 1.679 | — |
| ν = ln 2 / ln λ | 1.34 | 1.34 | 1 |

Start 10% below K* and the flow runs to 0; 10% above, to ∞. The geometric mean of the two K* gives T_c = 2.32.

**The lesson the approximation teaches.** The two orderings are a free choice. They disagree about *where* the transition is by a factor of 2 and agree *exactly* on the exponent. The location of a fixed point depends on details (even details of the approximation); the exponents depend only on the flow's behaviour near the fixed point. This is universality in miniature: T_c is non-universal (iron at 770 °C, nickel at 358 °C), the exponents are universal.

---

## 5. Block spins: Kadanoff's picture done on samples

Kadanoff (1966) proposed grouping spins into blocks and replacing each block by its majority. He couldn't compute K′. A computer can do the next best thing: sample the lattice at a temperature, block it, and watch a measurable stand-in for the coupling.

blockspin.py (`python3 blockspin.py blocks`, about a minute): an 81 × 81 lattice sampled by Metropolis, then 3 × 3 majority blocks, 81 → 27 → 9. The stand-in for K is the nearest-neighbour correlation ⟨s_i s_j⟩ of the block spins:

| T | 81 × 81 | 27 × 27 | 9 × 9 | flow |
|---|---|---|---|---|
| 2.000 | 0.873 | 0.971 | 1.000 | to order |
| 2.200 | 0.777 | 0.870 | 0.963 | to order |
| 2.269 | 0.683 | 0.649 | 0.509 | (see below) |
| 2.300 | 0.663 | 0.613 | 0.469 | to disorder |
| 2.400 | 0.603 | 0.500 | 0.324 | to disorder |
| 2.600 | 0.513 | 0.355 | 0.152 | to disorder |

Below T_c, zooming out makes the lattice look colder; above, hotter. The direction reverses between 2.2 and 2.3, bracketing Onsager's 2.269.

**At T_c itself the sampler can't be trusted, and that is a finding.** Started from random spins, the 2.269 row falls (shown). Started from all-up (an earlier run), it rose: 0.729 → 0.786 → 0.907. At a critical point, fluctuations exist at every scale, and Metropolis needs a number of sweeps growing roughly like L^2.17 to equilibrate. For L = 81 that's about 14,000 sweeps; the script uses 3,000. So the sample remembers its start. This is **critical slowing down**: the same divergence that makes a critical point a fixed point makes it slow to reach. (Swendsen–Wang and Wolff cluster algorithms, 1987–89, flip whole correlated clusters and largely remove it.)

The proper version of this experiment is **Monte Carlo renormalization group** (Swendsen 1979): measure several block correlations at each level and solve for the couplings K′ (nearest, next-nearest, four-spin) that reproduce them, then linearize the flow. It gives 2D Ising exponents to a few percent.

---

## 6. Linearizing: where exponents come from

Near a fixed point K*, write the distance as δ = K − K*. One RG step with zoom factor b multiplies it by λ = b^y:

  δ′ = b^y · δ

- **y > 0: relevant.** The deviation grows; any small offset eventually dominates. Temperature (distance from T_c) is relevant, and so is a magnetic field.
- **y < 0: irrelevant.** The deviation dies; the coarse description forgets it. Next-nearest-neighbour couplings, lattice shape, and most chemistry are irrelevant at the Ising fixed point.
- **y = 0: marginal.** Needs a closer look (logarithms).

The correlation length shrinks by b each step, so near T_c it goes as ξ ~ |T − T_c|^(−ν) with **ν = 1/y_T**. For Migdal–Kadanoff, y_T = ln 1.679 / ln 2 = 0.747, so ν = 1.34.

**Every exponent follows from two numbers.** The Ising fixed point in d dimensions has two relevant directions, temperature (y_T) and field (y_h). Then:

  β = (d − y_h)/y_T   γ = (2y_h − d)/y_T   ν = 1/y_T

**Check, 2D Ising** (exact: y_T = 1, y_h = 15/8, d = 2):
- β = (2 − 15/8)/1 = 1/8 ✓ (Onsager–Yang)
- γ = (15/4 − 2)/1 = 7/4 ✓
- ν = 1 ✓

This is why exponents are related to each other (the scaling relations Kadanoff guessed in 1966) and why there are so few independent ones: **two relevant directions, two numbers, every exponent.**

---

## 7. Universality classes

Systems that differ only in irrelevant directions flow to the same fixed point and share every exponent. The class is fixed by a few features:

- **dimension** of space
- **symmetry** of the order parameter (two-valued like Ising; a direction in a plane like a superfluid's phase; a direction in space like a Heisenberg magnet)
- **range** of interactions (short or long)

| Class | Examples | β | ν |
|---|---|---|---|
| 2D Ising | adsorbed monolayers; Onsager's model | 1/8 | 1 |
| 3D Ising | liquid–gas critical points (CO₂, xenon); uniaxial magnets; binary mixtures | ≈ 0.326 | ≈ 0.630 |
| 3D XY | superfluid helium-4 at the λ point | ≈ 0.35 | ≈ 0.672 |
| 3D Heisenberg | isotropic magnets (nickel, approximately) | ≈ 0.366 | ≈ 0.711 |
| mean field (d ≥ 4) | Landau's theory | 1/2 | 1/2 |

A boiling liquid and a magnet are in the same class because "liquid or gas" and "up or down" are both two-valued and both live in three dimensions. Everything else about water and iron is irrelevant at the fixed point.

**Why Landau gets ½.** Mean-field theory ignores fluctuations. Above four dimensions fluctuations are irrelevant at the fixed point and Landau is exactly right; below four they matter and the exponents shift. (Wilson and Fisher's ε-expansion, 1972, computes exponents as a series in ε = 4 − d.)

---

## 8. Finite-size scaling

A real sample of side L is the flow stopped after about log_b L steps. Finite-size effects are therefore not noise but the flow itself, and they scale with L by the same exponents.

From ising.py (8 × 8, 16 × 16, 32 × 32; *what-is-emergence.md* §4):

- **|m| at T_c falls like L^(−β/ν) = L^(−1/8):** 0.769, 0.705, 0.663; ratios 0.917 and 0.940 against the predicted 0.917 per doubling.
- **χ's peak grows like L^(γ/ν) = L^(7/4):** 1.75, 6.26, 16.5; about 1.62 as an exponent against 1.75 (the grid is coarse near T_c).
- **The Binder cumulant crosses at T_c:** 0.610, 0.608, 0.611 at T = 2.27, while below T_c the curves rise toward 2/3 with L and above it fall toward 0.

The practical rule, used in *what-is-emergence.md* §6 on language models: a transition is shown by (1) naming the size N, (2) having several sizes, (3) showing the width narrowing as a power of N, (4) finding a crossing. A sigmoid at one size proves nothing.

---

## 9. Effective field theory

Wilson's own formulation (1971) works in momentum space: integrate out the highest-momentum modes in a thin shell, rescale, repeat. Particle physicists use the same flow from short distances to long. An unknown theory at a high scale Λ shows up at energies E ≪ Λ as every interaction the symmetries allow, each suppressed by a power of E/Λ set by its dimension. Those powers are the irrelevant directions. Fermi's 1934 four-fermion theory of beta decay is the classic case: its strength G_F ≈ 1.17 × 10⁻⁵ GeV⁻² carries the scale of the W boson (G_F ~ g²/M_W²), and its failure near 100 GeV predicted new particles. Weinberg's 1979 "Phenomenological Lagrangians" made this a method. The Standard Model works without quantum gravity because gravity's effects at collider energies are suppressed by about (10⁴ GeV / 10¹⁹ GeV)² ≈ 10⁻³⁰.

**Relevant operators are the problem cases.** A relevant coupling grows toward low energy, so its value at low energy is sensitive to the high-energy details, unless a symmetry protects it. The Higgs mass is relevant and unprotected; why it is small is the hierarchy problem. That is the RG's way of saying where detail can't be ignored.

---

## 10. Coarse-graining as compression, and learned RG

An RG step keeps one number per block and discards the rest: lossy compression. Irrelevant couplings are the bits every round discards; relevant ones survive any number of rounds. Universality says that **repeated lossy compression of physical systems has few fixed points.**

**What the right compression keeps.** Koch-Janusz and Ringel (*Nature Physics* 2018) learn a coarse-graining from data by maximizing the mutual information between a block's summary and its *distant* environment, excluding a buffer. It recovers correct RG flows without being told the block spins. The optimal coarse-graining keeps exactly what predicts the far away. That ties the RG to *compression-is-prediction.md*: the same act, applied across space instead of time.

**Learning curves.** Peraza Coppola, Helias, and Ringel (arXiv 2510.25553, 2025; v2 2026) build an RG for non-lazy networks on power-law data, with relevant and irrelevant perturbations and universality of learning curves at a Gaussian-process-like fixed point. *Preprint; abstract-level only.* Mehta and Schwab's 2014 "exact mapping" to restricted Boltzmann machines is formal; Lin, Tegmark, and Rolnick (2017) showed a classifier's compression differs from the RG's. Assessment in *what-is-emergence.md* §5.

---

## 11. Positions

- **A critical point is where the correlation length is infinite**, so coarse-graining changes nothing; the fixed point and the divergence are one fact.
- **What the parts determine is what isn't universal.** T_c depends on details (even of the approximation, Migdal–Kadanoff's factor of 2); the exponents depend only on the fixed point. The working claim had it backwards.
- **Two relevant directions, every exponent.** Scaling relations are bookkeeping on y_T and y_h, not separate laws.
- **A regime is a basin of a fixed point**, and its closed laws are those of its relevant directions. This is the theory "regimes, not laws" lacked.
- **Finite-size effects are the flow, not noise**, and they are the only way any finite system shows a transition.
- **The fixed point is real; the infinite system is not.** Batterman's asymptotic explanations are statements about the map, not about infinite magnets (*what-is-emergence.md* §4).
- **Critical slowing down is the fixed point seen from the sampler**: the divergence that makes T_c scale-free makes it slow to equilibrate (the 2.269 row).

---

## Scripts

- *blockspin.py*: exact 1D decimation; both orders of Migdal–Kadanoff with K*, T_c, and ν; `blocks` mode for 3 × 3 majority blocking on sampled 81 × 81 lattices.
- *ising.py*: Metropolis for L = 8, 16, 32; |m|, χ, Binder cumulant.
- *landau.py*: second-order against first-order free energies; hysteresis.

## Reading

- Kadanoff, "Scaling laws for Ising models near T_c," *Physics* 2 (1966).
- Wilson, "The renormalization group and critical phenomena," Nobel lecture (1982); Wilson and Kogut, *Physics Reports* 12 (1974).
- Goldenfeld, *Lectures on Phase Transitions and the Renormalization Group* (1992), ch. 9–10: the clearest textbook route.
- Cardy, *Scaling and Renormalization in Statistical Physics* (1996), ch. 3–4.
- McComb, *Renormalization Methods: A Guide for Beginners* (2004): gentlest.
- Koch-Janusz and Ringel, "Mutual information, neural networks and the renormalization group," *Nature Physics* 14 (2018).
