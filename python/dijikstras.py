#Dijikstras is to find shortest distance from src node to all other nodes in the graph

import heapq
import sys
def construct(edges,V):
    adj = [[] for _ in range(V)]
    for edge in edges:
        u,v,wt = edge
        adj[u].append([v,wt])
        adj[v].append([u,wt])
    return adj

def dijikstras(V,edges,src):
    adj = construct(edges,V)
    pq = []
    dist = [sys.maxsize]*V
    heapq.heappush(pq,[0,src])
    dist[src] = 0

    while pq:
        u = heapq.heappop(pq)[1]
        for x in adj[u]:
            v,wt = x[0],x[1]
            if dist[v] > dist[u]+wt:
                dist[v] = dist[u]+wt
                heapq.heappush(pq,[dist[v],v])
    return dist


if __name__ == "__main__":
    edges =[[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]];
    V = 5
    src = 0
    result = dijikstras(V,edges,src)
    print(result)
