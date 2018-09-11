from __future__ import print_function
import os
import sys


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Convert left right representation of binary tree
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

def sumtree(root):
    if not root:
        return 0
    oldval = root.data
    root.data = sumtree(root.left) + sumtree(root.right)
    return root.data + oldval


def leftsumtree(root):
    if not root:
        return 0
    if not root.left or not root.right:
        return root.data
    leftsum = leftsumtree(root.left)
    rightsum = leftsumtree(root.right)

    root.data += leftsum
    return root.data+rightsum

def mirrortree(root):
    if not root:
        return None
    mirrortree(root.left)
    mirrortree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

def printtree(root):
    if not root:
        return None
    printtree(root.left)
    print(root.data, end=" ")
    printtree(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(7)
root.right.right = Node(6)
printtree(root)
print()
# sumtree(root)
# leftsumtree(root)
mirrortree(root)
printtree(root)
print()
