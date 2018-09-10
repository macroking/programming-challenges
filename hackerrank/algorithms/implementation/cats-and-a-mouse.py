from __future__ import print_function
import os
import sys

def catAndMouse(x, y, z):
    if abs(x-z) < abs(y-z):
        res = 'Cat A'
    elif abs(x-z) > abs(y-z):
        res = 'Cat B'
    else:
        res = 'Mouse C'
    return res

if __name__ == '__main__':
    f = open('./input.txt')
    q = int(f.readline().strip())
    for q_itr in range(q):
        xyz = f.readline().strip().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)