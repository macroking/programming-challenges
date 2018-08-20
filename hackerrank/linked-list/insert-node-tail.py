from  __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def print_singly_linked_list(self):
        cur = self.head
        while(cur.next):
            print(cur.data)
            cur = cur.next

    def insert_node_at_tail(self, head, data):
        while(head.next):
            head = head.next
        n = Node(data)
        head.next = n
        self.head = n

if __name__ == '__main__':
    pass
