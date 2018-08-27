from __future__ import print_function
import os
import sys

class Queue(object):
    def __init__(self):
        self.swap = list()
    def endque(self, data):
        self.swap.append(data)
    def dequeue(self):
        self.swap.pop(0)
    def printqueue(self):
        if self.swap:
            return self.swap[0]

if __name__ == '__main__':
    f = open('./hackerrank/queues/input.txt')
    q = Queue()
    for _ in range(int(f.readline().strip())):
        in_ = f.readline().strip().split(" ")
        op = in_[0]
        if len(in_) == 2:
            data = in_[1]
        if int(op) == 1:
            q.endque(int(data))
        elif int(op) == 2:
            q.dequeue()
        elif int(op) == 3:
            print(q.printqueue())
