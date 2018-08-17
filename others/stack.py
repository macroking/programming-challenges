'''
    implement stack
'''
from array import *

class Stack(object):
    def __init__(self, stacksize):
        self.stack = array('i', [])
        self.counter = -1

    def add(self, data):
        if type(data) == int:
            self.stack.append(data)
            self.counter += 1
        else:
            print('Can not insert {0} of type {1}'.format(data, type(data)))

    def pop(self):
        if self.counter > -1:
            print('Removed item {}'.format(self.stack.pop()))
            self.counter -= 1
        else:
            print('No item in the stack')

s = Stack(5)
s.add(1)
s.add(12)
s.add('w')
s.pop()
s.pop()
s.pop()