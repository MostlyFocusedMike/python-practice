"""
THIS IS A MULTI LINE COMMENT
This is just code for the introduction to Python.
It also won't be used anywhere else in the book.
"""
# type: ignore

# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they're helpful for anyone reading the code.
for i in [1, 2, 3, 4, 5]:
    print(i)                    # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)                # first line in "for j" block
        print(i + j)            # last line in "for j" block
    print(i)                    # last line in "for i" block
print("done looping")

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

two_plus_three = 2 + \
                 3

for i in [1, 2, 3, 4, 5]:

    # notice the blank line
    print(i)

# This is a standard import
import re
my_regex = re.compile("[0-9]+", re.I)

# This is an aliased import
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

# instead of using .method, .method2, you can specify explicitly
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

'''
It's not a good idea to use the star and import everything
match = 10
from re import *    # uh oh, re has a match function
print(match)        # "<function match at 0x10281e6a8>"
'''
# define functions using the def keyword and a :
def double(x):
    """
    This is where you put an optional docstring that explains what the
    function does. For example, this function multiplies its input by 2.
    """
    return x * 2

def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

# python has first class functions
my_double = double             # refers to the previously defined function
x = apply_to_one(my_double)    # equals 2

# assert does nothing if expression is true, raises an assertion error if it is not
assert x == 2

# lambdas are one line anonymous functions
y = apply_to_one(lambda x: x + 4)      # equals 5
# a lambda is `lambda arguments : expression`

assert y == 5

another_double_bad = lambda x: 2 * x       # Don't use a lambda in a variable, just use def

def another_double(x):
    """Do this instead"""
    return 2 * x


# Default arguments
def my_print(message = "my default message"):
    print(message)

my_print("hello")   # prints 'hello'
my_print()          # prints 'my default message'

def full_name(first = "What's-his-name", last = "Something"):
    return first + " " + last

full_name("Joel", "Grus")     # "Joel Grus"
full_name("Joel")             # "Joel Something"
full_name(last="Grus")        # "What's-his-name Grus"


assert full_name("Joel", "Grus")     == "Joel Grus"
assert full_name("Joel")             == "Joel Something"
assert full_name(last="Grus")        == "What's-his-name Grus"

# This is the closest thing to object destructuring in js
def create_user(user):
    name, age, bio = user
    print(f'name: {name}, age: {age}, bio: {bio}')

# Important to know: you can use both named and positional variables at once, the positionals come first






# Quote type doesn't matter
single_quoted_string = 'data science'
double_quoted_string = "data science"

# python uses \ for special characters
tab_string = "\t"       # represents the tab character
len(tab_string)         # is 1


assert len(tab_string) == 1

# if you want actual raw string backslashes, use the r"" string
not_tab_string = r"\t"  # represents the characters '\' and 't'
len(not_tab_string)     # is 2


assert len(not_tab_string) == 2

# newlines are preserved in these multi line strings
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name             # string addition
full_name2 = "{0} {1}".format(first_name, last_name)  # string.format

full_name3 = f"{first_name} {last_name}"







# exceptions are like this
try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")






# Arrays are called lists
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True] # can mix types no problem
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)     # equals 3
list_sum    = sum(integer_list)     # equals 6
assert list_length == 3
assert list_sum == 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0]          # equals 0, lists are 0-indexed
one = x[1]           # equals 1
nine = x[-1]         # equals 9, 'Pythonic' for last element
eight = x[-2]        # equals 8, 'Pythonic' for next-to-last element
x[0] = -1            # now x is [-1, 1, 2, 3, ..., 9]


