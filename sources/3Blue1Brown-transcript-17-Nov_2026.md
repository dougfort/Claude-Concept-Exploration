### Chapter 6: Reflections on “Compression is Intelligence”

27:33

27 minutes, 33 seconds

Now this phrase is something that's hard to analyze rigorously-intelligence is very ill defined, lots of people will disagree about what precisely it means.

27:41

27 minutes, 41 seconds

I think the better way to engage with it is to treat it like a proposed definition of intelligence.

27:47

27 minutes, 47 seconds

Suppose you wanted to give a mathematical foundation to this otherwise very squishy and human concept, is compression alone really enough to carry that burden?

27:56

27 minutes, 56 seconds

By analogy, I think of it like when Newton gave the word "energy" a mathematical meaning, this measurable quantity with units of kilogram meters per second squared.

28:05

28 minutes, 5 seconds

When he made this definition, it was reductive: it misses out on a lot of what people mean when they use the word "energy" colloquially.

28:12

28 minutes, 12 seconds

And yet, despite this more limited scope, it was still productive for him to make that definition, and, reductive though it might have been, it still managed to unify a number of seemingly disparate phenomena.

28:23

28 minutes, 23 seconds

Disparate concepts: Similarly any attempt to give a word like "intelligence" a mathematical meaning seems bound to miss out on some of the uniquely human nuance that our everyday usage bakes into that word.

28:35

28 minutes, 35 seconds

But the question is whether any such definition, even if reductive, is still productive, and manages to unify seemingly disparate aspects of intelligence.

28:45

28 minutes, 45 seconds

What I want to close with here are three specific ways that compression captures part of what I think I mean when I use the word intelligence.

28:52

28 minutes, 52 seconds

Where it plays into the topic for today is that in all three cases, having an algorithm like an arithmetic coding freshly in our minds makes the connection more concrete.

29:02

29 minutes, 2 seconds

To number one, compression and prediction are really two sides of the same coin, and prediction, in turn, seems a lot more clearly related to intelligence.

29:11

29 minutes, 11 seconds

Arithmetic codes show one half of this equivalence; specifically, they offer a nearly perfect way to turn an arbitrary predictor into a compressor.

29:19

29 minutes, 19 seconds

And you can go the other way around too.

29:21

29 minutes, 21 seconds

Suppose you have an arbitrary text compressor and you want to use it to make predictions about what might follow a given passage.

29:28

29 minutes, 28 seconds

I won't go into the full details, but here's the basic idea: for any potential string that might follow, you ask how much larger the compressed message would be with that addition versus without.

29:39

29 minutes, 39 seconds

If you let δ represent the difference between these two, then 2^-δ gives you a pretty good approximation for the implied predictive model's guess about how probable that next string is.

29:51

29 minutes, 51 seconds

Doing this over all strings in a given token vocabulary, for example, could give you a probability distribution analogous to the type we get out of modern language models.

30:00

30 minutes

So, in the sense that predictors can be turned into compressors and vice versa, compression and prediction really are equivalent,

30:07

30 minutes, 7 seconds

and, insofar as good prediction seems to require having a coherent model of what's really going on, this hints at the idea that compression ratios may be a good proxy for intelligence.

30:18

30 minutes, 18 seconds

This also ties to an influential theory in modern neuroscience known as predictive processing: it posits that the brain is continuously generating top-down predictions for

30:26

30 minutes, 26 seconds

sensory signals and then what gets passed back up from the sensory organs is not the full information of what they received, it's just the error between the prediction and the sensed reality.

30:37

30 minutes, 37 seconds

The upshot of this theory is that much of what we experience as intelligence may just boil down to neurological predictions and And compression.

30:46

30 minutes, 46 seconds

But there are aspects of intelligence, or at the very least what I think I mean when I use that word, the prediction alone would miss.

30:53

30 minutes, 53 seconds

Personally, I feel like I understand something better when it becomes smaller in my mind; when a handful of facts, or even just one,

31:00

31 minutes

are all I need to remember or rederive a wide swath of results.

31:04

31 minutes, 4 seconds

Progress in fields like physics also feels like this, having fewer, shorter laws feels like a step forward, even if they make identical predictions.

31:13

31 minutes, 13 seconds

This becomes more measurable in a machine learning context: if you have two models with equivalent predictive abilities, but one requires trillions of

31:21

31 minutes, 21 seconds

parameters and the other is small, it suggests that the smaller one is relying on fewer memorized assumptions.

31:28

31 minutes, 28 seconds

Now, if you plug each one of these into an arithmetic coding, if we assume each has equivalent prediction ability, that would mean that they compress a given large data set,

31:37

31 minutes, 37 seconds

say a gigabyte of Wikipedia, Down to the same size.

31:40

31 minutes, 40 seconds

After all, the whole point of this video so far is that that compression ratio is dependent only on the prediction.

31:46

31 minutes, 46 seconds

However, an honest account of the final compression ratio here should really take into account the size of the decoder program, which in this case includes the model itself.

31:56

31 minutes, 56 seconds

After all, if you actually wanted to send somebody a gigabyte of Wikipedia in a compressed package, the raw data stream coming out of that

32:04

32 minutes, 4 seconds

arithmetic coding would be useless if you didn't also give them the means of decoding it.

32:09

32 minutes, 9 seconds

This is, as I referenced earlier, how the Hutter Prize scores its results.

32:13

32 minutes, 13 seconds

If you didn't include the decoding program size in this, you could basically cheat by having such a decoding program just include a hard

32:20

32 minutes, 20 seconds

copy of all of Wikipedia in its source code, and then the supposed payload could be arbitrarily small.

