from __future__ import print_function
import os
import sys
from fractions import gcd
from functools import reduce

def getTotalX(a, b):
    a1 = reduce(gcd, a)
    b1 = reduce(gcd, b)
    print(a1, b1)
    return a1


if __name__ == '__main__':
    f = open('./input.txt')
    nm = f.readline().strip().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, f.readline().strip().split()))
    b = list(map(int, f.readline().strip().split()))
    total = getTotalX(a, b)
    print(total)