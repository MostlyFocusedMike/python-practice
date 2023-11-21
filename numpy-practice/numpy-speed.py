import numpy as np
import time
import random

print('Starting...')
'''
multiplying vectors requires you to multiply each item in one vector against each in the other
The point of this file is to show just how slow that is with lists (and clunky) compared to
the array() of numpy
'''
limit = 10000000
range_a = [random.random() for i in range(limit)]
range_b = [random.random() for i in range(limit)]

arr_1 = np.array(range_a)
arr_2 = np.array(range_b)

start = time.time()
comprehension_test = [range_a[i] * range_b[i] for i in range(limit)]
print('Comprehension time: ', time.time() - start)

start = time.time()
for_loop_test = []
for i in range(limit):
	for_loop_test.append(range_a[i] * range_b[i])

print('For Loop time: ', time.time() - start)



start = time.time()
nupmy_test = arr_1 * arr_2
print('numpy arr time: ', time.time() - start)

