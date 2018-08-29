from __future__ import print_function
import os
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

def print_doubly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next

class SinglyLinkedListNode(object):
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList(object):
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
