def floydWarshallAlgo(graph, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    

inf = 999999
graph = [[0, 3, 8, inf, -4],
[inf, 0, inf, 1, 7],
[inf, 4, 0, inf, inf],
[2, 5, -5, 0, -2],
[inf, inf, inf, 6, 0]]
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end=" ")
    print()

floydWarshallAlgo(graph, len(graph))
print("-----------after applying algo------------")
for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end=" ")
    print()

