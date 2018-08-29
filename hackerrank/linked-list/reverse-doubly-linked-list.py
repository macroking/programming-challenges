from  __future__ import print_function
import os
import sys
from linkedlistbase import DoublyLinkedList, DoublyLinkedListNode, print_doubly_linked_list


def reverse(head):
    pre = None
    cur = head
    next = None
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

if __name__ == '__main__':
    f = open('./hackerrank/input.txt')
    t = int(f.readline().strip())

    for t_itr in range(t):
        llist_count = int(f.readline().strip())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(f.readline().strip())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)
        print_doubly_linked_list(llist1)