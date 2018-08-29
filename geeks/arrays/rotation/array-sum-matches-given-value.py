from  __future__ import print_function
import os
import sys
from array import array

def sumofitems(arr, low, high, key):
    n = len(arr)
    cnt = 0
    while low != high:
        if ( arr[low] + arr[high] == key ):
            cnt += 1

            if ( low == (n + high - 1) % n):
                return cnt
            high = ( n + high - 1) % n
            low = (low + 1) % n

        elif ( arr[low] + arr[high] > key):
            high = ( n + high - 1) % n
        else:
            low = (low + 1) % n
    return cnt

def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)

def binarySearch(arr, low, high, key):
    if high < low:
        return -1
    mid = int((high + low)/2)
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)
    return binarySearch(arr, low, (mid - 1), key)

if __name__ == '__main__':
    arr = array('i', [11, 15, 26, 38, 8, 9, 10])
    n = len(arr)
    tot = 19
    high = findPivot(arr, 0, n - 1)
    low = (high + 1) % n
    op = sumofitems(arr, low, high , tot)
    print(arr, low, high)
    print(op)