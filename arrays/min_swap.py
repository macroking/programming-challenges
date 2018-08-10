from __future__ import print_function
import os
import sys
import copy
def minswap(arr, n, k):
    count = 0
    for i in range(0, n) :
        if (arr[i] <= k) :
            count = count + 1
    bad = 0
    for i in range(0, count) :
        if (arr[i] > k) :
            bad = bad + 1

    ans = bad
    j = count
    for i in range(0, n) :
        if(j == n) :
            break

        if (arr[i] > k) :
            bad = bad - 1

        if (arr[j] > k) :
            bad = bad + 1

        ans = min(ans, bad)

        j = j + 1

    return ans

if __name__ == '__main__':
    arr = [10, 2, 7, 9, 5, 8, 7, 4]
    k = 5
    op = minswap(arr, len(arr), k)
    print(op)
