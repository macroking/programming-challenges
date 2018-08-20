from  __future__ import print_function
import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
# This is naive approach does not scale for larger set of queries
def arrayManipulation1(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        for _ in range(a-1, b):
            arr[_] += k
    return max(arr)

def prefix_sum(arr):
    for _ in range(1, len(arr)):
        arr[_] = arr[_] + arr[_-1]
    return arr

# Using prefix sum array
def arrayManipulation2(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        arr[a-1] = arr[a-1] + k
        if b !=n :
            arr[b] = arr[b] - k
    return max(prefix_sum(arr))

if __name__ == '__main__':
    f = open('input.txt')
    nm = f.readline().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in xrange(m):
        queries.append(map(int, f.readline().rstrip().split()))
    result = arrayManipulation2(n, queries)
    print(result)
    # print('naive approach')
    # result = arrayManipulation1(n, queries)
    # print(result)
