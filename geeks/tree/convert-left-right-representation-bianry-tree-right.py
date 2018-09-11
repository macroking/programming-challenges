from __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def convert(root):
    if not root:
        return
    convert(root.left)
    convert(root.right)

    if not root.left:
        root.left = root.right
    else:
        root.left.right = root.right
    root.right = None

def printtree(root):
    if root:
        print(root.data, end=' ')
        printtree(root.right)
        printtree(root.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.left = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)
printtree(root)
print()
convert(root)
printtree(root)
print()