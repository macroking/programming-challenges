from  __future__ import print_function
import os
import sys
import math

def countingValleys(n, s):
    up = 0
    down = 0
    for _ in s:
        up += 1 if _ == "U" else 0
        down += 1 if _ == "D" else 0
    print(up, down)
    return 0

if __name__ == '__main__':
    f = open('./input.txt')
    n = int(f.readline().strip())
    p = f.readline().strip()
    result = countingValleys(n, p)
    print(result)
