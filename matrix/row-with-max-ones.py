from __future__ import print_function
import os
import sys


def rowWithMax1s(mat):
    r_cnt = len(mat)
    for _ in range(r_cnt):
        print(_, mat[_].count(1))

# Driver Code
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
      rowWithMax1s(mat))