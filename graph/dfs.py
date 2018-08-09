class Graph(object):
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def dfs(Graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in Graph[start] - visited:
        dfs(Graph, next, visited)
    return visited

if __name__ == '__main__':
    gdict = { "a" : set(["b","c"]),
                    "b" : set(["a", "d"]),
                    "c" : set(["a", "d"]),
                    "d" : set(["e"]),
                    "e" : set(["a"])
                    }


    dfs(gdict, 'a')
