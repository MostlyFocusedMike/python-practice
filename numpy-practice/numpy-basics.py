import numpy as np
from numpy import random

arr = np.array([1,2,3,4])
# print(arr)
# if you put that into the console it will say 'array([1,2,3,4])' instead of just '[1,2,3,4]' like a built in list would
# if you print to the screen, both just do [1,2,3,4]

# print(arr.size)
# 4

# print(arr.dtype)
# dtype('int64')

# print(arr.shape)
#(4,)
# that's the length of each arr, i think that's just how python prints tuples

# create a np array using a range, which is (0->(n-1)) or (x -> (n-1))
ten = np.arange(10) # 0 - 9
four = np.arange(1,3) # 1 - 2
# print('TEN: ', ten)


tuple_arr = np.array((1,2,3,4))
# print(tuple_arr)

u8_arr = np.array([1,2,3,4], dtype="uint8")
# print(u8_arr.dtype)


# Matrix
matrix = np.array([[1,2],[3,4],[5,6],[7,8]])
# print(matrix.shape)
# (4,2)
# the numbers correspond to the number of things at each level of the nested array, top down
# so in this case the top array as 4 elements, and each of those arrs have 2

matrix_2 = np.array([
	[
		[1,2,3,4], [5,6,7,8]
	],
	[
		[9,10,11,12], [13,14,15,16]
	],
	[
		[17,18,19,20], [21,22,23,24]
	],
])
# print(matrix_2.shape)
# (3,2,4)
# so that's 3 top arrs, each with 2 arrs in them, each with 4 items, so 3,2,4

# This would be tedious to do, so we can use the .zeros() function to create multidimensional vectors where each value is set to 0

zeroed_vec = np.zeros((2,3,4))
# print(zeroed_vec)
# print(zeroed_vec.shape)
# print(zeroed_vec.dtype)
# inited to floats, which we can fix

# print('Convert to uint')
zeroed_vec = np.zeros((2,3,4), dtype='uint32')
# print(zeroed_vec.dtype)
# We need to be concsious of type when building massive arrays because floats take up a lot of memory

# if we don't want 0s we can also use 1s

vec_ones = np.ones((2,3,4), dtype='uint32')
# print(vec_ones)
# print(vec_ones.dtype)

# the reason why .ones() is so good is because we can use multiplication of vectors to get any number we want


vec_12s = 12 * np.ones((2,3), dtype='uint32')
# print(vec_12s)
# remember a scalar value * a vector just multiplys each value of the vector, no looping required!
# this also holds true for other actions like +,-,/

# print(vec_12s.astype('uint8'))
# the as type method will attempt to copy the array cast as the given type. If the data can't fit (float64 to uint8) then the data will be lost

# numpy arrays are pass by reference, to may a copy do
base_arr = np.array([1,2,3,4,5])
copy_arr = base_arr.copy()
other_copy = base_arr[:]

# I think it's a shallow copy, tbd

# we can start with an array of one shape and then reshape it

a = np.arange(20)
# print('flat arr: ', a)
b = a.reshape((4,5))
# print('matrix 4 X 5', b)
# the reshape method tales a tuple, but there must be enough elements to remake it

c = np.arange(18).reshape((2,3,3))
# print('3d matrix: \n', c)

# ACCESSING ELEMENTS
# print(np.arange(10)[0]) # 0
# print(np.array([np.arange(10)])[0]) # [0 1 2 3 4 5 6 7 8 9]
# print(np.array([np.arange(10)])[0][0]) # 0
# print(np.array([np.arange(10)])[0,0]) # 0, this is shorthand of the above

# slicing arrays
# It's the same : syntax as lists, inclusive exclusive

a = np.arange(10)
# print(a[0:4]) # [0 1 2 3]
# print(a[2:4]) # [2 3]
# print(a[:4]) # [0 1 2 3]
# print(a[3:]) # [3 4 5 6 7 8 9]
# print(a[:]) # [0 1 2 3 4 5 6 7 8 9]  this is just a copy
# print(a[0:8:2]) # [0 2 4 6] the third optional arg is for step size, it's neat