assert x == [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Getting list slices with :
first_three = x[:3]                 # [-1, 1, 2] exclusive
three_to_end = x[3:]                # [3, 4, ..., 9] inclusive
one_to_four = x[1:5]                # [1, 2, 3, 4] inclusive:exclusive
last_three = x[-3:]                 # [7, 8, 9]
without_first_and_last = x[1:-1]    # [1, 2, ..., 8]
copy_of_x = x[:]                    # [-1, 1, 2, ..., 9] makes a copy

# Third argument indicates the 'stride' which is how it moves, it can be negative
every_third = x[::3]                 # [-1, 3, 6, 9]
five_to_three = x[5:2:-1]            # [5, 4, 3]


assert every_third == [-1, 3, 6, 9]
assert five_to_three == [5, 4, 3]

# the in operatore checks if something is in a list
1 in [1, 2, 3]    # True
0 in [1, 2, 3]    # False

# Mutational concatenation
x = [1, 2, 3]
x.extend([4, 5, 6])     # x is now [1, 2, 3, 4, 5, 6]


assert x == [1, 2, 3, 4, 5, 6]

# non mutational concatenation
x = [1, 2, 3]
y = x + [4, 5, 6]       # y is [1, 2, 3, 4, 5, 6]; x is unchanged

assert x == [1, 2, 3]
assert y == [1, 2, 3, 4, 5, 6]

# append adds to list
x = [1, 2, 3]
x.append(0)      # x is now [1, 2, 3, 0]
y = x[-1]        # equals 0
z = len(x)       # equals 4
assert x == [1, 2, 3, 0]
assert y == 0
assert z == 4

# list destructuring
x, y = [1, 2]    # now x is 1, y is 2
assert x == 1
assert y == 2

_, y = [1, 2]    # now y == 2, didn't care about the first element


# tuples are Immutable
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4  # please don't use this for me. I know it's allowed but please don't
my_list[1] = 3      # my_list is now [1, 3]

# try:
#     my_tuple[1] = 3
# except TypeError:
#     print("cannot modify a tuple they are immutable, remember?")

def sum_and_product(x, y):
    return (x + y), (x * y) # This is using a tuple without () and I super hate it

sp = sum_and_product(2, 3)     # sp is (5, 6)
s, p = sum_and_product(5, 10)  # s is 15, p is 50

x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # Pythonic way to swap variables; now x is 2, y is 1
assert x == 2
assert y == 1

# Dictionaries are like objects in JS
empty_dict = {}                     # Pythonic
empty_dict2 = dict()                # less Pythonic
grades = {"Joel": 80, "Tim": 95}    # dictionary literal

joels_grade = grades["Joel"]        # equals 80


assert joels_grade == 80

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate! Trying for a non existent key throws an actual error, be careful")

# Check if key exists with in
joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False
assert joel_has_grade
assert not kate_has_grade

# Or use the .get() method, which returns the value, or None (or a provided default)
joels_grade = grades.get("Joel", 0)   # equals 80
kates_grade = grades.get("Kate", 0)   # equals 0 (because Kate doesn't exist)
no_ones_grade = grades.get("No One")  # default default is None
assert joels_grade == 80
assert kates_grade == 0
assert no_ones_grade is None

grades["Tim"] = 99                    # replaces the old value
grades["Kate"] = 100                  # adds a third entry
num_students = len(grades)            # equals 3, len() works on dicts and lists
assert num_students == 3

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys   = tweet.keys()     # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items  = tweet.items()    # iterable for the (key, value) tuples

"user" in tweet_keys            # True, but not Pythonic
"user" in tweet                 # Pythonic way of checking for keys
"joelgrus" in tweet_values      # True (slow but the only way to check)
assert "user" in tweet_keys
assert "user" in tweet
assert "joelgrus" in tweet_values


# Imagine trying to count the number of times a word appears in a document
document = ["data", "science", "from", "scratch"]

# You could use `in` to check if key exists
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# You could just handle the exception
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
# You could also use get with a default argument
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1


# But ALL Those ways are kind of unweild, so defaultdict says if a lookup fails,
# it will auto insert a base (empty) value that you specify via a callback
from collections import defaultdict

word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # {"Joel" : {"City": Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0, 1]}



# Counter is a really cool way to take an iterator and turn it into a defaultdict(int)
from collections import Counter
c = Counter([0, 1, 2, 0])          # c is (basically) {0: 2, 1: 1, 2: 1}

# recall, document is a list of words
word_counts = Counter(document)

# Counter has a .mostCommon() method. It returns a list of tuplesprint the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print(word, count)


# Sets are a list of DISTINCT elements
primes_below_10 = {2, 3, 5, 7}

# create an empty set with set(), not {}
s = set()
s.add(1)       # s is now {1}
s.add(2)       # s is now {1, 2}
s.add(2)       # s is still {1, 2}
x = len(s)     # equals 2
y = 2 in s     # equals True
z = 3 in s     # equals False


hundreds_of_other_words = []  # required for the below code to run

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list     # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set      # very fast to check

# Sets are also good for removing dups real quick
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)                # 6
item_set = set(item_list)                 # {1, 2, 3}
num_distinct_items = len(item_set)        # 3
distinct_item_list = list(item_set)       # [1, 2, 3]


assert num_items == 6
assert item_set == {1, 2, 3}
assert num_distinct_items == 3
assert distinct_item_list == [1, 2, 3]

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

# This is the "ternary" version in one line
parity = "even" if x % 2 == 0 else "odd"

