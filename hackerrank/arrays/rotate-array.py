'''
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left.
'''
from __future__ import print_function
import os
import sys

# Approach 1 - built in
def rotate_left_1(arr, end, start):
    return arr[end:] + arr[: end]

# Approach 2  - data structure
def rotate_left_2(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    n = 5
    d = 4
    arr = [1, 2, 3, 4, 5]
    exout = rotate_left_1(arr, d, n)
    print(exout)

    arr = [1, 2, 3, 4, 5]
    rotate_left_2(arr, 0, d-1)
    rotate_left_2(arr, d, n-1)
    rotate_left_2(arr, 0, n-1)
    print(exout)