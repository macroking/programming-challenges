from __future__ import print_function
import os
import sys

def reverse_array(arr, start, end):
    while(start < end ):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def recursive_reverse_array(arr, start, end):
    if(start >= end):
        return
    arr[start], arr[end] = arr[end], arr[start]
    recursive_reverse_array(arr, start+1, end-1)

if __name__ == '__main__':
    arr = [1, 2, 3]
    cnt = len(arr)
    op = reverse_array(arr, 0, cnt-1)
    print(op)
    arr = [1, 2, 3]
    recursive_reverse_array(arr, 0, cnt-1)
    print(arr)
