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
            print(cur.data, end=" ")
            cur = cur.next

    def search_node_r(self, node, data):
        if not node:
            return None
        if node.data == data:
            return True
        else:
            return self.search_node_r(node.next, data)

    def search_node(self, data):
        cur = self.head
        while(cur):
            if(cur.data == data):
                return True
            cur = cur.next
        return False

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
    print('Is Node 3 present', llist.search_node(3))
    print('Is Node 31 present', llist.search_node(31))
    print()
    print('Is Node 3 present', llist.search_node_r(llist.head, 3))
    print('Is Node 31 present', llist.search_node_r(llist.head, 31))
