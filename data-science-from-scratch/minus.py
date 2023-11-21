from random import shuffle

first_nums = range(10,20)
second_nums = range(1,10)
pairs = []

for i, x in enumerate(first_nums):
    for y in second_nums[i:]:
        pairs.append((x,y))

shuffle(pairs)

for x,y in pairs:
    guess = input(f'{x} - {y} = ')
    print('Correct!' if int(guess) == x - y else f"NO it's {x - y}")
