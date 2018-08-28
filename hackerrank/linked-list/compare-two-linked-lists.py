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

def compare_lists(llist1, llist2):
    status = 1
    if not (llist1 and llist2):
        return 0
    list1_cur = llist1
    list2_cur = llist2

    while(list1_cur and list2_cur):
        if (list1_cur.data != list2_cur.data):
            status = 0
            break
        list1_cur = list1_cur.next
        list2_cur = list2_cur.next

    if (list1_cur or list2_cur):
        status = 0
    return status

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    tests = int(f.readline().strip())
    for tests_itr in range(tests):
        llist1_count = int(f.readline().strip())
        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(f.readline().strip())
            llist1.insert_node(llist1_item)

        llist2_count = int(f.readline().strip())
        llist2 = SinglyLinkedList()
        for _ in range(llist2_count):
            llist2_item = int(f.readline().strip())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)
        print(result)