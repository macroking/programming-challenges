from __future__ import print_function
import os
import sys

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.key)
        if self.right:
            self.right.print_tree()

    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)

if __name__ == '__main__':
    root = Node(12)
    a = [6, 14, 3]
    for _ in a:
        root.insert(_)
    root.print_tree()