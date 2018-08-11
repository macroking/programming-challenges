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

    def print_node(self):
        cur = self.head
        while(cur):
            print (cur.data, end=" ")
            cur = cur.next

    def count(self):
        cnt = 0
        cur = self.head
        while(cur):
            cnt += 1
            cur = cur.next
        return cnt

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert(1)
    llist.insert(3)
    llist.insert(1)
    llist.insert(2)
    llist.insert(1)
    print('Linked list: ')
    llist.print_node()
    print()
    print('Length of the list :', llist.count())
