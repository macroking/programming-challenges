from __future__ import print_function
import os
import sys


def countRotations(arr, low, high):
    if (high < low):
        return 0

    if (high == low):
        return low

    mid = low + (high - low)/2
    mid = int(mid)

    if (mid < high and arr[mid+1] < arr[mid]):
        return (mid+1)

    if (mid > low and arr[mid] < arr[mid - 1]):
        return mid

    if (arr[high] > arr[mid]):
        return countRotations(arr, low, mid-1)

    return countRotations(arr, mid+1, high)


if __name__ == '__main__':
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    print(countRotations(arr, 0, n-1))
