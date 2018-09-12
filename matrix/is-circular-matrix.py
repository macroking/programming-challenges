from __future__ import print_function
import os
import sys
import math

def iscircular(mat):
    stat = True
    row_cnt = len(mat)
    col_cnt = len(mat[0])
    for ii in range(1, row_cnt):
        start = -1
        for jj in range(0, col_cnt):
            if mat[ii][jj] != mat[ii-1][start]:
                stat = False
                break
            start += 1
        if not stat:
            break
        print()
    return stat

if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [4, 1, 2, 3],
           [3, 4, 1, 2],
           [2, 3, 4, 1]]
    N = len(mat)
    print(iscircular(mat))