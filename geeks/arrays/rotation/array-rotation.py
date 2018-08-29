from  __future__ import print_function
import os
import sys
from copy import copy
from array import array

'''
    Approach 1
'''
def rotate_array(arr, d, n):
    '''
        Time complexity : O(n)
        Auxiliary Space : O(d)
    '''
    temp = array('i')
    for _ in range(d):
        temp.append(arr[_])
    for _ in range(d, n):
        arr[_ - d] = arr[_]
    for _ in range(n-d , n):
        arr[_] = temp[n - _-d]
    return arr

'''
    Approach 2
'''
def left_rotate(arr, d, n):
    '''
        Time complexity : O(n * d)
        Auxiliary Space : O(1)
    '''
    for _ in range(d):
        leftRotatebyOne(arr, n)
    return arr

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp


if __name__ == '__main__':
    '''
        Rotation of the above array by 2 will make array
    '''
    arr = array('i', [1, 2, 3, 4, 5, 6, 7])
    op = rotate_array(copy(arr), 2, 7)
    print(op)
    op = left_rotate(copy(arr), 2, 7)
    print(op)
