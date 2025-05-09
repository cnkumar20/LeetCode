def buildGraph(edges):
    graph = dict()
    for edge in edges:
        u,v = edge
        if (u not in graph.keys()):
            graph[u] = []
        if(v not in graph.keys()):
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph






