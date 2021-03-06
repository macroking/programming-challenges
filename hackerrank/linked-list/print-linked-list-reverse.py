from __future__ import print_function
import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(node.data, end='')
        node = node.next

def reversePrint(head):
    if not head:
        return
    reversePrint(head.next)
    print(head.data)

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    tests = int(f.readline().strip())
    for tests_itr in range(tests):
        llist_count = int(f.readline().strip())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(f.readline().strip())
            llist.insert_node(llist_item)
        reversePrint(llist.head)
        print()