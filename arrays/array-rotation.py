from __future__ import print_function
from array  import *

arr = array('i', [1, 2, 3, 4, 5, 6, 7])
d = 2
n = 7

# Approach 1
for _ in range(d):
    arr.append(arr.pop(0))
print(arr)
print
