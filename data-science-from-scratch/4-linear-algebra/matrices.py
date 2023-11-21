from typing import List, Tuple, Callable
# Matrices are just a two dimensional collection of numbers. The inner list is the row
# Per math convention, use capital letters to define matrices
Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3],  # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

# In math, you would call it "row 1", but in python, typically refer to it as "row 0" or "1st row"

# The shape is the rows by cols, so rows n and cols k would be n X k matrix
def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (# of rows of A, # of columns of A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0   # number of elements in first row
    return num_rows, num_cols

assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns

# Sometimes we'll think of row n as a vector of lenth k, and each column as a vector of length n
def get_row(A: Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i]             # A[i] is already the ith row

def get_column(A: Matrix, j: int) -> Vector:
    """Returns the j-th column of A (as a Vector)"""
    return [row[j] for row in A]           # jth element of row row # for each row row

# We also want to be able to make a row X cols matrix of certain items
# Here is the main maker function, notice it takes a function to decide what to insert
# The two ints are the row and col idx
def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows x num_cols matrix
    whose (i,j)-th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  #   [entry_fn(i, 0), ... ]
            for i in range(num_rows)]   # create one list for each i

# That lambda then takes the i,j to put 1s on each diagonal (1st el on 1st row, 2nd el on 2nd row...)
def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]

# Matrices are important because they can deliver datasets of multiple vectors
# we'll later on use an nxk matrix to represent a linear function that makes k-dimensional vectors to n-dimensional vectors
data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19],
        # ....
       ]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# You can also convert the edges of a network like friendships into a matrix of binary
def matrix_maker(friendships: List[Tuple], num_of_users: int) -> Matrix:
    friend_matrix = [[] for _ in range(num_of_users)]
    friend_sets = {i: set() for i in range(num_of_users)}
    for i, j in friendships:
        friend_sets[i].add(j)
        friend_sets[j].add(i)
    for i in range(10): # row
        for j in range(10): #col
            friend_val = 1 if j in friend_sets.get(i) else 0
            friend_matrix[i].append(friend_val)

    return friend_matrix

#            user 0  1  2  3  4  5  6  7  8  9
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9
assert matrix_maker(friendships, 10) == friend_matrix

# Matrices can be wasteful if most of the nodes don't connect (you just store a lot of zeros )
# However, it is much faster to check if two nodes are connected, instead of checking every one in a graph,
# you can just do asimple lookup
assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"


# and it's similarly easy to look up all of a nodes connections
friends_of_five = [i
                   for i, is_friend in enumerate(friend_matrix[5])
                   if is_friend] # using the truthy/falsy of 1 and 0


# Like vectors, in real life you'd use numpy for matrices
# also check the book for linear algebra textbooks