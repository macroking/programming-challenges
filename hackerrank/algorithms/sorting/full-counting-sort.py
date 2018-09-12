from  __future__ import print_function
import os
import sys


def countSort(arr):
    arr_len = len(arr)
    op = [0] * arr_len
    final_op = ["-"] * arr_len
    # print(final_op)
    for _ in range(arr_len):
        op[int(arr[_][0])] += 1
    for _ in range(1, arr_len):
        op[_] += op[_-1]

    for _ in range(arr_len-1, -1, -1):
        ind = op[int(arr[_][0])]
        if ind > arr_len:
            continue
        if (_ > ((arr_len+1)/2)-1):
            final_op[ind-1] = arr[_][1]
        op[int(arr[_][0])] = ind-1
    print(' '.join(final_op))

if __name__ == '__main__':
    f = open('./input.txt')
    n = int(f.readline().strip())
    arr = []
    for _ in range(n):
        arr.append(f.readline().rstrip().split())
    countSort(arr)
