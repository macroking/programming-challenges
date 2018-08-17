'''
Implement tree
'''

class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def append(self, data):
        if self.data:
            if data > self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.append(data)
            elif data < self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.append(data)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

root = Tree(10)
root.append(12)
root.append(22)
root.append(3)
root.PrintTree()