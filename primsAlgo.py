class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]#initilizing a 2d list for storing the graph
    def printMst(self, parent):
        print("edge \tweight")
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
    #function to find the minimum from the key list and use mstsete list to find if the vertix is reached or not
    def minKey(self, key, mstset):
        m = 999
        for v in range(self.v):
            if key[v] < m and mstset[v] == False:
                m = key[v]
                min_index = v
        return min_index
    def primsAlgo(self):
        key = [999] * self.v#to store the minimum weighted edge 
        parent = [None] * self.v#to store the path of mst
        key[0] = 0
        mstset = [False] * self.v#to check if the particular edge is reached or not following the path 
        parent[0] = -1
        for i in range(self.v):
            u = self.minKey(key, mstset)
            mstset[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and mstset[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.printMst(parent)
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 

g.primsAlgo(); 


        