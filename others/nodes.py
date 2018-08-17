'''
Creating pointers/nodes
'''
from __future__ import print_function
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def appendfirst(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def appendlast(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next = n

    def insertafter(self, val, data):
        printval = self.head
        while(printval):
            if printval.data == val:
                n = Node(data)
                next_ = printval.next
                printval.next = n
                n.next = next_
                break
            else:
                printval = printval.next
        else:
            print("Can not insert {0} after {1}".format(data, val))

    def show(self):
        printval = self.head
        while(printval):
            print (printval.data, end="->")
            printval = printval.next

lst = LinkedList()
for _ in range(10):
    lst.appendfirst(_)
# lst.show()
for _ in range(11, 15, 2):
    lst.appendlast(_)
for _ in range(21, 25, 2):
    lst.appendfirst(_)
lst.show()
lst.insertafter(26, 45)
lst.show()