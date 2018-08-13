from __future__ import print_function
from collections import defaultdict
from functools import reduce
import os
import sys

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, l):
        y = self.graph.keys()
        x = reduce(lambda x,y: x+y, self.graph.values())
        x = (set(x).union(set(y)))
        visited = [False] * len(x)
        level = [0] * len(x)
        queue = []

        queue.append(s)
        visited[s] = True
        level[s] = 0

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    level[i] = level[s] + 1

        cnt = 0
        for i in range(len(x)):
            if level[i] == l:
                cnt += 1
        print()
        print('Number of nodes at level {} is {}'.format(l, cnt))

if __name__ == '__main__':
    g = Graph()
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(1, 3)
    g.add_vertex(1, 4)
    g.add_vertex(1, 5)
    g.add_vertex(2, 6)
    g.BFS(0, 2)

    g = Graph()
    g.add_vertex(0, 1)
    g.add_vertex(0, 2)
    g.add_vertex(1, 3)
    g.add_vertex(2, 4)
    g.add_vertex(2, 5)
    g.BFS(0, 2)
