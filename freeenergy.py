"""freeenergy.py — variational free energy on the smallest example.

Companion to 'What Is Intelligence?' stage 3a (addendum).
You see a dark patch on the road. Two possible hidden causes:
  shadow (prior 0.75) or puddle (prior 0.25).
A shadow makes a dark patch with probability 0.2, a puddle with 0.4.
q is the perceiver's guess: q(shadow), with q(puddle) = 1 - q(shadow).
F(q) = sum_c q(c) * [-log2 p(data, c)]  -  H(q)
     = "energy"                         -  "entropy"
F is never below -log2 p(data), and equals it when q is the true posterior.
"""
import math

prior = {"shadow": 0.75, "puddle": 0.25}
like  = {"shadow": 0.20, "puddle": 0.40}       # p(dark patch | cause)
joint = {c: prior[c] * like[c] for c in prior}  # p(dark patch, cause)
p_data = sum(joint.values())
post = {c: joint[c] / p_data for c in joint}

def lg(x): return -math.log2(x)

print("joint:      shadow %.2f   puddle %.2f" % (joint["shadow"], joint["puddle"]))
print("p(data) = %.2f   surprise -log2 p(data) = %.3f bits" % (p_data, lg(p_data)))
print("posterior:  shadow %.2f   puddle %.2f" % (post["shadow"], post["puddle"]))
print("'energy' of each cause, -log2 p(data, cause): shadow %.3f  puddle %.3f"
      % (lg(joint["shadow"]), lg(joint["puddle"])))
print()
print("  q(shadow)   energy   entropy   F = E - H   F - surprise (= KL)")
for qs in (1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.2, 0.0):
    q = {"shadow": qs, "puddle": 1 - qs}
    E = sum(q[c] * lg(joint[c]) for c in q if q[c] > 0)
    H = abs(sum(q[c] * math.log2(q[c]) for c in q if q[c] > 0))
    F = E - H
    print("   %4.1f      %6.3f    %6.3f     %6.3f        %6.3f" % (qs, E, H, F, F - lg(p_data)))

print()
print("Gaussian case: if the model predicts a pixel value mu with noise sigma,")
print("the energy of seeing x is (x - mu)^2 / (2 sigma^2) / ln 2 + constant bits.")
for sigma in (1, 4):
    for err in (0, 1, 2, 4):
        e = err**2 / (2 * sigma**2) / math.log(2)
        print("  sigma %d, prediction error %d: %.2f bits above the constant" % (sigma, err, e))