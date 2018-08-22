from __future__ import print_function
import os
import sys

def running_total(arr):
    for _ in xrange(1, len(arr)):
        arr[_] = arr[_] + arr[_-1]
    return arr

def twoStacks(x, a, b):
    while(a and b):
        print(a.pop(0))
        print(b.pop(0))
    return 0

if __name__ == '__main__':
    f = open('./hackerrank/input.txt')
    g = int(f.readline())

    for g_itr in range(g):
        nmx = f.readline().split()
        n = int(nmx[0])
        m = int(nmx[1])
        x = int(nmx[2])
        a = list(map(int, f.readline().rstrip().split()))
        b = list(map(int, f.readline().rstrip().split()))
        result = twoStacks(x, a, b)
        print(result)

    f.close()