x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

# range(10) is the numbers 0, 1, ..., 9
for x in range(10):
    print(f"{x} is less than 10")

for x in range(10):
    if x == 3:
        continue  # go immediately to the next iteration
    if x == 5:
        break     # quit the loop entirely (return in a function will also do this)
    print(x)

one_is_less_than_two = 1 < 2          # equals True
true_equals_false = True == False     # equals False
assert one_is_less_than_two
assert not true_equals_false

# Truthiness
# no Null, python uses None
x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"

# Falsy values
False
None
[]
{}
""
set()
0
0.0
# All others are truthy


def some_function_that_returns_a_string():
    return ""

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

# This is and short circuiting
first_char = s and s[0]

# This is or short circuiting
safe_x = x or 0

safe_x = x if x is not None else 0

all([True, 1, {3}])   # True, all are truthy
all([True, 1, {}])    # False, {} is falsy
any([True, 1, {}])    # True, True is truthy
all([])               # True, no falsy elements in the list
any([])               # False, no truthy elements in the list

x = [4, 1, 2, 3]
y = sorted(x)     # y is [1, 2, 3, 4], x is unchanged
x.sort()          # now x is [1, 2, 3, 4]
# sorted is pure and returns a copy, sort() is mutational and returns None

# sort the list by absolute value from largest to smallest
# reverse takes a boolean, and key takes a callback that passes in the values in the list, and then sorts the results (not -1, 0, 1 like JS, just the actual values)
# abs is a callback
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # is [-4, 3, -2, 1]

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(),
            key=lambda word_and_count: word_and_count[1],
            reverse=True)


# List comprehensions [expression for value in list if (condition)]
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares      = [x * x for x in range(5)]            # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]


assert even_numbers == [0, 2, 4]
assert squares == [0, 1, 4, 9, 16]
assert even_squares == [0, 4, 16]

zeros = [0 for _ in even_numbers]      # has the same length as even_numbers
assert zeros == [0, 0, 0]

# You can also use list comprehensions to create dicts and sets
square_dict = {x: x * x for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
square_set  = {x * x for x in [1, -1]}      # {1}
assert square_dict == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
assert square_set == {1}


# You can stack comprehensions. They don't link to each other like ternarys, think of them like nested for loops, and the first value can pull from any of the nested iterations
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0) (0,1) ... (9,8), (9,9)


assert len(pairs) == 100

# later comprehensions can pull from higher ones, just like nested for loops
increasing_pairs = [(x, y)                       # only pairs with x < y,
                    for x in range(10)           # range(lo, hi) equals
                    for y in range(x + 1, 10)]   # [lo, lo + 1, ..., hi - 1]


assert len(increasing_pairs) == 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
assert all(x < y for x, y in increasing_pairs)

assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't" # this shows the message on errors

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

def smallest_item2(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

# Object Oriented
class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    # dunder (double underscore) methods are sometimes magic, like __init__ is the constuctor
    # and __repr__ which is the string version of the class
    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times = 1):
        """Click the clicker some number of times."""
        self.count += num_times

    def read(self):
        return self.count
    def _fake_private(self):
        print('This is a convention for private methods, it does nothing though')

    def reset(self):
        self.count = 0

clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

# A subclass inherits all the behavior of its parent class.
class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker

    # Except that it has a reset method that does nothing.
    def reset(self):
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

# iterators and generators
# generators 'lazily' generate their values on demand instead of saving them all the time in storage
def generate_range(n):
    i = 0
    while i < n:
        yield i   # every call to yield produces a value of the generator
        i += 1

for i in generate_range(10):
    print(f"i: {i}")

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

# None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on


assert next(even_squares_ending_in_six) == 16
assert next(even_squares_ending_in_six) == 36
assert next(even_squares_ending_in_six) == 196

# Sometimes you also want indices while looping on a range, use enumerate to do so
names = ["Alice", "Bob", "Charlie", "Debbie"]

# not Pythonic
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

# also not Pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

# Pythonic
for i, name in enumerate(names):
    print(f"name {i} is {name}")

# destructure with a for loop
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room, area in house:
    print(room, area)

import random
random.seed(10)  # this ensures we get the same results every time

four_uniform_randoms = [random.random() for _ in range(4)]

# [0.5714025946899135,       # random.random() produces numbers
#  0.4288890546751146,       # uniformly between 0 and 1
#  0.5780913011344704,       # it's the random function we'll use
#  0.20609823213950174]      # most often

