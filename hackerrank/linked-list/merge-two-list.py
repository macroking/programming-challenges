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

def mergeLists_recursion(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if(head1.data < head2.data):
        head1.next = mergeLists_recursion(head1.next, head2)
        return head1
    else:
        head2.next = mergeLists_recursion(head1, head2.next)
        return head2

def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    cur_head1 = head1
    cur_head2 = head2

    llist3 = SinglyLinkedList()
    while cur_head1 and cur_head2:
        if cur_head1.data < cur_head2.data:
           llist3.insert_node(cur_head1.data)
           cur_head1 = cur_head1.next
        else:
            llist3.insert_node(cur_head2.data)
            cur_head2 = cur_head2.next
    if cur_head1:
        cur = cur_head1
        while cur:
            llist3.insert_node(cur.data)
            cur = cur.next
    if cur_head2:
        cur = cur_head2
        while cur:
            llist3.insert_node(cur.data)
            cur = cur.next
    return llist3.head


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

        # llist3 = mergeLists(llist1.head, llist2.head)
        llist3 = mergeLists_recursion(llist1.head, llist2.head)
        print_singly_linked_list(llist3)