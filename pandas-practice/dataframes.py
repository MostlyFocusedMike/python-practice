import pandas as pd
import numpy as np

cars = pd.read_csv('./cars-with-index.csv', index_col=0)
cars_no_idx = pd.read_csv('./cars-no-index.csv')

# print(cars_no_idx)
"""
   cars_per_cap                   country        drives_right
0           809             United States                True
1           731                 Australia               False
2           588                     Japan               False
3            18                     India               False
4           200                    Russia                True
5            70                   Morocco                True
6            45                     Egypt                True
"""

# print(cars)
"""
     cars_per_cap       country  drives_right
US            809  UnitedStates          True
AUS           731     Australia         False
JPN           588         Japan         False
IN             18         India         False
RU            200        Russia          True
MOR            70       Morocco          True
EG             45         Egypt          True
"""
cry = 'country'
dr = 'drives_right'
cap = 'cars_per_cap'

# print(f'\nFrame Subset:\n{cars[[cap, cry]]}')
# print(f'\nFrame Subset:\n{cars[0:4]}')
# print(f"data by label:\n{cars[cap]['US']}")
# print(f"Series:\n{cars[cap]}")
# print(f"Individual data point::\n{cars[cap]['US']}")


subset = cars.loc[['US', 'IN', 'EG']]
# print(f'\nFrame Subset:\n{subset}')
# print(cars[cap].shape)
# print(type(cars[cap]))
# print(f'\nSeries:\n{cars[1:2]}')
# print(type(cars[1:2]))


# print(cars.loc['US'])
# print(f"\n-----Using just the named index---\n{cars.loc[['US'], ['country']]}")
# print(f"\n-----Using just the named index---\n{cars.loc['US']}")
# print(f"-Using just the named index-\n{cars.loc[['US', 'IN']]}")
# print(f"-Using just the named index-\n{cars.loc[['US'], ['country']]}")
val = cars.iloc[:, [0]]
print(val)
print(type(val))
# print(cars.iloc[[0,1,2], [0,1]])

# print(f"\n-----Using just the named index---\n{cars}")

# simply filtering
all_drive_right = cars["drives_right"] # this is already a boolean series so this works
print(cars[all_drive_right])

# use comparison
big_cars_cap = cars['cars_per_cap'] > 200
print('\nbig cars cap')
print(cars[big_cars_cap])

# use comparison without ambiguity
extremes_cars_cap = np.logical_or(cars['cars_per_cap'] < 100, cars['cars_per_cap'] > 600)
print('\nextremes cars cap')
print(cars[extremes_cars_cap])

# Iterate through column names
for column in cars:
  print('\n------------------------')
  print(f"Column Name:\n{column}")

# Iterate through rows
for label, row in cars.iterrows():
  print('\n------------------------')
  print("label:", label)
  print(f"Row:\n{row}\n")
  print(f"Row as np array:\n{np.array(row)}")
  print(f"Type of Row: {type(row)}")

# Each row is a
for label, row in cars.iterrows():
  print('\n------------------------')
  print("label:", label)
  print(f"Row: {row['country']}")
  print(f"Row: {row['cars_per_cap']}")

for label, row in cars.iterrows() :
  cars.loc[label, "name_length"] = len(row["country"])



cars["name_length"] = cars["country"].apply(lambda x: x.upper())

