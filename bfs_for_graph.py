from collections import defaultdict
class Graph:
    def __init__(self):
        self.g = defaultdict(list) #creating a dictonary of lists
    #function to add graph to adjacency  list
    def add_edge(self, u, v):
        self.g[u].append(v)
    #to display the adjacency list for the given graph
    def display(self):
        print(self.g)
    #for bredth first search 
    def bsf(self ,s):
        visited = [False] * (max(self.g) + 1) # initilising all the element of the visisted list as false
        queue = [] #creating a queue
        queue.append(s)
        visited[s] = True
        #main logic
        while(queue):
            current = queue.pop(0)
            print(current)
            for i in self.g[current]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    #function for operating depth first search 
    def dfs_helper(self, v, visited_for_dfs):
        print(v, end="  ")
        visited_for_dfs.add(v)
        for i in self.g[v]:
            if i not in visited_for_dfs:
                self.dfs_helper(i, visited_for_dfs)
    #function for depth first search
    def dfs(self, start):
        visited_for_dfs = set()#set data structure for storing visited vertices
        self.dfs_helper(start, visited_for_dfs)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
graph.display()
graph.bsf(0)#starting point
graph.dfs(0)#starting point
