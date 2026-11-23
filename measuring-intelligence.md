# Measuring Intelligence: _g_ and Factor Analysis

_Side file to_ what-is-intelligence.md, _written at the close of the Intelligence exploration, November 2026. What Spearman's g is as a construct, worked in small numbers, and three mechanisms that produce the same table. By steering, limited to g as a construct: group-difference debates are out of scope. Runnable companion:_ factor.py.

***

## 1. The positive manifold

Spearman (1904) noticed that schoolchildren's marks in classics, French, English and mathematics, and scores on sensory tests such as pitch discrimination, all correlated positively. Every pair, no negatives. A century of testing has confirmed the pattern across very different tests; it is called the **positive manifold**.

That is the only fact. Everything else is interpretation of it.

***

## 2. One factor, worked

Spearman's model: each test score is a weighted share of one general factor _g_ plus a factor specific to that test. The weight is the test's **loading**. If the model holds, the correlation between two tests is the product of their loadings.

**The triad formula.** With three tests, you can solve for the loadings directly:

> loading₁ = √(r₁₂ × r₁₃ / r₂₃)

_Worked_ (_factor.py_ Part 1): r₁₂ = 0.72, r₁₃ = 0.63, r₂₃ = 0.56.

* loading₁ = √(0.72 × 0.63 / 0.56) = √0.81 = **0.90**
* loading₂ = r₁₂ / loading₁ = **0.80**; loading₃ = r₁₃ / loading₁ = **0.70**
* check: 0.80 × 0.70 = 0.56 = r₂₃.

**As compression.** Three loadings reproduce three correlations: no saving. Six tests: 6 numbers for 15 correlations. Ten tests: 10 for 45. _g_ is a short description of a correlation table, and the saving grows with the number of tests. That is the sense in which "intelligence" was first measured: as a compression of data about people (_What Is Intelligence?_ stage 1).

Spearman's own test of the model was the **tetrad difference**: with four tests, r₁₂r₃₄ − r₁₃r₂₄ should be zero if one factor explains everything. Real batteries leave residues, which is where the later disputes start.

***

## 3. Three mechanisms, one table

_factor.py_ Part 2 simulates 4,000 people taking 6 tests under three different mechanisms, then fits one factor to each correlation table.

```
           correlations              one-factor loadings              worst miss
g          min 0.33 mean 0.46 max 0.60   0.81 0.75 0.71 0.66 0.62 0.54   0.011
bonds      min 0.39 mean 0.49 max 0.57   0.72 0.71 0.76 0.71 0.68 0.62   0.106
mutualism  min 0.26 mean 0.28 max 0.31   0.52 0.54 0.54 0.52 0.54 0.51   0.018
```

All three give a positive manifold and a respectable first factor.

**g (Spearman 1904).** One general cause. The fit is near-perfect by construction (worst residual 0.011).

**Bonds (Thomson 1916).** The mind as many small independent capacities; each test draws on a random half of 100 of them. Two tests correlate in proportion to the bonds they share, so all correlations are positive, yet **no bond is general**. In the six-bond example of stage 2 (tests A = {1,2,3,4}, B = {3,4,5,6}, C = {1,2,5,6}) every correlation is 0.5 and one factor fits exactly. With random sampling the overlaps vary, and a single factor misses by up to 0.106: detectable with a large sample, invisible with a small one.

**Mutualism (van der Maas et al. 2006).** Abilities start independent (each person's capacities drawn separately) and grow logistically, each boosting the others while developing (vocabulary helps reading, reading helps vocabulary). After growth, every pair correlates positively and one factor fits almost exactly (worst residual 0.018). **There is no g at birth**; the general factor is produced by development.

***

## 4. The later history in brief

* **Thurstone** (1938) found seven "primary mental abilities" with a different rotation of the same data; Spearman's single factor reappeared when the primaries were themselves factor-analysed.
* **Cattell and Horn** separated fluid from crystallized ability (roughly, solving new problems against using acquired knowledge): Chollet's intelligence against skill (_What Is Intelligence?_ 3b), fifty years earlier.
* **Carroll** (1993), reanalysing over 460 datasets, settled on a three-stratum hierarchy: narrow abilities, about eight broad abilities, and _g_ at the top. The hierarchy describes the table; it does not say which mechanism produced it.
* **Boring** (1923): intelligence is what the tests test. An operational definition in the absence of theory.

***

## 5. What _g_ is and isn't

* **Is:** a real, stable regularity in test data (the positive manifold), a short description of it, and a useful predictor of outcomes across many tests.
* **Is not, on the table alone:** a single thing in the head. Three mechanisms produce the same table (§3). Distinguishing them takes evidence the table doesn't contain: development over time (mutualism predicts correlations that grow with age), interventions (training one ability should raise others under mutualism, not under _g_), and the brain.
* **Compared with atoms** (stage 1): Mach's atoms became real when independent routes converged on one number (Avogadro's). _g_ has no comparable second route yet.

***

## 6. Positions taken

* _g_ is a compression of a correlation table, and real as a description.
* Whether it names one cause is underdetermined by the table: Spearman, Thomson, and van der Maas produce the same positive manifold (the series' _prediction underdetermines mechanism_ thread, with people as the data).
* Fluid against crystallized ability is Chollet's intelligence against skill, in psychometric form.
* The first measure of intelligence was a short description of data about people; the C-test (stage 3b) was the first measure built from short descriptions of the test items themselves.

***

## Suggested next steps

* In _factor.py_, compute the tetrad differences for each mechanism and see which one leaves residues.
* Simulate mutualism at two ages (stop the growth at 100 and at 300 steps) and check whether the correlations rise with age, the mechanism's distinctive prediction.
* Under mutualism, "train" one ability (raise its capacity by 20% for half the people) and see whether the others rise too; under _g_, they shouldn't.
* Reading: Spearman, "General intelligence, objectively determined and measured" (1904); Thomson, "A hierarchy without a general factor" (1916); van der Maas et al., "A dynamical model of general intelligence" (_Psychological Review_, 2006); Carroll, _Human Cognitive Abilities_ (1993), ch. 1–2.
