'''
Can be optimized using
    1. While loop
    2. Set
'''
from __future__ import print_function
import os
import sys

def rearrange(arr, cnt):
    op =[-1]*cnt
    for _ in range(cnt):
        if arr[_] != -1:
            op[arr[_]] = arr[_]
    return op

if __name__ == '__main__':
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    cnt = len(arr)
    op = rearrange(arr, cnt)
    print()
    print(op)