from __future__ import print_function
import os
import sys

def viralAdvertising(n):
    out = 0
    start = 5
    for _ in range(n):
        op = (start/2)
        start = op * 3
        out += op
    return out

if __name__ == '__main__':
    f = open('./input.txt')
    days = int(f.readline().strip())
    out = viralAdvertising(days)
    print(out)
