# Chapters 1-3
# ch 1 setup, Basic Linear Algebra, Basic Statistics
TODO: make sure all deps are downloaded on page 3

# Basic linear Algebra

## Vectors
A `vector` is a one dimensional list of numbers. In math it might look like

```py
a = [0,1,2,3,4]
```
a<sub>2</sub> = 2, vectors are 0-indexed
When a vector may be written horizontally like that it's called a `row vector`

In math, a vector is almost always written vertically

```py
    [ 0 ]
    [ 1 ]
a = [ 2 ]
    [ 3 ]
    [ 4 ]
```
<!-- TODO: any ligatures for vertical vectors? -->
When a column is written this way it's a `column vector`

We'll typically use vectors to represent one `sample`: one set of features that we'll input into a model

Mathematically, vectors are used to represent points in space

so on a Cartesian (2D) plane we use a 1 dimensional vector with 2 numbers [x, y]

If we had a 3D plane, we'd use a 1 dimensional vector with 3 numbers

## Matrices
Vectors can have more than one dimension, meaning each value in a vector is another vector

```py
    [ 1  2  3 ]  0
a = [ 4  5  6 ]  1  first dimension
    [ 7  8  9 ]  2
      0  1  2
   second dimension
```
a<sub>1,2</sub> = 6 So I think the way that it goes is rows, then columns (not sure if this is always the case as in the book it looks like the matrix is written with 3 column vectors, which would imply the order is reversed?)

## Multiplying Vectors

```math
[1,2,3] X [4,5,6] = [4,10,18]
```
That's the default assumption, though really mathematically thats:

```math
[1]   [4]   [4 ]
[2] x [5] = [10]
[3]   [6]   [18]
```
It's assumed your dealing with column vectors unless specied

Specifying is important because multiplying a column and a row in different orders matters

A super script `T` means a vector is a row

AB<sup>T</sup> =
```math
[a]             [ad ae af]
[b] x [d e f] = [bd be bf]
[c]             [cd ce cf]
```
 the `outer product` is a matrix

A<sup>T</sup>B =

```math
          [d]
[a b c] x [e] = ad + be + ef
          [f]
```
the `inner product` (or `dot product`) is a single number, a `scalar`


## Multiplying Vectors and Matrices
When multiplying a vector and a matrix, the vector typically goes on the right side

It can only work if the number of columns in the matrix matches the number of elements in the vector
- The vector is assumed to be a column vector, not sure if row would change things
- otherwise the multiplication is undefined

The end result is a vector with as many rows as the original matrix

```math

[a b c]   [x]   [ax + by + cz]
[d e f] x [y] = [dx + ey + fz]
          [z]
```

The same idea applies to matrix x matrix multiplication

```math

[a b c]   [A B]   [aA + bC + cE   aB bD cF]
[d e f] x [C D] = [dA + eC + fE   dB eD fF]
          [E F]
```
Notice how we have a 2x3 matrix and a 3x2 matrix, and the output is 2x2 matrix

Generally we'll work with 3 and 4 dimensional vectors called `tensors` when we get to convoluted neural networks


# Basic Statistics

## Descriptive Statistics
`median`
- Sorted items first, then find the literal middle. If it's an even number of items, take the mean of the 2 middles

`mean` or `average`
- sum of all items/number of items

`standard error of the mean (SE)`
- A measure of how far each individual item is away from the mean

## Calculating Standard Error
Assume we have many (`n`) individual measurements (`x`), the length of a flower stem, we can calculate the mean (`X`).

Once we have that we can calculate the average spread of individual values around the mean by:
  - subtract each value from the mean
  - square that result

Then take all those individual results and add them together and then divide that by result by `n`, minus 1

That number that we just got is called the `variance`

Take the `variance` and square root it to get hte `standard deviation` (`o` (with a swoosh))

FINALLY to get the standard error it's

SE = `o` / n<sup>1/2</sup>

What that all boils down to is the smalled the standard error is, the more tightly clustered the data points are

We can interpret the value as the uncertainty we have about the mean (`X`) value

we can expect `X` which we don't technically know, to always be between `X` - SE and `X` + SE

`descriptive statistics` are values derived from the data, the three we used , `mean`, `median` and `standard deviation` are common


## Probability Distributions
`probability distributions` are how the data points are distributed

When we are training models, we give a set of ideal data that our model is approximation, this is the `parent distribution`

This book seems to refer to the model as an "oracle" giving a prediction.

There are many types of distributions, two common ones are `normal` and `uniform`

`uniform` means all options have the same chance of appearing
  - Mathematically written as `U(a,b)` where `U` means uniform and `a, b` are the range of data points
  - Unless specified, any real number between `a` and `b` is allowed, it's not just ints
  - we say `x ~ U(a,b)` meaning x is the value returned by the oracle
  - note that () are significant () means "exclude the bound" so (0,1) is all but not include 0 or 1, and [0, 1] means all including 0 and 1. Lastly, mix and match is ok [0, 1) means all not include 1, (0, 1] means all not include 0

`normal` is a bell curve (sometimes called `Gaussian Distribution`), where things clump around a most likely value. The further you go from that value, the less likely your data will appear.

The most likely value is the mean, and the parameter that determines how quickly the likely hood drops to 0 or 100 (without ever reaching it) is the standard deviation (sigma).
  - `x ~ N(X, o)` would be the sample from a normal distribution
  <!-- Todo, replace with greek mean and sigma -->

## Statistical Tests
We'll run tests on hypotheses. Typically the hypothesis is 2 sets of measurements, and whether or not those 2 measures resulted from the same parent distribution

If the stats calculated about them fall outside a certain range, it means we reject it because there's such low confidence in the result.

the `t-test` is a common stat test that assumes data is `normally distributed` (which it may or may not be)

the `t-test` is known as a `parametric test`
<!-- todo what is a parametric -->

the `Mann-Whitney U Test` is like a `t-test` but makes no assumptionas about the parent distributions.

the `Mann-Whitney U Test` is a `non-parametric test`

Whether or not parametric, each test gives us a `p-value` which is the probability that we sould see the test statistic  in the parent distribution

the `p-value` cutoff is 0.05 or less, indicating a 1-in-20 chance that we'd measure the test stat value even if the samples came from the same distribution

However, that's apparently too generous, and updated scientific rigors have said if the p value is 0.05 exactly, there's likely evidence against out hypothesis

if our p value is 0.01 we can be pretty confident the sample is *not* from our parent distribution.

In that case, we can say the difference is `statistically significant`

<!-- todo: your grasp on P value is tenuous at best, look it up later -->