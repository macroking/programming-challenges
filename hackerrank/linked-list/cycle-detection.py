from  __future__ import print_function
import os
import sys
from linkedlistbase import SinglyLinkedList, SinglyLinkedListNode, print_singly_linked_list

def has_cycle(head):
    c_stat = False

    return c_stat

if __name__ == '__main__':
    f = open('./hackerrank/linked-list/input.txt')
    tests = int(f.readline().strip())

    for tests_itr in range(tests):
        index = int(f.readline().strip())
        llist_count = int(f.readline().strip())
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(f.readline().strip())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head

        for i in range(llist_count):
            if i == index:
              	extra = temp

            if i != llist_count-1:
              	temp = temp.next

        temp.next = extra
        result = has_cycle(llist.head)
        print(str(int(result)))
