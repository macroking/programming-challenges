from __future__ import print_function
from collections import defaultdict
import os
import sys

class Graph(object):
    def __init__(self, v):
        self.vertex = v
        self.graph = defaultdict(list)

    def add_vertex(self, u, v):
        self.graph[u].append(v)

    def print_path(self, paths):
        print(paths)

    def countPaths(self, u, v):
        pass


if __name__ == '__main__':
    g = Graph(4)
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(0, 3)
    g.add_vertex(2, 0)
    g.add_vertex(2, 1)
    g.add_vertex(1, 3)

    s = 2
    d = 3
    p = g.countPaths(s, d)
    print('Number of paths from {} to {} is {}'.format(s, d, p))
