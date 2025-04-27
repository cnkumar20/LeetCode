class TopK:
    def __init__(self):
        pass

    def collect_frequency(self,arr):
        num_collection_list_of_tuples = list()
        map_1 = dict()
        for item in arr:
            if(item not in map_1):
                map_1[item] = 1
            else:
                map_1[item] += 1
        for k,v in map_1.items():
            num_collection_list_of_tuples.append((k,v))
        return num_collection_list_of_tuples

    def sort(self,arr):
        ans = list()
        for x in sorted(self.collect_frequency(arr),key = lambda a : a[1]):
            ans.append(x[0])
        return ans


if __name__ == "__main__":
    arr = [2,3,1,5,7,3,4,5,4,5,7]
    topk = TopK()
    print(topk.sort(arr))
