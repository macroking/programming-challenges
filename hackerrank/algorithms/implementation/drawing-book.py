from  __future__ import print_function
import os
import sys
import math

def pageCount(n, p):
    return min(p/2,n/2-p/2)

if __name__ == '__main__':
    f = open('./input.txt')
    n = int(f.readline().strip())
    p = int(f.readline().strip())
    result = pageCount(n, p)
    print(result)
