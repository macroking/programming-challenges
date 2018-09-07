from  __future__ import print_function
import os
import sys

def balancedSums(arr):
    status = 'NO'
    total = sum(arr)
    start = 0
    for _ in range(0, len(arr)):
        cur = arr[_]
        new_total = total - (start + cur)
        if new_total == start:
            status = 'YES'
            break
        start += cur
    return status

if __name__ == '__main__':
    f = open('./input.txt')
    T = int(f.readline().strip())
    for T_itr in range(T):
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().rstrip().split()))
        result = balancedSums(arr)
        print(result)
