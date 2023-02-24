import os
import numpy as np
from pathlib import Path

# not sure this path is right, but it works
abc_file = Path(os.getcwd()) / 'input-output-practice' / 'abc.txt'

# by default loadtxt uses whitespace as a delimiter with spaces and tabs
a = np.loadtxt(abc_file)
print(a)

# assumming i could make a tab deliniated file, i could load it like this
# tab_file = Path(os.getcwd()) / 'input-output-practice' / 'abc_tab.txt'
# b = np.loadtxt(tab_file)
# print(b)

# for csv files, you must specify the delimiter
abc_csv = Path(os.getcwd()) / 'input-output-practice' / 'abc.csv'
c = np.loadtxt(abc_csv, delimiter=',')
print(c)


# you can also save np arrays directly to files
abc_npy = Path(os.getcwd()) / 'input-output-practice' / 'abc.npy'
d = np.save(abc_npy, a)
d = np.load(abc_npy)
print(d)

# You can also save and load text and csv files
new_abc_txt = Path(os.getcwd()) / 'input-output-practice' / 'my-abc.txt'
new_abc_csv = Path(os.getcwd()) / 'input-output-practice' / 'my-abc.csv'
np.savetxt(new_abc_txt, a)
np.savetxt(new_abc_csv, a, delimiter=',', fmt='%d')
# be careful with the filename, it seems SORT OF case sensitive, where it will overwrite if the only dif is capitals
# but will respect case if there are changes. Just be careful

# note that you need to fmt things as ints %d if you want to save them as ints, otherwise they will be floats


# ------------------------------------------------------------------------------
# MULTIPLE ARRAYS PER FILE

# notice how now we use .npz instead of .npy
multi_file = Path(os.getcwd()) / 'input-output-practice' / 'multi.npz'

# .savez to save now but still just .load to load
np.savez(multi_file, a=a, c=c)
# the named arguments give us a dictionary like file
q = np.load(multi_file)
print(list(q.keys()))
arrs = np.array([q['a'], q['c']])
print(arrs)

# we can just save the arrays as a list

