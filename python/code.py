from collections import defaultdict
from collections import deque

class Container:
    def __init__(self) -> None:
        pass
    
def dfs(visited_map,map_1,k,st):
    if(k not in visited_map.keys() and k in map_1.keys()):
        for x in map_1[k]:
            visited_map[k] = 1
            dfs(visited_map,map_1,x,st)
    st.append(k)


def topologicalSort(map_1):
    st = deque()
    visited_map = dict()
    for k in map_1:
        dfs(visited_map,map_1,k,st)

    return st

if __name__ == "__main__":
    print("Hello")
    
    map_1 = {'a': ['b','d'],
             'b': ['e','f'],
             'c': ['b','e'],
             'd': ['e','k','a'],
             'e': ['k']
             }

    arr = topologicalSort(map_1)

    print(arr)





