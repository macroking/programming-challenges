from __future__ import print_function
import os
import sys


def save_the_prisoner(n, m, s):
    # m - number of sweets
    # n - number of prisoner
    # s - start chair
    return n if ((m+s-1) % n == 0) else (m+s-1) % n


if __name__ == '__main__':
    f = open('input.txt')
    t = int(f.readline().strip())
    for t_itr in range(t):
        nms = f.readline().strip().split()
        n = int(nms[0])
        m = int(nms[1])
        s = int(nms[2])
        result = save_the_prisoner(n, m, s)
        print(result)
