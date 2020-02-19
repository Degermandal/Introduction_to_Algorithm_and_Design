def isBipartite(graph):
    if len(graph) == 0: #base case for empty
        return True
    vertices = len(graph)
    #initialize colors for all vertices
    colors = [0]*vertices
    #color all the vertices with white color like not visited
    for i in range(len(colors)):
        colors[i] = "white"
    #visit the vertices for check
    for i in range(vertices):
        if colors[i] == "white":
            result = isBipartiteHelper(i, vertices, colors, graph)
            if result == False:
                return False
    return True

def isBipartiteHelper(i, vertices, colors, graph):
    #color the first vertex with RED
    if i == 0:
        colors[i] = "red"
    #travel all adjacent vertices
    for v in range(vertices):
        if ((graph[i][v] == 1) & (colors[v] == "white")):
            #color is with the alternate color of vertex v
            if colors[i] == "red":
                #if u is in red, make vertex v in green
                colors[v] = "green"
            elif colors[i] == "green":
                colors[v] = "red"
            return isBipartiteHelper(v, vertices, colors, graph)
        elif (graph[i][v] == 1) & (colors[i] == colors[v]):
            return False
    return True

graph = [[0, 1, 1, 1],
         [1, 0, 0, 1],
         [0, 0, 0, 1],
         [1, 1, 1, 0] ]
t = isBipartite(graph)
print("Graph is bipartite or not:", t)

graph1 = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]
t = isBipartite(graph1)
print("Graph is bipartite or not:", t)