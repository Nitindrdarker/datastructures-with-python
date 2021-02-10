from collections import defaultdict
class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def add_edge(self, u, v):
        self.g[u].append(v)
    def display(self):
        print(self.g)
    def bsf(self ,s):
        visited = [False] * (max(self.g) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while(queue):
            current = queue.pop(0)
            print(current)
            for i in self.g[current]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 2)
g.display()
g.bsf(2)
