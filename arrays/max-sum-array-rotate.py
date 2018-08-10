'''
source: https://www.geeksforgeeks.org/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/
'''
from __future__ import print_function
import os
import sys
import operator

def max_sum(arr):
    arrSum = 0
    currVal = 0

    n = len(arr)

    for i, _ in enumerate(arr):
        arrSum += _
        currVal += (i * _)
    maxVal = currVal

    for _ in range(1, n):
        currVal = currVal + arrSum - n * arr[n-_]
        if currVal > maxVal:
            maxVal = currVal
    return maxVal

if __name__ == '__main__':
    arr =  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [8, 3, 1, 2]
    op = max_sum(arr)
    print(op)
