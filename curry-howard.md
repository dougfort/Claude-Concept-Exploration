# Curry–Howard: Programs as Proofs

*Side-quest notes, September 2026. Written at the close of the computation exploration, which kept complexity in the main line and left this aside.*

---

## 1. The correspondence

**A proposition is a type; a proof of it is a program of that type; simplifying a proof is running the program.**

The dictionary, for the fragment where it is exact:

| Logic | Programming |
|---|---|
| proposition A | type A |
| proof of A | a program (term) of type A |
| A implies B | function type A → B |
| A and B | pair (A, B) — a product or struct |
| A or B | tagged union — Either A B, an enum with two cases |
| true | the unit type, one trivial value |
| false | the empty type, no values at all |
| for all x, P(x) | dependent function: given any x, returns a proof of P(x) |
| there exists x with P(x) | dependent pair: a specific x together with a proof of P(x) |
| simplifying a proof (cut elimination) | evaluating the program (β-reduction) |

Smallest case. The proposition "if A implies B, and B implies C, then A implies C" is the type

(A → B) → (B → C) → (A → C).

A program of that type is function composition: given f and g, return x ↦ g(f(x)). Writing the program *is* proving transitivity of implication. A programmer who has written `compose` has proved a theorem without meaning to.

Why "or" is a tagged union and not just a union: to use a proof of "A or B" you must handle both cases, and you must know which case you have. A pattern match on an enum is proof by cases.

Why "false" is the empty type: a function from the empty type to anything type-checks vacuously, because there's nothing to call it with. That is "from a falsehood, anything follows."

---

## 2. Where it came from

**Brouwer–Heyting–Kolmogorov (1920s–30s).** The intuitionists' explanation of what a proof *is*: a proof of "A implies B" is a *method* turning any proof of A into a proof of B; a proof of "A or B" is a proof of one of them together with which one; a proof of "there exists x" must exhibit the x. This was philosophy of mathematics, a reading of the logical constants as constructions. It is already Curry–Howard with "method" in place of "program," before anyone had the program.

**Curry (1934; with Feys, 1958).** Curry noticed that the types of his combinators are exactly the axioms of implicational logic. The combinator K, which takes x and y and returns x, has type A → (B → A) — an axiom. The combinator S has the type of the other axiom. Applying one combinator to another corresponds to *modus ponens*. A coincidence noted, not yet a correspondence.

**Gentzen (1934–35).** Natural deduction, and cut elimination: any proof can be transformed into one with no detours (no lemma proved only to be used once). The transformation is mechanical.

**Church (1940).** The simply typed λ-calculus, introduced to avoid the paradoxes that sank his untyped logic (stage 3 of the computation notes: Kleene–Rosser). Every typed term normalizes — every program halts.

**Howard (1969; circulated as a manuscript, published 1980).** The full statement: natural deduction proofs *are* simply typed λ-terms, and Gentzen's detour removal *is* β-reduction. Curry's coincidence becomes an isomorphism, with computation on one side and proof simplification on the other.

**De Bruijn's Automath (1967)**, independently: a language for writing mathematics so that a machine checks it, built on the same identification.

**Martin-Löf (1971–84).** Dependent type theory: types that mention values ("a list of length n"; "a proof that x < y"). Quantifiers enter the correspondence, and types become as expressive as mathematical statements.

**Girard (System F, 1972) and Reynolds (1974)**, independently: polymorphism — a function working for every type — corresponds to quantifying over propositions, second-order logic. Generics are second-order proofs.

**Coquand–Huet (1988), the Calculus of Constructions**, the basis of Coq (renamed Rocq in 2025). Then Agda, Lean. Machine-checked proofs of the Four Colour Theorem (Gonthier, 2005), Feit–Thompson (2012), and the Kepler conjecture (Flyspeck, 2014, in HOL Light and Isabelle — a different tradition, not type-theoretic in the same sense).

**Lambek (1970s):** a third vertex, cartesian closed categories. Hence "Curry–Howard–Lambek": logic, computation, and category theory as one structure.

