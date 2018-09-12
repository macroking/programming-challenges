from __future__ import print_function
from collections import defaultdict
import os
import sys


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFSIterative(self, v, visited):
        s = []
        s.append(v)

        while s:
            node = s.pop(0)
            if not visited[node]:
                print(node, end=" ")
                visited[node] = True
            for i in self.graph[node]:
                if visited[i] == False:
                    s.append(i)

    def DFS(self):
        v = len(self.graph)
        visited = [False] * v
        for i in range(v):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                # self.DFSIterative(i, visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print('Following is Breadth First Traversal')
    g.DFS()