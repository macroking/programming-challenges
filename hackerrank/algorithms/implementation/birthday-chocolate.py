from __future__ import print_function
import os
import sys

def birthday(s, d, m):
    cnt = 0
    for _ in range(len(s)):
        tmp = (s[_: m + _])
        if len(tmp) == m and sum(tmp) == d:
            cnt += 1
    return cnt

if __name__ == '__main__':
    f = open('./hackerrank/input.txt')
    n = int(f.readline().strip())
    s = list(map(int, f.readline().rstrip().split()))
    dm = f.readline().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(str(result))