'''
    FLOYDS LOOP Detection algorithm
'''
from  __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def detect_loop(self):
        cur_s = self.head
        cur_f = self.head

        while(cur_f and cur_s and cur_f.next):
            cur_s = cur_s.next
            cur_f = cur_f.next.next
            if cur_s == cur_f:
                print('Detected loop')
                return

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(20)
    llist.insert(4)
    llist.insert(15)
    llist.insert(10)

    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    llist.detect_loop()
