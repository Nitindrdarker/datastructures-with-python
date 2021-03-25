import sys
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    def result(self, dist):
        print("vertex \tdistance from source")
        for node in range(self.V):
            print(node,"\t", dist[node])
    #utilty function for findind the mimimum distance from the node in 'dist' list 
    def minDistance(self, dist, sptSet):
        m = 999999999999999
        for v in range(self.V):
            #logic to find the minimun form the 'dist' list 
            if dist[v] < m and sptSet[v] == False: 
                m = dist[v] 
                min_index = v
        #print(m, min_index)
        return min_index 
    def dijkstra(self, src):
        dist = [999999999999999] * self.V#initilising a list for storing the minimum distance form the source
        dist[src] = 0
        sptSet = [False] * self.V#list ot keep track of isited and unvisited node
        #main logical loop
        for i in range(self.V):
            u = self.minDistance(dist, sptSet)
            print(u)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                #print(dist, sptSet) 
        self.result(dist)
        
g = Graph(7)
#adjecency matrix
g.graph = [[0, 2, 6, 0, 0, 0, 0],
[2, 0, 0, 5, 0, 0, 0],
[6, 0, 0, 8, 0, 0, 0],
[0, 1, 8, 0, 10, 15, 0],
[0, 0, 0, 10, 0, 6, 2],
[0, 0, 0, 15, 6, 0, 6],
[0, 0, 0, 0, 2, 6, 0]]  
  
g.dijkstra(2); 