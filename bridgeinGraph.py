from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        self.low = [float("inf")] * self.v
        self.in_time = [float("inf")] * self.v
        self.visited = [False] * self.v
        self.timer = 0
        
    def addEdge(self, u, v):
        self.graph[u].append(v)#we have to insert out graph in both way so that our algo work
        self.graph[v].append(u)
    def depthFirtstSearch(self, node, parent):
        self.visited[node] = True
        self.in_time[node] = self.timer
        self.low[node] = self.timer
        self.timer += 1
        
        for child in self.graph[node]:
            if child == parent: #if the child of current node is its parents .. then do nothing
                continue
            if self.visited[child] == True:#edge node-child is a back edge
                self.low[node] = min(self.low[node], self.in_time[child])#self.low[node] because when we come back after recursive call then we dont want ot change the low time of parent node from its child node
            else:#edge node-child is forward edge
                self.depthFirtstSearch(child, node)
                if(self.low[child] > self.in_time[node]):#this line means if the  node is connected to any another node so its low time has reduced to the intime of that connected node's...This line will only be true if node is not connected to any other node other that its current parents
                    print(f"node {node} - node {child} is bridge")
                self.low[node] = min(self.low[node], self.low[child])#change the low of current node to its child beacuse if a child can reach a back track then parent can too 
g3 = Graph (7) 
g3.addEdge(0, 1) 
g3.addEdge(1, 2) 
g3.addEdge(2, 0) 
g3.addEdge(1, 3) 
g3.addEdge(1, 4) 
g3.addEdge(1, 6) 
g3.addEdge(3, 5) 
g3.addEdge(4, 5) 
print("\nBridges in this graph ")
g3.depthFirtstSearch(0, -1)#we are initilizing out algo from 0 with no parent






        
    
        


        