random.seed(10)         # set the seed to 10
print(random.random())  # 0.57140259469
random.seed(10)         # reset the seed to 10
print(random.random())  # 0.57140259469 again

random.randrange(10)    # choose randomly from range(10) = [0, 1, ..., 9]
random.randrange(3, 6)  # choose randomly from range(3, 6) = [3, 4, 5]

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
# [7, 2, 6, 8, 9, 4, 10, 1, 3, 5]   (your results will probably be different)

my_best_friend = random.choice(["Alice", "Bob", "Charlie"])     # "Bob" for me

# Use sample for a sample set with NO repeats
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)  # [16, 36, 10, 6, 25, 9]

# Use a comprehension with .choice if you want a randome sample WITH repeats (for some reason repeats are called replacements?)
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)  # [9, 4, 4, 2]

# Regular Expressions
import re

re_examples = [                        # all of these are true, because
    not re.match("a", "cat"),              #  'cat' doesn't start with 'a'
    re.search("a", "cat"),                 #  'cat' has an 'a' in it
    not re.search("c", "dog"),             #  'dog' doesn't have a 'c' in it
    3 == len(re.split("[ab]", "carbs")),   #  split on a or b to ['c','r','s']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") #  replace digits with dashes
    ]

assert all(re_examples), "all the regex examples should be True"

# zip is for combining two lists into tuples
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)]    # is [('a', 1), ('b', 2), ('c', 3)]
assert [pair for pair in zip(list1, list2)] == [('a', 1), ('b', 2), ('c', 3)]

# You can unzip things by using the * which does 'argument unpacking'
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

def add(a, b): return a + b

# Argument unpacking works on any function
add(1, 2)      # returns 3
# try:
#     add([1, 2])
# except TypeError:
#     print("add expects two inputs")
# add(*[1, 2])   # returns 3


# args and kwargs
def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)

    # And return that new function.
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8,  "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

def f2(x, y):
    return x + y

g = doubler(f2)
# try:
#     g(1, 2)
# except TypeError:
#     print("as defined, g only takes one argument")

# In order to deal with an unknown number of arguments, you can use *args, which
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")
# prints
#  unnamed args: (1, 2)
#  keyword args: {'key': 'word', 'key2': 'word2'}

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler should work now"






# Type annotations
def add_things(a, b):
    return a + b

assert add_things(10, 5) == 15,                  "+ is valid for numbers"
assert add_things([1, 2], [3]) == [1, 2, 3],     "+ is valid for lists"
assert add_things("hi ", "there") == "hi there", "+ is valid for strings"

try:
    add_things(10, "five")
except TypeError:
    print("cannot add_things an int to a string")

def add_things2(a: int, b: int) -> int:
    return a + b

add_things2(10, 5)           # you'd like this to be OK
add_things2("hi ", "there")  # you'd like this to be not OK


# This is not in the book, but it's needed
# to make the `dot_product` stubs not error out.
from typing import List
Vector = List[float]

def dot_product(x, y): ...

# we have not yet defined Vector, but imagine we had
# def dot_product(x: Vector, y: Vector) -> float: ...

# The typing module is what we need to add types to our code with more complex things
from typing import Union

def secretly_ugly_function(value, operation): ...

def ugly_function(value: int, operation: Union[str, int, float, bool]) -> int:
    ...

def total(xs: list) -> float:
    return sum(xs)

from typing import List  # note capital L

# def total(xs: List[float]) -> float:
#     return sum(xs)

# This is how to type-annotate variables when you define them.
# But this is unnecessary; it's "obvious" x is an int.
x: int = 5

values = []         # what's my type?
best_so_far = None  # what's my type?

from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None  # allowed to be either a float or None


lazy = True

# the type annotations in this snippet are all unnecessary
from typing import Dict, Iterable, Tuple

# keys are strings, values are ints
counts: Dict[str, int] = {'data': 1, 'science': 2}

# lists and generators are both iterable
if lazy:
    evens: Iterable[int] = (x for x in range(10) if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]

# tuples specify a type for each element
triple: Tuple[int, float, int] = (10, 2.3, 5)

# Callable is what we use when passing in first class functions
from typing import Callable

# The type hint says that repeater is a function that takes
# two arguments, a string and an int, and returns a string.
def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

Number = int
Numbers = List[Number]

# def total(xs: Numbers) -> Number:
#     return sum(xs)

# mypy is a tool you can use to run over your code types

# Operators
# 4 // 5  that's floor div, it rounds down

# Getting input
username = input("Enter username:")
print("Username is: " + username)

# Casting
# integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'