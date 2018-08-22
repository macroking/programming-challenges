from  __future__ import print_function
import os
import sys

class SinglyLinkedListNode(object):
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

def insertNodeAtHead(llist, data):
    llist_head = SinglyLinkedListNode(data)
    llist_head.next = llist
    return llist_head

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    llist_count = int(f.readline())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(f.readline())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