32:26

32 minutes, 26 seconds

If earlier it felt like cheating to have a huge model kind of memorize the U.S.

32:30

32 minutes, 30 seconds

Constitution and use that for prediction, this right here is how that would get accounted for.

32:35

32 minutes, 35 seconds

When you measure things this way, it means a small model, with equivalent predictive capacity to a larger one, would count as better compression.

32:43

32 minutes, 43 seconds

And this at the very least rhymes with the idea that a clearer understanding uses a smaller number of general principles, instead of a large number of memorized facts.

32:52

32 minutes, 52 seconds

And that to me is what makes the phrase "compression is intelligence" a lot more thought provoking than "prediction is intelligence" would be.

33:00

33 minutes

A third aspect of what I think I mean when I use the word intelligence is an ability to learn new things quickly.

33:06

33 minutes, 6 seconds

The smartest people I know are able to dive into a new field with relative ease.

33:11

33 minutes, 11 seconds

And again, at first glance this would seem not at all to be captured by a compression ratio.

33:16

33 minutes, 16 seconds

If we stay focused on our example of a predictive model plugged into an arithmetic coding, even if you measure things the way the Hutter Prize does,

33:23

33 minutes, 23 seconds

where you include the size of the decoder program, nothing about that final compression size depends on how long it took to train that underlying model in the first place.

33:33

33 minutes, 33 seconds

Except there actually is a case where learning rate influences this final score.

33:38

33 minutes, 38 seconds

Suppose you start with a set-up where the underlying predictive model was trained on some specific data set, like Wikipedia, but then later you want to apply the same

33:46

33 minutes, 46 seconds

encoder and decoder to a different kind of text, maybe encoding all of Shakespeare.

33:51

33 minutes, 51 seconds

Since the underlying model was trained in a different context, you would expect it to perform worse in this different setting-certainly worse than a model that was tailor trained to Shakespearean English.

34:01

34 minutes, 1 second

But here's a clever way that we can tweak the algorithm: rather than having the model stay static during the full compression process, what if you fine-tuned it on the fly?

34:10

34 minutes, 10 seconds

You let it adapt to the particular tokens that it sees along the way.

34:14

34 minutes, 14 seconds

Concretely, this would mean with each new token it sees, you would apply backpropagation to tweak all of the weights based on what it saw.

34:21

34 minutes, 21 seconds

What this would mean is that over the course of the compression process, the model would get better and better tailored to that new context. Text.

34:28

34 minutes, 28 seconds

In order for this to work, over on the decoding side you would have to have the decoder do exactly the same thing.

34:34

34 minutes, 34 seconds

As long as all of the updates are deterministic, the way that the model would get updated on the receiving side would be an identical replay of the way that it was updated during encoding.

34:45

34 minutes, 45 seconds

This is important because the predictions at each step have to stay identical.

34:49

34 minutes, 49 seconds

This is actually an idea used in practice, and in fact you can avoid the need to send any parameters at all.

34:54

34 minutes, 54 seconds

If you have the encoder and decoder start off by generating a completely random model, but pseudo random in a way that's identical for both of them,

35:02

35 minutes, 2 seconds

in either case, when you do this the final compression rate depends not just on the static predictive capacity, but also on how quickly the model

35:10

35 minutes, 10 seconds

is adapting to the new context, that is the better the learning rate, the better the compression.

35:16

35 minutes, 16 seconds

So, zooming out, if we look over the full trilogy, the conclusion from Part 1 was that when Shannon began studying compression rigorously, he was forced to engage with intelligence.

35:27

35 minutes, 27 seconds

Pure data analysis was not enough; he could only estimate the compressibility of English by surveying human predictions.

35:34

35 minutes, 34 seconds

The conclusion of Part 2 was that the modern engineering for artificial intelligence uses mathematical tools that were originally developed to study compression.

35:42

35 minutes, 42 seconds

Together, these two alone hint at a connection between compression and intelligence; it would appear that studying one forces you to engage with the other.

35:51

35 minutes, 51 seconds

For this third part, the upshot is that one of the best compression algorithms we have, say as measured by the Hutter prize, requires using a model which is

35:59

35 minutes, 59 seconds

effective at prediction while being small and which also learns quickly.

36:04

36 minutes, 4 seconds

So are compression and intelligence just really the same thing?

36:08

36 minutes, 8 seconds

The safe answer is of course "no," just as Newton's definition of energy is not the same as Webster's.

36:13

36 minutes, 13 seconds

But if you did need a mathematical definition for intelligence, my own takeaway here is that I was just genuinely surprised that compression takes

36:21

36 minutes, 21 seconds

off many more boxes than I would have guessed the first time that I ever thought about the seemingly innocent task of making files smaller.

### Chapter 7: Three ways to support

36:32

36 minutes, 32 seconds

If you enjoy these videos and you want to support the team behind them, there are three main ways you can do that.

36:37

36 minutes, 37 seconds

If any of you are looking for a career, we have a set of partner organizations actively recruiting and aiming to hire people like you. You can explore them at 3b1b.com slash talent.

36:46

36 minutes, 46 seconds

My main aim with that page is just to give you a little glimpse of each team's culture and what made each one stand out to me enough to recommend them.

36:54

36 minutes, 54 seconds

There is also of course the Patreon, a long-standing backbone of the channel, where channel supporters get early views of new videos.

37:00

37 minutes

That has always been helpful for me in getting feedback for the final edits.

37:04

37 minutes, 4 seconds

And last, there's the store, and there's a couple of fun items that I just added in there for the holidays, like a vinyl record and a fractal mug, so take a look if you're interested.
