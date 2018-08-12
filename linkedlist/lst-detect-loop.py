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

    def count_loop_length(self, node):
        '''
        Find the loop length
        '''
        cnt = 0
        temp = node
        while(temp.next != node):
            cnt += 1
            temp = temp.next
        return cnt

    def detect_loop(self):
        cur_s = self.head
        cur_f = self.head

        while(cur_f and cur_s and cur_f.next):
            cur_s = cur_s.next
            cur_f = cur_f.next.next
            print (cur_s.data, cur_f.data)
            if cur_s == cur_f:
                print('Detected loop')
                return self.count_loop_length(cur_s)

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(20)
    llist.insert(4)
    llist.insert(15)
    llist.insert(10)
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    cnt = llist.detect_loop()
    print('Loop length ', cnt)
