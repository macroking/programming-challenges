from __future__ import print_function
from array import array
from copy import copy
import os
import sys

# Reverse array list comprehension
def reverse_array_lst(arr):
    return arr[::-1]

# Reverse array using loop
def reverse_array_loop(arr):
    for _ in range(len(arr)-1, -1 , -1):
        print(arr[_], end = " ")

if __name__ == '__main__':
    arr = array('i', [1, 2, 3, 4, 5])
    print('Initial array')
    print(arr)

    print('Reversed array list comprehension')
    op = reverse_array_lst(copy(arr))
    print(op)

    print('Reversed array loop')
    reverse_array_loop(arr)