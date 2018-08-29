from  __future__ import print_function
import os
import sys
from linkedlistbase import DoublyLinkedList, DoublyLinkedListNode, print_doubly_linked_list


def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)
    if not head:
        return newNode
    elif head.data >= data:
        newNode.next = head
        newNode.next.prev = newNode
        return newNode

    cur = head
    while cur.next and cur.next.data < data:
        cur = cur.next

    newNode.next = cur.next
    if cur.next:
        cur.next.prev = newNode

    cur.next = newNode
    newNode.prev = cur

    return head

if __name__ == '__main__':
    f = open('./hackerrank/input.txt')
    t = int(f.readline().strip())

    for t_itr in xrange(t):
        llist_count = int(f.readline().strip())
        llist = DoublyLinkedList()

        for _ in xrange(llist_count):
            llist_item = int(f.readline().strip())
            llist.insert_node(llist_item)

        data = int(f.readline().strip())
        llist1 = sortedInsert(llist.head, data)
        print_doubly_linked_list(llist1)