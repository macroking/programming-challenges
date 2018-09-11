from __future__ import print_function
import os
import sys


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def isSumProperty(root):
    from Queue import Queue
    q = Queue()
    if not root:
        return None
    q.put(root)
    while not q.empty():
        node = q.get()
        comp = node.data
        _left, _right = 0, 0
        if node.left:
            q.put(node.left)
            _left = node.left.data
        if node.right:
            q.put(node.right)
            _right = node.right.data
        if (_left+_right) != comp:
            return False
    return True

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(15)
root.right.right = Node(2)
stat = isSumProperty(root)
print(stat)
if stat:
    print("The given tree satisfies the children sum property ")
else:
    print("The given tree does not satisfy the children sum property ")