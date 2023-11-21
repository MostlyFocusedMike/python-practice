from typing import List
from collections import Counter
import matplotlib.pyplot as plt

# Statistics refers to the mathematics and techniques used to understand data


num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


# Trying to determine data about the number of friends, you can make a histogram of the friends
histogram = Counter(num_friends)
print(histogram)

friend_counts = Counter(num_friends)
xs = range(101)                         # largest value is 100
ys = [friend_counts[x] for x in xs]     # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
# plt.show()

# That histogram doesn't give you many "fun facts" though
# So you can start looking for them with superlatives

num_points = len(num_friends)               # 204
largest_value = max(num_friends)            # 100
smallest_value = min(num_friends)           # 1

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]           # 1
second_smallest_value = sorted_values[1]    # 1
second_largest_value = sorted_values[-2]    # 49


# Central Tendencies
# We'll often want to know where the data is centered
# So finding the average (mean) is a good start
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

mean(num_friends)   # 7.333333

# fun: this is how you check for repeating quickly
assert 7.3333 < mean(num_friends) < 7.3334

# However, mean can be off due to highs or lows swerving data
# Median is the middle most value (or average of two middles if theres an even number of data points)

# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2 because // is floor round

    # We subtract one instead of add one because the len starts at 1, but indexes start at 0. So 4 middle is 2, but the low middle is 1
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2
assert median(num_friends) == 6

# A generalization of the median is the 'quantile' (not quartile, that's different) which represents the value under which a certain percentile of the data lies
# The median represents the value under which 50% of the data lies (which makes sense it's in the exact middle of the data points) Median is the 50th percentile/quantile (the names are the same)
# the median, 1st and 3rd quartile are just quantiles which chop the data into 4ths

def quantile(list_of_data: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(p * len(list_of_data)) # remember int fully rounds down (it just chops of the decimal)
    return sorted(list_of_data)[p_index]

assert quantile([1,2,3,4,5,6,7,8,9,10], 0.25) == 3
assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3 # often called the first quartile, Q1, so 1/4 of data is below
assert quantile(num_friends, 0.75) == 9 # The third quartile, Q3, so 3/4 of data is below
assert quantile(num_friends, 0.90) == 13  # called 90th percentile/quantile, you can use any number, not just he special 3

# Mode is also sometimes useful, it's the most frequent number that appears. That's it. There can also be more than one, and it doesn't show how many times the number appeared, just that the number was the most
def mode(x: List[float]) -> List[float]:
    """Returns a list, since there might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

assert set(mode(num_friends)) == {1, 6}

# Fun fact the "box plot" that you often see in graphs is a box from Q1 to Q2, and the top and bottom line are the max and min
# _____
#   |  _____ - max
#  ---   |
#  | |   |
#  | |  ---  - Q3
#  | |  | |
#  | |  | |
#  | |  | |  - median
#  | |  | |
#  | |  | |
#  | |  ---  - Q1
#  ---   |
#   |  ----- - min
#   |
# -----

# Dispersion
# Dispersion refers to the measures of spread that our data points are. low number = low spread and high number = high spread
# What that means is up to us, but it's called the 'range' of data (here we call it data_range, because range is a keyword)
# "range" already means something in Python, so we'll use a different name
def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

assert data_range(num_friends) == 99

from linear_algebra import sum_of_squares