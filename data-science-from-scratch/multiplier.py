import random
from os import system

pairs = []
wrong_answers = []
nums = [3,4,5,6,7,8,9,11,12]
score = 0
question = 1
correct = 'first'

for i, x in enumerate(nums):
    for y in nums[i:]:
        pairs.append((x,y))
random.shuffle(pairs)

for x, y in pairs:
    system('clear')
    if correct != 'first': print("Correct" if correct else "NO!")
    guess = input(f'{question}: {x} * {y} = ')
    if int(guess) == 0: break

    correct = int(guess) == x * y
    if correct:
        score += 1
        question += 1
    else:
        wrong_answers.append(f'{x} * {y} is {x * y}, not {guess}')

print(f'{score}/{len(pairs)}')
for ans in wrong_answers:
    print(ans)