'''
    Time Complexity: O(n)
    Auxiliary Space: O(1)
'''

from __future__ import print_function
import os
import sys


def cyc_rotate(lst, n):
    elm = lst[n - 1]
    for _ in range(n-1, 0, -1):
        lst[_], lst[_-1] = lst[_-1], lst[_]
    lst[0] = elm
    return lst


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n =  len(arr)
    print(cyc_rotate(arr, n))
