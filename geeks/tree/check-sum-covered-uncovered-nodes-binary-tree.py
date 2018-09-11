from __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printtree(root):
    if not root:
        return None
    printtree(root.left)
    print(root.data)
    printtree(root.right)

def uncoveredsumleft(root):
    if root.left == None and root.right == None:
        return root.data
    if root.left:
       return root.data + uncoveredsumleft(root.left)
    else:
        return root.data + uncoveredsumleft(root.right)

def uncoveredsumright(root):
    if root.left == None and root.right == None:
        return root.data
    if root.right:
       return root.data + uncoveredsumleft(root.right)
    else:
        return root.data + uncoveredsumleft(root.left)

def uncoveredsum(root):
    lb, rb = 0, 0

    if root.left:
        lb = uncoveredsumleft(root.left)
    if root.right:
        rb = uncoveredsumright(root.right)
    return root.data + lb+ rb

def sumofall(root):
    if not root:
        return 0
    return root.data + sumofall(root.left) + sumofall(root.right)

def isSumSame(root):
    sumofuncovered = uncoveredsum(root)
    totalsum = sumofall(root)
    if totalsum == sumofuncovered:
        return True
    else:
        return False

root = Node(8)
root.left = Node(3)

root.left.left = Node(1)
root.left.right =Node(6)
root.left.right.left = Node(4)
root.left.right.right =Node(7)

root.right =Node(10)
root.right.right =Node(14)
root.right.right.left = Node(13)

if (isSumSame(root)):
    print("Sum of covered and uncovered is same\n")
else:
    print("Sum of covered and uncovered is not same\n")