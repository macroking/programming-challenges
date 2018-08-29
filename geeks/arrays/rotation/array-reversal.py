from  __future__ import print_function
import os
import sys
from copy import copy
from array import array

def reverse_array(arr, start, end):
    '''
    Time Complexity : O(n)
    '''
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def leftrotate(arr, d):
    n = len(arr)
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)
    reverse_array(arr, 0, n-1)

if __name__ == '__main__':
    '''
        Rotation of the above array by 2 will make array
    '''
    arr = array('i', [1, 2, 3, 4, 5, 6, 7])
    leftrotate(arr, 2)
    print(arr)
