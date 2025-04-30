class Index:
    def __init__(self,list1):
        self.map_of_index = dict()  # instead of dict() extend to construct from list1
        self.key = None
        pass
    def create_map_of_index(self,interval)
        type = self.get_type(interval)
        return dict()
    def get_index(self,inter):
        self.key = self.get_key(inter)
        return self.key


class CompressInterval:

    def __init__(self,interval_list:list):
        self.index = Index(interval_list)
        self.parent:dict = self.index.create_map_of_index(interval_list)
        self.rank = {k:v for k,v in self.parent.items()} 
        self.boundary:dict[any,(int,int)] =   
    def find(self,interval):
        root = self.parent[self.get_index(interval)]
        if root != self.parent[self.index.get_index(interval)]:
            self.parent[self.index.get_index(interval)] = self.find(root)
            return self.parent[interval]
    
    def get_index(self,interval):
        return
    
    def create_map_of_index(self,interval_list) -> dict:
        interval_list
        return dict()
    
    def union(self,inter1,inter2):
        root1 = self.find(self.index.get_index(inter1))
        root2 = self.find(self.index.get_index(inter1))
        if(root1 == root2):
            return
        if(self.rank[root1] > self.rank[root2]):
            self.parent[root2] = root1
        elif(self.rank[root1] < self.rank[root2]):
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

