from __future__ import print_function
import os
import sys

def countSort(arr):
    count_ = [0 for _ in range(256)]
    ans = ["" for _ in arr]

    for _ in arr:
        count_[ord(_)] += 1
    for i in range(256):
        count_[i] += count_[i-1]

    for i in range(len(arr)-1, -1, -1):
        ans[count_[ord(arr[i])]-1] = arr[i]
        count_[ord(arr[i])] -= 1

    return ans

if __name__ == '__main__':
    arr = "geeksforgeeks"
    ans = countSort(arr)
    print("Sorted character array is %s"  %("".join(ans)))
