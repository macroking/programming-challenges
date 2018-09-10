from __future__ import print_function
import os
import sys


def flatlandSpaceStations(n, c):
    op = [0] * n
    c = sorted(c)
    i = 0
    left = None
    right = c[i]
    for _ in range(n):
        if left == None:
            tmp = abs(_ - right)
            op[_] = tmp
        elif left != None and right != None:
            tmp = min(abs(_ - left), abs(_ - right))
            op[_] = tmp
        elif right == None:
            tmp = abs(_ - left)
            op[_] = tmp
        # print(_, i, "left:", left , "right:", right, "op:", tmp)
        if _ == left or _ == right:
            i += 1
            tmp = c[i] if i < len(c) else None
            left, right = right, tmp
    return max(op)


if __name__ == '__main__':
    f = open('./input.txt')
    nm = f.readline().strip().split()
    n = int(nm[0])
    m = int(nm[1])
    c = map(int, f.readline().strip().rstrip().split())
    result = flatlandSpaceStations(n, list(c))
    print(result)
