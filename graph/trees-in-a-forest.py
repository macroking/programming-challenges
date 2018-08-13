from __future__ import print_function
from collections import defaultdict
import os
import sys

class Graph(object):
    def __init__(self,v ):
        self.vertex = v
        self.graph = defaultdict(list)

    def add_vertex(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def countTrees(self, v):
        visited = [False] * self.vertex
        res = 0
        for i in range(v):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                res += 1
        return res

if __name__ == '__main__':
    v = 5
    g = Graph(v)
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(3, 4)
    cnt = g.countTrees(v)
    print('Total numberof trees in the graph is {}'.format(cnt))