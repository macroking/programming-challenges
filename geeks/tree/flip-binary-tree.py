from __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def flipbinarytree(root):
    if not root:
        return root

    if not (root.left  and root.right):
        return root

    flippedroot = flipbinarytree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None
    return flippedroot

def printtree(root):
    if not root:
        return None
    from Queue import Queue
    q = Queue()

    q.put(root)
    while True:
        nodeCount = q.qsize()
        if nodeCount == 0:
            break
        while nodeCount > 0:
            node = q.get()
            print(node.data, end= " ")
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            nodeCount -= 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
printtree(root)
print()
root = flipbinarytree(root)
printtree(root)
print()