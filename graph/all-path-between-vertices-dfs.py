'''
    Print paths using DFS
'''

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

    def countPathsUtil(self, s, d, visited, pathcount, paths):
        visited[s] = True
        paths.append(s)

        if ( s == d ):
            pathcount += 1
            print(paths)
        else:
            for i in self.graph[s]:
                if visited[i] == False:
                    pathcount = self.countPathsUtil(i, d, visited, pathcount, paths)
        paths.pop()
        visited[s] = False
        return pathcount

    def countPaths(self, s, d):
        visited = [False] * self.vertex
        pathcount = 0
        paths = []
        pathcount = self.countPathsUtil(s, d, visited, pathcount, paths)
        return pathcount

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