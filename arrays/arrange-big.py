from __future__ import print_function
import os
import sys


def compare(x, y):
    a = str(x) + str(y)
    b = str(y) + str(x)
    return cmp(int(b) , int(a))

def arrange(arr):
    return sorted(arr, cmp=compare)


if __name__ == '__main__':
    arr = [54, 546, 548, 60]
    op = arrange(arr)
    print(''.join(map(str, op)))
