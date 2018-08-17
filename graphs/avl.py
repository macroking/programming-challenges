from  __future__ import print_function
import os
import sys

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        if key:
            if key < self.left:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.insert(key)


if __name__ == '__main__':
    pass
