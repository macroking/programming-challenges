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


def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next


def insertNodeAtTail(head, data):
    node = head
    if not node:
        newNode = SinglyLinkedListNode(data)
        newNode.next = node
        return newNode
    else:
        while node.next:
            node = node.next
        newNode = SinglyLinkedListNode(data)
        node.next = newNode
    return head


if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    llist_count = int(f.readline())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(f.readline())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head
    print_singly_linked_list(llist.head)
