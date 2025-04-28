class DisjoinUnionSets:
    def __init__(self,n):
        self.rank = [1]*n
        self.parent = [_ for _ in range(n)]
    
    def find(self,i):
        if(self.parent[i]==i):
            return i
        else:
            return self.find(self.parent[i])
    def union(self,u,v):
        root_u = self.find(self.parent[u])
        root_v = self.find(self.parent[v])

        if(root_u == root_v):
            return 
        
        if(self.rank[root_u] > self.rank[root_v]):
            self.parent[root_u] = root_v
        elif(self.rank[root_u] < self.rank[root_v]):
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] +=1


