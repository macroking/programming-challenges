from  __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def print_node(self):
        cur = self.head
        while(cur):
            print(cur.data, end=" ")
            cur = cur.next


    def ispalindrome(self):
        cur = self.head
        tmp = []
        while(cur):
            tmp.append(cur.data)
            cur = cur.next
        print(tmp)

        cur = self.head
        while(cur):
            if tmp.pop() != cur.data:
                return "Not Palindrome"
            cur = cur.next
        return "Palindrome"


if __name__ == '__main__':
    lst = LinkedList()
    for _ in "Apple":
        lst.insert(_)
    lst.print_node()
    print()
    istrue = lst.ispalindrome()
    print(istrue)

    lst = LinkedList()
    for _ in "abacaba":
        lst.insert(_)
    lst.print_node()
    print()
    istrue = lst.ispalindrome()
    print(istrue)
