from __future__ import print_function
import os
import sys

def fairRations(B):
    return 0

if __name__ == '__main__':
    f = open('./input.txt')
    N = int(f.readline().strip())
    B = map(int, f.readline().rstrip().split())
    result = fairRations(B)
    print(result)