---

## 3. Two results a programmer already knows

### General recursion makes the logic inconsistent

In a language with unrestricted recursion, write

loop : A
loop = loop

It has every type, including the empty type. As a proof, it proves *false* — and from false, everything. So:

- **A consistent logic must be a total language**: every program terminates. Coq's and Agda's cores check termination for exactly this reason.
- **A Turing-complete language, read as a logic, is inconsistent.**

This is the computation notes' position ("undecidability is the price of a closed definition") seen from the other side. Partiality was what made computability complete; partiality is exactly what makes a logic prove everything. You can have a language that expresses every computable function, or one whose programs are all proofs, not both. And a total language cannot contain its own interpreter — which is Gödel's second incompleteness theorem appearing as a programming fact: a consistent system cannot certify itself.

### Classical logic is control flow

The correspondence as stated is exact for *intuitionistic* logic, which lacks the law of excluded middle ("A or not A") and double-negation elimination ("not not A implies A"). Try to write a program of type ((A → False) → False) → A: you are handed a function that would refute any refutation of A, and must produce an actual A. There's no way to get one.

Griffin (1990): add `call/cc` — capture the current continuation, the rest of the computation, as a value — and classical logic comes back. The type of `call/cc` is Peirce's law, ((A → B) → A) → A, a classical tautology. Classical proofs are programs that can jump. Excluded middle is a program that answers "not A" provisionally and, if you ever produce an A to refute it, rewinds time and answers "A" instead.

---

## 4. What it is and isn't

It is *not* the claim that every program is an interesting proof. A function of type Int → Int proves "Int implies Int," which is trivial. The content of the proof lives in the type, and in ordinary languages types say little.

*Position:* the correspondence is less "programs are proofs" than **"types are specifications, and dependent types make specifications as expressive as mathematics."** In Lean, the type of a sorting function can state that its output is sorted and a permutation of its input; any program with that type is a verified sort. Type-checking becomes proof-checking.

---

## 5. Positions

- **Curry–Howard realizes Leibniz's calculemus in the one place it works: checking, not finding.** Frege wanted gapless proofs checkable by form alone; a proof assistant is exactly that, mechanized. Gödel's 1956 letter asked whether *finding* proofs could be mechanized efficiently — the P vs NP question. Checking is easy; finding is (probably) not. Proof assistants live entirely on the easy side, and the hard side is where mathematicians and, now, search programs work.
- **BHK was right before it had a model.** The intuitionist reading of proofs as constructions looked like philosophy in 1930 and turned out to be a specification of the typed λ-calculus. The same pattern as elsewhere in the series: a position taken for philosophical reasons became a mathematical structure.
- **The correspondence is a symmetry of the kind the symmetry notes describe:** two descriptions related by an exact dictionary, with the dictionary itself the content. What it doesn't settle is which side is primary — whether logic is a kind of computation or computation a kind of logic. I'd say neither: both are views of one structure, as the entropy notes said of system and knowledge.

---

## 6. Links

- *Computation* §3: partiality and the price of a closed definition; §5: Gödel's letter and checking vs. finding.
- *Proof* (proposed): Gentzen, Gödel's second theorem as the self-interpreter problem, proof assistants and the formalization of mathematics, natural proofs.
- *The function*: Church's λ-calculus as one answer to what a function is — a rule, not a graph.

---

## Suggested next steps

- In any language with generics, write functions with these types and read each as a proof: (A, B) → (B, A); A → (B → A); (A → B) → (B → C) → (A → C); Either A B → Either B A. Then try (A → B) → (B → A) and see that it can't be done — it isn't a theorem.
- Try to write ((A → Void) → Void) → A with Void the empty type; then look up how `call/cc` gives it.
- In a total language (Agda or Lean), try `loop = loop` and read the error.
- Reading: Wadler, "Propositions as Types" (2015), the best short introduction; Pierce et al., *Software Foundations*, vol. 1; Sørensen and Urzyczyn, *Lectures on the Curry–Howard Isomorphism* for the technical version.
