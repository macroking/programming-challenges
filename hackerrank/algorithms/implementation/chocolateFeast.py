from __future__ import print_function
import os
import sys


def chocolateFeast(n, c, m):
    ans = 0
    temp = divmod(n, c)
    quo = int(temp[0])
    ans += quo
    while quo >= m:
        temp = divmod(quo, m)
        ans += temp[0]
        quo = temp[0] + temp[1]

    return ans


if __name__ == '__main__':
    f = open('./input.txt')
    t = int(f.readline().strip())
    for _ in range(t):
        ncm = f.readline().strip().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])
        result = chocolateFeast(n, c, m)
        print(result)
