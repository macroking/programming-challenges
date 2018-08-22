from  __future__ import print_function
import os
import sys


class Node(object):
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def levelOrder(root):
    #Write your code here
    if not root:
        return
    queue = []
    queue.append(root)

    while(queue):
        print(queue[0].info, end=" ")
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

if __name__ == '__main__':
    tree = BinarySearchTree()
    f = open('./hackerrank/trees/input.txt')
    t = int(f.readline())

    arr = list(map(int, f.readline().split()))

    for i in range(t):
        tree.create(arr[i])

    levelOrder(tree.root)