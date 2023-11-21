from typing import List
from functools import reduce  # omit on Python 2
import operator

Vector = List[float]
# vectors are poins in finite-dimensional space. They are n-dimensional, with n being the number of coordinates inside
# [1,4] is a vector in 2D space. Can be as many points as needed


height_weight_age = [
    70,  # inches,
    170, # pounds,
    40,  # years
]

grades = [
    95,   # exam1
    80,   # exam2
    75,   # exam3
    62    # exam4
]

# Vectors can be added together, and they can be multiplied by _scalars_ (numbers) to form new vectors
# Adding is just adding each individual point together
# Adding this way is called "componentwise" (essentially, each point is a component)
def add(v: Vector, w: Vector) -> Vector: # it seems to be a math convention to use v and w for vec1 and vec2
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

# Subtraction is exactly the same idea
def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

# We might also want to sum many vectors together into one
# Remember that our typing module means we expect a list of vectors
def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_of_idxs = len(vectors[0])
    assert all(len(v) == num_of_idxs for v in vectors), "different sizes!"

    # the i-th element of the result is the sum of every vector[i]
    return [
        sum(vector[i] for vector in vectors) for i in range(num_of_idxs)
    ]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

def vector_subtract_all(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    num_of_idxs = len(vectors[0])
    assert all(len(v) == num_of_idxs for v in vectors), "different sizes!"

    # we're using reduce and __sub__ with reduce on
    return [
        reduce(operator.__sub__, [vector[i] for vector in vectors]) for i in range(num_of_idxs)
    ]

assert vector_subtract_all([[7, 8], [1, 2], [3, 4] ]) == [3, 2]

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    # remember multiplying by the inverse fraction is the same as division
    # So we're finding the mean vector by summing all vectors, and then dividing by the number we entered (via multiplication)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 6], [5, 10]]) == [3, 6]

# The dot product is the sum of their componentwise products (ie each point of the two vectors multiplied together, and then summing all those products)
# Not sure what this is good for
def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6

# Sum of squares seems to just be good for finding magnitude?
def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3


import math
# Magnitude is the length of the vector
def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function

assert magnitude([3, 4]) == 5


# Now we have all the functions needed to find the distance between 2 vectors:
#           ____________________________________
#          / (V1 - W1)^2 + ... + (Vn - Wn)^2
#        \/


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

# Here is the final distance function
def distance_raw(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))

# Although clearer that would be
def distance(v: Vector, w: Vector) -> float:  # type: ignore
    return magnitude(subtract(v, w))

#
#  So, everything built by hand would be better to use NumPy array class, since using lists like htis would be awful for performance
#

