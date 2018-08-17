from __future__ import print_function
import os
import sys

arr = []
op = -63
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)
for ii in xrange(0, 4):
    for jj in xrange(0, 4):
        op1 = sum(arr[ii][jj:jj+3]) + arr[ii+1][jj+1] + sum(arr[ii+2][jj:jj+3])
        if op1 > op:
            op = op1
print (op)
