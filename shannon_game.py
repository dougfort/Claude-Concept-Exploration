"""shannon_game.py — Shannon's guessing game (1951), played by a program.

A predictor reads text one letter at a time. Before each letter it ranks all
27 symbols (a-z and space) from most to least likely, given the two letters
before. We record the rank of the letter that actually came next: 1 if its
first guess was right, 2 if its second, and so on. Then it updates its counts.

Two things to see:
  1. The sequence of guess numbers is a code. An "identical twin" running the
     same predictor can turn the guess numbers back into the text exactly.
     Predicting and compressing are the same act.
  2. The predictor gets better as it reads (smaller guess numbers in the
     second half). That improvement is induction: the past changing the
     forecast for the future.

Pure Python, no libraries.
"""
import math
from collections import Counter, defaultdict

ALPHABET = "abcdefghijklmnopqrstuvwxyz "
ORDER = 2  # letters of context


def clean(text):
    text = text.lower()
    out = []
    for ch in text:
        if ch in ALPHABET:
            out.append(ch)
        elif out and out[-1] != " ":
            out.append(" ")
    return "".join(out).strip()


class Predictor:
    """Ranks next letters by how often each followed this context so far.
    Ties are broken by overall letter frequency so far, then alphabet order,
    so two copies of the predictor always rank identically."""

    def __init__(self):
        self.ctx_counts = defaultdict(Counter)
        self.uni = Counter()

    def ranking(self, ctx):
        c = self.ctx_counts[ctx]
        return sorted(ALPHABET, key=lambda s: (-c[s], -self.uni[s], ALPHABET.index(s)))

    def update(self, ctx, ch):
        self.ctx_counts[ctx][ch] += 1
        self.uni[ch] += 1


def encode(text):
    p, guesses = Predictor(), []
    for i, ch in enumerate(text):
        ctx = text[max(0, i - ORDER):i]
        guesses.append(p.ranking(ctx).index(ch) + 1)
        p.update(ctx, ch)
    return guesses


def decode(guesses):
    """The identical twin: same predictor, sees only the guess numbers."""
    p, text = Predictor(), ""
    for g in guesses:
        ctx = text[max(0, len(text) - ORDER):]
        ch = p.ranking(ctx)[g - 1]
        p.update(ctx, ch)
        text += ch
    return text


def entropy_of(values):
    n, counts = len(values), Counter(values)
    return -sum((k / n) * math.log2(k / n) for k in counts.values())


def report(label, guesses):
    n = len(guesses)
    first = sum(1 for g in guesses if g == 1) / n
    print(f"{label:<14} letters={n:5d}  right on 1st guess={first:5.1%}  "
          f"bits/letter (entropy of guess numbers)={entropy_of(guesses):.2f}")


TEXT = """
The sun has risen every morning that anyone has recorded, and so we expect it
to rise tomorrow. Nothing in the mornings already seen contains tomorrow. The
expectation is something we bring to them. We expect bread to nourish because
bread has nourished, and fire to burn because fire has burned. When we ask what
connects the past to the future, we find only that one kind of event has
followed another, again and again, and that we have come to expect it. The
question is whether that expectation is a piece of knowledge or only a habit,
and whether a machine that forms the same habit knows anything more than we do.
A reader who has seen many sentences can guess the next letter of a new one
with surprising success, and the better the reader knows the language, the
fewer guesses it needs. The guesses measure what the reader knows.
"""

if __name__ == "__main__":
    text = clean(TEXT)
    guesses = encode(text)
    assert decode(guesses) == text, "twin failed to recover the text"

    print(f"Uniform guessing over 27 symbols: log2(27) = {math.log2(27):.2f} bits/letter\n")
    half = len(guesses) // 2
    report("first half", guesses[:half])
    report("second half", guesses[half:])
    report("whole text", guesses)

    print("\nFirst 20 letters and their guess numbers:")
    print(" " + "  ".join(c if c != " " else "_" for c in text[:20]))
    print(" " + " ".join(f"{g:2d}" for g in guesses[:20]))
    print("\nTwin decoded the text from guess numbers alone:", decode(guesses) == text)
