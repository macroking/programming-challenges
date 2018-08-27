from __future__ import print_function
import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __str__(self):
        return str(self.data)

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
        print(str(node.data))
        node = node.next

def insertNodeAtPosition(head, data, position):
    node = head
    count = 1
    while count < position and node:
        count += 1
        node = node.next
    newNode = SinglyLinkedListNode(data)
    newNode.next = node.next
    node.next = newNode
    return head

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    llist_count = int(f.readline())
    llist = SinglyLinkedList()

    for _ in xrange(llist_count):
        llist_item = int(f.readline())
        llist.insert_node(llist_item)

    data = int(f.readline())
    position = int(f.readline())
    llist_head = insertNodeAtPosition(llist.head, data, position)
    print_singly_linked_list(llist.head)