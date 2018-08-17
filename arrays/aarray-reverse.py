from __future__ import print_function
from array  import *
arr = array('i', [1, 2, 3, 4, 5])
# Aproach 1
d = 4
def rotate_array(lst, start, end):
    while(start < end ):
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

rotate_array(arr, 0, d-1)
rotate_array(arr, d, len(arr) - 1)
rotate_array(arr, 0, len(arr) -1 )
print(arr)
