# Chapter 4 - Working with data
- "Garbage in, garbage out" - getting your model dataset right is crucial

## Classes and Labels
- "Classification" is breaking things down into `class` and `labels`
- `class` a discrete category ("dog breed", "flower")
- `label` are an identifier for a class ("border collie" OR a number like 0-10(that's best?))
- models don't know what a class is, they just label it
  - It's all numbers, so every dog to the model is just 5 and every cat is a 9

## Features and feature vectors
- Machine learning models take in `features` and output something
  - Example When using a classifier model, it would output a label
- `features` are always numbers
  - pixel color, object size, number of students
- We train the model with known features and outputs, and then give it unknown data to label
- if our model does poorly, it could be that the relationships in the features may not be as strong


## Types of features
- `features` = numbers representing something that is measured or known
- `feature vectors` are set of these numbers used as inputs to the model
- These numbers can take many forms:
  - continuous floating points (models like these, some even require it)
  - Numerical: discrete
    - The spaces between these numbers are called the `interval value` and should be the same (1 -> 2 is 3 -> 4)
    - There is no in between values
  - Numerical: continuous
    - When the numbers can have fractions between them
  - Categorical: Ordinal
    - When the order matters, but the `inteval value` is not the same across values
    - "completed masters" "completed college" and "completed high school", 3 > 2 > 1 but 3 and 2 are not the same distance as 2 to 1
  - Categorical: Nominal
    - These are categories that are discrete, but no ordinal or interval relationship
    - Example gender m f non binary have no ordinal or math value to each other
    - Usually encoded as numbers
    - Can take a single value and make it a vector of binary
    - 0, 1, 2 for m/f/n becomes [1 0 0]/[0 1 0]/[0 0 1] vectors
    - Now, we have 3 ordinal values "is male" "is female" "is non binary" 0 meaning "no" and 1 meaning "yes"
    - To do this, the categories must be mutually exclusive
    - Because only one nonzero value per row, this vectorizing is called "one-hot encoding"

## Feature selecting and the curse of dimensionality
- When determining features for the feature vector, only include features that will help the model to generalize new data
  - only use aspects of the data that help the model separate classes
- `curse of dimensionality` is the fact that as you get more features, the required sample size increases by a power of 10 to get an accurate reading of the feature space (feature space is the dimensions we'd need to see the dots represented in a grid)
  - Generating 100 data points in 2d and 3d space:
    - A 2d vector from [0,1) float requires 10 x 10 grid and we hit 40% of cells
    - A 3d vector from [0,1) float required 10 x 10 x 10 grid to sample we hit 5% of cells
    - A 4d vector from [0,1) float required 10 x 10 x 10 x 10 grid to sample we hit .05% of cells
- As the number of features increase, the training size increases by $10^d$ where $d$ is is the number of dimensions for the feature space
- So feature vector of 3 genders, 10 locations, 12 income brackets would need $3 \times 10 \times 12 = 10^{360}$ samples
- Modern deep learning has overcome this, but with traditional models it can still be present

## Features of a good Dataset
- Let's strictly defined `dataset` as a collection of $\{X,Y\}$ pairs, where X is some set of features with a Y label.
- for `supervised learning` we pretend to be a teacher and our model is the student. In this case the `dataset` is a collection of examples and `training` is just showing them over until the model correctly identifies what we know to be true

## Interpolation vs extrapolation
- `interpolation` means we're looking for a prediction *within* our trained data set (knowing population of planet from 1900-1960 every ten years, then guessing the population of 1943)
- `Extrapolation` is going *beyond* the trained data, it usually goes poorly
- The dataset must cover the full range of variation within the classes the model will see when the model is predicting labels for unknown inputs

## The parent distribution
- All datasets have the idea that they are a subset of some ideal `parent distribution` of perfection
- Like our "pictures of border collies" dataset is just a subset of a 100% accurate collection of perfect border collie pictures
- A `uniform parent distribution` is when all outcomes within the dataset *should* be the same (like the chance of rolling a number on a dice)
- It's an active area of research to overcome the problem of training a model on one parent distribution, and then using it for another (domain adaptation research)

## Prior Class Probabilities
- `prior class probability` is the probability that each class in the dataset appears in the wild
- So if class A appears 80% in the wild, and class B 20%, then we would want that to match our training set
- However, for super rare things, that may not be the case. If something is 1 in a million, we will need more than that to train the model to know what it is.
- We don't know why it works, but training rounds that start equal-ish and get more and more real world ratios allow neural nets to handle these better
  - 1/10th 4 leaf glovers, then 1/1000 then 1/1000000 etc
- Sometimes in Machine learning we'll know something works, but not why, and that's just how it is

## Confusers
- Its also important to include things that are close but not our classes to train our models
- `confusers` or `head negatives` are useful because they are similar but not exact matches that help train our model to know the boundaries
- eg dog vs not dog, make sure to include pictures of wolves so that it doesn't think they're dogs

## Dataset size
- There is no formula to determine the "right" amount of data for training
- You have to gauge where the big boosts are vs diminishing returns 100 - 10000 - 100000 are likely not the same gains
- Models have a `capacity` which determines the level of complexity that it can support relative to the amount of training data available
  - the `capacity` of a model is directly related to the number of parameters
  - More parameters === much more training data


# Data Preparation
- talking about how to scale and what to do with missing feature values

## Scaling Features
- Each feature could take on a wide range of values 0 $-$ 1 or -500 $-$ 4,000
- Some models won't like wide ranging features, and prefer everything to be close to 0
- The solution to these issues is scaling the features so that they aren't so different

Here is what a 5 feature vector
| Sample | $x_0$ | $x_1$ | $x_2$ | $x_3$ | $x_4$ | Label |
|--------|-------|-------|-------|-------|-------|-------|
| 0      | 9823  | 0.123 | ...   | ...   | ...   | 0     |
| 1      | 1230  | 0.890 | ...   | ...   | ...   | 1     |
| 2      | 1422  | 0.787 | ...   | ...   | ...   | 2     |
| 3      | 1001  | 0.581 | ...   | ...   | ...   | 2     |
------------------------------
(assume the ... are numbers )

- The sample id always starts at 0
- The label in this case has 3 possibilities
- When referring to full feature sets we could write $\{x_0, x_1, x_2, x_3, x_4\}$, but that's tedious, instead we say, for the third entry it would be $X_2$ for dataset $X$.

## Mean centering
- The idea behind mean centering is simple: subtract the mean of the feature from each individual feature value
- The goal is to maintain the range, but get the mean centered around 0, and not some positive or negative number
  - This avoids bias in the dataset
- Here's the formula:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$
$$
x_{i}^{'} = x_{i} - \bar{x}
$$

- And here's an example:
- Take this feature data from across the entire dataset: [2, 4, 6, 8, 10].
- Calculate the mean:
  Mean = (2 + 4 + 6 + 8 + 10) / 5 = 6
- Subtract the mean from each value
[2 - 6, 4 - 6, 6 - 6, 8 - 6, 10 - 6] = [-4, -2, 0, 2, 4]
- so the mean went from +6 to 0, but the range is still 8.

## Changing the standard deviation to 1
- For a refresher on standard deviation, see ch. 1
$$
\sigma = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} }
$$
- Anyway, the idea is to get the spread of the values, the `standard deviation` down to 1 (vs 8 like above).
- The formula is simple

$$
x \lArr \frac{x - \bar x}{\sigma}
$$

- For each feature in the vector, you just subtract the mean (mean centering) then divide by the standard deviation.
- Numpy does this for us *really* easily:

```python
import numpy as np
x = np.array([
  [6998, 0.1361, 0.3408, 0.00007350, 78596048],
  [6580, 0.4908, 3.0150, 0.00004484, 38462706],
  [7563, 0.9349, 4.3465, 0.00001003, 6700340],
  [8355, 0.6529, 2.1271, 0.00002966, 51430391],
  [2393, 0.4605, 2.7561, 0.00003395, 27284192],
  [9498, 0.0244, 2.7887, 0.00008880, 78543394],
  [4030, 0.6467, 4.8231, 0.00000403, 19101443],
])
x = (x - x.mean(axis=0)) / x.std(axis=0)
array([[ 0.22242681, -1.17689041, -1.86844102,  1.13414242,  1.37019878],
       [ 0.04007297,  0.04390722,  0.09521741,  0.14353921, -0.16920818],
       [ 0.46890987,  1.57239953,  1.07293456, -1.05963239, -1.38752704],
       [ 0.81442241,  0.60181896, -0.55676536, -0.38114177,  0.32819731],
       [-1.78651919, -0.06037857, -0.09489222, -0.23286236, -0.59798588],
       [ 1.31305982, -1.56133668, -0.07095412,  1.66297107,  1.36817912],
       [-1.0723727 ,  0.58047995,  1.42290075, -1.26701617, -0.91185411]])
```
- the `.mean` and `.std` find the mean and standard deviation of the entire array by default, however including `axis` will make it find the value for (in a 2d array) either each row (`axis=1`) or each column (`axis=0`)
  - Numpy is then smart enough to apply these arrays of means and deviations to the whole array like we'd want through broadcasting
- This is called `standardization` or `normalizing` and in general we want to do this to all our datasets
- Whenever possible you want the mean to be as close to 0 and the standard deviation to be as close to 1

## Missing Features
- Two main strategies:
  - Fill in missing data with outside the range of data and hope the model picks it up to ignore it
    - Some models do this automatically and replace certain features with 0
  - Find the mean of the existing features, and then replace any missing data with the mean
- The mean approach works best when very few features are missing

# Training, Validation, and Test Data
- Once you have your dataset, you split it up into 3 different parts
- `training` this is about 90% and it's used to actually train the model
- `validation` this is about 5% and it's not required. You can use it to validate whether your training is going well, or if you should 90stop and try something different
- `testing` this is that last 5% and you must *never* show it to the training until you're done. That's cheating, because your model would then test on data it's already seen.
- on newer models, testing and validation may only be 1% of the data each, but older models may need more so 80 10 and 10

```python
import numpy as np
from sklearn.datasets import make_classification

x,y = make_classification(n_samples=10000, weights=(0.9,0.1))
x.shape
```


- Here's how the make_classification works:

```python
from sklearn.datasets import make_classification

dataset, labels = make_classification(
    n_samples=100, # 100 observations
    n_features=4,
    n_classes=2, # binary target/label default 2
    weights=(0.9,0.1)
)

# This seems to be convention for x y
x, y = make_classification(
    n_samples=100, # 1000 observations
    n_features=5, # 5 total features
    n_informative=3, # 3 'useful' features
    n_classes=2, # binary target/label default 2
    random_state=999 # if you want the same results as mine
)
```










