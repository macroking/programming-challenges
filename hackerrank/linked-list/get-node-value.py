from __future__ import print_function
import os
import sys

from linkedlistbase import SinglyLinkedList, SinglyLinkedListNode, print_singly_linked_list

def getNode(head, positionFromTail):
    temp = 0
    if not head:
        return
    getNode(head.next, positionFromTail)
    temp += 1
    if (temp == positionFromTail):
        return head.data

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    tests = int(f.readline().strip())

    for tests_itr in range(tests):
        llist_count = int(f.readline().strip())
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(f.readline().strip())
            llist.insert_node(llist_item)
        position = int(f.readline().strip())
        result = getNode(llist.head, position)
        print(result)

