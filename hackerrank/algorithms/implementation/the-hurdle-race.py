from __future__ import print_function
import os
import sys

def hurdleRace(k, height):
    result = 0
    _max = max(height)
    diff = k - _max
    result = abs(diff) if diff < 0 else 0
    return result

if __name__ == '__main__':
    f = open('./input.txt')
    nk = f.readline().strip().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, f.readline().strip().rstrip().split()))
    result = hurdleRace(k, height)
    print(result)