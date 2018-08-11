from  __future__ import print_function
import os
import sys
import math

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

    def get_node_at(self, index):
        cnt = 0
        cur = self.head
        while(cur):
            cnt += 1
            if cnt == index+1:
                return cur.data
            cur = cur.next
        return cnt

    def get_node_at_r(self, node, index):
        cnt = 0
        if not node:
            return None
        if cnt == index:
            return node.data
        else:
            return self.get_node_at_r(node.next, index - 1)

    def search_node(self, data):
        cur = self.head
        while(cur):
            if(cur.data == data):
                return True
            cur = cur.next
        return False

    def search_node_r(self, node, data):
        if not node:
            return None
        if node.data == data:
            return True
        else:
            return self.search_node_r(node.next, data)

    def count(self):
        cnt = 0
        cur = self.head
        while(cur):
            cnt += 1
            cur = cur.next
        return cnt

if __name__ == '__main__':
    llist = LinkedList()
    for _ in range(5, 0, -1):
        llist.insert(_)
    print('Linked list: ')
    llist.print_node()
    print()
    cnt = llist.count()/2
    print('Middle element ', llist.get_node_at(cnt))

