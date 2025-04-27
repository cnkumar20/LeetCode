import sys
def bellmanFord(V,edges,src):
    dist = [100000]*V
    dist[src] = 0

    for i in range(V):
        for edge in edges:
            u,v,wt = edge
            if dist[v] != sys.maxsize and dist[v] > wt+dist[u]:
                if i == V-1:
                    return [-1]
                dist[v] = wt+dist[u]
    return dist

if __name__ == "__main__":
    V=5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    src =0
    ans = bellmanFord(V,edges,src)
    print(' '.join(map(str, ans)))
