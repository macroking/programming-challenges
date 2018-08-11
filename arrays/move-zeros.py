from  __future__ import print_function
import os
import sys


def movezeros(arr, cnt):
    _cnt = 0
    for _ in range(cnt):
        if arr[_] != 0:
            arr[_cnt] = arr[_]
            _cnt += 1
    for _ in range(_cnt, cnt, 1):
        arr[_] = 0
    return arr

if __name__ == '__main__':
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    op = movezeros(arr, len(arr))
    print(op)
