from  __future__ import print_function
import os
import sys
from linkedlistbase import print_singly_linked_list, SinglyLinkedList, SinglyLinkedListNode

def removeDuplicates(head):
    cur = head
    while cur:
        next_node = cur.next
        if next_node and cur.data == next_node.data:
            new_next = next_node.next
            cur.next = new_next
        else:
            cur = cur.next
    return head

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    t = int(f.readline().strip())

    for t_itr in range(t):
        llist_count = int(f.readline().strip())
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(f.readline().strip())
            llist.insert_node(llist_item)
    result = removeDuplicates(llist.head)
    print_singly_linked_list(result)

