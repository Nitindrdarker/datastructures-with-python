from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def union(self, parent, x, y):
        parent[x] = y
    def findparent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.findparent(parent, parent[i])
    def findCycle(self):
        parent = [-1] * self.v
        for i in self.graph:
            for j in self.graph[i]:
                x = self.findparent(parent, i)
                y = self.findparent(parent, j)
            if x == y:
                return True
            self.union(parent, x, y)

g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
 
if g.findCycle():
    print("Graph contains cycle")
else :
    print("Graph does not contain cycle ")