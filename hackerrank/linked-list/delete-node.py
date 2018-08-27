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
        print(str(node.data))
        node = node.next

def deleteNode(head, position):
    if not head:
        return
    count = 0
    pre = None
    cur = head
    while( cur and count < position):
        count += 1
        pre = cur
        cur = cur.next
    if count != position:
        print("Not enough nodes in the list")
    else:
        if pre is None:
            head = cur.next
        else:
            pre.next = pre.next.next
    return head

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    llist_count = int(f.readline())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(f.readline())
        llist.insert_node(llist_item)

    position = int(f.readline())
    llist1 = deleteNode(llist.head, position)
    print_singly_linked_list(llist1)
