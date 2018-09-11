from __future__ import print_function
import os
import sys


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if not self.root:
            self.root = Node(data)

        return self.root

    # Recursion
    def inordertraversal(self, root):
        if root:
            self.inordertraversal(root.left)
            print(root.data)
            self.inordertraversal(root.right)

    # Without Recursion, using STACK
    def inordertraversal_stack(self, root):
        s = []
        cur = root
        s.append(cur)
        done = 0

        while not done:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                if s:
                    cur = s.pop()
                    print(cur.data)
                    cur = cur.right
                else:
                    done = 1

    def preordertraversal(self, root):
        if root:
            print(root.data)
            self.inordertraversal(root.left)
            self.inordertraversal(root.right)

    def postordertraversal(self, root):
        if root:
            self.inordertraversal(root.right)
            self.inordertraversal(root.left)
            print(root.data)

if __name__ == '__main__':
    root = Tree()
    root.insert_node(4)