# print(a[-1]) # 9
# print(a[-2]) # 8
# print(a[:-2]) # [0 1 2 3 4 5 6 7]
# print(a[::-1]) # [9 8 7 6 5 4 3 2 1 0] real neat trick, since step can be negative, this will reverse the arr


# We can replace elements with assignments
a = np.arange(10)
a[2] = 20
# print("replaced 2: ", a)

# but we can also replace multi dimensional arrays with OTHER multi dimensional arrays
c = np.arange(27).reshape((3,3,3))
# print('3x3X3 matrix: ', c)

b = np.ones((3,3))
# print('3x3 matrix of ones: \n', b, '\n')

c[0] = b
# print('replaced: \n', c)

# OK but you can also do it this way for some reason? I don't know why we need to specify when totally replacing
c[1,:,:] = b
# print('weird replaced: \n', c)

# theres a shorthand for the above, which is this:
c[2,...] = b
# print('weird shorthand replaced: \n', c)

#  The book says that the ellipse shorthand is used a lot, so there must be something i'm missing

# OPERATORS AND BROADCASTING
# "Broadcasting" seems to be the method by which numpy decides how to do math operations
a = np.arange(4)
print(a+1)
# for scalar values, it just applies the operation to every item in the array, regardless of shape

# But broadcasting is smart enough to figure out if an array matches some dimension of another, when they are operated on
# it will make it work. So here a 5x5 array multiplied each row by the single dimension array of 5 elements
a = np.arange(5)
b = np.arange(25).reshape((5,5))

print('b 5X5 starting arr: \n', b)
print('b multiplied by single dimension array: \n', b*a)

# BUT remember that the dimensions SOMEHOW have to match, here a 3 len array fails to multiply a 5x5 arr and throws an err

a = np.arange(3)
b = np.arange(25).reshape((5,5))

print('b 5X5 starting arr: \n', b)
# print('b multiplied by single dimension array: \n', b*a)
# ValueError: operands could not be broadcast together with shapes (5,5) (3,)


# the .dot function and linear algebra matrix maths
# in linear algebra the "dot product" of two vectors is to multiply each element to the corresponding element, then add them all together

x = np.arange(5)
print('The dot is 30: ', np.dot(x,x))
# [0,1,2,3,4] x [0,1,2,3,4] = [0,1,4,9,16] = 0 + 1 + 4 + 9 + 16 = 30

# It gets mor complicated for matrices
a = np.arange(9).reshape((3,3))
b = np.arange(9).reshape((3,3))

dot_a_b = np.dot(a,b)
print('dot_a_b: \n', dot_a_b)
#  [
#    [ 15  18  21]
#    [ 42  54  66]
#    [ 69  90 111]
#  ]
# the way that matrix dot products work is like this
# the dot still needs vectors, so it goes like 2 cross beams

'''
0 1 2       0 1 2     a b c
3 4 5  dot  3 4 5  =  d e f
6 7 8       6 7 8     g h i

a
x - -
|
|

[0,1,2] X [0,3,6] = 0 + 3 + 12 = 15

b
- x -
  |
	|

[0,1,2] x [1,4,7] = 0 + 4 + 14 = 18

'''
# This beam pattern extend out with each dimension i think, i can't really visualize beyond 3d though
# Remember dot() [dot product) is NOT the same as striaght multiplication, which just multiplies each
#  corresponding element

#-------------------------------
# RANDOM NUMBERS
# the 'random' library

# Random distribution is even choice of any 0-1 num
print(random.random())
# normal is a bell curve distribution
print(random.normal())

# Use a seed value (no idea if 1 is good idea) to make sure that
# each call is a random number, but from the start it is repeatable
random.seed(1)
print('-------------------------------')
print('Same every time')
print(random.random())
print(random.normal())
print(random.random())
print(random.normal())
# these always output the same random numbers now, but are different from each other
#-------------------------------