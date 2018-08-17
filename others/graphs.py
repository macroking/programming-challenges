class Graph(object):
    def __init__(self, gdict):
        if not gdict:
            gdict = []
        self.gdict = gdict

    def get_vertices(self):
        print(self.gdict.keys())

    def get_edges(self):
        edge = []
        for k in self.gdict:
            for s in self.gdict[k]:
                if {s, k} not in edge:
                    edge.append({s, k})
        return edge

    def add_edge(self, vertex):
        vertex = set(vertex)
        ver1, ver2 = tuple(vertex)
        if ver1 in self.gdict:
            self.gdict[ver1].append(ver2)
        else:
            self.gdict[ver1] = ver2

graph = {"a": ["b", "c"],
         "b": ["a", "d"],
         "c": ["a", "d"],
         "d": ["e"],
         "e": ["d"]
         }
g = Graph(graph)
g.get_vertices()
print g.get_edges()
g.add_edge({'a', 'z'})
print g.get_edges()